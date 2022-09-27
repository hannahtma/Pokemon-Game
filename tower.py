from __future__ import annotations
from abc import abstractmethod

from node import Node
from linked_list import LinkedList
from poke_team import PokeTeam
from battle import Battle
from random_gen import RandomGen

class BattleTower:

    def __init__(self, battle: Battle|None=None) -> None:
        self.battle = battle
        self.head = LinkedList()
    
    def set_my_team(self, team: PokeTeam) -> None:
        self.team = team
    
    def generate_teams(self, n: int) -> None:
        for index in range(n):
            self.head = Node.append(index,PokeTeam.random_team("Team "+ str(index), [RandomGen.randint(0,1),RandomGen.randint(2,10)]))

    def __iter__(self):
        return BattleTowerIterator(self.head)

    @abstractmethod
    def next(self, my_iterable):
        pass

class BattleTowerIterator:

    def __init__(self,node):
        self.current = node
    
    def __iter__(self):
        return self

    def next(self, my_iterable):
        return tuple(Battle.battle(self.team,self.__iter__),self.__iter__,self.__iter__.item[1])

    def avoid_duplicates(self):
        pass

    def sort_by_lives(self):
        # 1054
        raise NotImplementedError()
