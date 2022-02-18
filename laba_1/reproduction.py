CAN_NOT_REPRODUCE = ('empty place', )


class Reproduction:

    @staticmethod
    def reproduction(field):
        for region, list_of_cells in field.area.items():
            for cell_num, cell in enumerate(list_of_cells):
                creatures_copy = cell.creatures.copy()
                for creature in creatures_copy:
                    if creature.type not in CAN_NOT_REPRODUCE:
                        if creature.life_cycle is False:
                            creature.reproduce(field, region, cell_num)
