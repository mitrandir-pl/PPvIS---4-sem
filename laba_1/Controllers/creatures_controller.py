import random
from abc import ABC, abstractmethod

from Animals.animals import Animal
from Controllers.cells_controller import CellsController, CellsController
from Field.cell import Cell
from Field.field import Field


RABBIT_RUN_AWAY_CHANCE = 50


class CreaturesController(ABC):

    def __init__(self, cells_controller: CellsController,
                 field: Field) -> None:
        self.cell_controller = cells_controller
        self._field = field

    @abstractmethod
    def make_decision(self, cell: Cell, creature: Animal):
        pass

    def trying_to_eat_bear(self, cell, eater, bear):
        if eater._health >= bear._health:
            self.eating(cell, eater, bear)
            eater._health += 30
            eater._hunger -= 10
        else:
            eater._health -= 30


    def trying_to_eat_boar(self, cell, eater, boar):
        if eater._health >= boar._health:
            self.eating(cell, eater, boar)
            eater._health += 20
            eater._hunger -= 8
        else:
            eater._health -= 20

    def trying_to_eat_rabbit(self, cell, eater, rabbit):
        if random.randint(0, 100) > RABBIT_RUN_AWAY_CHANCE:
            self.eating(cell, eater, rabbit)
            eater._health += 15
            eater._hunger -= 6

    def eating_bush(self, cell, eater, bush):
        self.eating(cell, eater, bush)
        eater._health += 10
        eater._hunger -= 4

    def eating(self, cell, eater, victim):
        index = self.cell_controller.get_victim_place(cell, victim)
        self.dyuing(cell, victim)
        self.cell_controller.move_to_victim_place(cell, eater, index)

    def is_alive(self, creature):
        return creature._health > 0 and creature._hunger < 20

    def dyuing(self, cell, dying_creature):
        dying_creature_index = cell.creatures.index(dying_creature)
        cell.creatures[dying_creature_index] = None
        del dying_creature

    def starvation(self, creature):
        creature._hunger += 1

    def move(self, cell: Cell, creature):
        if self._field.add_to_field(creature):
            index = cell.creatures.index(creature)
            cell.creatures[index] = None
