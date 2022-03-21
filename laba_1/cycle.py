import os

from Controllers.bears_controller import BearsController
from Controllers.boars_controller import BoarsController
from Controllers.bushs_controller import BushsController
from Controllers.cells_controller import CellsController
from Controllers.dragon_eggs_controller import DragonEggsController
from Controllers.dragons_controller import DragonsController
from Controllers.rabbits_controller import RabbitsController


class Cycle:

    def __init__(self, field) -> None:
        self.field = field

    def life_cycle(self, counter) -> None:
        cell_controller = CellsController()
        dragons_controller = DragonsController(cell_controller, self.field)
        dragon_eggs_controller = DragonEggsController(cell_controller, self.field)
        bears_controller = BearsController(cell_controller, self.field)
        boars_controller = BoarsController(cell_controller, self.field)
        rabbits_controller = RabbitsController(cell_controller, self.field)
        bushs_controller = BushsController(cell_controller, self.field)
        for list_of_cells in self.field.area.values():
            for cell in list_of_cells:
                for creature in cell.creatures:
                    if creature:
                        match creature.type:
                            case 'bear':
                                bears_controller.make_decision(
                                    cell, creature
                                )
                                counter['bears'] += 1
                            case 'dragon':
                                dragons_controller.make_decision(
                                    cell, creature
                                )
                                counter['dragons'] += 1
                            case 'rabbit':
                                rabbits_controller.make_decision(
                                    cell, creature
                                )
                                counter['rabbits'] += 1
                            case 'boar':
                                boars_controller.make_decision(
                                    cell, creature
                                )
                                counter['boars'] += 1
                            case 'bush':
                                bushs_controller.make_decision(
                                    cell, creature
                                )
                                counter['bushs'] += 1
                            case 'dragon_egg':
                                dragon_eggs_controller.make_decision(
                                    cell, creature
                                )
                                counter['dragon eggs'] += 1
                    else:
                        counter['empty'] += 1