from Archmage import Archmage
from DeathKnight import DeathKnight
from DrawRanger import DrawRanger
from party import Party

from settings import test_party


def build_archmage(args=None):
    if args:
        name, mana, regen, modifier = args.split()
    else:
        name, mana, regen, modifier = input().split()

    return Archmage(str(name), int(mana), int(regen), int(modifier))


def build_death_knight(args=None):
    if args:
        name, mana, regen = args.split()
    else:
        name, mana, regen = input().split()

    return DeathKnight(str(name), int(mana), int(regen))


def build_draw_ranger(args=None):
    if args:
        name, mana, regen = args.split()
    else:
        name, mana, regen = input().split()

    return DrawRanger(str(name), int(mana), int(regen))


def build_party(counts, test=False):
    party = Party()
    for k, v in counts.items():
        if k == "archmage":
            for h in range(v):
                mage = build_archmage(test_party[0] if test else None)
                party.add_archmage(mage)
        elif k == "death_knight":
            for h in range(v):
                dk = build_death_knight(test_party[1] if test else None)
                party.add_death_knight(dk)
        elif k == "draw_ranger":
            for h in range(v):
                dr = build_draw_ranger(test_party[2] if test else None)
                party.add_draw_ranger(dr)
    return party
