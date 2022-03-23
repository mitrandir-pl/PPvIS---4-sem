import random

from Controllers.cells_controller import CellsController
from Field.cell import Cell
from Field.field import Field
from Plants.plants import Bush


REPRODUCE_CHANCE = 5


class BushsController:

    def __init__(self, cells_controller: CellsController,
                 field: Field) -> None:
        self.cell_controller = cells_controller
        self._field = field
    
    def make_decision(self, cell: Cell, bush: Bush):
        if self.is_alive(bush):
            self.weakening
            if random.randint(0, 100) < REPRODUCE_CHANCE:
                self.reproduce(cell, bush)
        else:
            self.dying

    def reproduce(self, cell: Cell, boar: Bush):
        self._field.add_to_field(Bush())

    def is_alive(self, creature):
        return creature._health > 0

    def weakening(self, bush: Bush):
        bush._health -= 10

    def dyuing(self, cell, dying_plant):
        dying_plant_index = cell.creatures.index(dying_plant)
        cell.creatures[dying_plant_index] = None
        del dying_plant
