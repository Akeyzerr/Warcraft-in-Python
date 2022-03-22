from spells import Spell
from settings import *


class Hero:
    def __init__(self, char_type: str, name: str, mana: int, mana_regen_rate: int):
        self._SPELLS = {}
        self.char_type = char_type
        self._name = name
        self._current_mana = mana
        self._MAX_MANA = mana
        self._mana_regen_rate = mana_regen_rate
        self._assign_basic_spell()
        self._assign_ultimate_spell()

    def __repr__(self):
        return __class__.__name__

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Name not valid!")
        self._name = value

    @property
    def mana(self):
        return self._current_mana

    @mana.setter
    def mana(self, val: int):
        self._current_mana = val
        if self._current_mana > self._MAX_MANA:
            self._current_mana = self._MAX_MANA

    @property
    def regen_rate(self):
        return self._mana_regen_rate

    def _assign_basic_spell(self):
        self._SPELLS["basic"] = Spell(TYPES[self.char_type]["basic"]["name"],
                                      TYPES[self.char_type]["basic"]["mana_cost"])

    def _assign_ultimate_spell(self):
        self._SPELLS["ultimate"] = Spell(TYPES[self.char_type]["ultimate"]["name"],
                                         TYPES[self.char_type]["ultimate"]["mana_cost"])

    def has_enough_mana(self, needed_mana):
        return self.mana >= needed_mana

    def _cast_spell(self, spell_type: str, **kwargs):
        mana_needed = None
        if "free_cast" not in kwargs.keys():
            try:
                mana_needed = self._SPELLS[spell_type].mana_cost
            except KeyError:
                print("Spell not found")
        else:
            mana_needed = 0

        if mana_needed is not None and self.has_enough_mana(mana_needed):
            self.mana -= mana_needed
            return f"{self._name}" + self._SPELLS[spell_type].cast_spell(mana_needed)
        else:
            return f"{self._name} - not enough mana to cast {self._SPELLS[spell_type]}"

    def regenerate_mana(self):
        self.mana = self.mana + self.regen_rate

    def cast_basic_spell(self, *args, **kwargs):
        return self._cast_spell(spell_type="basic", *args, **kwargs)

    def cast_ultimate_spell(self, *args, **kwargs):
        return self._cast_spell(spell_type="ultimate", *args, **kwargs)

    def is_spell_cast(spell):
        def wrapper(self, *args, **kwargs):
            ret = spell(self, *args, **kwargs)
            return [ret, True] if "not enough" not in ret else (ret, False)

        return wrapper

    def free_cast(spell):
        def wrapper(self, *args, **kwargs):
            return spell(self, free_cast=True, *args, **kwargs)

        return wrapper
