import os


class Movement:

    @staticmethod
    def moving(field):
        lists_of_cells = field.area.values()
        for list_of_cells in lists_of_cells:
            for cell in list_of_cells:
                index = 0
                for creature in cell.creatures.copy():
                    if creature.life_cycle is False:
                        field.add_to_field(cell.creatures.pop(index))
                        creature.life_cycle = True

                    else:
                        index += 1
