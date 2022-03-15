from .plant import Plant


class Bash(Plant):

    def __init__(self):
        super().__init__()
        self._species = 'bash'

    @property
    def species(self):
        return self._species

    def show(self):
        print(self.species, end=' ')

    def reproduce(self, field, region, cell_num):
        if super().check_reproduce(field, region, cell_num):
            cell = field.area[region][cell_num]
            index = cell.get_index_of_empty_place()
            cell.add_by_index(index, Bash())
            self.life_cycle = True
