import argparse

from controller.cycle import Cycle
from utility.file_manager import FileManager
from view.field_interface import FieldInterface


parser = argparse.ArgumentParser("Choose type of the interface")
parser.add_argument("-p", "--previous", action="store_true", help="Continue previous simulation")
parser.add_argument("-t", "--template", action="store_true", help="Start simulation using template")
parser.add_argument("-a", "--add", help="add a chosen animal in random place")
parser.add_argument("-r", "--region", help="if this attribute is specified, then animal will be added to chosen region")
parser.add_argument("-c", "--cell", help="if this attribute is specified, then animal will be added to chosen cell")
parser.add_argument("-i", "--index", help="if this attribute is specified, then animal will be added to chosen index")
args = parser.parse_args()


def add_animal():
    if args.add:
        match args.add:
            case "bear":
                creature = Bear()
            case "boar":
                creature = Boar()
            case "dragon":
                creature = Dragon()
            case "rabbit":
                creature = Rabbit()
            case "bush":
                creature = Bush()
            case _:
                print("wrong creature input")
                return
        if creature:
            region, cell, index = False, False, False
            if args.add:
                if args.region:
                    if args.region in ["center", "north", "south", "east", "west"]:
                        region = args.region
                    else:
                        print("wrong region input")
                try:
                    if args.cell:
                        if type(int(args.cell)) is int:
                            if -1 < int(args.cell) < 9:
                                cell = int(args.cell)
                            else:
                                print("wrong cell input")
                        else:
                            print("wrong cell input")
                    if args.index:
                        if type(int(args.index)) is int:
                            if -1 < int(args.index) < 9:
                                index = int(args.index)
                            else:
                                print("wrong index input")
                        else:
                            print("wrong index input")
                except TypeError:
                    print("wrong index input")
                if region:
                    if cell:
                        if index:
                            if forest.area[region][cell].creatures[index]:
                                print("chosen place is not empty")
                            else:
                                forest.add_to_cell_by_index(region, cell, index, creature)
                        else:
                            forest.add_to_current_cell(region, cell, creature)
                    else:
                        forest.add_to_current_region(region, creature)
                else:
                    forest.add_to_field(creature)


if __name__ == "__main__":
    if args.template:
        file_manager = FileManager()
        forest = file_manager.load_template()
    elif args.previous:
        file_manager = FileManager()
        forest = file_manager.load_previous_simulation()
    else:
        print("You didn't enter type of simulation")
        raise SystemExit
    add_animal()
    field_interface = FieldInterface(forest)
    field_interface.show_field()
    forest_life_cycle = Cycle(forest)
    forest_life_cycle.life_cycle()
    field_interface.show_field()
    file_manager.upload(forest)
