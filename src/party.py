class Party:
    def __init__(self):
        self.archmages = []
        self.death_knights = []
        self.draw_rangers = []

    def add_archmage(self, archmage):
        if archmage in self.archmages:
            raise ValueError("That Archmage is in the party!")
        self.archmages.append(archmage)

    def add_death_knight(self, death_knight):
        if death_knight in self.death_knights:
            raise ValueError("That Death Knight is in the party!")
        self.death_knights.append(death_knight)

    def add_draw_ranger(self, draw_ranger):
        if draw_ranger in self.draw_rangers:
            raise ValueError("That Draw Ranger is in the party!")
        self.draw_rangers.append(draw_ranger)

    def party_cast_basic_spell(self):
        for hero in self.archmages + self.death_knights + self.draw_rangers:
            print(hero.cast_basic_spell())

    def party_cast_ultimate_spell(self):
        for hero in self.archmages + self.death_knights + self.draw_rangers:
            print(hero.cast_ultimate_spell())

    def party_regenerate_mana(self):
        for hero in self.archmages + self.death_knights + self.draw_rangers:
            hero.regenerate_mana()
