from __future__ import annotations
from linked_list import LinkedList

from poke_team import PokeTeam
from battle import Battle
from random_gen import RandomGen
from poke_team import Criterion

class BattleTower:

    def __init__(self, battle: Battle|None=None) -> None:
        self.battle = battle
        self.tower_teams = LinkedList(PokeTeam)
    
    def set_my_team(self, team: PokeTeam) -> None:
        self.team = team
    
    def generate_teams(self, n: int) -> None:
        for index in range(n):
            self.tower_teams.__setitem__(index, PokeTeam.random_team())

    def __iter__(self):
        return BattleTowerIterator(self.head)
    
    def __next__(self):
        if self._index < (len(self._battle_tower.battle)):
            result = self._battle_tower.battle[self._index]
            self._index += 1

            return result
        
        raise StopIteration

class BattleTowerIterator:

    def __init__(self, battle_tower):
        self._battle_tower = battle_tower
        self._index = 0

    def avoid_duplicates(self):
        print(self.team)
        # for i in range(len())

    def sort_by_lives(self):
        # 1054
        pass

if __name__ == "__main__":
    RandomGen.set_seed(51234)
    bt = BattleTower(Battle(verbosity=0))
    bt.set_my_team(PokeTeam.random_team("N", 2, team_size=6, criterion=Criterion.HP))
    bt.generate_teams(4)
    # Teams have 7, 10, 10, 3 lives.
    RandomGen.set_seed(213098)
    results = [
        (1, 6),
        (1, 9),
        (1, 9),
        (1, 2),
        (1, 5),
        (2, 9)
    ]
    it = iter(bt)
    for (expected_res, expected_lives), (res, me, tower, lives) in zip(results, it):
        self.assertEqual(expected_res, res, (expected_res, expected_lives))
        self.assertEqual(expected_lives, lives)
