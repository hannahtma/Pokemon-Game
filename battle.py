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
            Performs the battle between team1 and team2
            
            Parameters:
                team1 - PokeTeam 1
                team2 - PokeTeam 2 
            
            Returns:
                0 if draw, 1 if team1 wins, 2 if team2 wins
        """

        # Each PokeTeam retrieves a pokemon to send into the field
        pokemon1 = team1.retrieve_pokemon()
        pokemon2 = team2.retrieve_pokemon()
        
        # Set each team's heal count to 0
        self.team1_heal_count = 0
        self.team2_heal_count = 0

        # While both teams are not empty, the battle will continue
        while not((team1.is_empty() == True and pokemon1 == None) or (team2.is_empty() == True and pokemon2 == None)):

            # Team 1
            # Handle swap actions
            if team1.choose_battle_option(pokemon1,pokemon2) == Action.SWAP:
                team1.return_pokemon(pokemon1)
                pokemon1 = team1.retrieve_pokemon()
            # Handle special actions
            elif team1.choose_battle_option(pokemon1,pokemon2) == Action.SPECIAL:
                team1.return_pokemon(pokemon1)
                team1.special()
                pokemon1 = team1.retrieve_pokemon()
            # Handle heal actions
            elif team1.choose_battle_option(pokemon1,pokemon2) == Action.HEAL:
                # If team1's heal count is less than 3, heal
                if self.team1_heal_count <= 3:
                    pokemon1.heal()
                # Otherwise, team2 wins
                else:
                    return 2

            # Team 2
            # Handle swap actions
            if team2.choose_battle_option(pokemon2,pokemon1) == Action.SWAP:
                team2.return_pokemon(pokemon2)
                pokemon2 = team2.retrieve_pokemon()
            # Handle special actions
            elif team2.choose_battle_option(pokemon2,pokemon1) == Action.SPECIAL:
                team2.return_pokemon(pokemon2)
                team2.special()
                pokemon2 = team2.retrieve_pokemon()
            # Handle heal actions
            elif team2.choose_battle_option(pokemon2,pokemon1) == Action.HEAL:
                # If team2's heal count is less than 3, heal
                if self.team2_heal_count <= 3:
                    pokemon2.heal()
                # Otherwise, team1 wins
                else:
                    return 1

            # Handle attack actions if both teams battle_option is attack
            if team1.choose_battle_option(pokemon1,pokemon2) == Action.ATTACK and team2.choose_battle_option(pokemon2,pokemon1) == Action.ATTACK:
                # If pokemon2's speed is faster than pokemon1's speed, pokemon2 attack first
                if pokemon2.get_speed() > pokemon1.get_speed():
                    pokemon2.attack(pokemon1)
                    # If pokemon1 is not fainted, then pokemon1 will attack pokemon2
                    if pokemon1.is_fainted() == False:
                        pokemon1.attack(pokemon2)
                # If pokemon1's speed is faster than pokemon2's speed, pokemon2 attack first
                elif pokemon1.get_speed() > pokemon2.get_speed():
                    pokemon1.attack(pokemon2)
                    # If pokemon2 is not fainted, then pokemon2 will attack pokemon1
                    if pokemon2.is_fainted() == False:
                        pokemon2.attack(pokemon1)
                # If pokemon1's speed is the same as pokemon2's speed, pokemon1 will attack first and then pokemon2
                elif pokemon1.get_speed() == pokemon2.get_speed():
                    pokemon1.attack(pokemon2)
                    pokemon2.attack(pokemon1)
            # Handle attack actions for team1
            elif team1.choose_battle_option(pokemon1,pokemon2) == Action.ATTACK:
                pokemon1.attack(pokemon2)

            # Handle attack actions for team2
            elif team2.choose_battle_option(pokemon2,pokemon1) == Action.ATTACK:
                pokemon2.attack(pokemon1)

            # If both pokemon are not fainted, they will both lose 1 hp
            if pokemon1.is_fainted() == False and pokemon2.is_fainted() == False:
                pokemon1.lose_hp(1)
                pokemon2.lose_hp(1)

            # If pokemon1 is fainted and pokemon2 is not fainted, pokemon2 levels up
            if pokemon1.is_fainted() == True and pokemon2.is_fainted() == False:
                pokemon2.level_up()
                # If pokemon2 should evolve, then pokemon2 evolves
                if pokemon2.should_evolve() == True:
                    pokemon2 = pokemon2.get_evolved_version()
                # A new pokemon is retrieved from team1
                pokemon1 = team1.retrieve_pokemon()
            # If pokemon2 is fainted and pokemon1 is not, pokemon1 levels up
            elif pokemon2.is_fainted() == True and pokemon1.is_fainted() == False:
                pokemon1.level_up()
                # If pokemon1 should evolve, then pokemon1 evolves
                if pokemon1.should_evolve() == True:
                    pokemon1 = pokemon1.get_evolved_version()
                # A new pokemon is retrieved from team2
                pokemon2 = team2.retrieve_pokemon()

        # If both teams are empty, return 0
        if pokemon1 == None and pokemon2 == None:
            result = 0
        # If only team1 is empty, return pokemon2 to team2 and team2 wins
        elif pokemon1 == None:
            team2.return_pokemon(pokemon2)
            result = 2
        # If only team2 is empty, return pokemon1 to team1 and team1 wins
        elif pokemon2 == None:
            team1.return_pokemon(pokemon1)
            result = 1

        return result

if __name__ == "__main__":
    # RandomGen.set_seed(1337)
    # team1 = PokeTeam("Ash", [1, 1, 1, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
    # team2 = PokeTeam("Gary", [0, 0, 0, 0, 3], 0, PokeTeam.AI.ALWAYS_ATTACK)
    # b = Battle(verbosity=0)
    # res = b.battle(team1, team2)
    # print(res) #1
    # print(team2.is_empty()) #True
    # print(team1)
    # print(team2)
    # remaining = []
    # while not team1.is_empty():
    #     remaining.append(team1.retrieve_pokemon())
    # print(len(remaining))#2
    # print(remaining[0].get_hp()) #1
    # print(remaining[0]) # Venusaur
    # print(remaining[1].get_hp()) #11
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