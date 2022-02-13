from Animal import Animal
from Field import Field


class Bear(Animal):

    def __init__(self, field):
        super().__init__()
        self.type = 'B'
        field.add_to_field(self)

    def show(self):
        print('Bear', end='')
