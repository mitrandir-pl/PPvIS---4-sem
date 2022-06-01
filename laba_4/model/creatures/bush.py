import random
import emoji

from model.field import Field, Cell


REPRODUCE_CHANCE = 50


class Plant:

    def __init__(self, field, cells_controller) -> None:
        self._health = 60
        self._type = 'plant'
        self.cell_controller = cells_controller
        self._field = field

    @property
    def type(self) -> str:
        return self._type


class Bush(Plant):

    def __init__(self) -> None:
        super().__init__()
        self._type = 'bush'

    def __str__(self) -> str:
        return emoji.emojize(':herb:')

    def make_decision(self, cell: Cell, bush) -> None:
        if self.is_alive(bush):
            self.weakening(bush)
            if random.randint(0, 100) <= REPRODUCE_CHANCE:
                self.reproduce()
        else:
            self.dying(cell, bush)

    def reproduce(self) -> None:
        self._field.add_to_field(Bush())

    def is_alive(self, creature) -> bool:
        return creature._health > 0

    def weakening(self, bush) -> None:
        bush._health -= 40

    def dying(self, cell: Cell, dying_plant) -> None:
        dying_plant_index = cell.creatures.index(dying_plant)
        cell.creatures[dying_plant_index] = None
        del dying_plant
