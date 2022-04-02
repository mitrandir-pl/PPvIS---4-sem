import unittest

from Controllers.cells_controller import CellsController
from Field.cell import Cell
from Animals.animals import Dragon, Boar
from Controllers.dragons_controller import DragonsController
from Field.field import Field


class DragonFixtures:
    def setup_dragon_controller(self):
        field = Field()
        cell_controller = CellsController()
        self.dragons_controller = DragonsController(cell_controller, field)


class TestDragons(unittest.TestCase, DragonFixtures):
    def test_reproduce(self):
        cell = Cell()
        self.setup_dragon_controller()
        dragon_male = Dragon()
        dragon_male._sex = 'male' # create male dragon
        dragon_female = Dragon()
        dragon_female._sex = 'female' # create female dragon
        cell.creatures.append(dragon_male)
        cell.creatures.append(dragon_female)
        cell.creatures.append(None)
        self.dragons_controller.reproduce(cell, dragon_male)
        for dragon in cell.creatures:
            self.assertTrue(True)

    def test_eating(self):
        for _ in range(10):
            cell = Cell()
            self.setup_dragon_controller()
            dragon = Dragon()
            dragon._hunger = 10 # making dragon hungry
            boar = Boar()
            cell.creatures.append(dragon)
            cell.creatures.append(boar)
            self.dragons_controller.make_decision(cell, dragon)
            if None in cell.creatures:
                break

    def test_dying(self):
        cell = Cell()
        self.setup_dragon_controller()
        dragon = Dragon()
        dragon._health = 0
        cell.creatures.append(dragon)
        self.dragons_controller.make_decision(cell, dragon)
        self.assertTrue(None in cell.creatures)


if __name__ == '__main__':
    unittest.main()
