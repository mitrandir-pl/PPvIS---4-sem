class Plant:

    def __init__(self):
        self._health = 100
        self._life_cycle = False
        self._type = 'plant'

    @property
    def type(self):
        return self._type

    @property
    def life_cycle(self):
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        self._life_cycle = life_cycle

    @staticmethod
    def check_reproduce(field, region, cell_num):
        cell = field.area[region][cell_num]
        if cell.has_empty_place():
            return True if cell.has_empty_place() else False
