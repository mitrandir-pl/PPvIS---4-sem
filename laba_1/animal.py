from abc import ABC, abstractmethod
import random


class Animal(ABC):

    def __init__(self):
        self._health = 100
        self._hunger = 0
        self._life_cycle = False
        self._type = 'animal'
        self._sex = random.choice(['male', 'female'])

    def move(self, field):
        field.add_to_field(self)
        self.life_cycle = True

    @property
    def type(self):
        return self._type

    @property
    def sex(self):
        return self._sex

    @property
    def life_cycle(self):
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        self._life_cycle = life_cycle

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def check_reproduce(self, field, region, cell_num):
        cell = field.area[region][cell_num]
        if cell.has_empty_place():
            partner = cell.get_partner(self)
            return partner if partner else False
