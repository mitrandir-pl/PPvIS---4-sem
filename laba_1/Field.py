import random


class Field:

    def __init__(self):
        self.area = {
            'center': [],
            'south': [],
            'north': [],
            'east': [],
            'west': [],
        }

    def add_to_field(self, creature):
        region = random.choice(list(self.area))
        self.area[region].append(creature)

    def add_to_current_region(self, region, creature):
        self.area[region].append(creature)

    def show_field(self):
        for key, list_value in self.area.items():
            print(key.capitalize(), end=' - ')
            for value in list_value:
                value.show()
            print()

    def set_life_cycles_true(self):
        for key, list_value in self.area.items():
            for value in list_value:
                value.life_cycle = False
