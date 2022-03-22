from hero import Hero


class DrawRanger(Hero):
    def __init__(self, name=None, mana=None, mana_regen_rate=None):
        super().__init__("draw_ranger", name, mana, mana_regen_rate)

    def __repr__(self):
        return f"{super().name} of type {self.__class__.__name__}"

    def do_special(func):
        def wrapper(self, *args, **kwargs):
            ret = func(self, *args, **kwargs)
            if ret[1]:
                return ret[0] + "\n" + self.free_cast_basic()
            else:
                return ret[0]

        return wrapper

    @do_special
    @Hero.is_spell_cast
    def cast_basic_spell(self):
        return super().cast_basic_spell()

    @Hero.free_cast
    def free_cast_basic(self, *args, **kwargs):
        return super().cast_basic_spell(*args, **kwargs)
