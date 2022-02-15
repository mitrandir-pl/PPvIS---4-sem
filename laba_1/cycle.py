import time
import os

from nutrition import Nutrition
from movement import Movement


class Cycle:
    processes = (
        # 'eating',
        'moving',
        # 'reproduction',
    )

    @staticmethod
    def life(field):
        # clear = lambda: os.system('cls')
        while True:
            for process in Cycle.processes:
                match process:
                    case 'moving':
                        Movement.moving(field)
                    case 'eating':
                        Nutrition.eating(field)
                    # case 'reproduction':
                    #     pass
                field.show_field()
                field.set_life_cycles_true()
                time.sleep(3)
                os.system('cls')
