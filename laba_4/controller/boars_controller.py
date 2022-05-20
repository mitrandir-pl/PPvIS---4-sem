import random
import emoji

from model.field import Cell
from .creatures_controller import CreaturesController, Animal


CHANCE_TO_LOOK_AROUND_FOR_BOAR = 20
CHANCE_TO_GO_AWAY = 45


class Boar(Animal):

    def __init__(self) -> None:
        super().__init__()
        self._type = 'boar'
        self._health = 80

    def __str__(self) -> str:
        return emoji.emojize(':boar:')


class BoarsController(CreaturesController):
    
    def make_decision(self, cell: Cell, boar: Boar) -> None:
        if self.is_alive(boar):
            self.weakening(boar)
            if random.randint(0, 100) < CHANCE_TO_LOOK_AROUND_FOR_BOAR:
                if self.cell_controller.is_creature_in_cell(cell, 'dragon'):
                    self.move(cell, boar)
                    self.starvation(boar)
                elif self.cell_controller.is_creature_in_cell(cell, 'bear'):
                    self.move(cell, boar)
                    self.starvation(boar)
            else:
                if boar._hunger > 8:
                    if self.cell_controller.is_creature_in_cell(cell, 'rabbit'):
                        rabbit = self.cell_controller.get_creature(cell, 'rabbit')
                        self.trying_to_eat_rabbit(cell, boar, rabbit)
                elif boar._hunger <= 8:
                    self.reproduce(cell, boar)
                if random.randint(0, 100) < CHANCE_TO_GO_AWAY:
                    self.move(cell, boar)
                    self.starvation(boar)
        else:
            self.dyuing(cell, boar)

    def reproduce(self, cell: Cell, boar: Boar) -> None:
        if cell.has_empty_place():
            partner = self.cell_controller.get_partner(cell, boar)
            if partner:
                index = cell.get_index_of_empty_place()
                cell.creatures[index] = Boar()

    def weakening(self, boar: Boar) -> None:
        boar._health -= 22
        boar._hunger += 1
