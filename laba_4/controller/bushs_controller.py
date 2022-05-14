import random

from controller.cells_controller import CellsController
from model.cell import Cell
from model.field import Field
from model.plants import Bush


REPRODUCE_CHANCE = 50


class BushsController:

    def __init__(self, cells_controller: CellsController,
                 field: Field) -> None:
        self.cell_controller = cells_controller
        self._field = field
    
    def make_decision(self, cell: Cell, bush: Bush) -> None:
        if self.is_alive(bush):
            self.weakening(bush)
            if random.randint(0, 100) <= REPRODUCE_CHANCE:
                self.reproduce()
        else:
            self.dying(cell, bush)

    def reproduce(self) -> None:
        self._field.add_to_field(Bush())

    def is_alive(self, creature: Bush) -> bool:
        return creature._health > 0

    def weakening(self, bush: Bush) -> None:
        bush._health -= 40

    def dying(self, cell: Cell, dying_plant: Bush) -> None:
        dying_plant_index = cell.creatures.index(dying_plant)
        cell.creatures[dying_plant_index] = None
        del dying_plant
