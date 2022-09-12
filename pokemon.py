"""
"""
from pokemon_base import PokemonBase

from pokemon_base import PokemonBase

class Charmander(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        self.hp = 8 + 1 * self.level
        self.attack = 6 + 1 * self.level
        self.speed = 7 + 1 * self.level
        self.defence = 4
        # defence calculation

        super().__init__(hp, poke_type)

class Squirtle(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        self.hp = 9 + 2 * self.level
        self.attack = 4 + (self.level // 2)
        self.speed = 7
        self.defence = 6 + self.level
        # defence calculation

        super().__init__(hp, poke_type)

class Bulbasaur(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        self.hp = 12 + 1 * self.level
        self.attack = 5
        self.speed = 7 + (self.level // 2)
        self.defence = 5
        # defence calculation

        super().__init__(hp, poke_type)

class Gastly(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        self.hp = 6 + (self.level // 2)
        self.attack = 4
        self.speed = 2
        self.defence = 8
        # defence calculation

        super().__init__(hp, poke_type)

class Eevee(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        self.hp = 10
        self.attack = 6 + self.level
        self.speed = 7 + self.level
        self.defence = 4 + self.level
        # defence calculation

        super().__init__(hp, poke_type)

class Charizard(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 3
        self.hp = 12 + 1 * self.level
        self.attack = 10 + 2 * self.level
        self.speed = 9 + 1 * self.level
        self.defence = 4
        # defence calculation

        super().__init__(hp, poke_type)

class Blastoise(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 3
        self.hp = 15 + 2 * self.level
        self.attack = 8 + (self.level // 2)
        self.speed = 10
        self.defence = 8 + 1 * self.level
        # defence calculation

        super().__init__(hp, poke_type)

class Venusaur(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 2
        self.hp = 20 + (self.level // 2)
        self.attack = 5
        self.speed = 3 + (self.level // 2)
        self.defence = 10
        # defence calculation

        super().__init__(hp, poke_type)

class Haunter(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        self.hp = 9 + (self.level // 2)
        self.attack = 8
        self.speed = 6
        self.defence = 6
        # defence calculation

        super().__init__(hp, poke_type)

class Gengar(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 3
        self.hp = 12 + (self.level // 2)
        self.attack = 18
        self.speed = 12
        self.defence = 3
        # defence calculation

        super().__init__(hp, poke_type)

if __name__ == "__main__":
    e = Charmander(50, "fire")
    print(e.get_level())
