from __future__ import annotations
from linked_list import LinkedList

from node import Node
from linked_list import LinkedList
from poke_team import PokeTeam
from battle import Battle
from random_gen import RandomGen
from poke_team import Criterion

class BattleTower:

    def __init__(self, battle: Battle|None=None) -> None:
        self.battle = battle
        self.teams = LinkedList()
        self.lives = LinkedList()
    
    def set_my_team(self, team: PokeTeam) -> None:
        self.team = Node(team)
    
    def generate_teams(self, n: int) -> None:
        i = 1
        #print(self.tower.__len__())
        # self.teams.append(self.team)
        #print(self.tower)
        while i < n:
            battle_mode = RandomGen.randint(0,1)
            life = RandomGen.randint(2,10)
            other_team = PokeTeam.random_team(str(i), battle_mode)
            self.teams.append(other_team)
            self.lives.append(life)
            i += 1
        
    def __iter__(self):
        return BattleTowerIterator(self.team)

class BattleTowerIterator:

    def __init__(self, node: Node[T]):
        self.current = node
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        BattleTower(self.current, self.current.next())

        item = self.current.item
        self.current = self.current

        if self.current is None:
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
    print(it)
    for (expected_res, expected_lives), (res, me, tower, lives) in zip(results, it):
        print("expected res: ",expected_res, ", res: ",res)
        print("(expected_res, expected_lives): ", (expected_res, expected_lives))
        print("expected_lives: ",expected_lives)
        print("lives",lives)
