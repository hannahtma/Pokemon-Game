"""
"""
from pokemon_base import PokemonBase, PokeType
from random_gen import RandomGen

class Charmander(PokemonBase):
    def __init__(self):
        self.poke_name = "Charmander"
        self.poke_type = "Fire"
        self.level = 1
        self.hp = int(8 + 1 * self.level)
        self.attack_damage = int(6 + 1 * self.level)
        self.speed = int(7 + 1 * self.level)
        self.defence = 4
        self.status_effect = ""
        self.effective_attack = 0

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        holder = self.base_hp - self.hp
        self.hp = 8 + 1 * self.level
        self.base_hp = self.hp
        self.hp -= holder

    def set_attack(self) -> None:
        self.attack_damage = 6 + 1 * self.level

    def set_speed(self) -> None:
        self.speed = 7 + 1 * self.level

    def set_defence(self) -> None:
        return None

    def defend(self, damage: int) -> None:
        if damage > self.defence:
            self.hp -= damage
        else:
            self.hp -= damage // 2

    def attack(self, other: PokemonBase):
        if self.get_status_effect() == "Sleep":
            return None
        elif RandomGen.random_chance(0.5) == True and self.get_status_effect() == "Confusion":
            other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Grass":
            self.effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Water":
            self.effective_attack = int(self.attack_damage * 0.5)
        elif other.get_poke_type() == "Ghost":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            self.effective_attack = self.attack_damage * 1

        if self.get_status_effect() == "Burn":
            self.effective_attack // 2

        other.defend(self.effective_attack)

        self.health_cuts()

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Burn"

    def can_evolve(self) -> bool:
        if self.level == 3:
            return True
        else:
            return False

    def get_evolved_version(self) -> PokemonBase:
        c = Charizard()
        holder = self.base_hp - self.hp
        c.hp -= holder
        return c

class Squirtle(PokemonBase):
    def __init__(self):
        self.poke_name = "Squirtle"
        self.poke_type = "Water"
        self.level = 1
        self.hp = int(9 + 2 * self.level)
        self.attack_damage = int(4 + (self.level // 2))
        self.speed = int(7)
        self.defence = int(6 + self.level)
        self.status_effect = ""
        self.effective_attack = 0

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        holder = self.base_hp - self.hp
        self.hp = 9 + 2 * self.level
        self.base_hp = self.hp
        self.hp -= holder

    def set_attack(self) -> None:
        self.attack_damage = 4 + (self.level // 2)

    def set_speed(self) -> None:
        return None

    def set_defence(self) -> None:
        self.defence = 6 + self.level

    def defend(self, damage: int) -> None:
        if damage > (self.defence * 2):
            self.hp -= damage
        else:
            self.hp -= damage // 2

    def attack(self, other: PokemonBase):
        if self.get_status_effect() == "Sleep":
            return None
        elif RandomGen.random_chance(0.5) == True and self.get_status_effect() == "Confusion":
            other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            self.effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Grass":
            self.effective_attack = int(self.attack_damage * 0.5)
        elif other.get_poke_type() == "Water":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Ghost":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            self.effective_attack = self.attack_damage * 1

        if self.get_status_effect() == "Burn":
            self.effective_attack // 2

        other.defend(self.effective_attack)

        self.health_cuts()

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Paralysis"

    def can_evolve(self) -> bool:
        if self.level == 3:
            return True
        else:
            return False

    def get_evolved_version(self) -> PokemonBase:
        b = Blastoise()
        holder = self.base_hp - self.hp
        b.hp -= holder
        return b

class Bulbasaur(PokemonBase):
    def __init__(self):
        self.poke_name = "Bulbasaur"
        self.poke_type = "Grass"
        self.level = 1
        self.hp = int(12 + 1 * self.level)
        self.attack_damage = int(5)
        self.speed = int(7 + (self.level // 2))
        self.defence = int(5)
        self.status_effect = ""
        self.effective_attack = 0

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        holder = self.base_hp - self.hp
        self.hp = int(12 + 1 * self.level)
        self.base_hp = self.hp
        self.hp -= holder

    def set_attack(self) -> None:
        return None

    def set_speed(self) -> None:
        self.speed = int(7 + (self.level // 2))

    def set_defence(self) -> None:
        return None

    def defend(self, damage: int) -> None:
        if damage > (self.defence + 5):
            self.hp -= damage
        else:
            self.hp -= damage // 2

    def attack(self, other: PokemonBase):
        if self.get_status_effect() == "Sleep":
            return None
        elif RandomGen.random_chance(0.5) == True and self.get_status_effect() == "Confusion":
            other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            self.effective_attack = int(self.attack_damage * 0.5)
        elif other.get_poke_type() == "Grass":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Water":
            self.effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Ghost":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            self.effective_attack = self.attack_damage * 1

        if self.get_status_effect() == "Burn":
            self.effective_attack // 2

        other.defend(self.effective_attack)

        self.health_cuts()

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Poison"

    def can_evolve(self) -> bool:
        if self.level == 2:
            return True
        else:
            return False

    def get_evolved_version(self) -> PokemonBase:
        v = Venusaur()
        holder = self.base_hp - self.hp
        v.hp -= holder
        return v
    
class Gastly(PokemonBase):
    def __init__(self):
        self.poke_name = "Gastly"
        self.poke_type = "Ghost"
        self.level = 1
        self.hp = 6 + (self.level // 2)
        self.attack_damage = 4
        self.speed = 2
        self.defence = 8
        self.status_effect = ""
        self.effective_attack = 0

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        holder = self.base_hp - self.hp
        self.hp = 6 + (self.level // 2)
        self.base_hp = self.hp
        self.hp -= holder

    def set_attack(self) -> None:
        return None

    def set_speed(self) -> None:
        return None

    def set_defence(self) -> None:
        return None

    def defend(self, damage: int) -> None:
        self.hp -= damage

    def attack(self, other: PokemonBase):
        if self.get_status_effect() == "Sleep":
            return None
        elif RandomGen.random_chance(0.5) == True and self.get_status_effect() == "Confusion":
            other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Grass":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Water":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Ghost":
            self.effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Normal":
            self.effective_attack = 0

        if self.get_status_effect() == "Burn":
            self.effective_attack // 2

        other.defend(self.effective_attack)

        self.health_cuts()

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Sleep"

    def can_evolve(self) -> bool:
        if self.level == 1:
            return True
        else:
            return False

    def get_evolved_version(self) -> PokemonBase:
        h = Haunter()
        holder = self.base_hp - self.hp
        h.hp -= holder
        return h

class Eevee(PokemonBase):
    def __init__(self):
        self.poke_name = "Eevee"
        self.poke_type = "Normal"
        self.level = 1
        self.hp = int(10)
        self.attack_damage = int(6 + self.level)
        self.speed = int(7 + self.level)
        self.defence = int(4 + self.level)
        self.status_effect = ""
        self.effective_attack = 0

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        return None

    def set_attack(self) -> None:
        self.attack_damage = int(6 + self.level)

    def set_speed(self) -> None:
        self.speed = int(7 + self.level)

    def set_defence(self) -> None:
        self.defence = int(4 + self.level)

    def defend(self, damage: int) -> None:
        if damage >= self.defence:
            self.hp -= damage

    def attack(self, other: PokemonBase):
        if self.get_status_effect() == "Sleep":
            return None
        elif RandomGen.random_chance(0.5) == True and self.get_status_effect() == "Confusion":
            other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Grass":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Water":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Ghost":
            self.effective_attack = 0
        elif other.get_poke_type() == "Normal":
            self.effective_attack = self.attack_damage

        if self.get_status_effect() == "Burn":
            self.effective_attack // 2

        other.defend(self.effective_attack)

        self.health_cuts()

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Confusion"

    def can_evolve(self) -> bool:
        return False

    def get_evolved_version(self) -> PokemonBase:
        raise Exception('This pokemon does not have an evolved version')

class Charizard(PokemonBase):
    def __init__(self):
        self.poke_name = "Charizard"
        self.poke_type = "Fire"
        self.level = 3
        self.hp = 12 + 1 * self.level
        self.attack_damage = 10 + 2 * self.level
        self.speed = 9 + 1 * self.level
        self.defence = 4
        self.status_effect = ""
        self.effective_attack = 0

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        holder = self.base_hp - self.hp
        self.hp = 12 + 1 * self.level
        self.base_hp = self.hp
        self.hp -= holder

    def set_attack(self) -> None:
        self.attack_damage = 10 + 2 * self.level

    def set_speed(self) -> None:
        self.speed = 9 + 1 * self.level

    def set_defence(self) -> None:
        return None

    def defend(self, damage: int) -> None:
        if damage > self.defence:
            self.hp -= damage * 2
        else:
            self.hp -= damage

    def attack(self, other: PokemonBase):
        if self.get_status_effect() == "Sleep":
            return None
        elif RandomGen.random_chance(0.5) == True and self.get_status_effect() == "Confusion":
            other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Grass":
            self.effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Water":
            self.effective_attack = int(self.attack_damage * 0.5)
        elif other.get_poke_type() == "Ghost":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            self.effective_attack = self.attack_damage * 1

        if self.get_status_effect() == "Burn":
            self.effective_attack // 2

        other.defend(self.effective_attack)

        self.health_cuts()

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Burn"

    def can_evolve(self) -> bool:
        return False

    def get_evolved_version(self) -> PokemonBase:
        raise Exception('This pokemon does not have an evolved version')

class Blastoise(PokemonBase):
    def __init__(self):
        self.poke_name = "Blastoise"
        self.poke_type = "Water"
        self.level = 3
        self.hp = 15 + 2 * self.level
        self.attack_damage = 8 + (self.level // 2)
        self.speed = 10
        self.defence = 8 + 1 * self.level
        self.status_effect = ""
        self.effective_attack = 0

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        holder = self.base_hp - self.hp
        self.hp = 15 + 2 * self.level
        self.base_hp = self.hp
        self.hp -= holder

    def set_attack(self) -> None:
        self.attack_damage = 8 + (self.level // 2)

    def set_speed(self) -> None:
        return None

    def set_defence(self) -> None:
        self.defence = 8 + 1 * self.level

    def defend(self, damage: int) -> None:
        if damage > (self.defence * 2):
            self.hp -= damage
        else:
            self.hp -= damage // 2

    def attack(self, other: PokemonBase):
        if self.get_status_effect() == "Sleep":
            return None
        elif RandomGen.random_chance(0.5) == True and self.get_status_effect() == "Confusion":
            other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            self.effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Grass":
            self.effective_attack = int(self.attack_damage * 0.5)
        elif other.get_poke_type() == "Water":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Ghost":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            self.effective_attack = self.attack_damage * 1

        if self.get_status_effect() == "Burn":
            self.effective_attack // 2

        other.defend(self.effective_attack)

        self.health_cuts()

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Paralysis"

    def can_evolve(self) -> bool:
        return False

    def get_evolved_version(self) -> PokemonBase:
        raise Exception('This pokemon does not have an evolved version')

class Venusaur(PokemonBase):
    def __init__(self):
        self.poke_name = "Venusaur"
        self.poke_type = "Grass"
        self.level = 2
        self.hp = int(20 + (self.level // 2))
        self.attack_damage = int(5)
        self.speed = int(3 + (self.level // 2))
        self.defence = int(10)
        self.status_effect = ""
        self.effective_attack = 0

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        holder = self.base_hp - self.hp
        self.hp = int(20 + (self.level // 2))
        self.base_hp = self.hp
        self.hp -= holder

    def set_attack(self) -> None:
        return None

    def set_speed(self) -> None:
        self.speed = 3 + (self.level // 2)

    def set_defence(self) -> None:
        return None

    def defend(self, damage: int) -> None:
        if damage > (self.defence + 5):
            self.hp -= damage
        else:
            self.hp -= damage // 2

    def attack(self, other: PokemonBase):
        if self.get_status_effect() == "Sleep":
            return None
        elif RandomGen.random_chance(0.5) == True and self.get_status_effect() == "Confusion":
            other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            self.effective_attack = int(self.attack_damage * 0.5)
        elif other.get_poke_type() == "Grass":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Water":
            self.effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Ghost":
            self.effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            self.effective_attack = self.attack_damage * 1

        if self.get_status_effect() == "Burn":
            self.effective_attack // 2

        other.defend(self.effective_attack)

        self.health_cuts()

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Poison"

    def can_evolve(self) -> bool:
        return False

    def get_evolved_version(self) -> PokemonBase:
        raise Exception('This pokemon does not have an evolved version')


class Haunter(PokemonBase):
    def __init__(self):
        self.poke_name = "Haunter"
        self.poke_type = "Ghost"
        self.level = 1
        self.hp = 9 + (self.level // 2)
        self.attack_damage = 8
        self.speed = 6
        self.defence = 6
        self.status_effect = ""
        self.effective_attack = 0

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        holder = self.base_hp - self.hp
        self.hp = 9 + (self.level // 2)
        self.base_hp = self.hp
        self.hp -= holder

    def set_attack(self) -> None:
        return None

    def set_speed(self) -> None:
        return None

    def set_defence(self) -> None:
        return None

    def defend(self, damage: int) -> None:
        self.hp -= damage

    def attack(self, other: PokemonBase):
        if self.get_status_effect() == "Sleep":
            return None
        elif RandomGen.random_chance(0.5) == True and self.get_status_effect() == "Confusion":
            other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Grass":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Water":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Ghost":
            self.effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Normal":
            self.effective_attack = 0

        if self.get_status_effect() == "Burn":
            self.effective_attack // 2

        other.defend(self.effective_attack)

        self.health_cuts()

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Sleep"

    def can_evolve(self) -> bool:
        if self.level == 3:
            return True
        else:
            return False

    def get_evolved_version(self) -> PokemonBase:
        g = Gengar()
        holder = self.base_hp - self.hp
        g.hp -= holder
        return g

class Gengar(PokemonBase):
    def __init__(self):
        self.poke_name = "Gengar"
        self.poke_type = "Ghost"
        self.level = 3
        self.hp = 12 + (self.level // 2)
        self.attack_damage = 18
        self.speed = 12
        self.defence = 3
        self.status_effect = ""
        self.effective_attack = 0

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        holder = self.base_hp - self.hp
        self.hp = 12 + (self.level // 2)
        self.base_hp = self.hp
        self.hp -= holder

    def set_attack(self) -> None:
        return None

    def set_speed(self) -> None:
        return None

    def set_defence(self) -> None:
        return None

    def defend(self, damage: int) -> None:
        self.hp -= damage

    def attack(self, other: PokemonBase):
        if self.get_status_effect() == "Sleep":
            return None
        elif RandomGen.random_chance(0.5) == True and self.get_status_effect() == "Confusion":
            other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Grass":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Water":
            self.effective_attack = int(self.attack_damage * 1.25)
        elif other.get_poke_type() == "Ghost":
            self.effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Normal":
            self.effective_attack = 0

        if self.get_status_effect() == "Burn":
            self.effective_attack // 2

        other.defend(self.effective_attack)

        self.health_cuts()

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Sleep"

    def can_evolve(self) -> bool:
        return False

    def get_evolved_version(self) -> PokemonBase:
        raise Exception('This pokemon does not have an evolved version')


if __name__ == "__main__":
    s = Squirtle()
    print(s.get_hp())
    print(s.get_attack_damage())

    
