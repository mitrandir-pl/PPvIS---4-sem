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

    # def get_partner(self, animal):
    #     gender_for_search = 'male' if animal.sex == 'female' else 'female'
    #     for creature in self.creatures:
    #         if animal.type == creature.type and animal is not creature:
    #             if creature.sex == gender_for_search:
    #                 return creature
