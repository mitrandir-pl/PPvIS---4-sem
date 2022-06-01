import random
import emoji

from model.field import Cell
from .animal import Animal


CHANCE_TO_GO_AWAY = 25


class DragonEgg:

    def __init__(self) -> None:
        self._type = 'dragon_egg'
        self._age = 0

    @property
    def type(self) -> str:
        return self._type

    def __str__(self) -> str:
        return emoji.emojize(':egg:')

    def make_decision(self, cell: Cell, egg) -> None:
        if egg._age == 3:
            self.dragon_borning(cell, egg)
        else:
            egg._age += 1

    def dragon_borning(self, cell: Cell, egg) -> None:
        index = cell.creatures.index(egg)
        cell.creatures[index] = Dragon()


class Dragon(Animal):

    def __init__(self) -> None:
        super().__init__()
        self._type = 'dragon'
        self._health = 400

    def __str__(self) -> str:
        return emoji.emojize(':dragon:')

    def make_decision(self, cell: Cell, dragon) -> None:
        if self.is_alive(dragon):
            self.weakening(dragon)
            if dragon._hunger > 10 and dragon._health >= 100:
                if self.cell_controller.is_creature_in_cell(cell, 'bear'):
                    bear = self.cell_controller.get_creature(cell, 'bear')
                    self.trying_to_eat_bear(cell, dragon, bear)
            if dragon._hunger > 9 and dragon._health >= 80:
                if self.cell_controller.is_creature_in_cell(cell, 'boar'):
                    boar = self.cell_controller.get_creature(cell, 'boar')
                    self.trying_to_eat_boar(cell, dragon, boar)
            if dragon._hunger > 8:
                if self.cell_controller.is_creature_in_cell(cell, 'rabbit'):
                    rabbit = self.cell_controller.get_creature(cell, 'rabbit')
                    self.trying_to_eat_rabbit(cell, dragon, rabbit)
            elif dragon._hunger <= 5:
                self.reproduce(cell, dragon)
            if random.randint(0, 100) < CHANCE_TO_GO_AWAY:
                self.move(cell, dragon)
                self.starvation(dragon)
        else:
            self.dyuing(cell, dragon)

    def reproduce(self, cell: Cell, dragon) -> None:
        if cell.has_empty_place():
            partner = self.cell_controller.get_partner(cell, dragon)
            if partner:
                index = cell.get_index_of_empty_place()
                cell.creatures[index] = DragonEgg()

    def weakening(self, dragon) -> None:
        dragon._health -= 30
        dragon._hunger += 1
