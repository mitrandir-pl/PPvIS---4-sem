from Field.field import Field
from Animals.bear import Bear
from Animals.dragon import Dragon
from cycle import Cycle
from empty_place import EmptyPlace
from Animals.rabbit import Rabbit
from Animals.boar import Boar
from Plants.bash import Bash


class FileManager:

    @staticmethod
    def load(file_name: str) -> None:
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
    def upload(file_name: str) -> None:
        pass
