import pickle

from model.creatures.bear import Bear
from model.creatures.boar import Boar
from model.creatures.rabbit import Rabbit
from model.creatures.dragon import Dragon, DragonEgg
from model.creatures.bush import Bush
from model.field import Field


class FileManager:

    def load_template(self) -> Field:
        field = Field()
        try:
            with open("field store/field.txt", "r") as file:
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
            return False
        return field

    def load_previous_simulation(self) -> Field:
        try:
            with open('field store/field.pickle', 'rb') as f:
                field = pickle.load(f)
        except FileNotFoundError:
            print("No file with previous simulation!!!")
            raise SystemExit
        return field

    def upload(self, field: Field) -> None:
        with open('field store/field.pickle', 'wb') as f:
            pickle.dump(field, f)
