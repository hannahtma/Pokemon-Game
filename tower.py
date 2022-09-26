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
        self.head = self.team
    
    def generate_teams(self, n: int) -> None:
        i = 0
        self.tower = LinkedList(n+1)
        #print(self.tower.__len__())
        self.tower.append(self.team)
        #print(self.tower)
        while i < n:
            battle_mode = RandomGen.randint(0,1)
            lives = RandomGen.randint(2,10)
            print(lives)
            other_team = PokeTeam.random_team(str(i), battle_mode)
            self.tower.append(other_team)
            i += 1

        # for x in self.tower:
        #     print(x)

    def __iter__(self):
        return BattleTowerIterator(self)

class BattleTowerIterator:

    def __init__(self, tower):
        self.tower = tower

    def __iter__(self):
        return self

    def __next__(self):
        item = self.cur.item
        self.cur = self.cur.link

        self.battle(self.head, self.cur)

        if self.cur is None:
            raise StopIteration

        return item

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
    for (expected_res, expected_lives), (res, me, tower, lives) in zip(results, it):
        self.assertEqual(expected_res, res, (expected_res, expected_lives))
        self.assertEqual(expected_lives, lives)
