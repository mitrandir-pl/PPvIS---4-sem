from abc import ABC, abstractmethod
import random


class Animal(ABC):

    def __init__(self, field):
        self._health = 100
        self._life_cycle = False
        self._sex = random.choice(['male', 'female'])
        field.add_to_field(self)

    def move(self):
        pass

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

    @abstractmethod
    def reproduction(self):
        pass
