from model.field import Cell


class CellsController:

    def is_creature_in_cell(self, cell: Cell, creature_type: str) -> bool:
        for creature in cell.creatures:
            if creature:
                if creature.type == creature_type:
                    return True

    def get_creature(self, cell, creature_type):
        for creature in cell.creatures:
            if creature:
                if creature.type == creature_type:
                    return creature

    def get_partner(self, cell: Cell, animal):
        sex_for_search = 'male' if animal.sex == 'female' else 'female'
        for creature in cell.creatures:
            if creature:
                if animal.type == creature.type and animal is not creature:
                    if creature.sex == sex_for_search:
                        return creature

    def get_victim_place(self, cell, victim):
        return cell.creatures.index(victim)

    def move_to_victim_place(self, cell, creature, new_place):
        creature_index = cell.creatures.index(creature)
        cell.creatures[creature_index] = None
        cell.creatures[new_place] = creature
