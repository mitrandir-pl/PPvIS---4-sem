import argparse
import os

from controller.cycle import Cycle
from utility.file_manager import FileManager
from view.field_interface import FieldInterface

parser = argparse.ArgumentParser("Choose type of the interface")
parser.add_argument("-c", "--console", action="store_true", help="CLI interface")
parser.add_argument("-g", "--graphic", action="store_true", help="GUI interface")
args = parser.parse_args()


if __name__ == "__main__":
    # if args.console:
    print('Choose variant: ')
    print('1. Generate forest from template file')
    print('2. Continue previous simulation')
    while True:
        choice = input('Enter: ')
        forest = False
        match choice:
            case '1':
                file_manager = FileManager()
                forest = file_manager.load_template()
            case '2':
                file_manager = FileManager()
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
