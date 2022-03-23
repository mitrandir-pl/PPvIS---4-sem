import pickle

from Field.field import Field
from Animals.animals import Bear, Dragon, Rabbit, Boar
from Interfaces.field_interface import FieldInterface
from Plants.plants import Bush


class FileManager:

    def __init__(self, file_name):
        self._file_name = file_name

    def load_template(self) -> Field:
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
            print('ERROR. No such file:', self._file_name)
            return False
        return field

    def load_previous_simulation(self):
        field = Field()
        try:
            with open('Field/field.pickle', 'rb') as f:
                field = pickle.load(f)
        except FileNotFoundError:
            print('ERROR. No file with previous simulation')
            return False
        return field

    def upload(self, field) -> None:
        with open('Field/field.pickle', 'wb') as f:
            pickle.dump(field, f)
