"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from random_gen import RandomGen
from poke_team import Action, PokeTeam, Criterion
from print_screen import print_game_screen

class Battle:
    
    def __init__(self, verbosity=0) -> None:
        self.verbosity = verbosity

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        team1_healcount = 0
        team2_healcount = 0
        team1_pokemon = team1.retrieve_pokemon()
        team2_pokemon = team2.retrieve_pokemon()
        while not team1.is_empty() and not team2.is_empty():
            team1_battle_option = team1.choose_battle_option(team1_pokemon, team2_pokemon)
            team2_battle_option = team2.choose_battle_option(team2_pokemon, team1_pokemon)
            if team1_battle_option == Action.ATTACK and team2_battle_option == Action.ATTACK:
                if team1_pokemon.get_speed() >= team2_pokemon.get_speed() and team1_pokemon.is_fainted() == False:
                    team1_pokemon.attack(team2_pokemon)
                    print(team1_pokemon.get_attack())
                    print(team2_pokemon.get_hp())
                    team2_pokemon.attack(team1_pokemon)

                elif team2_pokemon.get_speed() > team1_pokemon.get_speed() and team2_pokemon.is_fainted() == False:
                    team2_pokemon.attack(team1_pokemon)
                    team1_pokemon.attack(team2_pokemon)

            elif team1_battle_option == Action.SWAP:
                team1.return_pokemon(team1_pokemon)
                team1.retrieve_pokemon()
            elif team2_battle_option == Action.SWAP:
                team2.return_pokemon(team2_pokemon)
                team2.retrieve_pokemon()

            elif team1_battle_option == Action.SPECIAL:
                team1.return_pokemon(team1_pokemon)
                team1.special()
                team1_pokemon = team1.retrieve_pokemon()
            elif team2_battle_option == Action.SPECIAL:
                team2.return_pokemon(team2_pokemon)
                team2.special()
                team2_pokemon = team2.retrieve_pokemon()
            elif team1_battle_option == Action.HEAL:
                if team1_healcount >= 3:
                    return 2
                else:
                    team1_pokemon.heal()
            elif team2_battle_option == Action.HEAL:
                if team2_healcount >= 3:
                    return 1
                else:
                    team2_pokemon.heal()

            if team1_pokemon.get_hp() > 0 and team2_pokemon.get_hp() > 0:
                team1_pokemon.lose_hp(1)
                team2_pokemon.lose_hp(1)

            if team1_pokemon.is_fainted() == True and team2_pokemon.is_fainted() == False:
                team2_pokemon.level_up()
            elif team2_pokemon.is_fainted() == True and team1_pokemon.is_fainted() == False:
                team1_pokemon.level_up()

            if team1_pokemon.is_fainted() == False and team1_pokemon.can_evolve() == True:
                team1_pokemon.evolve()
            if team2_pokemon.is_fainted() == False and team2_pokemon.can_evolve() == True:
                team2_pokemon.get_evolved_version()

            if team1_pokemon.is_fainted():
                team1.return_pokemon(team1_pokemon)
                team1_pokemon = team1.retrieve_pokemon()
            if team2_pokemon.is_fainted():
                team2.return_pokemon(team2_pokemon)
                team2_pokemon = team2.retrieve_pokemon()
            print("Empty?",team2.is_empty())

        if team1.is_empty() and team2.is_empty():
            return 0
        elif team1.is_empty():
            return 2
        elif team2.is_empty():
            return 1

if __name__ == "__main__":
    RandomGen.set_seed(1337)
    team1 = PokeTeam("Ash", [1, 1, 1, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
    print(team1)
    team2 = PokeTeam("Gary", [0, 0, 0, 0, 3], 0, PokeTeam.AI.ALWAYS_ATTACK)
    print(team2)
    b = Battle(verbosity=0)
    res = b.battle(team1, team2)
    print("res",res) # 1
    print(team1)
    print(team2)
    remaining = []
    while not team1.is_empty():
        remaining.append(team1.retrieve_pokemon())
    print(len(remaining)) # 2
    print(remaining[0].get_hp()) # 1 
    print(remaining[0]) # Venusaur
    print(remaining[1].get_hp()) # 11
    print(remaining[1]) # Squirtle
