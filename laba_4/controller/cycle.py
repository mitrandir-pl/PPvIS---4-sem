from controller.bears_controller import BearsController
from controller.boars_controller import BoarsController
from controller.bushs_controller import BushsController
from controller.cells_controller import CellsController
from controller.dragons_controller import DragonsController, DragonEggsController
from controller.rabbits_controller import RabbitsController
from model.field import Field


class Cycle:

    def __init__(self, field: Field) -> None:
        self.field = field

    def life_cycle(self) -> None:
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
                            case 'dragon':
                                dragons_controller.make_decision(
                                    cell, creature
                                )
                            case 'rabbit':
                                rabbits_controller.make_decision(
                                    cell, creature
                                )
                            case 'boar':
                                boars_controller.make_decision(
                                    cell, creature
                                )
                            case 'bush':
                                bushs_controller.make_decision(
                                    cell, creature
                                )
                            case 'dragon_egg':
                                dragon_eggs_controller.make_decision(
                                    cell, creature
                                )
