import random
from .cell import Cell


class Field:

    def __init__(self) -> None:
        self.area = {
            'center': [],
            'south': [],
            'north': [],
            'east': [],
            'west': [],
        }
        for region in self.area:
            for _ in range(9):
                self.area[region].append(Cell())

    def add_to_field(self, creature):
        for _ in range(3):
            region = random.choice(list(self.area))
            cell = self.area[region][random.randint(0, 8)]
            if not cell.has_empty_place():
                continue
            else:
                index = cell.get_index_of_empty_place()
                cell.add_by_index(index, creature)
                return True

    def add_to_current_region(self, region, creature):
        for cell in self.area[region]:
            if cell.is_empty():
                cell.add(creature)
                break

    def add_to_cell_by_index(self, region, cell_num, index, creature):
        self.area[region][cell_num].add_by_index(index, creature)
