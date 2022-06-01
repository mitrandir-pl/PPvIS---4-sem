from model.field import Field


class Cycle:

    def __init__(self, field: Field) -> None:
        self.field = field

    def life_cycle(self) -> None:
        cell_controller = Cell()
        dragons_controller = Dragon(cell_controller, self.field)
        dragon_eggs_controller = DragonEgg(cell_controller, self.field)
        bears_controller = Bear(cell_controller, self.field)
        boars_controller = Boar(cell_controller, self.field)
        rabbits_controller = Rabbit(cell_controller, self.field)
        bushs_controller = Bush(cell_controller, self.field)
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
