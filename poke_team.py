from __future__ import annotations

from .random_gen import RandomGen

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from enum import Enum, auto
from pokemon_base import PokeType, PokemonBase
from stack_adt import Stack
from queue_adt import Queue

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
        RandomGen.randint()
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
                self.new_stack = Stack() 
                for pokemon in range(len(pokemon_team)-1, -1, -1):
                    self.new_stack.push(pokemon_team[pokemon])
                retrieved_pokemon = self.new_stack.pop()
            elif self.battle_mode == 1:
                self.new_queue = Queue()
                for pokemon in pokemon_team:
                    self.new_queue.append(pokemon)
                retrieved_pokemon = self.new_queue.serve()
            elif self.battle_mode == 2:
                retrieved_pokemon = self.remove()

            return retrieved_pokemon

    def special(self):

    def regenerate_team(self):
        raise NotImplementedError()

    def __str__(self):
        poke_team_string = f"{self.team_name} ({self.team_numbers}): [{self.battle_mode}]"
        return poke_team_string

        #"Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Charmander: 9 HP]"
    
    def is_empty(self):
        raise NotImplementedError()

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        raise NotImplementedError()

    @classmethod
    def leaderboard_team(cls):
        raise NotImplementedError()
