from field import Field
from bear import Bear
from dragon import Dragon
from cycle import Cycle
from empty_place import EmptyPlace
from rabbit import Rabbit
from boar import Boar
from bash import Bash


class FileManager:

    @staticmethod
    def load(file_name):
        forest = Field()
        try:
            with open(file_name, "r") as file:
                for region, line in zip(forest.area, file):
                    for creature in line.strip().split():
                        match creature:
                            case 'Bear':
                                forest.add_to_current_region(region, Bear())
                            case 'Dragon':
                                forest.add_to_current_region(region, Dragon())
                            case 'Rabbit':
                                forest.add_to_current_region(region, Rabbit())
                            case 'Boar':
                                forest.add_to_current_region(region, Boar())
                            case 'Bash':
                                forest.add_to_current_region(region, Bash())
                            case 'Empty':
                                forest.add_to_current_region(region, EmptyPlace())
                forest.show_field()
                Cycle.life(forest)
        except FileNotFoundError:
            print('ERROR. No such file or directory:', file_name)

    @staticmethod
    def upload(file_name):
        pass
