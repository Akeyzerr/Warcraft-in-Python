from hero import Hero


class Archmage(Hero):
    def __init__(self, name=None, mana=None, mana_regen_rate=None, mana_regen_modifier=None):
        super().__init__("archmage", name, mana, mana_regen_rate)
        self.mana_regen_modifier = mana_regen_modifier

    def __repr__(self):
        return f"{super().name} of type {self.__class__.__name__}"

    def regenerate_mana(self):
        self.mana += self.regen_rate * self.mana_regen_modifier

    def do_special(func):
        def wrapper(self, *args, **kwargs):
            ret = func(self, *args, **kwargs)
            if ret[1]:
                self.regenerate_mana()
                return ret[0]
            else:
                return ret[0]

        return wrapper

    @do_special
    @Hero.is_spell_cast
    def cast_ultimate_spell(self):
        return super().cast_ultimate_spell()
