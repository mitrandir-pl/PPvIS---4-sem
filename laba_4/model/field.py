import random


class Cell:

    def __init__(self) -> None:
        self.creatures = []

    def add(self, creature):
        self.creatures.append(creature)

    def add_by_index(self, index, creature):
        self.creatures[index] = creature

    def is_empty(self):
        return len(self.creatures) < 9

    def has_empty_place(self):
        for creature in self.creatures:
            if creature is None:
                return True
        return False

    def get_index_of_empty_place(self):
        for index, creature in enumerate(self.creatures):
            if creature is None:
                return index

    def is_creature_in_cell(self, creature_type: str) -> bool:
        for creature in self.creatures:
            if creature:
                if creature.type == creature_type:
                    return True

    def get_creature(self, creature_type):
        for creature in self.creatures:
            if creature:
                if creature.type == creature_type:
                    return creature

    def get_partner(self, animal):
        sex_for_search = 'male' if animal.sex == 'female' else 'female'
        for creature in self.creatures:
            if creature:
                if animal.type == creature.type and animal is not creature:
                    if creature.sex == sex_for_search:
                        return creature

    def get_victim_place(self, victim):
        return self.creatures.index(victim)

    def move_to_victim_place(self, creature, new_place):
        creature_index = self.creatures.index(creature)
        self.creatures[creature_index] = None
        self.creatures[new_place] = creature


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
