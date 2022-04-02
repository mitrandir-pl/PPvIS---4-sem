import random

from Controllers.cells_controller import CellsController
from Field.cell import Cell
from Field.field import Field
from Plants.plants import Bush


REPRODUCE_CHANCE = 1


class BushsController:

    def __init__(self, cells_controller: CellsController,
                 field: Field) -> None:
        self.cell_controller = cells_controller
        self._field = field
    
    def make_decision(self, cell: Cell, bush: Bush) -> None:
        if self.is_alive(bush):
            self.weakening
            if random.randint(0, 100) == REPRODUCE_CHANCE:
                self.reproduce()
        else:
            breakpoint()
            self.dying(cell, bush)

    def reproduce(self) -> None:
        self._field.add_to_field(Bush())

    def is_alive(self, creature: Bush) -> bool:
        return creature._health > 0

    def weakening(self, bush: Bush) -> None:
        bush._health -= 70

    def dying(self, cell: Cell, dying_plant: Bush) -> None:
        dying_plant_index = cell.creatures.index(dying_plant)
        cell.creatures[dying_plant_index] = None
        del dying_plant
