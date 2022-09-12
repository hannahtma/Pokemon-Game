from __future__ import annotations

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

class PokemonBase:

    def __init__(self, hp: int, poke_type) -> None:
       self.currenthp = hp
       self.poke_type = poke_type

    def is_fainted(self) -> bool:
        if self.currenthp <= 0:
            return True
        else:
            return False

    def get_level(self) -> int:
        return self.level

    def level_up(self) -> None:
        self.level = self.get_level + 1

    def get_speed(self) -> int:
        return self.speed

    def get_attack_damage(self) -> int:
        return self.attack

    def get_defence(self) -> int:
        return self.defence

    def lose_hp(self, lost_hp: int) -> None:
        self.currenthp -= lost_hp

    def defend(self, damage: int) -> None:
        pass

    def attack(self, other: PokemonBase):
        raise NotImplementedError()
        # Step 1: Status effects on attack damage / redirecting attacks
        # Step 2: Do the attack
        # Step 3: Losing hp to status effects
        # Step 4: Possibly applying status effects

    def get_poke_name(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()

    def should_evolve(self) -> bool:
        raise NotImplementedError()

    def can_evolve(self) -> bool:
        raise NotImplementedError()

    def get_evolved_version(self) -> PokemonBase:
        raise NotImplementedError()

class PokeType:
    attack_multiplier = [[1,2,0.5,1,1],
                         [0.5,1,2,1,1],
                         [2,0.5,1,1,1],
                         [1.25,1.25,1.25,2,0],
                         [1.25,1.25,1.25,0,1]]
    FIRE = attack_multiplier[0]
    GRASS = attack_multiplier[1]
    WATER = attack_multiplier[2]
    GHOST = attack_multiplier[3]
    NORMAL = attack_multiplier[4]