import random

from Animals.animals import Rabbit
from Controllers.bears_controller import CHANCE_TO_LOOK_AROUND_FOR_BEAR
from Field.cell import Cell

from .creatures_controller import CreaturesController


CHANCE_TO_LOOK_AROUND_FOR_RABBIT = 35
CHANCE_TO_GO_AWAY = 25


class RabbitsController(CreaturesController):
    
    def make_decision(self, cell: Cell, rabbit: Rabbit) -> None:
        if self.is_alive(rabbit):
            self.weakening(rabbit)
            if random.randint(0, 100) < CHANCE_TO_LOOK_AROUND_FOR_RABBIT:
                if self.cell_controller.is_creature_in_cell(cell, 'boar'):
                    self.move(cell, rabbit)
                elif self.cell_controller.is_creature_in_cell(cell, 'bear'):
                    self.move(cell, rabbit)
                elif self.cell_controller.is_creature_in_cell(cell, 'dragon'):
                    self.move(cell, rabbit)
            else:
                if rabbit._hunger > 7:
                    if self.cell_controller.is_creature_in_cell(cell, 'bush'):
                        bush = self.cell_controller.get_creature(cell, 'bush')
                        self.eating_bush(cell, rabbit, bush)
                elif rabbit._hunger <= 7:
                    for _ in range(3):
                        self.reproduce(cell, rabbit)
                if random.randint(0, 100) < CHANCE_TO_GO_AWAY:
                    self.move(cell, rabbit)
                    self.starvation(rabbit)
        else:
            self.dyuing(cell, rabbit)

    def reproduce(self, cell: Cell, rabbit: Rabbit) -> None:
        if cell.has_empty_place():
            partner = self.cell_controller.get_partner(cell, rabbit)
            if partner:
                index = cell.get_index_of_empty_place()
                cell.creatures[index] = Rabbit()

    def weakening(self, rabbit: Rabbit) -> None:
        rabbit._health -= 18
        rabbit._hunger += 1
