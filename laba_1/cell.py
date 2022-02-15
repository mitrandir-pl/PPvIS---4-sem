class Cell:

    def __init__(self):
        self.creatures = []

    def show(self):
        for creature in self.creatures:
            creature.show()
        print()

    def add(self, creature):
        self.creatures.append(creature)
