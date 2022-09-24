from __future__ import annotations

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from abc import abstractmethod
from enum import Enum, auto

class PokemonBase:

    def __init__(self, hp: int, poke_type: PokeType) -> None:
        if type(poke_type) != PokeType:
            raise TypeError(str(poke_type) + ' is invalid, only string values accepted')
        if type(hp) != int:
            raise TypeError(hp + " is invalid, only integer values accepted")
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
        self.level += 1
        self.set_hp()
        self.set_attack()
        self.set_speed()
        self.set_defence()

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
        if self.can_evolve() == False:
            raise Exception("This pokemon cannot be evolved")
        elif self.is_fainted() == False:
            return True
        else:
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

