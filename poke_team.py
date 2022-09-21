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
            i = 0
            pokemon_total = 0
            for index in range(-1, -(team_size+1), -1):
                if index > -(team_size) and team_numbers[index] != 0:
                    pokemon_total += team_numbers[index]
                    number = 0
                    while number < team_numbers[index]:
                        while i < pokemon_total:
                            self.pokemon_team.push(pokemon_arranged[index])
                            i += 1
                        number += 1
            self.pokemon_team.push(pokemon_arranged[0])
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
            for index in range(self.pokemon_team):
                pass
        else:
            raise Exception("Battle Mode doesn't exist")
    
    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size=None, ai_mode=None, **kwargs):
        if team_size == None:
            team_size = RandomGen.randint(3,6)
        
        team = []
        team.append(0)
        team.append(team_size)
        num = 0
        while num < 4:
            team.append(RandomGen.randint(0,team_size))
            num += 1
        
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
        else:
            raise Exception("Battle Mode doesn't exist")

    def retrieve_pokemon(self) -> PokemonBase | None:
        if self.is_empty():
            return None
        else:
            if self.battle_mode == 0:
                retrieved_pokemon = self.pokemon_team.pop()
            elif self.battle_mode == 1:
                retrieved_pokemon = self.pokemon_team.serve()
            elif self.battle_mode == 2:
                retrieved_pokemon = self.pokemon_team.remove()

            return retrieved_pokemon

    def special(self):
        if self.battle_mode == 0:
            top = self.pokemon_team.pop()
            bottom = self.pokemon_team.index(0)
            self.pokemon_team.push(bottom)

            temporary_stack = ArrayStack(self.pokemon_team.__len__())

            x = 0
            while x < self.pokemon_team.__len__():
                temporary_stack.push(self.pokemon_team.pop())
                x += 1
            
            temporary_stack.pop()
            temporary_stack.push(top)

            y = 0
            while y < temporary_stack.__len__():
                self.pokemon_team.push(temporary_stack.pop())
                y += 1
            
            z = 0
            while z < self.pokemon_team.__len__():
                print(self.pokemon_team.pop())
                z += 1
                
        elif self.battle_mode == 1:
            new_team_size = self.pokemon_team.__len__() // 2
            temporary_stack = ArrayStack(new_team_size)
            for x in range(new_team_size):
                temporary_pokemon = self.pokemon_team.serve()
                temporary_stack.push(temporary_pokemon)
            
            for x in range(temporary_stack.__len__()):
                temporary_pokemon = temporary_stack.pop()
                self.pokemon_team.append(temporary_pokemon)




    def regenerate_team(self):
        team_size = 0
        for number in range(len(self.team_numbers)):
            team_size += self.team_numbers.__getitem__(number)

        pokemon_arranged = [Charmander(), Bulbasaur(), Squirtle(), Gastly(), Eevee()]

        if self.battle_mode == 0:
            self.pokemon_team = ArrayStack(team_size)
            print(team_size)
            i = 0
            pokemon_total = 0
            for index in range(-1, (team_size+1)*-1, -1):
                if index > -(team_size) and self.team_numbers[index] != 0:
                    pokemon_total += self.team_numbers[index]
                    number = 0
                    while number < self.team_numbers[index]: # 0 < 1
                        while i < pokemon_total: # 0 < 1
                            self.pokemon_team.push(pokemon_arranged[index])
                            i += 1
                        number += 1
        elif self.battle_mode == 1:
            self.pokemon_team = CircularQueue(team_size)
            i = 0
            pokemon_total = 0
            for index in range(len(self.team_numbers)):
                if self.team_numbers[index] != 0:
                    pokemon_total += self.team_numbers[index]
                    number = 0
                    while number < self.team_numbers[index]: # 0 < 1
                        while i < pokemon_total: # 0 < 1
                            self.pokemon_team.append(pokemon_arranged[index])
                            i += 1
                        number += 1
        elif self.battle_mode == 2:
            self.pokemon_team = ArraySortedList(team_size)
            i = 0
            pokemon_total = 0
            for index in range(len(self.team_numbers)):
                if self.team_numbers[index] != 0:
                    pokemon_total += self.team_numbers[index]
                    number = 0
                    while number < self.team_numbers[index]: # 0 < 1
                        while i < pokemon_total: # 0 < 1
                            self.pokemon_team.add(pokemon_arranged[index])
                            i += 1
                        number += 1
            for index in range(self.pokemon_team):
                pass
        else:
            raise Exception("Battle Mode doesn't exist")


    def __str__(self):
        if self.battle_mode == 0:
            poke_team_string = ""
            poke_team_string += f"{self.team_name} ({self.battle_mode}): ["
            for pokemon in range(-1, -((self.pokemon_team.__len__())),-1):
                poke_team_string += f"{self.pokemon_team.index(pokemon)}, "
            poke_team_string += f"{self.pokemon_team.index(0)}]"

            return poke_team_string
        elif self.battle_mode == 1:
            poke_team_string = ""
            poke_team_string += f"{self.team_name} ({self.battle_mode}): ["
            for pokemon in range((self.pokemon_team.__len__())-1):
                poke_team_string += f"{self.pokemon_team.index(pokemon)}, "
            poke_team_string += f"{self.pokemon_team.index(-1)}]"

            return poke_team_string
        elif self.battle_mode == 2:
            pass
        else:
            raise Exception("This battle mode doesn't exist")
    
    def is_empty(self):
        return len(self.pokemon_team) == 0

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        counter = 0
        if self.ai_type == None:
            return Action.RANDOM
        else:
            if self.ai_type == PokeTeam.AI.ALWAYS_ATTACK:
                return Action.ATTACK
            elif self.ai_type == PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE:
                return Action.SWAP
            elif self.ai_type == PokeTeam.AI.RANDOM:
                random_action = RandomGen.randint(0, 3)
                if random_action == 2 and counter < 4:
                    counter += 1
                    return Action(random_action)
                else:
                    return Action(random_action)
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

    t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 1, PokeTeam.AI.RANDOM, Criterion.DEF)
    print(t.__str__())
    # self.assertEqual(str(t), "Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP]")
