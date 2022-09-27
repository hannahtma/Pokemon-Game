from __future__ import annotations
from unittest.mock import NonCallableMagicMock

from random_gen import RandomGen

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from enum import Enum, auto
from pokemon_base import PokeType, PokemonBase
from pokemon import Charmander, Bulbasaur, Squirtle, Gastly, Eevee
from referential_array import ArrayR
from stack_adt import ArrayStack
from queue_adt import CircularQueue
from array_sorted_list import ArraySortedList

class Action(Enum):
    ATTACK = auto()
    SWAP = auto()
    HEAL = auto()
    SPECIAL = auto()
    
class Criterion(Enum):
    SPD = auto()
    HP = auto()
    LV = auto()
    DEF = auto()

class PokeTeam:

    class AI(Enum):
        ALWAYS_ATTACK = auto()
        SWAP_ON_SUPER_EFFECTIVE = auto()
        RANDOM = auto()
        USER_INPUT = auto()

    def __init__(self, team_name: str, team_numbers: list[int], battle_mode: int, ai_type: PokeTeam.AI, criterion=None, criterion_value=None) -> None:
        self.team_name = team_name
        self.team_numbers = team_numbers
        self.battle_mode = battle_mode
        self.ai_type = ai_type
        self.criterion = criterion
        self.criterion_value = criterion_value

        team_size = 0
        for number in range(len(team_numbers)):
            team_size += team_numbers.__getitem__(number)

        pokemon_arranged = [Charmander(), Bulbasaur(), Squirtle(), Gastly(), Eevee()]

        if battle_mode == 0:
            self.pokemon_team = ArrayStack(team_size)
            print(team_size)
            i = 0
            pokemon_total = 0
            for index in range(-1, (team_size)*-1, -1):
                if team_numbers[index] != 0:
                    pokemon_total += team_numbers[index]
                    number = 0
                    while number < team_numbers[index]: # 0 < 1
                        while i < pokemon_total: # 0 < 1
                            self.pokemon_team.push(pokemon_arranged[index])
                            i += 1
                        number += 1
        elif battle_mode == 1:
            self.pokemon_team = CircularQueue(team_size)
            i = 0
            pokemon_total = 0
            for index in range(len(team_numbers)):
                if team_numbers[index] != 0:
                    pokemon_total += team_numbers[index]
                    number = 0
                    while number < team_numbers[index]: # 0 < 1
                        while i < pokemon_total: # 0 < 1
                            self.pokemon_team.append(pokemon_arranged[index])
                            i += 1
                        number += 1
        elif battle_mode == 2:
            self.pokemon_team = ArraySortedList(team_size)
            i = 0
            pokemon_total = 0
            for index in range(len(team_numbers)):
                if team_numbers[index] != 0:
                    pokemon_total += team_numbers[index]
                    number = 0
                    while number < team_numbers[index]: # 0 < 1
                        while i < pokemon_total: # 0 < 1
                            self.pokemon_team.add(pokemon_arranged[index])
                            i += 1
                        number += 1
    
    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size=None, ai_mode=None, **kwargs):
        if team_size == None:
            team_size = RandomGen.randint(3,6)
        
        team = []
        team.append(0)
        team.append(team_size)
        for num in range(4):
            team.append(RandomGen.randint(0,team_size))
        
        team.sort()
        team_count = []
        for pokemon in range(len(team)-1):
            number = team[pokemon+1] - team[pokemon]
            team_count.append(number)
        team_count = team_count[len(team_count)-5:]

        return PokeTeam(team_name, team_count, battle_mode, ai_mode)
    
    def return_pokemon(self, poke: PokemonBase) -> None:
        if self.battle_mode == 0:
            self.new_stack.push(poke)
        elif self.battle_mode == 1:
            self.new_queue.append(poke)
        elif self.battle_mode == 2:
            self.add(poke)

    def retrieve_pokemon(self) -> PokemonBase | None:
        if self.is_empty():
            return None
        else:
            if self.battle_mode == 0:
                retrieved_pokemon = self.pokemon_team.pop()
            elif self.battle_mode == 1:
                retrieved_pokemon = self.serve()
            elif self.battle_mode == 2:
                retrieved_pokemon = self.remove()

            return retrieved_pokemon

    def special(self):
        raise NotImplementedError()

    def regenerate_team(self):
        PokeTeam(self.team_name, self.team_numbers, self.battle_mode, self.ai_type, self.criterion, self.criterion_value)

    def __str__(self):
        poke_team_string = ""
        poke_team_string += f"{self.team_name} ({self.battle_mode}): "
        for pokemon in range(len(self.pokemon_team)):
            poke_team_string += f"["
            temporary_string = f"{self.pokemon_team[pokemon]}"
            poke_team_string += temporary_string 
            poke_team_string += f"]"

        return poke_team_string
    
    def is_empty(self):
        return len(self.pokemon_team) == 0

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        counter = 0
        if self.ai_type == None:
            self.ai_type = PokeTeam.AI.RANDOM

        if self.ai_type == PokeTeam.AI.ALWAYS_ATTACK:
            return Action.ATTACK
        elif self.ai_type == PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE:
            if their_pokemon.get_effective_attack() >= (1.5 * their_pokemon.get_attack_damage()):
                return Action.SWAP
            else:
                return Action.ATTACK
        elif self.ai_type == PokeTeam.AI.RANDOM:
            random_action = RandomGen.randint(0, 3)
            if random_action == 2 and counter < 3:
                counter += 1
                return Action.random_action
            elif random_action == 2 and counter >= 3:
                raise ValueError("Heal count exceeded 3")
            else:
                return Action.random_action
        elif self.ai_type == PokeTeam.AI.USER_INPUT:
            action_choice = input("Choose your battle option: \n 1. ATTACK 2. SWAP 3. HEAL 4. SPECIAL")
            if action_choice == 1:
                return Action.ATTACK
            elif action_choice == 2:
                return Action.SWAP
            elif action_choice == 3 and counter < 4:
                counter += 1
                return Action.HEAL
            elif action_choice == 4:
                return Action.SPECIAL
            else:
                while action_choice not in range(1,4):
                    action_choice = input("Please enter a valid choice.\nChoose your battle option: \n 1. ATTACK 2. SWAP 3. HEAL 4. SPECIAL")


    @classmethod
    def leaderboard_team(cls):
        raise NotImplementedError()

if __name__ == "__main__":
    # RandomGen.set_seed(123456789)
    # t = PokeTeam.random_team("Cynthia", 0)
    # pokemon = []
    # while not t.is_empty():
    #     pokemon.append(t.retrieve_pokemon())
    # print(pokemon)
    # expected_classes = [Squirtle, Gastly, Eevee, Eevee, Eevee, Eevee]
    # print(len(pokemon))
    # print(len(expected_classes))
    # for p, e in zip(pokemon, expected_classes):
    #     print("p",p)
    #     print("e",e)
    
    # t = PokeTeam("Wallace", [1, 0, 0, 0, 0], 1, PokeTeam.AI.ALWAYS_ATTACK)
    # p = t.retrieve_pokemon()
    # e = Eevee()
    # print(t.choose_battle_option(p, e))

    # RandomGen.set_seed(123456789)
    # t = PokeTeam.random_team("Cynthia", 0)
    # for index in range(len(t)):
    #     print(str(t.__getitem__(index)))

    t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, Criterion.DEF)
    print(t.__str__())
        # self.assertEqual(str(t), "Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP]")
 