"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from random_gen import RandomGen
from poke_team import Action, PokeTeam, Criterion
from print_screen import print_game_screen

class Battle:
    
    def __init__(self, verbosity=0) -> None:
        raise NotImplementedError()

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        team1_pokemon = team1.retrieve_pokemon()
        team2_pokemon = team2.retrieve_pokemon()
        team1_battle_option = team1.choose_battle_option(team1_pokemon, team2_pokemon)
        team2_battle_option = team2.choose_battle_option(team2_pokemon, team1_pokemon)
        if team1_battle_option == "swap":
            team1.return_pokemon(team1_pokemon)
            team1.retrieve_pokemon()
        elif team2_battle_option == "swap":
            team2.return_pokemon(team2_pokemon)
            team2.retrieve_pokemon()
        elif team1_battle_option == "special":
            team1.special()
            team1.retrieve_pokemon()
        elif team2_battle_option == "special":
            team2.special()
            team2.retrieve_pokemon()
        elif team1_battle_option == "heal":
            if heal_count >= 3:
                return 2
            else:
                team1_pokemon.heal()
        elif team2_battle_option == "heal":
            if heal_count >= 3:
                return 1
            else:
                team2_pokemon.heal()
        elif team1_battle_option == "attack":
            team1_pokemon.attack()
        elif team2_battle_option == "attack":
            team2_pokemon.attack()

        if team1_pokemon.get_hp() > 0 and team2_pokemon.get_hp() > 0:
            team1_pokemon.hp -= 1
            team2_pokemon.hp -= 1
        if team1_pokemon.is_fainted() == True and team2_pokemon.is_fainted() == False:
            team2_pokemon.level_up()
        if team2_pokemon.is_fainted() == True and team1_pokemon.is_fainted() == False:
            team1_pokemon.level_up()
        if team1_pokemon.is_fainted() == False and team1_pokemon.can_evolve() == True:
            team1_pokemon.evolve()
        if team2_pokemon.is_fainted() == False and team2_pokemon.can_evolve() == True:
            team2_pokemon.evolve()
        if team1_pokemon.is_fainted() == True:
            team1.return_pokemon(team1_pokemon)
            team1_pokemon = team1.retrieve_pokemon()
        if team2_pokemon.is_fainted() == True:
            team2.return_pokemon(team2_pokemon)
            team2_pokemon = team2.retrieve_pokemon()
        if team1.is_empty() == True and team2.is_empty() == True:
            return 0
        if team1.is_empty() == True:
            return 2
        if team2.is_empty() == True:
            return 1

if __name__ == "__main__":
    b = Battle(verbosity=3)
    RandomGen.set_seed(16)
    t1 = PokeTeam.random_team("Cynthia", 0, criterion=Criterion.SPD)
    t1.ai_type = PokeTeam.AI.USER_INPUT
    t2 = PokeTeam.random_team("Barry", 1)
    print(b.battle(t1, t2))
