import random


class Field:

    def __init__(self):
        self.field = {
            'center': [],
            'south': [],
            'north': [],
            'east': [],
            'west': [],
        }

    def add_to_field(self, creature):
        region = random.choice(list(self.field))
        self.field[region].append(creature)
        self.show_field()

    def show_field(self):
        for key, list_value in self.field.items():
            print(key.capitalize(), end=' - ')
            for value in list_value:
                value.show()
            print('\n')
