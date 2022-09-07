from __future__ import annotations

from .random_gen import RandomGen

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from enum import Enum, auto
from pokemon_base import PokemonBase

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
        for num in range (team_size):
            if num == 0:
                team.append(0)
            elif num == team_size-1:
                team.append(team_size)
            else:
                team.append(RandomGen.randint(0,team_size))

        sorted_team = team.sort()

        pokemon_team = []
        pokemon_arranged = ["Charmander","Bulbasaur","Squirtle","Gastly","Eevee"]
        for index in range(len(sorted_team)):
            if index == 0:
                number = 0
                while number < range(sorted_team[index]):
                    pokemon_team.append(pokemon_arranged[index])
            else:
                number = 0
                while number < range(sorted_team[index]-sorted_team[index-1]):
                    pokemon_team.append(pokemon_arranged[index])
                



    def return_pokemon(self, poke: PokemonBase) -> None:
        raise NotImplementedError()

    def retrieve_pokemon(self) -> PokemonBase | None:
        raise NotImplementedError()

    def special(self):
        raise NotImplementedError()

    def regenerate_team(self):
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()

    def is_empty(self):
        raise NotImplementedError()

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        raise NotImplementedError()

    @classmethod
    def leaderboard_team(cls):
        raise NotImplementedError()
