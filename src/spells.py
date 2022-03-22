from abc import ABC


class Spell:
    def __init__(self, name: str, mana_cost: int):
        self._name = name
        self._mana_cost = mana_cost

    def get_info(self):
        return f"{self.name} costs {self.mana_cost}"

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def mana_cost(self):
        return int(self._mana_cost)

    @mana_cost.setter
    def mana_cost(self, val):
        self._mana_cost = val

    def cast_spell(self, mana_cost=None):
        return f" cast {self.name} for {mana_cost if mana_cost is not None else self.mana_cost}"
