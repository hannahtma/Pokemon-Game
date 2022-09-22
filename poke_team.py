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
from sorted_list import ListItem

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
        print(self.criterion)

        kwargs = {"criterion":self.criterion}

        team_size = 0
        for number in range(len(team_numbers)):
            team_size += team_numbers.__getitem__(number)

        pokemon_arranged = [Charmander(), Bulbasaur(), Squirtle(), Gastly(), Eevee()]

        if battle_mode == 0:
            self.pokemon_team = ArrayStack(team_size)
            i = 0
            pokemon_total = 0
            for index in range(-1, (team_size+1)*-1, -1):
                if index > -(team_size) and team_numbers[index] != 0:
                    pokemon_total += team_numbers[index]
                    number = 0
                    while number < team_numbers[index]:
                        while i < pokemon_total:
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
            self.temporary_list = ArraySortedList(team_size)
            i = 0
            pokemon_total = 0
            for index in range(len(team_numbers)):
                if team_numbers[index] != 0:
                    pokemon_total += team_numbers[index]
                    number = 0
                    while number < team_numbers[index]:
                        while i < pokemon_total:
                            self.pokemon_class = pokemon_arranged[index]
                            pokemon = ListItem(pokemon_arranged[index], self.pokemon_criterion(self.pokemon_class))
                            self.temporary_list.add(pokemon)
                            i += 1
                        number += 1
            
            self.pokemon_team = ArraySortedList(team_size)
            counter = 0
            while counter < team_size:
                for element in range(-1, -(self.temporary_list.__len__() + 1), -1):
                    print(element)
                    print(counter)
                    self.pokemon_team.__setitem__(counter, self.temporary_list.__getitem__(element))

                    counter += 1

            pokemon = ListItem(Bulbasaur(), 13)
            print(self.pokemon_team.__contains__(pokemon))
            #print(self.pokemon_team.is_full())
            for x in self.pokemon_team:
                print("x",x)

            print("hello",self.pokemon_team.delete_at_index().value)

            # self.unsorted_poketeam = ArraySortedList(team_size)
            # i = 0
            # pokemon_total = 0
            # for index in range(len(team_numbers)):
            #     if team_numbers[index] != 0:
            #         pokemon_total += team_numbers[index]
            #         number = 0
            #         while number < team_numbers[index]: # 0 < 1
            #             while i < pokemon_total: # 0 < 1
            #                 self.unsorted_poketeam.__setitem__(index, pokemon_arranged[index])
            #                 i += 1
            #             number += 1
            
            # print(self.unsorted_poketeam.__getitem__(index))

    def pokemon_criterion(self, pokemon: PokemonBase):
        if self.criterion == Criterion.SPD:
            return pokemon.get_speed()
        elif self.criterion == Criterion.HP:
            return pokemon.get_hp()
        elif self.criterion == Criterion.LV:
            return pokemon.get_level()
        elif self.criterion == Criterion.DEF:
            return pokemon.get_defence()

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

        return PokeTeam(team_name, team_count, battle_mode, ai_mode, kwargs)
    
    def return_pokemon(self, poke: PokemonBase) -> None:
        if self.battle_mode == 0:
            self.pokemon_team.push(poke)
        elif self.battle_mode == 1:
            self.pokemon_team.append(poke)
        elif self.battle_mode == 2:
            pokemon = ListItem(poke, self.pokemon_criterion(poke))
            self.pokemon_team.add(pokemon)

            #pokemon = ListItem(pokemon_arranged[index], self.pokemon_criterion(self.pokemon_class))

    def retrieve_pokemon(self) -> PokemonBase | None:
        if self.is_empty():
            return None
        else:
            if self.battle_mode == 0:
                retrieved_pokemon = self.pokemon_team.pop()
            elif self.battle_mode == 1:
                retrieved_pokemon = self.pokemon_team.serve()
            elif self.battle_mode == 2:
                retrieved_pokemon = self.pokemon_team.delete_at_index(0).value

            return retrieved_pokemon

    def special(self):
        if self.battle_mode == 0:
            top = self.pokemon_team.pop()
            bottom = self.pokemon_team.index(0)
            self.pokemon_team.push(bottom)

            temporary_stack = ArrayStack(self.pokemon_team.__len__())

            for x in range(self.pokemon_team.__len__()):
                temporary_stack.push(self.pokemon_team.pop())
            
            temporary_stack.pop()
            temporary_stack.push(top)

            for x in range(temporary_stack.__len__()):
                self.pokemon_team.push(temporary_stack.pop())
                        
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
        PokeTeam(self.team_name, self.team_numbers, self.battle_mode, self.ai_type, self.criterion, self.criterion_value)

    def __str__(self):
        poke_team_string = ""
        poke_team_string += f"{self.team_name} ({self.battle_mode}): ["

        for pokemon in range(self.pokemon_team.__len__()):
            if self.battle_mode == 0:
                temporary_string = f"{self.pokemon_team.index(pokemon)} "
                poke_team_string += temporary_string
            elif self.battle_mode == 1:
                temporary_string = f"{self.pokemon_team.serve()} "
                poke_team_string += temporary_string
            elif self.battle_mode == 2:
                temporary_string = f"{self.pokemon_team.__getitem__(pokemon).value}, "
                poke_team_string += temporary_string

        poke_team_string += f"]"

        return poke_team_string

        # final_string = "" #initializing the string
        # for x in range(len(self.people)): #adding each person to the string
        #     string = f"{self.people[x+1]}\n"
        #     final_string += string
        # return final_string

        #"Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Charmander: 9 HP]"
    
    def is_empty(self):
        return self.pokemon_team.__len__() == 0

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
    # t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 0, PokeTeam.AI.RANDOM, Criterion.DEF)
    # print(type(t.retrieve_pokemon()))
    # print(t.__str__())
        #self.assertEqual(str(t), "Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Eevee: 10 HP, LV. 1 Charmander: 9 HP]")
    
    t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, Criterion.HP)
    p = t.retrieve_pokemon()
    # print("p",p)
    # p.lose_hp(1)
    # t.return_pokemon(p)

    # print(str(t))
    