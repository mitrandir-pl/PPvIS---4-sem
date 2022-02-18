class Nutrition:

    @staticmethod
    def eating(field):
        lists_of_cells = field.area.values()
        for list_of_cells in lists_of_cells:
            for cell in list_of_cells:
                for creature in cell.creatures.copy():
                    # creature.eat(cell)
                    pass
