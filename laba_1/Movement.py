class Movement:

    @staticmethod
    def moving(field):
        lists_of_creatures = field.area.values()
        for creatures in lists_of_creatures:
            index = 0
            for creature in creatures.copy():
                if creature.life_cycle is False:
                    field.add_to_field(creatures.pop(index))
                    creature.life_cycle = True
                else:
                    index += 1
