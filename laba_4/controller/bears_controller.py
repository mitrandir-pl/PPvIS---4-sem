import random
import emoji

from model.field import Cell
from .creatures_controller import CreaturesController, Animal


CHANCE_TO_LOOK_AROUND_FOR_BEAR = 100
CHANCE_TO_GO_AWAY = 45


class Bear(Animal):

    def __init__(self) -> None:
        super().__init__()
        self._type = 'bear'
        self._health = 100

    def __str__(self) -> str:
        return emoji.emojize(':bear:')


class BearsController(CreaturesController):

    def make_decision(self, cell: Cell, bear: Bear) -> None:
        if self.is_alive(bear):
            self.weakening(bear)
            if random.randint(0, 100) < CHANCE_TO_LOOK_AROUND_FOR_BEAR:
                if self.cell_controller.is_creature_in_cell(cell, 'dragon'):
                    self.move(cell, bear)
                    self.starvation(bear)
            else:
                if bear._hunger > 9 and bear._health >= 70:
                    if self.cell_controller.is_creature_in_cell(cell, 'boar'):
                        boar = self.cell_controller.get_creature(cell, 'boar')
                        self.trying_to_eat_boar(cell, bear, boar)
                if bear._hunger > 8:
                    if self.cell_controller.is_creature_in_cell(cell, 'bush'):
                        bush = self.cell_controller.get_creature(cell, 'bush')
                        self.eating_bush(cell, bear, bush)
                    elif self.cell_controller.is_creature_in_cell(cell, 'rabbit'):
                        rabbit = self.cell_controller.get_creature(cell, 'rabbit')
                        self.trying_to_eat_rabbit(cell, bear, rabbit)
                elif bear._hunger <= 5:
                    self.reproduce(cell, bear)
                if random.randint(0, 100) < CHANCE_TO_GO_AWAY:
                    self.move(cell, bear)
                    self.starvation(bear)
        else:
            self.dyuing(cell, bear)

    def reproduce(self, cell: Cell, bear: Bear) -> None:
        if cell.has_empty_place():
            partner = self.cell_controller.get_partner(cell, bear)
            if partner:
                index = cell.get_index_of_empty_place()
                cell.creatures[index] = Bear()

    def weakening(self, bear: Bear) -> None:
        bear._health -= 7
        bear._hunger += 1
