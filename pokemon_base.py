from __future__ import annotations

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from abc import abstractmethod
from enum import Enum, auto

class PokemonBase:

    def __init__(self, hp: int, poke_type: str) -> None:
        """
            PokemonBase class definition which initializes max hit points of the pokemon and pokemon type
            
            Parameters: the hit points in integer form and pokemon type in string form
        """
        # Raise error if poke_type is not a string 
        if type(poke_type) != str:
            raise TypeError(poke_type + ' is invalid, only string values accepted')
        self.base_hp = hp
        self.poke_type = poke_type

    def is_fainted(self) -> bool:
        """
            Determine if the pokemon fainted

            Parameters:
                self - refers to this instance of the class
        """
        # if hit points goes down or to or below 0, the pokemon is 'fainted'
        if self.hp <= 0:
            return True
        else:
            return False

    def get_poke_name(self) -> str:
        """
            Define getter method for pokemon name

            Returns: 
                self.poke_name
        """
        return self.poke_name

    def get_level(self) -> int:
        """
            Define getter method for level of pokemon

            Returns: 
                self.level
        """
        return self.level

    def get_hp(self) -> int:
        """
            Define getter method for hit points of pokemon

            Returns: 
                self.hp
        """
        return self.hp

    def get_speed(self) -> int:
        """
            Define getter method for speed points of pokemon

            Returns: 
                self.speed
        """
        return self.speed

    def level_up(self) -> None:
        """
            Method for pokemon to level up

            Parameters:
                self - refers to this instance of the class
        """
        self.level += 1
        self.set_hp()
        self.set_attack()
        self.set_speed()
        self.set_defence()

    def get_attack_damage(self) -> int:
        """
            Define getter method for attack points of pokemon

            Returns: 
                self.attack_damage
        """
        return self.attack_damage

    def get_defence(self) -> int:
        """
            Define getter method for defence points of pokemon

            Returns: 
                self.defence
        """
        return self.defence

    def lose_hp(self, lost_hp: int) -> None:
        """
            Method for pokemon losing hit points

            Parameters:
                self - refers to this instance of the class
                lost_hp - the hit points lost due to the attack
        """
        self.hp -= lost_hp

    def get_poke_type(self) -> str:
        """
            Define getter method for type of pokemon

            Returns: 
                self.poke_type
        """
        return self.poke_type

    def get_status_effect(self) -> str:
        """
            Define getter method for defence points of pokemon

            Returns: 
                self.defence
        """
        return self.status_effect

    @abstractmethod
    def defend(self, damage: int) -> None:
        pass

    @abstractmethod
    def attack(self, other: PokemonBase):
        pass
        # Step 1: Status effects on attack damage / redirecting attacks
        # Step 2: Do the attack
        # Step 3: Losing hp to status effects
        # Step 4: Possibly applying status effects

    def should_evolve(self) -> bool:
        if self.is_fainted() == False and self.can_evolve() == True:
            return True
        elif self.is_fainted() == True:
            return False
        
    @abstractmethod
    def set_hp(self) -> None:
        pass

    @abstractmethod
    def set_attack(self) -> None:
        pass

    @abstractmethod
    def set_speed(self) -> None:
        pass

    @abstractmethod
    def set_defence(self) -> None:
        pass

    @abstractmethod
    def can_evolve(self) -> bool:
        pass

    def heal(self) -> None:
        self.hp = self.base_hp
        self.status_effect = ""

    @abstractmethod
    def get_evolved_version(self) -> PokemonBase:
        pass

    def __str__(self) -> str:
        pokemon_string = f"LV. {self.level} {self.poke_name}: {self.hp} HP"
        return pokemon_string

class PokeType(Enum):
    FIRE = auto()
    GRASS = auto()
    WATER = auto()
    GHOST = auto()
    NORMAL = auto()

