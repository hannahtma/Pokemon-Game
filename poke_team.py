from __future__ import annotations

from .random_gen import RandomGen

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from enum import Enum, auto
from pokemon_base import PokeType, PokemonBase
from pokemon import Charmander, Bulbasaur, Squirtle, Gastly, Eevee
from array_sorted_list import ArraySortedList
from stack_adt import Stack
from queue_adt import Queue
from sorted_list import SortedList

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
    
    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size=None, ai_mode=None, **kwargs):
        if team_size == None:
            team_size = RandomGen.randint(3,6)
        
        team = []
        for num in range (team_size+2):
            if num == 0:
                team.append(0)
            elif num == team_size+1:
                team.append(team_size)
            else:
                team.append(RandomGen.randint(0,team_size))

        sorted_team = team.sort()
        team_count = []
        for pokemon in range (len(sorted_team)):
            number = sorted_team[pokemon+1] - sorted_team[pokemon]
            team_count.append(number)

        pokemon_team = []
        pokemon_arranged = ["Charmander","Bulbasaur","Squirtle","Gastly","Eevee"]
        for index in range(len(team_count)):
            if index == 0:
                number = 0
                while number < range(sorted_team[index]):
                    pokemon_team.append(pokemon_arranged[index])
            else:
                number = 0
                while number < range(sorted_team[index]-sorted_team[index-1]):
                    pokemon_team.append(pokemon_arranged[index])
                



        team.sort()
        team_count = []
        for pokemon in range(len(team)-1):
            number = team[pokemon+1] - team[pokemon]
            team_count.append(number)
        team_count = team_count[2:]

        cls.pokemon_team = ArraySortedList(len(team_count))
        pokemon_arranged = [Charmander, Bulbasaur, Squirtle, Gastly, Eevee]
        for index in range(len(team_count)):
            if index == 0:
                number = 0
                while number < team[index]:
                    cls.pokemon_team.add(pokemon_arranged[index])
                    number += 1
            else:
                number = 0
                while number < (team[index]-team[index-1]):
                    cls.pokemon_team.add(pokemon_arranged[index])
                    number += 1

        return cls.pokemon_team
    
    def return_pokemon(self, poke: PokemonBase) -> None:
        if self.battle_mode == 0:
            self.new_stack.push(poke)
        elif self.battle_mode == 1:
            self.new_queue.append(poke)
        elif self.battle_mode == 2:
            self.add(poke)

    def retrieve_pokemon(self) -> PokemonBase | None:
        if self.is_empty():
            print("here")
            return None
        else:
            print("there")
            if self.battle_mode == 0:
                self.new_stack = Stack() 
                for pokemon in range((self.pokemon_team.__len__() - 1), -1, -1):
                    self.new_stack.push(self.pokemon_team.__getitem__(pokemon))
                retrieved_pokemon = self.new_stack.pop()
            elif self.battle_mode == 1:
                self.new_queue = Queue()
                for pokemon in self.pokemon_team:
                    self.new_queue.append(pokemon)
                retrieved_pokemon = self.new_queue.serve()
            elif self.battle_mode == 2:
                new_sorted_list = SortedList()
                for pokemon in range(len(self.pokemon_team)):
                    pass

            return retrieved_pokemon

    def special(self):
        raise NotImplementedError()

    def regenerate_team(self):
        raise NotImplementedError()

    def __str__(self):
        poke_team_string = f"{self.team_name} ({self.team_numbers}): [{self.battle_mode}]"
        return poke_team_string

        #"Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Charmander: 9 HP]"
    
    def is_empty(self):
        return cls(**self)
        return len(self) == 0

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        raise NotImplementedError()

    @classmethod
    def leaderboard_team(cls):
        raise NotImplementedError()

if __name__ == "__main__":
    RandomGen.set_seed(123456789)
    t = PokeTeam.random_team("Cynthia", 0)
    pokemon = []
    while not t.is_empty():
        pokemon.append(t.retrieve_pokemon())
    expected_classes = [Squirtle, Gastly, Eevee, Eevee, Eevee, Eevee]
    print(len(pokemon))
    print(len(expected_classes))
    for p, e in zip(pokemon, expected_classes):
        print(p)
        print(e)
