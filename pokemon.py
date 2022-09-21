"""
"""
from pokemon_base import PokemonBase
from random_gen import RandomGen

class Charmander(PokemonBase):
    def __init__(self):
        self.poke_name = "Charmander"
        self.poke_type = "Fire"
        self.level = 1
        self.hp = 8 + 1 * self.level
        self.attack_damage = 6 + 1 * self.level
        self.speed = 7 + 1 * self.level
        self.defence = 4
        self.status_effect = ""

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
        elif self.get_status_effect() == "Confusion":
            if RandomGen.random_chance(0.5) == True:
                other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Grass":
            effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Water":
            effective_attack = self.attack_damage * 0.5
        elif other.get_poke_type() == "Ghost":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            effective_attack = self.attack_damage * 1

        other.defend(effective_attack)

        if self.get_status_effect() == "Burn":
            self.hp -= 1
        elif self.get_status_effect() == "Poison":
            self.hp -= 3

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
        self.hp = 9 + 2 * self.level
        self.attack_damage = 4 + (self.level // 2)
        self.speed = 7
        self.defence = 6 + self.level
        self.status_effect = ""

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
        elif self.get_status_effect() == "Confusion":
            if RandomGen.random_chance(0.5) == True:
                other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Grass":
            effective_attack = self.attack_damage * 0.5
        elif other.get_poke_type() == "Water":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Ghost":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            effective_attack = self.attack_damage * 1

        other.defend(effective_attack)

        if self.get_status_effect() == "Burn":
            self.hp -= 1
        elif self.get_status_effect() == "Poison":
            self.hp -= 3

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
        self.hp = 12 + 1 * self.level
        self.attack_damage = 5
        self.speed = 7 + (self.level // 2)
        self.defence = 5
        self.status_effect = ""

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        holder = self.base_hp - self.hp
        self.hp = 12 + 1 * self.level
        self.base_hp = self.hp
        self.hp -= holder

    def set_attack(self) -> None:
        return None

    def set_speed(self) -> None:
        self.speed = 7 + (self.level // 2)

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
        elif self.get_status_effect() == "Confusion":
            if RandomGen.random_chance(0.5) == True:
                other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            effective_attack = self.attack_damage * 0.5
        elif other.get_poke_type() == "Grass":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Water":
            effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Ghost":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            effective_attack = self.attack_damage * 1

        other.defend(effective_attack)

        if self.get_status_effect() == "Burn":
            self.hp -= 1
        elif self.get_status_effect() == "Poison":
            self.hp -= 3

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
        elif self.get_status_effect() == "Confusion":
            if RandomGen.random_chance(0.5) == True:
                other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Grass":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Water":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Ghost":
            effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Normal":
            effective_attack = self.attack_damage * 0

        other.defend(effective_attack)

        if self.get_status_effect() == "Burn":
            self.hp -= 1
        elif self.get_status_effect() == "Poison":
            self.hp -= 3

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
        self.hp = 10
        self.attack_damage = 6 + self.level
        self.speed = 7 + self.level
        self.defence = 4 + self.level
        self.status_effect = ""

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        return None

    def set_attack(self) -> None:
        self.attack_damage = 6 + self.level

    def set_speed(self) -> None:
        self.speed = 7 + self.level

    def set_defence(self) -> None:
        self.defence = 4 + self.level

    def defend(self, damage: int) -> None:
        if damage >= self.defence:
            self.hp -= damage

    def attack(self, other: PokemonBase):
        if self.get_status_effect() == "Sleep":
            return None
        elif self.get_status_effect() == "Confusion":
            if RandomGen.random_chance(0.5) == True:
                other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Grass":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Water":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Ghost":
            effective_attack = self.attack_damage * 0
        elif other.get_poke_type() == "Normal":
            effective_attack = self.attack_damage * 1

        other.defend(effective_attack)

        if self.get_status_effect() == "Burn":
            self.hp -= 1
        elif self.get_status_effect() == "Poison":
            self.hp -= 3

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Confusion"

    def can_evolve(self) -> bool:
        raise Exception('This pokemon cannot be evolved')

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
        elif self.get_status_effect() == "Confusion":
            if RandomGen.random_chance(0.5) == True:
                other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Grass":
            effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Water":
            effective_attack = self.attack_damage * 0.5
        elif other.get_poke_type() == "Ghost":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            effective_attack = self.attack_damage * 1

        other.defend(effective_attack)

        if self.get_status_effect() == "Burn":
            self.hp -= 1
        elif self.get_status_effect() == "Poison":
            self.hp -= 3

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Burn"

    def can_evolve(self) -> bool:
        raise Exception('This pokemon cannot be evolved')

    def get_evolved_version(self) -> PokemonBase:
        raise Exception('This pokemon does not have an evolved version')

class Blastoise(PokemonBase):
    def __init__(self):
        self.poke_name = "Blastoise"
        self.poke_type = "Squirtle"
        self.level = 3
        self.hp = 15 + 2 * self.level
        self.attack_damage = 8 + (self.level // 2)
        self.speed = 10
        self.defence = 8 + 1 * self.level
        self.status_effect = ""

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
        elif self.get_status_effect() == "Confusion":
            if RandomGen.random_chance(0.5) == True:
                other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Grass":
            effective_attack = self.attack_damage * 0.5
        elif other.get_poke_type() == "Water":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Ghost":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            effective_attack = self.attack_damage * 1

        other.defend(effective_attack)

        if self.get_status_effect() == "Burn":
            self.hp -= 1
        elif self.get_status_effect() == "Poison":
            self.hp -= 3

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Paralysis"

    def can_evolve(self) -> bool:
        raise Exception('This pokemon cannot be evolved')

    def get_evolved_version(self) -> PokemonBase:
        raise Exception('This pokemon does not have an evolved version')

class Venusaur(PokemonBase):
    def __init__(self):
        self.poke_name = "Venusaur"
        self.poke_type = "Grass"
        self.level = 2
        self.hp = 20 + (self.level // 2)
        self.attack_damage = 5
        self.speed = 3 + (self.level // 2)
        self.defence = 10
        self.status_effect = ""

        super().__init__(self.hp, self.poke_type)

    def set_hp(self) -> None:
        holder = self.base_hp - self.hp
        self.hp = 20 + (self.level // 2)
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
        elif self.get_status_effect() == "Confusion":
            if RandomGen.random_chance(0.5) == True:
                other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            effective_attack = self.attack_damage * 0.5
        elif other.get_poke_type() == "Grass":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Water":
            effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Ghost":
            effective_attack = self.attack_damage * 1
        elif other.get_poke_type() == "Normal":
            effective_attack = self.attack_damage * 1

        other.defend(effective_attack)

        if self.get_status_effect() == "Burn":
            self.hp -= 1
        elif self.get_status_effect() == "Poison":
            self.hp -= 3

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Poison"

    def can_evolve(self) -> bool:
        raise Exception('This pokemon cannot be evolved')

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
        elif self.get_status_effect() == "Confusion":
            if RandomGen.random_chance(0.5) == True:
                other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Grass":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Water":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Ghost":
            effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Normal":
            effective_attack = self.attack_damage * 0

        other.defend(effective_attack)

        if self.get_status_effect() == "Burn":
            self.hp -= 1
        elif self.get_status_effect() == "Poison":
            self.hp -= 3

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
        elif self.get_status_effect() == "Confusion":
            if RandomGen.random_chance(0.5) == True:
                other = self
        elif self.get_status_effect() == "Paralysis":
            self.speed = self.speed // 2

        if other.get_poke_type() == "Fire":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Grass":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Water":
            effective_attack = self.attack_damage * 1.25
        elif other.get_poke_type() == "Ghost":
            effective_attack = self.attack_damage * 2
        elif other.get_poke_type() == "Normal":
            effective_attack = self.attack_damage * 0

        other.defend(effective_attack)

        if self.get_status_effect() == "Burn":
            self.hp -= 1
        elif self.get_status_effect() == "Poison":
            self.hp -= 3

        if RandomGen.random_chance(0.2) == True:
            other.status_effect = "Sleep"

    def can_evolve(self) -> bool:
        raise Exception('This pokemon cannot be evolved')

    def get_evolved_version(self) -> PokemonBase:
        raise Exception('This pokemon does not have an evolved version')

if __name__ == "__main__":
    RandomGen.set_seed(0)
    e1 = Eevee()
    e2 = Eevee()
    e1.attack(e2)
    # e2 now is confused.
    e2.attack(e1)
    # e2 takes damage in confusion.
    print(e1.get_hp()) #10

    
