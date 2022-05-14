import emoji

from model.field import Field
from model.cell import Cell


class FieldInterface:

    def __init__(self, field: Field) -> None:
        self.field = field

    def show_field(self) -> None:
        north = self.field.area['north']
        east = self.field.area['east']
        center = self.field.area['center']
        west = self.field.area['west']
        south = self.field.area['south']
        self.print_region(north, 0, 3)
        self.print_region(north, 3, 6)
        self.print_region(north, 6, 9)
        self.print_middle_regions(east, center, west, 0, 3)
        self.print_middle_regions(east, center, west, 3, 6)
        self.print_middle_regions(east, center, west, 6, 9)
        self.print_region(south, 0, 3)
        self.print_region(south, 3, 6)
        self.print_region(south, 6, 9)

    def print_region(self, region: dict[str, list[Cell]],
                     start_index: int, end_index: int) -> None:
        print('\n' + 36*' ', end='')
        for i in range(start_index, end_index):
            self.print_first_line(region, i)
            print(end='  ')
        print('\n' + 36*' ', end='')
        for i in range(start_index, end_index):
            self.print_second_line(region, i)
            print(end='  ')
        print('\n' + 36*' ', end='')
        for i in range(start_index, end_index):
            self.print_third_line(region, i)
            print(end='  ')
        print(end='\n\n')

    def print_middle_regions(
            self, region1: dict[str, list[Cell]],
            region2: dict[str, list[Cell]],
            region3: dict[str, list[Cell]],
            start_index: int, end_index: int) -> None:
        print('\n', end='')
        for i in range(start_index, end_index):
            self.print_first_line(region1, i)
            print(end='   ')
        for i in range(start_index, end_index):
            self.print_first_line(region2, i)
            print(end='   ')
        for i in range(start_index, end_index):
            self.print_first_line(region2, i)
            print(end='   ')
        print()
        for i in range(start_index, end_index):
            self.print_second_line(region1, i)
            print(end='   ')
        for i in range(start_index, end_index):
            self.print_second_line(region2, i)
            print(end='   ')
        for i in range(start_index, end_index):
            self.print_second_line(region2, i)
            print(end='   ')
        print()
        for i in range(start_index, end_index):
            self.print_third_line(region1, i)
            print(end='   ')
        for i in range(start_index, end_index):
            self.print_third_line(region2, i)
            print(end='   ')
        for i in range(start_index, end_index):
            self.print_third_line(region2, i)
            print(end='   ')
        print(end='\n\n')

    def print_first_line(self, region: dict[str, list[Cell]],
                         cell_num: int) -> None:
        for j in range(3):
            if region[cell_num].creatures[j]:
                print(region[cell_num].creatures[j], end=' ')
            else:
                print(emoji.emojize(':black_large_square:'), end=' ')

    def print_second_line(self, region: dict[str, list[Cell]],
                          cell_num: int) -> None:
        for j in range(3, 6):
            if region[cell_num].creatures[j]:
                print(region[cell_num].creatures[j], end=' ')
            else:
                print(emoji.emojize(':black_large_square:'), end=' ')

    def print_third_line(self, region: dict[str, list[Cell]],
                         cell_num: int) -> None:
        for j in range(6, 9):
            if region[cell_num].creatures[j]:
                print(region[cell_num].creatures[j], end=' ')
            else:
                print(emoji.emojize(':black_large_square:'), end=' ')
