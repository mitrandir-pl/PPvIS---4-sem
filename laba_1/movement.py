from empty_place import EmptyPlace


CAN_NOT_MOVE = ('plant', 'empty place')


class Movement:

    @staticmethod
    def moving(field):
        for region, list_of_cells in field.area.items():
            for cell_num, cell in enumerate(list_of_cells):
                creatures_copy = cell.creatures.copy()
                for creature in creatures_copy:
                    if creature.type not in CAN_NOT_MOVE:
                        if creature.life_cycle is False:
                            index = creatures_copy.index(creature)
                            if creature.move(field):
                                field.add_to_cell_by_index(
                                    region, cell_num, index,
                                    EmptyPlace()
                                )
