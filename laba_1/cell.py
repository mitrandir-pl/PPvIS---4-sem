class Cell:

    def __init__(self):
        self.creatures = []

    def show(self):
        for creature in self.creatures:
            creature.show()
        print()

    def add(self, creature):
        self.creatures.append(creature)

    def add_by_index(self, index, creature):
        self.creatures[index] = creature

    def is_empty(self):
        return len(self.creatures) < 5

    def has_empty_place(self):
        for index, creature in enumerate(self.creatures):
            if creature.type == 'empty place':
                return True

    def get_index_of_empty_place(self):
        for index, creature in enumerate(self.creatures):
            if creature.type == 'empty place':
                return index

    def get_partner(self, animal):
        gender_for_search = 'male' if animal.sex == 'female' else 'female'
        for creature in self.creatures:
            if animal.type == creature.type and animal is not creature:
                if creature.sex == gender_for_search:
                    return creature
