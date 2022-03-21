import random


class Animal():

    def __init__(self):
        self._hunger = 0
        self._type = 'animal'
        self._sex = random.choice(['male', 'female'])

    @property
    def type(self):
        return self._type

    @property
    def sex(self):
        return self._sex

    def __str__(self):
        return self._type


class Bear(Animal):

    def __init__(self):
        super().__init__()
        self._type = 'bear'
        self._health = 100


class Boar(Animal):

    def __init__(self):
        super().__init__()
        self._type = 'boar'
        self._health = 80


class Dragon(Animal):

    def __init__(self):
        super().__init__()
        self._type = 'dragon'
        self._health = 200


class Rabbit(Animal):

    def __init__(self):
        super().__init__()
        self._type = 'rabbit'
        self._health = 60


class DragonEgg:

    def __init__(self) -> None:
        self._type = 'dragon_egg'
        self._age = 0

    @property
    def type(self):
        return self._type

    def __str__(self):
        return self._type
