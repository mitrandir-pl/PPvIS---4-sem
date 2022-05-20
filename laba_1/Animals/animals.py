import random
import emoji


class Animal():

    def __init__(self) -> None:
        self._hunger = 0
        self._type = 'animal'
        self._sex = random.choice(['male', 'female'])

    @property
    def type(self) -> str:
        return self._type

    @property
    def sex(self) -> str:
        return self._sex


class Bear(Animal):

    def __init__(self) -> None:
        super().__init__()
        self._type = 'bear'
        self._health = 100

    def __str__(self)-> str:
        return emoji.emojize(':bear:')


class Boar(Animal):

    def __init__(self) -> None:
        super().__init__()
        self._type = 'boar'
        self._health = 80

    def __str__(self) -> str:
        return emoji.emojize(':boar:')


class Dragon(Animal):

    def __init__(self) -> None:
        super().__init__()
        self._type = 'dragon'
        self._health = 400

    def __str__(self) -> str:
        return emoji.emojize(':dragon:')


class Rabbit(Animal):

    def __init__(self) -> None:
        super().__init__()
        self._type = 'rabbit'
        self._health = 70

    def __str__(self) -> str:
        return emoji.emojize(':rabbit_face:')


class DragonEgg:

    def __init__(self) -> None:
        self._type = 'dragon_egg'
        self._age = 0

    @property
    def type(self) -> str:
        return self._type

    def __str__(self) -> str:
        return emoji.emojize(':egg:')
