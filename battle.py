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
        counter = 1
        while team1.is_empty() == False and team2.is_empty() == False:
            print("================\nTHIS IS ROUND ",counter,"\n")
            team1_battle_option = team1.choose_battle_option(team1_pokemon, team2_pokemon)
            team2_battle_option = team2.choose_battle_option(team2_pokemon, team1_pokemon)
            if team1_battle_option == Action.ATTACK and team2_battle_option == Action.ATTACK:
                if team1_pokemon.get_speed() >= team2_pokemon.get_speed() and team1_pokemon.is_fainted() == False:
                    print("pokemon1 attack first")
                    print("p2 hp",team2_pokemon,team2_pokemon.get_hp())
                    team1_pokemon.attack(team2_pokemon)
                    print("p1 attack damage",team1_pokemon.get_attack_damage())
                    print("p2 hp",team2_pokemon.get_hp())
                    print("p1 hp",team1_pokemon,team1_pokemon.get_hp())
                    team2_pokemon.attack(team1_pokemon)
                    print("p2 attack damage",team1_pokemon.get_attack_damage())
                    print("p1 hp",team1_pokemon.get_hp())
                elif team2_pokemon.get_speed() > team1_pokemon.get_speed() and team2_pokemon.is_fainted() == False:
                    print("pokemon2 attack first")
                    print("p1 hp",team1_pokemon,team1_pokemon.get_hp())
                    team2_pokemon.attack(team1_pokemon)
                    print("p2 attack damage",team2_pokemon.get_attack_damage(),team2_pokemon.get_poke_name())
                    print("p1 hp",team1_pokemon.get_hp())
                    print("p2 hp",team2_pokemon,team2_pokemon.get_hp())
                    team1_pokemon.attack(team2_pokemon)
                    print("p1 attack damage",team1_pokemon.get_attack_damage())
                    print("p2 hp",team2_pokemon.get_hp())

            
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
                print("before pokemon1 lose 1 hp",team1_pokemon.get_hp())
                team1_pokemon.lose_hp(1)
                print("after pokemon1 lose 1 hp",team1_pokemon.get_hp())
                print("before pokemon2 lose 1 hp",team2_pokemon.get_hp())
                team2_pokemon.lose_hp(1)
                print("after pokemon2 lose 1 hp",team2_pokemon.get_hp())

            if team1_pokemon.is_fainted() == True and team2_pokemon.is_fainted() == False:
                team2_pokemon.level_up()
            elif team2_pokemon.is_fainted() == True and team1_pokemon.is_fainted() == False:
                team1_pokemon.level_up()

            if team1_pokemon.is_fainted() == False and team1_pokemon.can_evolve() == True:
                team1_pokemon.evolve()
            if team2_pokemon.is_fainted() == False and team2_pokemon.can_evolve() == True:
                team2_pokemon.get_evolved_version()

            if team1_pokemon.is_fainted():
                print("pokemon1 is dead")
                team1_pokemon = team1.retrieve_pokemon()
                print("so what is team1 new pokemon?",team1_pokemon)
            elif team1_pokemon.is_fainted() == False:
                team1.return_pokemon(team1_pokemon)
                team1_pokemon = team1.retrieve_pokemon()
            if team2_pokemon.is_fainted():
                print("pokemon2 is dead")
                team2_pokemon = team2.retrieve_pokemon()
                print("so what is team2 new pokemon?",team2_pokemon)
            elif team2_pokemon.is_fainted() == False:
                team2.return_pokemon(team2_pokemon)
                team2_pokemon = team2.retrieve_pokemon()
                
            counter += 1

        if team1.is_empty() and team2.is_empty():
            return 0
        elif team1.is_empty():
            return 2
        elif team2.is_empty():
            return 1

if __name__ == "__main__":
    RandomGen.set_seed(1337)
    team1 = PokeTeam("Ash", [1, 1, 1, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK) # [LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP]
    print("Before battle: ",team1)
    team2 = PokeTeam("Gary", [0, 0, 0, 0, 3], 0, PokeTeam.AI.ALWAYS_ATTACK) # [LV. 1 Eevee: 10 HP, LV. 1 Eevee: 10 HP, LV. 1 Eevee: 10 HP]
    print("Before battle: ",team2)
    e = team2.retrieve_pokemon()
    b = Battle(verbosity=0)
    res = b.battle(team1, team2)
    print("res",res) # 1
    print("After battle: ",team1)
    print("After battle: ",team2)
    remaining = []
    while not team1.is_empty():
        remaining.append(team1.retrieve_pokemon())
    print(len(remaining)) # 2
    print(remaining[0].get_hp()) # 1 
    print(remaining[0]) # Venusaur
    print(remaining[1].get_hp()) # 11
    print(remaining[1]) # Squirtle
