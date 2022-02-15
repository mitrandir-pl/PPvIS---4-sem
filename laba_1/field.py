import random
from cell import Cell


class Field:

    def __init__(self):
        self.area = {
            'center': [],
            'south': [],
            'north': [],
            'east': [],
            'west': [],
        }
        for region in self.area:
            for _ in range(5):
                self.area[region].append(Cell())

    def add_to_field(self, creature):
        region = random.choice(list(self.area))
        self.area[region][random.randint(0, 4)].add(creature)

    def add_to_current_region(self, region, creature):
        self.area[region][random.randint(0, 4)].add(creature)

    def show_field(self):
        for key, list_of_cells in self.area.items():
            print(key.capitalize(), end=':\n')
            for num, cell in enumerate(list_of_cells, start=1):
                print(num, end=' - ')
                cell.show()
            print()

    def set_life_cycles_true(self):
        for lists_of_cells in self.area.values():
            for cell in lists_of_cells:
                for creature in cell.creatures:
                    creature.life_cycle = False
