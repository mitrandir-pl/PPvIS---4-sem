import random
import emoji

from model.field import Cell
from .creatures_controller import CreaturesController, Animal

CHANCE_TO_LOOK_AROUND_FOR_RABBIT = 25
CHANCE_TO_GO_AWAY = 25


class Rabbit(Animal):

    def __init__(self) -> None:
        super().__init__()
        self._type = 'rabbit'
        self._health = 70

    def __str__(self) -> str:
        return emoji.emojize(':rabbit_face:')


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
                if rabbit._hunger > 2:
                    if self.cell_controller.is_creature_in_cell(cell, 'bush'):
                        bush = self.cell_controller.get_creature(cell, 'bush')
                        self.eating_bush(cell, rabbit, bush)
                elif rabbit._hunger <= 2:
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
        rabbit._health -= 30
        rabbit._hunger += 1
