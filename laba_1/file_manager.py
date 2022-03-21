import pickle

from Field.field import Field
from Animals.animals import Bear, Dragon, Rabbit, Boar
from Plants.plants import Bush


class FileManager:

    def __init__(self, file_name):
        self._file_name = file_name

    def load(self) -> Field:
        field = Field()
        try:
            with open(self._file_name, "r") as file:
                for region, line in zip(field.area, file):
                    for creature in line.strip().split():
                        match creature:
                            case 'Bear':
                                field.add_to_current_region(region, Bear())
                            case 'Dragon':
                                field.add_to_current_region(region, Dragon())
                            case 'Rabbit':
                                field.add_to_current_region(region, Rabbit())
                            case 'Boar':
                                field.add_to_current_region(region, Boar())
                            case 'Bush':
                                field.add_to_current_region(region, Bush())
                            case 'None':
                                field.add_to_current_region(region, None)
        except FileNotFoundError:
            print('ERROR. No such file or directory:', self._file_name)
        # try:
        #     with open('data.pickle', 'rb') as f:
        #         field = pickle.load(f)
        # except FileNotFoundError:
        #     print('ERROR. No such file or directory:', self._file_name)
        # interface = FieldInterface(field)
        # interface.show_field()
        return field

    def upload(self, field) -> None:
        with open('data.pickle', 'wb') as f:
            pickle.dump(field, f)
