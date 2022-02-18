import time
import os

from nutrition import Nutrition
from movement import Movement
from reproduction import Reproduction


class Cycle:
    processes = (
        # 'moving',
        # 'eating',
        'reproduction',
    )

    @staticmethod
    def life(field):
        while True:
            for process in Cycle.processes:
                match process:
                    # case 'moving':
                    #     Movement.moving(field)
                    # case 'eating':
                    #     Nutrition.eating(field)
                    case 'reproduction':
                        Reproduction.reproduction(field)
                field.show_field()
                field.set_life_cycles_false()
                input()
                os.system('cls')
