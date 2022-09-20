from __future__ import annotations

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from abc import abstractmethod
from enum import Enum

class PokemonBase:

    def __init__(self, hp: int, poke_type: str) -> None:
       self.base_hp = hp
       self.poke_type = poke_type

    def is_fainted(self) -> bool:
        if self.hp <= 0:
            return True
        else:
            return False

    def get_poke_name(self) -> str:
        return self.poke_name

    def get_level(self) -> int:
        return self.level

    def get_hp(self) -> int:
        return self.hp

    def get_speed(self) -> int:
        return self.speed

    def get_hp(self):
        return self.hp

    def get_level(self) -> int:
        return self.level

    def level_up(self) -> None:
        holder = self.base_hp - self.hp
        self.level += 1
        self.hp = self.hp - holder

    def get_speed(self) -> int:
        return self.speed

    def get_attack_damage(self) -> int:
        return self.attack_damage

    def get_defence(self) -> int:
        return self.defence

    def lose_hp(self, lost_hp: int) -> None:
        self.hp -= lost_hp

    def get_poke_type(self) -> str:
        return self.poke_type

    def get_status_effect(self) -> str:
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
            holder = self.base_hp - self.hp
            a = self.get_evolved_version()
            a.hp = a.hp - holder
            return True
        elif self.is_fainted() == True:
            return False
        
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
    FIRE = "Fire"
    GRASS = "Grass"
    WATER = "Water"
    GHOST = "Ghost"
    NORMAL = "Normal"

