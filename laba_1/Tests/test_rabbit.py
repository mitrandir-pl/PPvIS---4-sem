import unittest

from Controllers.cells_controller import CellsController
from Field.cell import Cell
from Animals.animals import Rabbit, Boar
from Controllers.rabbits_controller import RabbitsController
from Field.field import Field


class RabbitFixtures:
    def setup_rabbit_controller(self):
        field = Field()
        cell_controller = CellsController()
        self.rabbits_controller = RabbitsController(cell_controller, field)


class TestRabbits(unittest.TestCase, RabbitFixtures):
    def test_reproduce(self):
        cell = Cell()
        self.setup_rabbit_controller()
        rabbit_male = Rabbit()
        rabbit_male._sex = 'male' # create male rabbit
        rabbit_female = Rabbit()
        rabbit_female._sex = 'female' # create female rabbit
        cell.creatures.append(rabbit_male)
        cell.creatures.append(rabbit_female)
        cell.creatures.append(None)
        self.rabbits_controller.reproduce(cell, rabbit_male)
        for rabbit in cell.creatures:
            self.assertEqual(rabbit._type, 'rabbit')

    def test_eating(self):
        for _ in range(10):
            cell = Cell()
            self.setup_rabbit_controller()
            rabbit = Rabbit()
            rabbit._hunger = 10 # making rabbit hungry
            boar = Boar()
            cell.creatures.append(rabbit)
            cell.creatures.append(boar)
            self.rabbits_controller.make_decision(cell, rabbit)
            if None in cell.creatures:
                break

    def test_dying(self):
        cell = Cell()
        self.setup_rabbit_controller()
        rabbit = Rabbit()
        rabbit._health = 0
        cell.creatures.append(rabbit)
        self.rabbits_controller.make_decision(cell, rabbit)
        self.assertTrue(None in cell.creatures)


if __name__ == '__main__':
    unittest.main()
