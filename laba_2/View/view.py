from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from Controller.controller import Controller


class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        box_layout = BoxLayout(orientation="vertical")
        menu_label = Label(text="Menu", font_size=30)
        add_button = Button(text="Add", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                            on_press=lambda x: set_screen("add"), background_color=[1, 0, 1, 1])
        remove_button = Button(text="Delete", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                               on_press=lambda x: set_screen("remove"), background_color=[1, 0, 1, 1])
        show_button = Button(text="Show", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                             on_press=lambda x: set_screen("show"), background_color=[1, 0, 1, 1])
        box_layout.add_widget(menu_label)
        box_layout.add_widget(add_button)
        box_layout.add_widget(remove_button)
        box_layout.add_widget(show_button)
        self.add_widget(box_layout)


class AddScreen(Screen):
    def __init__(self, **kw):
        super(AddScreen, self).__init__(**kw)

        self._controller = Controller()

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

        create_button = Button(text="Create ->", on_press=lambda x: self.create_field(),
                               background_color=[0.11, .12, 0.76, 1])
        back_button = Button(text="<- Back", on_press=lambda x: set_screen("menu"),
                             background_color=[0.11, .12, 0.76, 1])

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
        added_fields.add_widget(back_button)
        added_fields.add_widget(create_button)

        self.add_widget(added_fields)

    def on_enter(self, *args):
        pass

    def on_leave(self, *args):
        pass

    def create_field(self):
        pass


class RemoveScreen(Screen):
    def __init__(self, **kw):
        super(RemoveScreen, self).__init__(**kw)

        self.choice = 0
        select_remove = BoxLayout(orientation="vertical")
        self.menu_label = Label(text="Deleting by:", font_size=30)
        fio_author_remove_button = Button(
            text="Author", font_size=30, on_press=lambda x: self.set_choice(1))
        author_and_publisher_remove_button = Button(
            text="Author and Publisher", font_size=30, on_press=lambda x: self.set_choice(2))
        amount_of_volumes_remove_button = Button(
            text="Amount of volumes", font_size=30, on_press=lambda x: self.set_choice(3))
        book_name_remove_button = Button(
            text="Book Name", font_size=30, on_press=lambda x: self.set_choice(4))
        less_than_specified_amount_remove_button = Button(
            text="Less than specified amount of volumes", font_size=30, on_press=lambda x: self.set_choice(5))
        more_than_specified_amount_remove_button = Button(
            text="More than specified amount of volumes", font_size=30, on_press=lambda x: self.set_choice(5))
        self.remove_input = TextInput()
        go_back_buttons = BoxLayout()
        remove_button = Button(text="Remove ->", on_press=lambda x: self.remove_field(),
                               background_color=[0.11, .12, 0.76, 1])
        back_button = Button(text="<- Back", on_press=lambda x: set_screen("menu"),
                             background_color=[0.11, .12, 0.76, 1])
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

    def set_choice(self, choice):
        self.choice = choice


class ShowScreen(Screen):
    fields_on_screens = 10

    def __init__(self, **kw):
        super(ShowScreen, self).__init__(**kw)

        self.list_of_screens = []
        self.index_of_screen = 0
        self.present_fields_screen = None

        test_layout = AnchorLayout(anchor_x='left', anchor_y="top")
        travel_layout = AnchorLayout(anchor_x='left', anchor_y="bottom")
        bl = BoxLayout(orientation="vertical", padding=[0, 0, 0, 0])
        gl2 = GridLayout(cols=6)
        fio_patient = Button(text="ФИО пациента", size_hint_x=None, width=200, size_hint_y=None, height=80, background_color=[0, 1, 0, 1])
        place_of_residence = Button(text="Адрес прописки", size_hint_y=None, height=80, background_color=[0, 1, 0, 1])
        date_of_birth = Button(text="Дата рождения", size_hint_y=None, height=80, background_color=[0, 1, 0, 1])
        date_of_receipt = Button(text="Дата приема", size_hint_y=None, height=80, background_color=[0, 1, 0, 1])
        fio_doctor = Button(text="ФИО врача", size_hint_x=None, width=200, size_hint_y=None, height=80, background_color=[0, 1, 0, 1])
        conclusion = Button(text="Заключение", size_hint_y=None, height=80, background_color=[0, 1, 0, 1])

        gl2.add_widget(fio_patient)
        gl2.add_widget(place_of_residence)
        gl2.add_widget(date_of_birth)
        gl2.add_widget(date_of_receipt)
        gl2.add_widget(fio_doctor)
        gl2.add_widget(conclusion)

        bl2 = BoxLayout()
        number_of_page_boxlayout = BoxLayout(orientation="vertical")
        index_of_page_boxlayout = BoxLayout(orientation="vertical")
        number_of_elements_boxlayout = BoxLayout(orientation="vertical")

        back_button = Button(text="<- Back", on_press=lambda x: set_screen("menu"),
                             size_hint_y=None, height=80, background_color=[0.11, .12, 0.76, 1])
        first_page_button = Button(text="First page", on_press=lambda x: self.set_present_fields_screen(0),
                                   size_hint_y=None, height=80, background_color=[0.11, .12, 0.76, 1])
        last_page_button = Button(text="Last page",
                                  on_press=lambda x: self.set_present_fields_screen(len(self.list_of_screens) - 1),
                                  size_hint_y=None, height=80, background_color=[0.11, .12, 0.76, 1])
        next_page_button = Button(text="Next page",
                                  on_press=lambda x: self.set_present_fields_screen(self.index_of_screen + 1),
                                  size_hint_y=None, height=80, background_color=[0.11, .12, 0.76, 1])
        past_page_button = Button(text="Past page",
                                  on_press=lambda x: self.set_present_fields_screen(self.index_of_screen - 1),
                                  size_hint_y=None, height=80, background_color=[0.11, .12, 0.76, 1])
        number_of_page_text = Button(text="№ page",
                                  size_hint_y=None, height=40, background_color=[0.11, .12, 0.76, 1])
        index_of_page_text = Button(text="Count pages",
                                  size_hint_y=None, height=40, background_color=[0.11, .12, 0.76, 1])
        number_of_elements_text = Button(text="Count el",
                                  size_hint_y=None, height=40, background_color=[0.11, .12, 0.76, 1])
        self.number_of_page_text = Button(text=str(self.index_of_screen),
                                     size_hint_y=None, height=40, background_color=[0.11, .12, 0.76, 1])
        self.index_of_page_text = Button(text=str(len(self.list_of_screens)),
                                    size_hint_y=None, height=40, background_color=[0.11, .12, 0.76, 1])
        # self.number_of_elements_text = Button(text=str(len(list_of_fields)),
        #                                  size_hint_y=None, height=40, background_color=[0.11, .12, 0.76, 1])

        number_of_page_boxlayout.add_widget(number_of_page_text)
        number_of_page_boxlayout.add_widget(self.number_of_page_text)

        index_of_page_boxlayout.add_widget(index_of_page_text)
        index_of_page_boxlayout.add_widget(self.index_of_page_text)

        # number_of_elements_boxlayout.add_widget(number_of_elements_text)
        # number_of_elements_boxlayout.add_widget(self.number_of_elements_text)

        bl2.add_widget(back_button)
        bl2.add_widget(first_page_button)
        bl2.add_widget(past_page_button)
        bl2.add_widget(next_page_button)
        bl2.add_widget(last_page_button)
        bl2.add_widget(number_of_page_boxlayout)
        bl2.add_widget(index_of_page_boxlayout)
        bl2.add_widget(number_of_elements_boxlayout)
        travel_layout.add_widget(bl2)
        test_layout.add_widget(gl2)
        self.add_widget(travel_layout)
        self.add_widget(test_layout)

    # def on_enter(self):
    #
    #     # 720 - 180
    #     self.list_of_screens = []
    #     self.index_of_screen = 0
    #     self.number_of_elements_text.text = str(len(list_of_fields))
    #     counter_of_screens = ShowScreen.fields_on_screens
    #     number_of_screens = 0
    #     gl1 = GridLayout(cols=6, padding=[0, 80, 0, 80], row_force_default=True,
    #                      row_default_height=(720 - 160) / ShowScreen.fields_on_screens)
    #     for field in list_of_fields:
    #         if ShowScreen.fields_on_screens == counter_of_screens:
    #             counter_of_screens = 0
    #             gl1 = GridLayout(cols=6, padding=[0, 80, 0, 80], row_force_default=True,
    #                              row_default_height=(720 - 160) / 10)
    #             self.list_of_screens.append(gl1)
    #             number_of_screens += 1
    #
    #         gl1.add_widget(Button(text=field.name_patient, font_size=12, size_hint_x=None, width=200))
    #         gl1.add_widget(Button(text=field.place_of_residence, font_size=12))
    #         gl1.add_widget(Button(text=str(field.date_of_birth), font_size=12))
    #         gl1.add_widget(Button(text=str(field.date_of_receipt), font_size=12))
    #         gl1.add_widget(Button(text=field.name_doctor, font_size=12, size_hint_x=None, width=200))
    #         gl1.add_widget(Button(text=field.conclusion, font_size=12))
    #         counter_of_screens += 1
    #
    #     self.present_fields_screen = self.list_of_screens[self.index_of_screen]
    #     self.number_of_page_text.text = str(self.index_of_screen + 1)
    #     self.index_of_page_text.text = str(len(self.list_of_screens))
    #     self.add_widget(self.present_fields_screen)
    #
    # def set_present_fields_screen(self, index_of_screen):
    #     if -1 < index_of_screen < len(self.list_of_screens):
    #         self.index_of_screen = index_of_screen
    #         self.remove_widget(self.present_fields_screen)
    #         self.present_fields_screen = self.list_of_screens[index_of_screen]
    #         self.add_widget(self.present_fields_screen)
    #         self.number_of_page_text.text = str(self.index_of_screen + 1)
    #         # self.add_widget(self.list_of_screens[index_of_screen])
    #
    # def on_leave(self, *args):
    #     self.remove_widget(self.present_fields_screen)


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
