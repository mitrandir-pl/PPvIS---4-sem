import emoji


class Plant:

    def __init__(self) -> None:
        self._health = 60
        self._type = 'plant'

    @property
    def type(self) -> str:
        return self._type


class Bush(Plant):

    def __init__(self) -> None:
        super().__init__()
        self._type = 'bush'


    def __str__(self) -> str:
        return emoji.emojize(':herb:')
