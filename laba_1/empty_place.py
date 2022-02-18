class EmptyPlace:

    def __init__(self):
        self._type = 'empty place'

    @staticmethod
    def show():
        print('EmptyPlace', end=' ')

    @property
    def type(self):
        return self._type
