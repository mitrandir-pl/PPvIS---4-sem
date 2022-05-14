from model.animals import Dragon, DragonEgg
from model.cell import Cell
from .creatures_controller import CreaturesController


class DragonEggsController(CreaturesController):
    
    def make_decision(self, cell: Cell, egg: DragonEgg) -> None:
        if egg._age == 3:
            self.dragon_borning(cell, egg)
        else:
            egg._age += 1

    def dragon_borning(self, cell: Cell, egg: DragonEgg) -> None:
        index = cell.creatures.index(egg)
        cell.creatures[index] = Dragon()