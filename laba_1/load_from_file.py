from field import Field
from bear import Bear
from dragon import Dragon
from cycle import Cycle
from rabbit import Rabbit


class LoadFromFile:

    @staticmethod
    def begin(file_name):
        forest = Field()
        try:
            with open(file_name, "r") as file:
                for region, line in zip(forest.area, file):
                    for creature in line.strip().split():
                        match creature:
                            case 'B':
                                Bear(forest, region)
                            case 'D':
                                Dragon(forest, region)
                            case 'R':
                                Rabbit(forest, region)
                forest.show_field()
                Cycle.life(forest)
        except FileNotFoundError:
            print('ERROR. No such file or directory:', file_name)
