class FieldInterface:

    def __init__(self, field):
        self.field = field

    def show_field(self):
        for key, list_of_cells in self.field.area.items():
            print(key.capitalize(), end=':\n')
            for num, cell in enumerate(list_of_cells, start=1):
                print(num, end=' - ')
                for creature in cell.creatures:
                    print(creature, end=' ')
                print()
            print()
