from build_heroes import build_party
from settings import HEROES_COUNT


def game_on(*args):
    party = build_party(HEROES_COUNT, test=True)
    for cmd in str(args[0]).split():
        if cmd == "0":
            party.party_cast_basic_spell()
        elif cmd == "1":
            party.party_cast_ultimate_spell()
        elif cmd == "2":
            party.party_regenerate_mana()


if __name__ == '__main__':
    commands = "0 2 1 1"
    game_on(commands)
