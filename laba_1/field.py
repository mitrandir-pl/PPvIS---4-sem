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
        for _ in range(5):
            region = random.choice(list(self.area))
            cell = self.area[region][random.randint(0, 4)]
            cell.has_empty_place()
            if cell.has_empty_place() is None:
                continue
            else:
                index = cell.get_index_of_empty_place()
                cell.add_by_index(index, creature)
                break

    def add_to_current_region(self, region, creature):
        for cell in self.area[region]:
            if cell.is_empty():
                cell.add(creature)
                break

    def add_to_cell_by_index(self, region, cell_num, index, creature):
        self.area[region][cell_num].add_by_index(index, creature)

    def show_field(self):
        for key, list_of_cells in self.area.items():
            print(key.capitalize(), end=':\n')
            for num, cell in enumerate(list_of_cells, start=1):
                print(num, end=' - ')
                cell.show()
            print()

    def set_life_cycles_false(self):
        for lists_of_cells in self.area.values():
            for cell in lists_of_cells:
                for creature in cell.creatures:
                    creature.life_cycle = False
