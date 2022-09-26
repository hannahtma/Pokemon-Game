from __future__ import annotations
from symbol import xor_expr

from poke_team import PokeTeam
from battle import Battle
from random_gen import RandomGen
from poke_team import Criterion
from node import Node, T
from linked_list import LinkedList

class BattleTower:

    def __init__(self, battle: Battle|None=None) -> None:
        self.battle = battle
        self.index = 0
    
    def set_my_team(self, team: PokeTeam) -> None:
        self.team = team
    
    def generate_teams(self, n: int) -> None:
        i = 1
        self.teams = LinkedList(n+1)
        #print(self.tower.__len__())
        # self.teams.append(self.team)
        #print(self.tower)
        while i < n:
            battle_mode = RandomGen.randint(0,1)
            lives = RandomGen.randint(2,10)
            print(lives)
            other_team = PokeTeam.random_team(str(i), battle_mode)
            self.teams.append(other_team)
            i += 1
        
        print(str(self.teams))

    def __iter__(self):
        return BattleTowerIterator(self.battle, self.team, self.teams)

class BattleTowerIterator:

    def __init__(self, b, my_team, tower):
        self.b = b
        self.tower = tower
        self.my_team = my_team
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.b.battle(self.my_team, self.tower[self.current_index])

        if self.current_index < self.tower.__len__():
            return self.tower[self.current_index+1]

        else:
            raise StopIteration

    def avoid_duplicates(self):
        pass

    def sort_by_lives(self):
        # 1054
        pass

if __name__ == "__main__":
    RandomGen.set_seed(51234)
    bt = BattleTower(Battle(verbosity=0))
    bt.set_my_team(PokeTeam.random_team("N", 2, team_size=6, criterion=Criterion.HP))
    bt.generate_teams(4)
    # Teams have 7, 10, 10, 3 lives.
    RandomGen.set_seed(1029873918273)
    results = [
        (1, 6),
        (1, 9),
        (2, 10)
    ]
    it = iter(bt)
    print(type(bt))
    print(zip(it))
    for (expected_res, expected_lives), (res, me, tower, lives) in zip(results, it):
        print("expected res: ",expected_res, ", res: ",res)
        print("(expected_res, expected_lives): ", (expected_res, expected_lives))
        print("expected_lives: ",expected_lives)
        print("lives",lives)
