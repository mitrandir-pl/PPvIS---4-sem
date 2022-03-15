import os

from nutrition import Nutrition
from movement import Movement
from reproduction import Reproduction


class Cycle:
    processes = (
        'moving',
        # 'eating',
        'reproduction',
    )

    @staticmethod
    def life(field) -> None:
        while True:
            for process in Cycle.processes:
                match process:
                    case 'moving':
                        print('Moving:')
                        Movement.moving(field)
                    # case 'eating':
                    #     Nutrition.eating(field)
                    case 'reproduction':
                        print('reproduction')
                        Reproduction.reproduction(field)
                field.show_field()
                field.set_life_cycles_false()
                field.empty_count()
                check_exit = input()
                if check_exit == 'q':
                    raise SystemExit
                os.system('cls')
