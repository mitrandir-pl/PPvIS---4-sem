import unittest

from Controllers.cells_controller import CellsController
from Field.cell import Cell
from Animals.animals import Bear, Boar
from Controllers.bears_controller import BearsController
from Field.field import Field


class BearFixtures:
    def setup_bear_controller(self):
        field = Field()
        cell_controller = CellsController()
        self.bears_controller = BearsController(cell_controller, field)


class TestBears(unittest.TestCase, BearFixtures):
    def test_reproduce(self):
        cell = Cell()
        self.setup_bear_controller()
        bear_male = Bear()
        bear_male._sex = 'male' # create male bear
        bear_female = Bear()
        bear_female._sex = 'female' # create female bear
        cell.creatures.append(bear_male)
        cell.creatures.append(bear_female)
        cell.creatures.append(None)
        self.bears_controller.reproduce(cell, bear_male)
        for bear in cell.creatures:
            self.assertEqual(bear._type, 'bear')

    def test_eating(self):
        for _ in range(10):
            cell = Cell()
            self.setup_bear_controller()
            bear = Bear()
            bear._hunger = 10 # making bear hungry
            boar = Boar()
            cell.creatures.append(bear)
            cell.creatures.append(boar)
            self.bears_controller.make_decision(cell, bear)
            if None in cell.creatures:
                break

    def test_dying(self):
        cell = Cell()
        self.setup_bear_controller()
        bear = Bear()
        bear._health = 0
        cell.creatures.append(bear)
        self.bears_controller.make_decision(cell, bear)
        self.assertTrue(None in cell.creatures)


if __name__ == '__main__':
    unittest.main()
