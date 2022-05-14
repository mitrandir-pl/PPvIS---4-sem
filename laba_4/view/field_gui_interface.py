from kivy.config import Config
from kivy.uix.label import Label


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '890')
Config.set('graphics', 'height', '890')

from kivy.app import App
from utility.file_manager import FileManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from controller.cycle import Cycle

RED = [1, 0, 0, 1]
GREEN = [0, 1, 0, 1]
BLUE = [0, 0, 1, 1]
ORANGE = [236/255, 146/255, 31/255, .8]
YELLOW = [1, 1, 0, 1]
GRAY = [1, 1, 1, 1]


class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)

        box_layout = BoxLayout(orientation="vertical")
        add_button = Button(text="Previous simulation", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                            on_press=lambda x: self.choice_simulation("previous", add_button), background_color=ORANGE)
        remove_button = Button(text="Simulation from template", font_size=30, size_hint=(.5, 1),
                               pos_hint={"center_x": .5},
                               on_press=lambda x: self.choice_simulation("template", remove_button),
                               background_color=ORANGE)
        exit_button = Button(text="Exit", font_size=30, size_hint=(.5, 1), pos_hint={"center_x": .5},
                             on_press=lambda x: self.exit_program(), background_color=ORANGE)
        box_layout.add_widget(add_button)
        box_layout.add_widget(remove_button)
        box_layout.add_widget(exit_button)
        self.add_widget(box_layout)


    def choice_simulation(self, simulation_type, choice_button):
        match simulation_type:
            case "previous":
                file_manager = FileManager()
                forest = file_manager.load_previous_simulation()
                if not forest:
                    choice_button.disabled = True
                    choice_button.text = "No previous simulation"
                    return
            case "template":
                file_manager = FileManager()
                forest = file_manager.load_template()

        screen_manager.add_widget(SimulationInterface(forest, name="simulation"))
        set_screen("simulation")

    def exit_program(self):
        raise SystemExit


class SimulationInterface(Screen):
    def __init__(self, field, **kw):
        super(SimulationInterface, self).__init__(**kw)
        self.north_region = GridLayout(cols=3, padding=[300, 0, 300, 600])
        self.field = field
        self.file_manager = FileManager()
        self.forest_life_cycle = Cycle(field)
        self.list_of_widgets = []
        self.show_simulation()
        self.control_buttons = BoxLayout(padding=[650, 800, 0, 0])
        exit_ = Button(text="quit", background_color=YELLOW, on_press=lambda x: self.exit_program())
        continue_simulation = Button(text="continue", background_color=YELLOW, on_press=lambda x: self.continue_simulation())
        self.control_buttons.add_widget(exit_)
        self.control_buttons.add_widget(continue_simulation)
        self.add_widget(self.control_buttons)

    def show_simulation(self):
        self.print_north()
        self.print_east()
        self.print_center()
        self.print_west()
        self.print_south()

    def print_north(self) -> None:
        left_indent = 300
        top_indent = 0
        right_indent = 500
        bottom_indent = 800
        for index, cell in enumerate(self.field.area["north"]):
            if index != 0:
                left_indent += 100
                right_indent -= 100
                if index % 3 == 0:
                    top_indent += 100
                    bottom_indent -= 100
                    left_indent = 300
                    right_indent = 500
            self.fullness_region(cell, left_indent, top_indent,
                                 right_indent, bottom_indent)

    def print_east(self) -> None:
        left_indent = 0
        top_indent = 300
        right_indent = 800
        bottom_indent = 500
        for index, cell in enumerate(self.field.area["east"]):
            if index != 0:
                left_indent += 100
                right_indent -= 100
                if index % 3 == 0:
                    top_indent += 100
                    bottom_indent -= 100
                    left_indent = 0
                    right_indent = 800
            self.fullness_region(cell, left_indent, top_indent,
                                 right_indent, bottom_indent)

    def print_center(self) -> None:
        left_indent = 300
        top_indent = 300
        right_indent = 500
        bottom_indent = 500
        for index, cell in enumerate(self.field.area["center"]):
            if index != 0:
                left_indent += 100
                right_indent -= 100
                if index % 3 == 0:
                    top_indent += 100
                    bottom_indent -= 100
                    left_indent = 300
                    right_indent = 500
            self.fullness_region(cell, left_indent, top_indent,
                                 right_indent, bottom_indent)

    def print_west(self) -> None:
        left_indent = 600
        top_indent = 300
        right_indent = 200
        bottom_indent = 500
        for index, cell in enumerate(self.field.area["west"]):
            if index != 0:
                left_indent += 100
                right_indent -= 100
                if index % 3 == 0:
                    top_indent += 100
                    bottom_indent -= 100
                    left_indent = 600
                    right_indent = 200
            self.fullness_region(cell, left_indent, top_indent,
                                 right_indent, bottom_indent)

    def print_south(self) -> None:
        left_indent = 300
        top_indent = 600
        right_indent = 500
        bottom_indent = 200
        for index, cell in enumerate(self.field.area["south"]):
            if index != 0:
                left_indent += 100
                right_indent -= 100
                if index % 3 == 0:
                    top_indent += 100
                    bottom_indent -= 100
                    left_indent = 300
                    right_indent = 500
            self.fullness_region(cell, left_indent, top_indent,
                                 right_indent, bottom_indent)

    def fullness_region(self, cell, left_indent, top_indent, right_indent, bottom_indent):
        cell_grid_layout = GridLayout(cols=3, padding=[left_indent, top_indent, right_indent, bottom_indent])
        self.list_of_widgets.append(cell_grid_layout)
        for creature in cell.creatures:
            if creature:
                match creature.type:
                    case 'bear':
                        bear = Image(source="view/images/bear.png")
                        cell_grid_layout.add_widget(bear)
                    case 'dragon':
                        dragon = Image(source="view/images/dragon.png")
                        cell_grid_layout.add_widget(dragon)
                    case 'rabbit':
                        rabbit = Image(source="view/images/rabbit.png")
                        cell_grid_layout.add_widget(rabbit)
                    case 'boar':
                        boar = Image(source="view/images/boar.png")
                        cell_grid_layout.add_widget(boar)
                    case 'bush':
                        bush = Image(source="view/images/bush.png")
                        cell_grid_layout.add_widget(bush)
                    case 'dragon_egg':
                        dragon_egg = Image(source="view/images/dragon_egg.png")
                        cell_grid_layout.add_widget(dragon_egg)
            else:
                empty = Label()
                cell_grid_layout.add_widget(empty)
        self.add_widget(cell_grid_layout)

    def continue_simulation(self):
        for widget in self.list_of_widgets:
            self.remove_widget(widget)
        self.forest_life_cycle.life_cycle()
        self.show_simulation()


    def exit_program(self):
        self.file_manager.upload(self.field)
        raise SystemExit


screen_manager = ScreenManager()
screen_manager.add_widget(MenuScreen(name="menu"))


def set_screen(screen_name):
    screen_manager.current = screen_name


class TheLabApp(App):

    def build(self):
        Window.clearcolor = (124/255, 136/255, 2/255, .8)
        return screen_manager
