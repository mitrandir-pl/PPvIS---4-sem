import argparse
import os

from controller.cycle import Cycle
from utility.file_manager import FileManager
from view.field_interface import FieldInterface

parser = argparse.ArgumentParser("Choose type of the interface")
parser.add_argument("-p", "--previous", action="store_true", help="Continue previous simulation")
parser.add_argument("-t", "--template", action="store_true", help="Start simulation using template")
args = parser.parse_args()


if __name__ == "__main__":
    if args.template:
        file_manager = FileManager()
        forest = file_manager.load_template()
    elif args.previous:
        file_manager = FileManager()
        forest = file_manager.load_previous_simulation()
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
