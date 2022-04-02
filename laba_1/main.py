import os

from Field.field import Field
from file_manager import FileManager
from Interfaces.field_interface import FieldInterface
from cycle import Cycle

if __name__ == "__main__":
    print('Choose variant: ')
    print('1. Generate forest from template file')
    print('2. Continue previous simulation')
    while True:
        choice = input('Enter: ')
        forest = False
        match choice:
            case '1':
                file_manager = FileManager('Field/field.txt')
                forest = file_manager.load_template()
            case '2':
                file_manager = FileManager('Field/field.pickle')
                forest = file_manager.load_previous_simulation()
            case _:
                print('Wrong input!!!')
        if forest:
            break
    field_interface = FieldInterface(forest)
    field_interface.show_field()
    forest_life_cycle = Cycle(forest)
    while True:
        forest_life_cycle.life_cycle()
        field_interface.show_field()
        print('To exit enter q:', end=' ')
        check_exit = input()
        if check_exit == 'q':
            file_manager.upload(forest)
            raise SystemExit
        os.system('clear')
