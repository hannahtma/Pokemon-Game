"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from random_gen import RandomGen
from pokemon_base import PokemonBase
from poke_team import Action, PokeTeam, Criterion
from print_screen import print_game_screen

class Battle:
    
    def __init__(self, verbosity=0) -> None:
        self.verbosity = verbosity

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        """
        
        """
        pokemon1 = team1.retrieve_pokemon()
        pokemon2 = team2.retrieve_pokemon()
        
        self.team1_heal_count = 0
        self.team2_heal_count = 0
        count = 1

        while team1.retrieve_pokemon() != None and team2.retrieve_pokemon() != None:
            print("Round",count)
            if team1.choose_battle_option(pokemon1,pokemon2) == Action.SWAP:
                team1.return_pokemon(pokemon1)
                team1.retrieve_pokemon()
            elif team1.choose_battle_option(pokemon1,pokemon2) == Action.SPECIAL:
                team1.return_pokemon(pokemon1)
                team1.special()
                team1.retrieve_pokemon()
            elif team1.choose_battle_option(pokemon1,pokemon2) == Action.HEAL:
                if self.team1_heal_count <= 3:
                    pokemon1.heal()
                else:
                    return 2

            if team2.choose_battle_option(pokemon2,pokemon1) == Action.SWAP:
                team2.return_pokemon(pokemon2)
                team2.retrieve_pokemon()
            elif team2.choose_battle_option(pokemon2,pokemon1) == Action.SPECIAL:
                team2.return_pokemon(pokemon2)
                team2.special()
                team2.retrieve_pokemon()
            elif team2.choose_battle_option(pokemon2,pokemon1) == Action.HEAL:
                if self.team2_heal_count <= 3:
                    pokemon2.heal()
                else:
                    return 1
            
            if team1.choose_battle_option(pokemon1,pokemon2) == Action.ATTACK and team2.choose_battle_option(pokemon2,pokemon1) == Action.ATTACK:
                if pokemon1.get_speed() >= pokemon2.get_speed():
                    pokemon1.attack(pokemon2)
                    if pokemon2.is_fainted() == False:
                        pokemon2.attack(pokemon1)
                else:
                    pokemon2.attack(pokemon1)
                    if pokemon1.is_fainted() == False:
                        pokemon1.attack(pokemon2)
            elif team1.choose_battle_option(pokemon1,pokemon2) == Action.ATTACK:
                pokemon1.attack(pokemon2)
            elif team2.choose_battle_option(pokemon2,pokemon1) == Action.ATTACK:
                pokemon2.attack(pokemon1)

            print("this round:",pokemon1)
            print("this round:",pokemon2)

            if pokemon1.is_fainted() == False and pokemon2.is_fainted() == False:
                print("hi")
                pokemon1.lose_hp(1)
                pokemon2.lose_hp(1)

            print("this round:",pokemon1)
            print("this round:",pokemon2)

            if pokemon1.is_fainted() == True and pokemon2.is_fainted() == False:
                print("blah")
                pokemon2.level_up()
                if pokemon2.should_evolve() == True:
                    pokemon2 = pokemon2.get_evolved_version()
                team2.return_pokemon(pokemon2)
            elif pokemon2.is_fainted() == True and pokemon1.is_fainted() == False:
                print("damnit")
                pokemon1.level_up()
                if pokemon1.should_evolve() == True:
                    pokemon1 = pokemon1.get_evolved_version()
                team1.return_pokemon(pokemon1)

            pokemon1 = team1.retrieve_pokemon()
            pokemon2 = team2.retrieve_pokemon()
            
            print("next round:",pokemon1)
            print("next round:",pokemon2)
            count += 1

        print(pokemon1)
        print(pokemon1.get_hp)
        print(pokemon2)
        print(pokemon2.get_hp)
        if team1.is_empty() == True and team2.is_empty() == False:
            result = 2
        elif team2.is_empty() == True and team1.is_empty() == False:
            result = 1
        elif team1.is_empty() == True and team2.is_empty() == True:
            result = 0
        
        return result

if __name__ == "__main__":
    RandomGen.set_seed(1337)
    team1 = PokeTeam("Ash", [1, 1, 1, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
    print(team1)
    team2 = PokeTeam("Gary", [0, 0, 0, 0, 3], 0, PokeTeam.AI.ALWAYS_ATTACK)
    print(team2)
    b = Battle(verbosity=0)
    res = b.battle(team1, team2)
    print(res) #1
    print(team2.is_empty()) #True
    print(team1)
    print(team2)
    remaining = []
    while not team1.is_empty():
        remaining.append(team1.retrieve_pokemon())
    print(len(remaining))#2
    print(remaining[0].get_hp()) #1
    print(remaining[0]) # Venusaur
    print(remaining[1].get_hp()) #11
    print(remaining[1]) # Squirtle

    # RandomGen.set_seed(192837465)
    # team1 = PokeTeam("Brock", [1, 1, 1, 1, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.HP)
    # print(team1)
    # team2 = PokeTeam("Misty", [0, 0, 0, 3, 3], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.SPD)
    # print(team2)
    # b = Battle(verbosity=0)
    # res = b.battle(team1, team2)
    # print(res) # 1
    # remaining = []
    # while not team1.is_empty():
    #     remaining.append(team1.retrieve_pokemon())
    # print(len(remaining)) # 2
    # print(remaining[0].get_hp()) # 11
    # print(remaining[0]) # Charizard
    # print(remaining[1].get_hp()) # 6
    # print(remaining[1]) # Gastly
