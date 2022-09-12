from __future__ import annotations

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from enum import Enum

class PokemonBase:

    def __init__(self, hp: int, poke_type: str) -> None:
       self.hp = hp
       self.poke_type = poke_type

    def is_fainted(self) -> bool:
        if self.hp <= 0:
            return True
        else:
            return False

    def get_level(self) -> int:
        return self.level

    def level_up(self) -> None:
        self.level = self.get_level() + 1

    def get_speed(self) -> int:
        return self.speed

    def get_attack_damage(self) -> int:
        return self.attack_damage

    def get_defence(self) -> int:
        return self.defence

    def lose_hp(self, lost_hp: int) -> None:
        self.hp -= lost_hp

    def defend(self, damage: int) -> None:
        pokemon_name = self.get_poke_name()
        if pokemon_name == "Charmander":
            if damage >= self.defence:
                self.hp -= damage
            else:
                self.hp -= damage // 2
        elif pokemon_name == "Squirtle" or pokemon_name == "Blastoise":
            if damage > 2 * self.defence:
                self.hp -= damage
            else:
                self.hp -= damage // 2
        elif pokemon_name == "Bulbasaur" or pokemon_name == "Venusaur":
            if damage > self.defence + 5:
                self.hp -= damage
            else:
                self.hp -= damage // 2
        elif pokemon_name == "Gastly" or pokemon_name == "Haunter" or pokemon_name == "Gengar":
            self.hp -= damage
        elif pokemon_name == "Eevee":
            if damage >= self.defence:
                self.hp -= damage
            else:
                self.hp = self.hp
        elif pokemon_name == "Charizard":
            if damage > self.defence:
                self.hp -= 2 * damage
            else:
                self.hp -= damage

    def attack(self, other: PokemonBase):
        if other.get_defence() == 
        # Step 1: Status effects on attack damage / redirecting attacks
        # Step 2: Do the attack
        # Step 3: Losing hp to status effects
        # Step 4: Possibly applying status effects

    def get_poke_name(self) -> str:
        return self.poke_name

    def should_evolve(self) -> bool:
        if self.is_fainted() == False:
            return True
        elif self.is_fainter() == True:
            return False
        
    def can_evolve(self) -> bool:
        if self.get_level() == 1 and self.get_poke_name == "Gastly":
            return True
        elif self.get_level() == 3 and (self.get_poke_name == "Charmander" or self.get_poke_name == "Squirtle" or self.get_poke_name == "Haunter"):
            return True
        elif self.get_level() == 2 and self.get_poke_name == "Bulbasaur":
            return True
        else:
            return False

    def heal(self):
        if self.get_poke_name == "Charmander":
            self.hp = 8 + 1 * self.get_level()
        elif self.get_poke_name == "Squirtle":
            self.hp = 9 + 2 * self.get_level()
        elif self.get_poke_name == "Bulbasaur" or self.get_poke_name == "Charizard":
            self.hp = 12 + 1 * self.get_level()
        elif self.get_poke_name == "Gastly":
            self.hp = 6 + (self.get_level() // 2)
        elif self.get_poke_name == "Eevee":
            self.hp = 10
        elif self.get_poke_name == "Blastoise":
            self.hp = 15 + 2 * self.get_level()
        elif self.get_poke_name == "Venusaur":
            self.hp = 20 + (self.get_level() // 2)
        elif self.get_poke_name == "Haunter":
            self.hp = 9 + (self.get_level() // 2)
        elif self.get_poke_name == "Gengar":
            self.hp = 12 + (self.get_level() // 2)

    def get_evolved_version(self) -> PokemonBase:
        if PokeType == FIRE:

    def __str__(self) -> str:
        raise NotImplementedError()

class PokeType:
    def __init__(self):
        attack_multiplier = [[1, 2, 0.5, 1, 1],[0.5, 1, 2, 1, 1],[2, 0.5, 1, 1, 1],[1.25, 1.25, 1.25, 2, 0],[1.25, 1.25, 1.25, 0, 1]]
        FIRE = attack_multiplier[0]
        GRASS = attack_multiplier[1]
        WATER = attack_multiplier[2]
        GHOST = attack_multiplier[3]
        NORMAL = attack_multiplier[4]
