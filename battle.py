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
        print(team1_pokemon)
        team2_pokemon = team2.retrieve_pokemon()
        print(team2_pokemon)
        team1_battle_option = team1.choose_battle_option(team1_pokemon, team2_pokemon)
        print(team1_battle_option)
        team2_battle_option = team2.choose_battle_option(team2_pokemon, team1_pokemon)
        print(team2_battle_option)
        while team1.is_empty() == False or team2.is_empty() == False:
            if team1_battle_option == Action.ATTACK and team2_battle_option == Action.ATTACK:
                while team1_pokemon.is_fainted() == False or team2_pokemon.is_fainted() == False:
                    print("here")
                    if team1_pokemon.get_speed() >= team2_pokemon.get_speed():
                        team1_pokemon.attack(team2_pokemon)
                    elif team2_pokemon.get_speed() > team1_pokemon.get_speed():
                        team2_pokemon.attack(team1_pokemon)

            if team1_battle_option == Action.SWAP:
                team1.return_pokemon(team1_pokemon)
                team1.retrieve_pokemon()
            elif team2_battle_option == Action.SWAP:
                team2.return_pokemon(team2_pokemon)
                team2.retrieve_pokemon()

            elif team1_battle_option == Action.SPECIAL:
                team1.special()
                team1.retrieve_pokemon()
            elif team2_battle_option == Action.SPECIAL:
                team2.special()
                team2.retrieve_pokemon()
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
                team1_pokemon.hp -= 1
                team2_pokemon.hp -= 1

            if team1_pokemon.is_fainted() == True and team2_pokemon.is_fainted() == False:
                team2_pokemon.level_up()
            elif team2_pokemon.is_fainted() == True and team1_pokemon.is_fainted() == False:
                team1_pokemon.level_up()

            if team1_pokemon.is_fainted() == False and team1_pokemon.can_evolve() == True:
                team1_pokemon.evolve()
            elif team2_pokemon.is_fainted() == False and team2_pokemon.can_evolve() == True:
                team2_pokemon.evolve()

            if team1_pokemon.is_fainted() == True:
                team1.return_pokemon(team1_pokemon)
                team1_pokemon = team1.retrieve_pokemon()
            elif team2_pokemon.is_fainted() == True:
                team2.return_pokemon(team2_pokemon)
                team2_pokemon = team2.retrieve_pokemon()

        if team1.is_empty() == True and team2.is_empty() == True:
            return 0
        if team1.is_empty() == True:
            return 2
        if team2.is_empty() == True:
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
    print(team2)
    remaining = []
    while not team1.is_empty():
        remaining.append(team1.retrieve_pokemon())
    print(remaining)
    print(len(remaining)) # 2
    print(remaining[0].get_hp()) # 1 
    print(remaining[0]) # Venusaur
    print(remaining[1].get_hp()) # 11
    print(remaining[1]) # Squirtle
