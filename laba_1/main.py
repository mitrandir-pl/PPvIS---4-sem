from itertools import count
import os

from file_manager import FileManager
from Interfaces.field_interface import FieldInterface
from cycle import Cycle

if __name__ == "__main__":
    file_manager = FileManager('Field/field.txt')
    forest = file_manager.load()
    field_interface = FieldInterface(forest)
    field_interface.show_field()
    forest_life_cycle = Cycle(forest)
    while True:
        counter = {
            'dragons': 0,
            'bears': 0,
            'boars': 0,
            'rabbits': 0,
            'dragon eggs': 0,
            'bushs': 0,
            'empty': 0,
        }
        forest_life_cycle.life_cycle(counter)
        field_interface.show_field()
        for key, value in counter.items():
            print(f'{key}: {value}')
        check_exit = input()
        if check_exit == 'q':
            raise SystemExit
        os.system('clear')
    file_manager.upload(forest)
