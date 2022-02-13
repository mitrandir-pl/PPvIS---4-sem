from abc import ABC, abstractmethod
import random


class Animal(ABC):

    @abstractmethod
    def __init__(self):
        self.health = 100
        self.sex = random.choice(['male', 'female'])
