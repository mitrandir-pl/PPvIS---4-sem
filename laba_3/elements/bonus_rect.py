from pygame import Rect


class BonusRect(Rect):
    def __init__(self, x_pos, y_pos, x, y, bonus_index: str):
        super().__init__(x_pos, y_pos, x, y)
        self.bonus_index = bonus_index 


def main():
    mr = BonusRect(x_pos=15 + 52, y_pos=50 + 22, x=50, y=20, bonus_index=1)
    print(mr.bonus_index)


if __name__ == "__main__":
    main()