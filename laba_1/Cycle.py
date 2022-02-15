import time

from Nutrition import Nutrition
from Movement import Movement


class Cycle:
    processes = (
        'eating',
        'moving',
        'reproduction',
    )

    @staticmethod
    def life(field):
        while True:
            for process in Cycle.processes:
                match process:
                    case 'moving':
                        Movement.moving(field)
                    # case 'eating':
                    #     Nutrition.eating(field)
                    # case 'reproduction':
                    #     pass
                field.show_field()
                time.sleep(20)
