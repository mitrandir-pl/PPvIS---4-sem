import random

from Animals.animals import Dragon, DragonEgg
from Field.cell import Cell
from .creatures_controller import CreaturesController


class DragonsController(CreaturesController):

    def make_decision(self, cell: Cell, dragon: Dragon) -> None:
        if self.is_alive(dragon):
            self.weakening(dragon)
            if dragon._hunger > 7 and dragon._health >= 100:
                if self.cell_controller.is_creature_in_cell(cell, 'bear'):
                    bear = self.cell_controller.get_creature(cell, 'bear')
                    self.trying_to_eat_bear(cell, dragon, bear)
            if dragon._hunger > 6 and dragon._health >= 80:
                if self.cell_controller.is_creature_in_cell(cell, 'boar'):
                    boar = self.cell_controller.get_creature(cell, 'boar')
                    self.trying_to_eat_boar(cell, dragon, boar)
            if dragon._hunger > 5:
                if self.cell_controller.is_creature_in_cell(cell, 'rabbit'):
                    rabbit = self.cell_controller.get_creature(cell, 'rabbit')
                    self.trying_to_eat_rabbit(cell, dragon, rabbit)
            elif dragon._hunger <= 5:
                self.reproduce(cell, dragon)
            if random.randint(1, 2) == random.randint(1, 2):
                self.move(cell, dragon)
                self.starvation(dragon)
        else:
            self.dyuing(cell, dragon)

    def reproduce(self, cell: Cell, dragon: Dragon):
        if cell.has_empty_place():
            partner = self.cell_controller.get_partner(cell, dragon)
            if partner:
                index = cell.get_index_of_empty_place()
                cell.creatures[index] = DragonEgg()

    def weakening(self, bear: Dragon):
        bear._health -= 10
        bear._hunger += 1
