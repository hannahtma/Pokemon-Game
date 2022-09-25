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
        counter = 1
        pokemon1 = team1.retrieve_pokemon()
        pokemon2 = team2.retrieve_pokemon()
        while pokemon1 != None and pokemon2 != None:
            print("================\nTHIS IS ROUND ",counter,"\n")
            print(pokemon1)
            print(pokemon2)
            team1_battle_option = team1.choose_battle_option(pokemon1, pokemon2)
            team2_battle_option = team2.choose_battle_option(pokemon2, pokemon1)
            if team1_battle_option == Action.ATTACK and team2_battle_option == Action.ATTACK:
                if pokemon1.get_speed() >= pokemon2.get_speed() and pokemon1.is_fainted() == False and pokemon2.is_fainted() == False:
                    print("pokemon1 attack first")
                    print("pokemon2's hp before attack",pokemon2,pokemon2.get_hp())
                    pokemon1.attack(pokemon2)
                    print("pokemon1's attack damage",pokemon1.get_attack_damage())
                    print("pokemon2's hp after attack",pokemon2.get_hp())
                    print()
                    print("pokemon1's hp before attack",pokemon1,pokemon1.get_hp())
                    pokemon2.attack(pokemon1)
                    print("pokemon2's attack damage",pokemon1.get_attack_damage())
                    print("pokemon1's hp after attack",pokemon1.get_hp())
                    print()
                elif pokemon2.get_speed() > pokemon1.get_speed() and pokemon2.is_fainted() == False and pokemon2.is_fainted() == False:
                    print("pokemon2 attack first")
                    print("pokemon1's hp before attack",pokemon1,pokemon1.get_hp())
                    pokemon2.attack(pokemon1)
                    print("pokemon2's attack damage",pokemon1.get_attack_damage())
                    print("pokemon1's hp after attack",pokemon1.get_hp())
                    print()
                    print("pokemon2's hp before attack",pokemon2,pokemon2.get_hp())
                    pokemon1.attack(pokemon2)
                    print("did eevee take damage?")
                    print("pokemon1's attack damage",pokemon1.get_attack_damage())
                    print("pokemon2's hp after attack",pokemon2.get_hp())
                    print()
                
            elif team1_battle_option == Action.SWAP:
                team1.return_pokemon(pokemon1)
                team1.retrieve_pokemon()
            elif team2_battle_option == Action.SWAP:
                team2.return_pokemon(pokemon2)
                team2.retrieve_pokemon()

            elif team1_battle_option == Action.SPECIAL:
                team1.return_pokemon(pokemon1)
                team1.special()
                pokemon1 = team1.retrieve_pokemon()
            elif team2_battle_option == Action.SPECIAL:
                team2.return_pokemon(pokemon2)
                team2.special()
                pokemon2 = team2.retrieve_pokemon()
            elif team1_battle_option == Action.HEAL:
                if team1_healcount >= 3:
                    return 2
                else:
                    pokemon1.heal()
            elif team2_battle_option == Action.HEAL:
                if team2_healcount >= 3:
                    return 1
                else:
                    pokemon2.heal()
            
            print(pokemon1,"my status effect is: ",pokemon1.get_status_effect())
            print(pokemon2,"my status effect is: ",pokemon2.get_status_effect())
            
            if pokemon1.get_hp() > 0 and pokemon2.get_hp() > 0:
                print("before pokemon1 lose 1 hp",pokemon1.get_hp())
                pokemon1.lose_hp(1)
                print("after pokemon1 lose 1 hp",pokemon1.get_hp())
                print("before pokemon2 lose 1 hp",pokemon2.get_hp())
                pokemon2.lose_hp(1)
                print("after pokemon2 lose 1 hp",pokemon2.get_hp())

            if pokemon1.is_fainted() == True and pokemon2.is_fainted() == False:
                pokemon2.level_up()
            elif pokemon2.is_fainted() == True and pokemon1.is_fainted() == False:
                pokemon1.level_up()

            if pokemon1.is_fainted() == False and pokemon1.can_evolve() == True:
                pokemon1 = pokemon1.get_evolved_version()
            if pokemon2.is_fainted() == False and pokemon2.can_evolve() == True:
                pokemon2 = pokemon2.get_evolved_version()

            if pokemon1.is_fainted():
                print("pokemon1 is dead")
                pokemon1 = team1.retrieve_pokemon()
                print("so what is team1 new pokemon?",pokemon1)
            elif pokemon1.is_fainted() == False:
                pokemon1.remove_status_effect()
            if pokemon2.is_fainted():
                print("pokemon2 is dead")
                pokemon2 = team2.retrieve_pokemon()
                print("so what is team2 new pokemon?",pokemon2)
            elif pokemon2.is_fainted() == False:
                pokemon2.remove_status_effect()

            counter += 1
        print("is team2 empty?",team2.is_empty())

        if pokemon1 != None:
            team1.return_pokemon(pokemon1)
        if pokemon2 != None:
            team2.return_pokemon(pokemon2)

        if team1.is_empty() and pokemon1 == None and team2.is_empty() and pokemon2 == None:
            return 0
        elif team1.is_empty() and pokemon1 == None:
            return 2
        elif team2.is_empty() and pokemon2 == None:
            print("Team 1 won")
            return 1

if __name__ == "__main__":
    # RandomGen.set_seed(1337)
    # team1 = PokeTeam("Ash", [1, 1, 1, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK) # [LV. 1 Charmander: 9 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Squirtle: 11 HP]
    # print("Before battle: ",team1)
    # team2 = PokeTeam("Gary", [0, 0, 0, 0, 3], 0, PokeTeam.AI.ALWAYS_ATTACK) # [LV. 1 Eevee: 10 HP, LV. 1 Eevee: 10 HP, LV. 1 Eevee: 10 HP]
    # print("Before battle: ",team2)
    # e = team2.retrieve_pokemon()
    # b = Battle(verbosity=0)
    # res = b.battle(team1, team2)
    # print(res) # 1
    # remaining = []
    # while not team1.is_empty():
    #     remaining.append(team1.retrieve_pokemon())
    # print(len(remaining)) # 2
    # print(remaining[0].get_hp()) # 1 
    # print(remaining[0]) # Venusaur
    # print(remaining[1].get_hp()) # 11
    # print(remaining[1]) # Squirtle

    RandomGen.set_seed(192837465)
    team1 = PokeTeam("Brock", [1, 1, 1, 1, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.HP)
    print(team1)
    team2 = PokeTeam("Misty", [0, 0, 0, 3, 3], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.SPD)
    print(team2)
    b = Battle(verbosity=0)
    res = b.battle(team1, team2)
    print(res) # 1
    remaining = []
    while not team1.is_empty():
        remaining.append(team1.retrieve_pokemon())
    print(len(remaining)) # 2
    print(remaining[0].get_hp()) # 11
    print(remaining[0]) # Charizard
    print(remaining[1].get_hp()) # 6
    print(remaining[1]) # Gastly
