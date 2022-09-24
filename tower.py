from __future__ import annotations

from poke_team import PokeTeam
from battle import Battle
from random_gen import RandomGen
from queue_adt import CircularQueue
from poke_team import Criterion

class BattleTower:

    def __init__(self, battle: Battle|None=None) -> None:
        self.battle = battle
    
    def set_my_team(self, team: PokeTeam) -> None:
        self.team = team
    
    def generate_teams(self, n: int) -> None:
        self.tower_queue = CircularQueue(n)
        i = 1
        while i < n:
            battle_mode = RandomGen.randint(0,1)
            other_team = PokeTeam.random_team(str(i), battle_mode)
            self.tower_queue.append(other_team)
            i += 1

    def __iter__(self):
        return BattleTowerIterator(self)
    
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
