from Field import Field
from laba_1.Bear import Bear


class LoadFromFile:

    @staticmethod
    def begin(file_name):
        forest = Field()
        try:
            with open(file_name, "r") as file:
                for line in file:
                    for creature in line.strip():
                        match creature:
                            case 'B':
                                Bear(forest)
                            case 'W':
                                pass
        except FileNotFoundError:
            print('ERROR. No such file or directory:', file_name)
