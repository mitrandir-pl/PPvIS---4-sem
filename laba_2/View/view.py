from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '720')

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from Controller.controller import DataBaseController
from Model.model import Book


db_controller = DataBaseController()


class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        self._controller = db_controller

        box_layout = BoxLayout(orientation="vertical")
        menu_label = Label(text="Menu", font_size=30)
        add_button = Button(text="Add", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                            on_press=lambda x: set_screen("add"), background_color=[1, 0, 1, 1])
        remove_button = Button(text="Delete", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                               on_press=lambda x: set_screen("remove"), background_color=[1, 0, 1, 1])
        show_button = Button(text="Show", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                             on_press=lambda x: set_screen("show"), background_color=[1, 0, 1, 1])
        exit_button = Button(text="Exit", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                             on_press=lambda x: self.exit_program(), background_color=[1, 0, 1, 1])
        box_layout.add_widget(menu_label)
        box_layout.add_widget(add_button)
        box_layout.add_widget(remove_button)
        box_layout.add_widget(show_button)
        box_layout.add_widget(exit_button)
        self.add_widget(box_layout)

    def exit_program(self):
        self._controller.write_data_into_file()
        raise SystemExit


class AddScreen(Screen):
    def __init__(self, **kw):
        super(AddScreen, self).__init__(**kw)

        self._controller = db_controller

        added_fields = GridLayout(cols=2)

        book_name = Button(text="Book name", background_color=[1, 0, 1, 1])
        self.book_name_input = TextInput()

        fio_author_text = Button(text="Author", background_color=[1, 0, 1, 1])
        fio_author_input = GridLayout(cols=3)
        name_author_text = Button(text="Name", background_color=[1, 0, 1, 1])
        surname_author_text = Button(text="Last name", background_color=[1, 0, 1, 1])
        patronymic_author_text = Button(text="Patronymic", background_color=[1, 0, 1, 1])
        self.name_author_input = TextInput()
        self.surname_author_input = TextInput()
        self.patronymic_author_input = TextInput()
        fio_author_input.add_widget(surname_author_text)
        fio_author_input.add_widget(name_author_text)
        fio_author_input.add_widget(patronymic_author_text)
        fio_author_input.add_widget(self.surname_author_input)
        fio_author_input.add_widget(self.name_author_input)
        fio_author_input.add_widget(self.patronymic_author_input)

        publisher = Button(text="Publisher", background_color=[1, 0, 1, 1])
        self.publisher_input = TextInput()

        amount_of_volumes = Button(text="Amount of volumes", background_color=[1, 0, 1, 1])
        self.amount_of_volumes_input = TextInput()

        circulation = Button(text="Circulation", background_color=[1, 0, 1, 1])
        self.circulation_input = TextInput()

        status = Button(text="Status", background_color=[1, 0, 1, 1])
        self.status_of_process = Button(background_color=[1, 1, 1, 1])

        create_button = Button(text="Create ->", on_press=lambda x: self.create_field(),
                               background_color=[0, 0, 1, 1])
        back_button = Button(text="<- Back", on_press=lambda x: set_screen("menu"),
                             background_color=[0, 0, 1, 1])

        added_fields.add_widget(book_name)
        added_fields.add_widget(self.book_name_input)
        added_fields.add_widget(fio_author_text)
        added_fields.add_widget(fio_author_input)
        added_fields.add_widget(publisher)
        added_fields.add_widget(self.publisher_input)
        added_fields.add_widget(amount_of_volumes)
        added_fields.add_widget(self.amount_of_volumes_input)
        added_fields.add_widget(circulation)
        added_fields.add_widget(self.circulation_input)
        added_fields.add_widget(status)
        added_fields.add_widget(self.status_of_process)
        added_fields.add_widget(back_button)
        added_fields.add_widget(create_button)

        self.add_widget(added_fields)

    def clear_all_fields(self):
        self.book_name_input.text = ''
        self.name_author_input.text = ''
        self.surname_author_input.text = ''
        self.patronymic_author_input.text = ''
        self.publisher_input.text = ''
        self.amount_of_volumes_input.text = ''
        self.circulation_input.text = ''

        self.book_name_input.background_color = [1, 1, 1, 1]
        self.name_author_input.background_color = [1, 1, 1, 1]
        self.surname_author_input.background_color = [1, 1, 1, 1]
        self.patronymic_author_input.background_color = [1, 1, 1, 1]
        self.publisher_input.background_color = [1, 1, 1, 1]
        self.amount_of_volumes_input.background_color = [1, 1, 1, 1]
        self.circulation_input.background_color = [1, 1, 1, 1]

    def on_enter(self, *args):
        pass

    def on_leave(self, *args):
        self.clear_all_fields()
        self.status_of_process.text = ''
        self.status_of_process.background_color = [1, 1, 1, 1]

    def is_not_empty(self, input_):
        if input_.text == '':
            input_.background_color = [1, 0, 0, 1]
            return False
        else:
            input_.background_color = [1, 1, 1, 1]
            return True

    def is_type_is_int(self, input_):
        try:
            int(input_.text)
            return True
        except Exception:
            input_.background_color = [1, 0, 0, 1]
            return False

    def check(self):
        if all((self.is_not_empty(self.book_name_input),
                self.is_not_empty(self.name_author_input),
                self.is_not_empty(self.surname_author_input),
                self.is_not_empty(self.patronymic_author_input),
                self.is_not_empty(self.publisher_input),
                self.is_not_empty(self.amount_of_volumes_input),
                self.is_not_empty(self.circulation_input),
                self.is_type_is_int(self.amount_of_volumes_input),
                self.is_type_is_int(self.circulation_input))):
            return True

    def create_field(self):
        if self.check():
            book = Book(
                self.book_name_input.text,
                self.name_author_input.text,
                self.surname_author_input.text,
                self.patronymic_author_input.text,
                self.publisher_input.text,
                self.amount_of_volumes_input.text,
                self.circulation_input.text,
            )
            self._controller.add_book(book)
            self.clear_all_fields()
            self.status_of_process.background_color = [0, 1, 0, 1]
            self.status_of_process.text = 'Completed'
        else:
            self.status_of_process.background_color = [1, 0, 0, 1]
            self.status_of_process.text = 'Error!!!'


class RemoveScreen(Screen):
    def __init__(self, **kw):
        super(RemoveScreen, self).__init__(**kw)
        self._controller = db_controller
        self.choice = 0
        select_remove = BoxLayout(orientation="vertical")
        self.menu_label = Label(text="Deleting by:", font_size=30)
        fio_author_remove_button = Button(
            text="Author last name", font_size=30, on_press=lambda x: self.set_choice(1, fio_author_remove_button))
        author_and_publisher_remove_button = Button(
            text="Author last name and Publisher", font_size=30,
            on_press=lambda x: self.set_choice(2, author_and_publisher_remove_button))
        amount_of_volumes_remove_button = Button(
            text="Amount of volumes", font_size=30,
            on_press=lambda x: self.set_choice(3, amount_of_volumes_remove_button))
        book_name_remove_button = Button(
            text="Book Name", font_size=30,
            on_press=lambda x: self.set_choice(4, book_name_remove_button))
        less_than_specified_amount_remove_button = Button(
            text="Less than specified amount of volumes", font_size=30,
            on_press=lambda x: self.set_choice(5, less_than_specified_amount_remove_button))
        more_than_specified_amount_remove_button = Button(
            text="More than specified amount of volumes", font_size=30,
            on_press=lambda x: self.set_choice(6, more_than_specified_amount_remove_button))
        self.choice_buttons = list()
        self.choice_buttons.append(fio_author_remove_button)
        self.choice_buttons.append(author_and_publisher_remove_button)
        self.choice_buttons.append(amount_of_volumes_remove_button)
        self.choice_buttons.append(book_name_remove_button)
        self.choice_buttons.append(less_than_specified_amount_remove_button)
        self.choice_buttons.append(more_than_specified_amount_remove_button)
        self.remove_input = TextInput()
        go_back_buttons = BoxLayout()
        remove_button = Button(text="Remove ->", on_press=lambda x: self.remove_field(),
                               background_color=[0, 0, 1, 1])
        back_button = Button(text="<- Back", on_press=lambda x: set_screen("menu"),
                             background_color=[0, 0, 1, 1])
        select_remove.add_widget(self.menu_label)
        select_remove.add_widget(fio_author_remove_button)
        select_remove.add_widget(author_and_publisher_remove_button)
        select_remove.add_widget(amount_of_volumes_remove_button)
        select_remove.add_widget(book_name_remove_button)
        select_remove.add_widget(less_than_specified_amount_remove_button)
        select_remove.add_widget(more_than_specified_amount_remove_button)
        select_remove.add_widget(self.remove_input)
        go_back_buttons.add_widget(back_button)
        go_back_buttons.add_widget(remove_button)
        select_remove.add_widget(go_back_buttons)
        self.add_widget(select_remove)

    def on_leave(self, *args):
        self.menu_label.text = "Deleting by:"
        self.choice = 0
        self.remove_input.background_color = [1, 1, 1, 1]
        self.remove_input.text = ""

    def set_choice(self, choice, choice_button):
        self.choice = choice
        for button in self.choice_buttons:
            button.background_color = [1, 1, 1, 1]
        choice_button.background_color = [0, 1, 0, 1]

    def is_type_is_int(self, input_):
        try:
            int(input_.text)
            return True
        except Exception:
            input_.background_color = [1, 0, 0, 1]
            return False

    def remove_field(self):
        is_removed = False
        if 0 < self.choice < 7:
            if self.remove_input.text == "":
                self.remove_input.background_color = [1, 0, 0, 1]
            else:
                match self.choice:
                    case 1:
                        is_removed = self._controller.delete_by_author_last_name(self.remove_input.text)
                    case 2:
                        try:
                            author, publisher = self.remove_input.text.split()
                            is_removed = self._controller.delete_by_author_and_publisher(author, publisher)
                        except Exception:
                            self.massage_wrong_input()
                            self.remove_input.background_color = [1, 0, 0, 1]
                            return
                    case 3:
                        if self.is_type_is_int(self.remove_input):
                            is_removed = self._controller.delete_by_amount_of_volumes(self.remove_input.text)
                        else:
                            self.massage_wrong_input()
                            return
                    case 4:
                        is_removed = self._controller.delete_by_book_name(self.remove_input.text)
                    case 5:
                        if self.is_type_is_int(self.remove_input):
                            is_removed = self._controller.delete_less_than_amount_of_volumes(self.remove_input.text)
                        else:
                            self.massage_wrong_input()
                            return
                    case 6:
                        if self.is_type_is_int(self.remove_input):
                            is_removed = self._controller.delete_more_than_amount_of_volumes(self.remove_input.text)
                        else:
                            self.massage_wrong_input()
                            return
                if is_removed:
                    self.menu_label.text = "Remove complete!"
                else:
                    self.menu_label.text = "No such records!"
                self.remove_input.background_color = [1, 1, 1, 1]
        else:
            self.menu_label.text = "Choice way of remove!"

    def massage_wrong_input(self):
        self.menu_label.text = "Invalid input!"

class ShowScreen(Screen):
    fields_on_screens = 5

    def __init__(self, **kw):
        super(ShowScreen, self).__init__(**kw)
        self.list_of_screens = []
        self.index_of_screen = 0
        self.choice = 0
        self.present_fields_screen = None
        self._controller = db_controller

        test_layout = GridLayout(cols=5, padding=[0, 300, 0, 80])
        travel_layout = AnchorLayout(anchor_x='left', anchor_y="bottom")
        search_columns = GridLayout(cols=2, padding=[0, 0, 0, 80], row_force_default=True,
                                    row_default_height=(300/7))
        search_author_surname = Button(text="Search by author last name", background_color=[1, 1, 1, 1],
                                       on_press=lambda x: self.set_search(1, search_author_surname))
        self.author_surname_input = TextInput()
        search_author_surname_and_publisher = Button(
            text="Search by author last name and publisher",
            background_color=[1, 1, 1, 1],
            on_press=lambda x: self.set_search(2, search_author_surname_and_publisher))
        self.author_surname_and_publisher_input = TextInput()
        search_amount_of_values = Button(
            text="Search by amount of values",
            background_color=[1, 1, 1, 1],
            on_press=lambda x: self.set_search(3, search_amount_of_values)
        )
        self.amount_of_values_input = TextInput()
        search_book_name = Button(text="Search by book name", background_color=[1, 1, 1, 1],
                                  on_press=lambda x: self.set_search(4, search_book_name))
        self.book_name_input = TextInput()
        search_less_than_current = Button(
            text="Search less than current amount of values",
            background_color=[1, 1, 1, 1],
            on_press=lambda x: self.set_search(5, search_less_than_current)
        )
        self.less_than_current = TextInput()
        search_more_than_current = Button(
            text="Search more than current amount of values",
            background_color=[1, 1, 1, 1],
            on_press=lambda x: self.set_search(6, search_more_than_current)
        )
        self.more_than_current = TextInput()
        self.search_info = Button(text="SEARCH", background_color=[1, 1, 1, 1],
                                  on_press=lambda x: self.search())
        search = Button(text="ALL", background_color=[1, 1, 1, 1],
                        on_press=lambda x: self.show(self._controller.get_all_books()))
        self.search_buttons = list()
        self.search_buttons.append(search_author_surname)
        self.search_buttons.append(search_author_surname_and_publisher)
        self.search_buttons.append(search_amount_of_values)
        self.search_buttons.append(search_book_name)
        self.search_buttons.append(search_less_than_current)
        self.search_buttons.append(search_more_than_current)
        search_columns.add_widget(search_author_surname)
        search_columns.add_widget(self.author_surname_input)
        search_columns.add_widget(search_author_surname_and_publisher)
        search_columns.add_widget(self.author_surname_and_publisher_input)
        search_columns.add_widget(search_amount_of_values)
        search_columns.add_widget(self.amount_of_values_input)
        search_columns.add_widget(search_book_name)
        search_columns.add_widget(self.book_name_input)
        search_columns.add_widget(search_less_than_current)
        search_columns.add_widget(self.less_than_current)
        search_columns.add_widget(search_more_than_current)
        search_columns.add_widget(self.more_than_current)
        search_columns.add_widget(search)
        search_columns.add_widget(self.search_info)
        columns_names = GridLayout(cols=5)
        book_name = Button(text="Book name", size_hint_x=None, width=200, size_hint_y=None, height=60, background_color=[0, 1, 0, 1])
        author = Button(text="Author", size_hint_y=None, height=60, background_color=[0, 1, 0, 1])
        publisher = Button(text="Publisher", size_hint_y=None, height=60, background_color=[0, 1, 0, 1])
        amount_of_volumes = Button(text="Amount of volumes", size_hint_y=None, height=60, background_color=[0, 1, 0, 1])
        circulation = Button(text="Circulation", size_hint_y=None, width=80, height=60, background_color=[0, 1, 0, 1])

        columns_names.add_widget(book_name)
        columns_names.add_widget(author)
        columns_names.add_widget(publisher)
        columns_names.add_widget(amount_of_volumes)
        columns_names.add_widget(circulation)

        bl2 = BoxLayout()
        number_of_page_boxlayout = BoxLayout(orientation="vertical")
        index_of_page_boxlayout = BoxLayout(orientation="vertical")
        number_of_elements_boxlayout = BoxLayout(orientation="vertical")

        back_button = Button(text="<- Back", on_press=lambda x: set_screen("menu"),
                             size_hint_y=None, height=80, background_color=[0, 0, 1, 1])
        first_page_button = Button(text="First page", on_press=lambda x: self.set_present_fields_screen(0),
                                   size_hint_y=None, height=80, background_color=[0, 0, 1, 1])
        last_page_button = Button(text="Last page",
                                  on_press=lambda x: self.set_present_fields_screen(len(self.list_of_screens) - 1),
                                  size_hint_y=None, height=80, background_color=[0, 0, 1, 1])
        next_page_button = Button(text="Next page",
                                  on_press=lambda x: self.set_present_fields_screen(self.index_of_screen + 1),
                                  size_hint_y=None, height=80, background_color=[0, 0, 1, 1])
        past_page_button = Button(text="Past page",
                                  on_press=lambda x: self.set_present_fields_screen(self.index_of_screen - 1),
                                  size_hint_y=None, height=80, background_color=[0, 0, 1, 1])
        number_of_page_text = Button(text="№ page",
                                     size_hint_y=None, height=40, background_color=[0, 0, 1, 1])
        index_of_page_text = Button(text="Count pages",
                                    size_hint_y=None, height=40, background_color=[0, 0, 1, 1])
        number_of_elements_text = Button(text="Count el",
                                         size_hint_y=None, height=40, background_color=[0, 0, 1, 1])
        self.number_of_page_text = Button(text=str(self.index_of_screen),
                                          size_hint_y=None, height=40, background_color=[0, 0, 1, 1])
        self.index_of_page_text = Button(text=str(len(self.list_of_screens)),
                                         size_hint_y=None, height=40, background_color=[0, 0, 1, 1])
        self.number_of_elements_text = Button(text=str(len(self._controller.get_all_books())),
                                         size_hint_y=None, height=40, background_color=[0, 0, 1, 1])

        number_of_page_boxlayout.add_widget(number_of_page_text)
        number_of_page_boxlayout.add_widget(self.number_of_page_text)

        index_of_page_boxlayout.add_widget(index_of_page_text)
        index_of_page_boxlayout.add_widget(self.index_of_page_text)

        number_of_elements_boxlayout.add_widget(number_of_elements_text)
        number_of_elements_boxlayout.add_widget(self.number_of_elements_text)

        bl2.add_widget(back_button)
        bl2.add_widget(first_page_button)
        bl2.add_widget(past_page_button)
        bl2.add_widget(next_page_button)
        bl2.add_widget(last_page_button)
        bl2.add_widget(number_of_page_boxlayout)
        bl2.add_widget(index_of_page_boxlayout)
        bl2.add_widget(number_of_elements_boxlayout)
        travel_layout.add_widget(bl2)
        test_layout.add_widget(columns_names)
        self.add_widget(search_columns)
        self.add_widget(travel_layout)
        self.add_widget(test_layout)

    def set_search(self, search, choice_button):
        self.choice = search
        for button in self.search_buttons:
            button.background_color = [1, 1, 1, 1]
        choice_button.background_color = [0, 1, 0, 1]

    def is_type_is_int(self, input_):
        try:
            int(input_.text)
            return True
        except Exception:
            input_.background_color = [1, 0, 0, 1]
            return False

    def search(self):
        if 0 < self.choice < 7:
            match self.choice:
                case 1:
                    author_last_name = self.author_surname_input.text
                    if author_last_name == '':
                        self.author_surname_input.background_color = [1, 0, 0, 1]
                    else:
                        self.author_surname_input.background_color = [1, 1, 1, 1]
                        found_books = self._controller.search_by_author_last_name(author_last_name)
                        self.show(found_books)
                        self.clear_search_fields()
                case 2:
                    if self.author_surname_and_publisher_input.text == '':
                        self.author_surname_and_publisher_input.background_color = [1, 0, 0, 1]
                    else:
                        try:
                            author, publisher = self.author_surname_and_publisher_input.text.split()
                            found_books = self._controller.search_by_author_last_name_and_publisher(author, publisher)
                            self.author_surname_and_publisher_input.background_color = [1, 1, 1, 1]
                            self.show(found_books)
                            self.clear_search_fields()
                        except Exception:
                            self.massage_wrong_input()
                case 3:
                    if self.amount_of_values_input.text == '':
                        self.amount_of_values_input.background_color = [1, 0, 0, 1]
                    else:
                        if self.is_type_is_int(self.amount_of_values_input):
                            self.clear_search_fields()
                            self.amount_of_values_input.background_color = [1, 1, 1, 1]
                            found_books = self._controller.search_by_amount_of_volumes(
                                self.amount_of_values_input.text
                            )
                            self.show(found_books)
                            self.clear_search_fields()
                case 4:
                    if self.book_name_input.text == '':
                        self.book_name_input.background_color = [1, 0, 0, 1]
                    else:
                        self.book_name_input.background_color = [1, 1, 1, 1]
                        found_books = self._controller.search_by_book_name(
                            self.book_name_input.text
                        )
                        self.show(found_books)
                        self.clear_search_fields()
                case 5:
                    if self.less_than_current.text == '':
                        self.less_than_current.background_color = [1, 0, 0, 1]
                    else:
                        if self.is_type_is_int(self.less_than_current):
                            self.less_than_current.background_color = [1, 1, 1, 1]
                            found_books = self._controller.search_less_than_current_amount(
                                self.less_than_current.text
                            )
                            self.show(found_books)
                            self.clear_search_fields()
                case 6:
                    if self.more_than_current.text == '':
                        self.more_than_current.background_color = [1, 0, 0, 1]
                    else:
                        if self.is_type_is_int(self.more_than_current):
                            self.more_than_current.background_color = [1, 1, 1, 1]
                            found_books = self._controller.search_more_than_current_amount(
                                self.more_than_current.text
                            )
                            self.show(found_books)
                            self.clear_search_fields()
        else:
            if self.present_fields_screen:
                self.remove_widget(self.present_fields_screen)
            self.present_fields_screen = GridLayout(
                cols=5, padding=[0, 360, 0, 80],
                row_force_default=True,
                row_default_height=100)
            not_found = Button(text="Choose variant of searching")
            self.present_fields_screen.add_widget(not_found)
            self.add_widget(self.present_fields_screen)

    def massage_wrong_input(self):
        if self.present_fields_screen:
            self.remove_widget(self.present_fields_screen)
        self.present_fields_screen = GridLayout(
            cols=1, padding=[0, 360, 0, 80],
            row_force_default=True,
            row_default_height=100)
        not_found = Button(text="Invalid input")
        self.present_fields_screen.add_widget(not_found)
        self.add_widget(self.present_fields_screen)

    def show(self, list_of_fields):
        if self.present_fields_screen:
            self.remove_widget(self.present_fields_screen)
        if not list_of_fields:
            self.present_fields_screen = GridLayout(
                cols=1, padding=[0, 360, 0, 80],
                row_force_default=True,
                row_default_height=100)
            not_found = Button(text="Nothing found")
            self.present_fields_screen.add_widget(not_found)
            self.add_widget(self.present_fields_screen)
            return
        # 720 - 180
        self.list_of_screens = []
        self.index_of_screen = 0
        # list_of_fields = self._controller.get_all_books()
        self.number_of_elements_text.text = str(len(list_of_fields))
        counter_of_screens = ShowScreen.fields_on_screens
        number_of_screens = 0
        # gl1 = GridLayout(cols=6, padding=[0, 80, 0, 80], row_force_default=True,
        #                  row_default_height=(720 - 160) / ShowScreen.fields_on_screens)
        for field in list_of_fields:
            if ShowScreen.fields_on_screens == counter_of_screens:
                counter_of_screens = 0
                gl1 = GridLayout(cols=5, padding=[0, 360, 0, 80], row_force_default=True,
                                 row_default_height=(720 - 160) / 10)
                self.list_of_screens.append(gl1)
                number_of_screens += 1
            author = f"{field.author_name} {field.author_last_name} {field.author_patronymic}"
            gl1.add_widget(Button(text=field.book_name, font_size=12, size_hint_x=None, width=200))
            gl1.add_widget(Button(text=author, font_size=12))
            gl1.add_widget(Button(text=field.publisher, font_size=12))
            gl1.add_widget(Button(text=str(field.amount_of_volumes), font_size=12))
            gl1.add_widget(Button(text=str(field.circulation), font_size=12, size_hint_x=None, width=206))
            counter_of_screens += 1

        self.present_fields_screen = self.list_of_screens[self.index_of_screen]
        self.number_of_page_text.text = str(self.index_of_screen + 1)
        self.index_of_page_text.text = str(len(self.list_of_screens))
        self.add_widget(self.present_fields_screen)

    def set_present_fields_screen(self, index_of_screen):
        if -1 < index_of_screen < len(self.list_of_screens):
            self.index_of_screen = index_of_screen
            self.remove_widget(self.present_fields_screen)
            self.present_fields_screen = self.list_of_screens[index_of_screen]
            self.add_widget(self.present_fields_screen)
            self.number_of_page_text.text = str(self.index_of_screen + 1)

    def clear_search_fields(self):
        self.author_surname_input.text = ''
        self.author_surname_and_publisher_input.text = ''
        self.amount_of_values_input.text = ''
        self.book_name_input.text = ''
        self.less_than_current.text = ''
        self.more_than_current.text = ''
        self.author_surname_input.background_color = [1, 1, 1, 1]
        self.author_surname_and_publisher_input.background_color = [1, 1, 1, 1]
        self.amount_of_values_input.background_color = [1, 1, 1, 1]
        self.book_name_input.background_color = [1, 1, 1, 1]
        self.less_than_current.background_color = [1, 1, 1, 1]
        self.more_than_current.background_color = [1, 1, 1, 1]

    def on_leave(self, *args):
        for button in self.search_buttons:
            button.background_color = [1, 1, 1, 1]
        self.choice = 0
        self.clear_search_fields()
        if self.present_fields_screen:
            self.remove_widget(self.present_fields_screen)


screen_manager = ScreenManager()
screen_manager.add_widget(MenuScreen(name="menu"))
screen_manager.add_widget(AddScreen(name="add"))
screen_manager.add_widget(RemoveScreen(name="remove"))
screen_manager.add_widget(ShowScreen(name="show"))


def set_screen(screen_name):
    screen_manager.current = screen_name


class TheLabApp(App):

    def build(self):
        return screen_manager
