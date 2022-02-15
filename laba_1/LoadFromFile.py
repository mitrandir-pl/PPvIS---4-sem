from Field import Field
from Bear import Bear
from Dragon import Dragon
from Cycle import Cycle
from Rabbit import Rabbit


class LoadFromFile:

    @staticmethod
    def begin(file_name):
        forest = Field()
        try:
            with open(file_name, "r") as file:
                for key, line in zip(forest.area, file):
                    for creature in line.strip().split():
                        match creature:
                            case 'B':
                                Bear(forest)
                            case 'D':
                                Dragon(forest)
                            case 'R':
                                Rabbit(forest)
                forest.show_field()
                Cycle.life(forest)
        except FileNotFoundError:
            print('ERROR. No such file or directory:', file_name)
