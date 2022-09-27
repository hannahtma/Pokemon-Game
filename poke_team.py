from __future__ import annotations
from unittest.mock import NonCallableMagicMock

from random_gen import RandomGen

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by everyone"

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
        """
            PokeTeam class definition which initializes the features of the pokemon team
            
            Parameters: 
                self - refers to this instance of the class
                team_name - name of pokemon team
                team_numbers - numbers in the team in a list
                battle_mode - battle mode number
                ai_type - PokeTeam.AI
                criterion - None value
                criterion_value - None value
        """
        self.team_name = team_name
        self.team_numbers = team_numbers
        self.battle_mode = battle_mode
        self.ai_type = ai_type
        self.criterion = criterion
        self.criterion_value = criterion_value

        team_size = 0
        for number in range(len(self.team_numbers)):
            team_size += self.team_numbers.__getitem__(number)
        
        if self.battle_mode == 0:
            self.pokemon_team = ArrayStack(team_size)
            i = 0
            pokemon_total = 0
            for index in range(-1, -(len(self.team_numbers)+1), -1):
                if index > -7 and self.team_numbers[index] != 0:
                    pokemon_total += self.team_numbers[index]
                    number = 0
                    while number < self.team_numbers[index]:
                        while i < pokemon_total:
                            if index == -1:
                                self.pokemon_team.push(Eevee())
                            elif index == -2:
                                self.pokemon_team.push(Gastly())
                            elif index == -3:
                                self.pokemon_team.push(Squirtle())
                            elif index == -4:
                                self.pokemon_team.push(Bulbasaur())
                            elif index == -5:
                                self.pokemon_team.push(Charmander())
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
                            if index == 0:
                                self.pokemon_team.append(Charmander())
                            elif index == 1:
                                self.pokemon_team.append(Bulbasaur())
                            elif index == 2:
                                self.pokemon_team.append(Squirtle())
                            elif index == 3:
                                self.pokemon_team.append(Gastly())
                            elif index == 4:
                                self.pokemon_team.append(Eevee())
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
                    while number < self.team_numbers[index]:
                        while i < pokemon_total:
                            if index == 0:
                                self.pokemon_class = Charmander()
                                pokemon = ListItem(self.pokemon_class, self.pokemon_criterion(self.pokemon_class))
                                self.pokemon_team.add(pokemon)
                            elif index == 1:
                                self.pokemon_class = Bulbasaur()
                                pokemon = ListItem(self.pokemon_class, self.pokemon_criterion(self.pokemon_class))
                                self.pokemon_team.add(pokemon)
                            elif index == 2:
                                self.pokemon_class = Squirtle()
                                pokemon = ListItem(self.pokemon_class, self.pokemon_criterion(self.pokemon_class))
                                self.pokemon_team.add(pokemon)
                            elif index == 3:
                                self.pokemon_class = Gastly()
                                pokemon = ListItem(self.pokemon_class, self.pokemon_criterion(self.pokemon_class))
                                self.pokemon_team.add(pokemon)
                            elif index == 4:
                                self.pokemon_class = Eevee()
                                pokemon = ListItem(self.pokemon_class, self.pokemon_criterion(self.pokemon_class))
                                self.pokemon_team.add(pokemon)
                            i += 1
                        number += 1

    def pokemon_criterion(self, pokemon: PokemonBase):
        """ Method that determines criterion of pokemon
        
            Parameter: 
                self - refers to this instance of the class
                pokemon - pokemon from pokemon base
            
            Returns:
                getter method according to the criterion
        """
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
        """ Method that creates a random team according to the rules
        
            Parameter: 
                cls - refers to this class
                team_name - name of pokemon team
                battle_mode - battle mode number
                team_size - None value
                ai_mode - None value
                **kwargs - takes a not predefined argument in the form of a dictionary
            
            Returns:
                a random PokeTeam
        """
        if kwargs == {}:
            criterion = None
        elif kwargs != None:
            criterion = kwargs["criterion"]

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

        return PokeTeam(team_name, team_count, battle_mode, ai_mode, criterion)
    
    def return_pokemon(self, poke: PokemonBase) -> None:
        """ Method that returns a pokemon to a team
        
            Parameter: 
                self - refers to this instance of the class
                poke - PokemonBase class
        """
        poke.status_effect = ""
        if self.battle_mode == 0:
            if poke.is_fainted() == False:
                self.pokemon_team.push(poke)
        elif self.battle_mode == 1:
            if poke.is_fainted() == False:
                self.pokemon_team.append(poke)
        elif self.battle_mode == 2:
            if poke.is_fainted() == False:
                pokemon = ListItem(poke, self.pokemon_criterion(poke))
                self.pokemon_team.add(pokemon)

    def retrieve_pokemon(self) -> PokemonBase | None:
        """ Method that  retrieves a pokemon from the team.
            If the team is empty, return None
        
            Parameter: 
                self - refers to this instance of the class

            Returns:
                retrieved pokemon
        """
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
        """
            Complete the special operation on the team depending on battle mode
        """
        # If battle mode 0, swap the first and the last pokemon by using a temporary_stack
        if self.battle_mode == 0:
            # Assign the pokemon at the top of stack to top
            top = self.pokemon_team.pop()
            # Assign the pokemon at the bottom of the stack to bottom
            bottom = self.pokemon_team.index(0)
            self.pokemon_team.push(bottom)

            temporary_stack = ArrayStack(self.pokemon_team.__len__())

            # Push the pokemon into a temporary stack
            for x in range(self.pokemon_team.__len__()):
                temporary_stack.push(self.pokemon_team.pop())
            
            # Remove the pokemon from the top of the stack
            temporary_stack.pop()
            # Add the top pokemon back to top of stack
            temporary_stack.push(top)

            # Push the temporary stack back to pokemon team
            for x in range(temporary_stack.__len__()):
                self.pokemon_team.push(temporary_stack.pop())
        
        # If battle mode 1, move the end pokemon to the front of the queue and reverse the front pokemon and add it to the back of the queue
        elif self.battle_mode == 1:
            # Get the front pokemon that needs to be moved
            new_team_size = self.pokemon_team.__len__() // 2
            temporary_stack = ArrayStack(new_team_size)
            # Push the front pokemon to a temporary stack 
            for x in range(new_team_size):
                temporary_pokemon = self.pokemon_team.serve()
                temporary_stack.push(temporary_pokemon)
            
            # Add the pokemon from the temporary stack back to the queue
            for x in range(temporary_stack.__len__()):
                temporary_pokemon = temporary_stack.pop()
                self.pokemon_team.append(temporary_pokemon)

    def regenerate_team(self):
        """
            Regenerate the team from the same battle numbers. Used to make a team ready for another battle.

            Returns:
                regenerated PokeTeam
        """
        # Initialise team_size to 0
        team_size = 0
        # Iterate through self.team_numbers and add total number of pokemon to team_size
        for number in range(len(self.team_numbers)):
            team_size += self.team_numbers.__getitem__(number)
        
        # If self.battle_mode == 0, create an ArrayStack
        if self.battle_mode == 0:
            self.pokemon_team = ArrayStack(team_size)
            i = 0
            pokemon_total = 0
            # Iterate through self.team_numbers and add pokemon to self.pokemon_team using stack adt
            for index in range(-1, -(len(self.team_numbers)+1), -1):
                if index > -7 and self.team_numbers[index] != 0:
                    pokemon_total += self.team_numbers[index]
                    number = 0
                    while number < self.team_numbers[index]:
                        while i < pokemon_total:
                            # Use push to add pokemon following pokedex order
                            if index == -1:
                                self.pokemon_team.push(Eevee())
                            elif index == -2:
                                self.pokemon_team.push(Gastly())
                            elif index == -3:
                                self.pokemon_team.push(Squirtle())
                            elif index == -4:
                                self.pokemon_team.push(Bulbasaur())
                            elif index == -5:
                                self.pokemon_team.push(Charmander())
                            i += 1
                        number += 1
        # If self.battle_mode == 0, create a CircularQueue
        elif self.battle_mode == 1:
            self.pokemon_team = CircularQueue(team_size)
            i = 0
            pokemon_total = 0
            # Iterate through self.team_numbers and add pokemon to self.pokemon_team using queue adt
            for index in range(len(self.team_numbers)):
                if self.team_numbers[index] != 0:
                    pokemon_total += self.team_numbers[index]
                    number = 0
                    while number < self.team_numbers[index]: # 0 < 1
                        while i < pokemon_total: # 0 < 1
                            # Use append to add pokemon following pokedex order
                            if index == 0:
                                self.pokemon_team.append(Charmander())
                            elif index == 1:
                                self.pokemon_team.append(Bulbasaur())
                            elif index == 2:
                                self.pokemon_team.append(Squirtle())
                            elif index == 3:
                                self.pokemon_team.append(Gastly())
                            elif index == 4:
                                self.pokemon_team.append(Eevee())
                            i += 1
                        number += 1
        # If self.battle_mode == 0, create an ArraySortedList
        elif self.battle_mode == 2:
            self.pokemon_team = ArraySortedList(team_size)
            i = 0
            pokemon_total = 0
            # Iterate through self.team_numbers and add pokemon to self.pokemon_team using array sorted list adt
            for index in range(len(self.team_numbers)):
                if self.team_numbers[index] != 0:
                    pokemon_total += self.team_numbers[index]
                    number = 0
                    while number < self.team_numbers[index]:
                        while i < pokemon_total:
                            # Use add to add pokemon following pokedex order
                            if index == 0:
                                self.pokemon_class = Charmander()
                                pokemon = ListItem(self.pokemon_class, self.pokemon_criterion(self.pokemon_class))
                                self.pokemon_team.add(pokemon)
                            elif index == 1:
                                self.pokemon_class = Bulbasaur()
                                pokemon = ListItem(self.pokemon_class, self.pokemon_criterion(self.pokemon_class))
                                self.pokemon_team.add(pokemon)
                            elif index == 2:
                                self.pokemon_class = Squirtle()
                                pokemon = ListItem(self.pokemon_class, self.pokemon_criterion(self.pokemon_class))
                                self.pokemon_team.add(pokemon)
                            elif index == 3:
                                self.pokemon_class = Gastly()
                                pokemon = ListItem(self.pokemon_class, self.pokemon_criterion(self.pokemon_class))
                                self.pokemon_team.add(pokemon)
                            elif index == 4:
                                self.pokemon_class = Eevee()
                                pokemon = ListItem(self.pokemon_class, self.pokemon_criterion(self.pokemon_class))
                                self.pokemon_team.add(pokemon)
                            i += 1
                        number += 1

    def __str__(self):
        """
            String representation of PokeTeam based on battle mode
        """
        # Initialise empty poke_team_string
        poke_team_string = ""
        # Add self.team_name and self.battle_mode
        poke_team_string += f"{self.team_name} ({self.battle_mode}): ["
        # If battle mode 0, string the pokemon from top of stack to bottom of stack
        if self.battle_mode == 0:
            for pokemon in range(-1, -((self.pokemon_team.__len__())),-1):
                poke_team_string += f"{self.pokemon_team.index(pokemon)}, "
            poke_team_string += f"{self.pokemon_team.index(0)}]"
        # If battle mode 1, string the pokemon from front of queue to back of queue
        elif self.battle_mode == 1:
            for pokemon in range((self.pokemon_team.__len__())-1):
                poke_team_string += f"{self.pokemon_team.index(pokemon)}, "
            poke_team_string += f"{self.pokemon_team.index(-1)}]"
        # If battle mode 2, string the pokemon following criterion value
        elif self.battle_mode == 2:
            for pokemon in range((self.pokemon_team.__len__())-1):
                poke_team_string += f"{self.pokemon_team.__getitem__(pokemon).value}, "
            poke_team_string += f"{self.pokemon_team.__getitem__(-1).value}]"
        # Otherwise, raise exception for non-existent battle mode
        else:
            raise Exception("This battle mode doesn't exist")
        
        return poke_team_string

    def is_empty(self):
        """
            Checks whether the team is currently empty.

            Returns:
                boolean based on whether the team is empty
        """
        # Return True if self.pokemon_team is empty
        return self.pokemon_team.__len__() == 0

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        """
            Decides on an action depending on the pokemon currently in the field.

            Parameters:
                my_pokemon - pokemon of my team
                their_pokemon - pokemon of opposing team

            Returns:
                Action based on the ai_type and pokemon

        """

        counter = 0
        # if self.ai_type is None, set self.ai_type to RANDOM
        if self.ai_type == None:
            self.ai_type = PokeTeam.AI.RANDOM

        # If self.ai_type is ALWAYS_ATTACK, return action ATTACK
        if self.ai_type == PokeTeam.AI.ALWAYS_ATTACK:
            return Action.ATTACK
        # If self.ai_type is SWAP_ON_SUPER_EFFECTIVE
        elif self.ai_type == PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE:
            # If effective attack is more than or equal to 1.5 times their attack damage, return action SWAP
            if their_pokemon.get_effective_attack() >= (1.5 * their_pokemon.get_attack_damage()):
                return Action.SWAP
            # If not, return action ATTTACK
            else:
                return Action.ATTACK
        # If self.ai_type is RANDOM
        elif self.ai_type == PokeTeam.AI.RANDOM:
            # Random generate an action between 0 and 3
            random_action = RandomGen.randint(0, 3)
            # If random_action is 2 (heal) and counter < 3, then return action HEAL
            if random_action == 2 and counter < 3:
                counter += 1
                return Action.random_action
            # If random_action is 2 (heal) and counter >= 3, then raise error
            elif random_action == 2 and counter >= 3:
                raise ValueError("Heal count exceeded 3")
            # Otherwise, return action based on random
            else:
                return Action.random_action
        # If self.ai_type is USER_INPUT
        elif self.ai_type == PokeTeam.AI.USER_INPUT:
            # Prompt for user input
            action_choice = input("Choose your battle option: \n 1. ATTACK 2. SWAP 3. HEAL 4. SPECIAL")
            # If action_choice is 1, return action ATTACK
            if action_choice == 1:
                return Action.ATTACK
            # If action_choice is 2, return action SWAP
            elif action_choice == 2:
                return Action.SWAP
            # If action_choice is 3 and counter is less than 4, then return action HEAL
            elif action_choice == 3 and counter < 4:
                counter += 1
                return Action.HEAL
            # If action_choice is 4, return action SPECIAL
            elif action_choice == 4:
                return Action.SPECIAL
            # Otherwise, keep prompting until user enters valid action
            else:
                while action_choice not in range(1,4):
                    action_choice = input("Please enter a valid choice.\nChoose your battle option: \n 1. ATTACK 2. SWAP 3. HEAL 4. SPECIAL")

    @classmethod
    def leaderboard_team(cls):
        raise NotImplementedError()


if __name__ == "__main__":
    RandomGen.set_seed(123456789)
    t = PokeTeam.random_team("Cynthia", 2, team_size=4, criterion=Criterion.HP)
    # This should end, since all pokemon are fainted, slowly.
    while not t.is_empty():
        p = t.retrieve_pokemon()
        p.lose_hp(1)
        t.return_pokemon(p)
    print(t.is_empty())
    t.regenerate_team()
    print(t)
    pokemon = []
    while not t.is_empty():
        print("Here")
        pokemon.append(t.retrieve_pokemon())
    expected_classes = [Bulbasaur, Eevee, Charmander, Gastly]
    print("pokemon length",len(pokemon))
    print("expected classes length", len(expected_classes))
    for p, e in zip(pokemon, expected_classes):
        print("p",p)
        print("e",e)