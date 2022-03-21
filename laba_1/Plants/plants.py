class Plant:

    def __init__(self):
        self._health = 100
        self._type = 'plant'

    @property
    def type(self):
        return self._type

    def __str__(self):
        return self._type


class Bush(Plant):

    def __init__(self):
        super().__init__()
        self._type = 'bush'
