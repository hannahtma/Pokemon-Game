"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

class Charmander(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        hp = 8 + 1 * self.level
        attack = 6 + 1 * self.level
        speed = 7 + 1 * self.level
        defence = 4
        # defence calculation

        super().__init__(hp, poke_type)

class Squirtle(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        hp = 9 + 2 * self.level
        attack = 4 + (self.level // 2)
        speed = 7
        defence = 6 + self.level
        # defence calculation

        super().__init__(hp, poke_type)

class Bulbasaur(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        hp = 12 + 1 * self.level
        attack = 5
        speed = 7 + (self.level // 2)
        defence = 5
        # defence calculation

        super().__init__(hp, poke_type)

class Gastly(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        hp = 6 + (self.level // 2)
        attack = 4
        speed = 2
        defence = 8
        # defence calculation

        super().__init__(hp, poke_type)

class Eevee(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        hp = 10
        attack = 6 + self.level
        speed = 7 + self.level
        defence = 4 + self.level
        # defence calculation

        super().__init__(hp, poke_type)

class Charizard(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 3
        hp = 12 + 1 * self.level
        attack = 10 + 2 * self.level
        speed = 9 + 1 * self.level
        defence = 4
        # defence calculation

        super().__init__(hp, poke_type)

class Blastoise(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 3
        hp = 15 + 2 * self.level
        attack = 8 + (self.level // 2)
        speed = 10
        defence = 8 + 1 * self.level
        # defence calculation

        super().__init__(hp, poke_type)

class Venusaur(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 2
        hp = 20 + (self.level // 2)
        attack = 5
        speed = 3 + (self.level // 2)
        defence = 10
        # defence calculation

        super().__init__(hp, poke_type)

class Haunter(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 1
        hp = 9 + (self.level // 2)
        attack = 8
        speed = 6
        defence = 6
        # defence calculation

        super().__init__(hp, poke_type)

class Gengar(PokemonBase):
    def __init__(self, hp, poke_type):
        self.level = 3
        hp = 12 + (self.level // 2)
        attack = 18
        speed = 12
        defence = 3
        # defence calculation

        super().__init__(hp, poke_type)
