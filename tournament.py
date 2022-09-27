from __future__ import annotations

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by everyone"

from poke_team import PokeTeam
from battle import Battle
from linked_list import LinkedList

class Tournament:
    
    def __init__(self, battle: Battle|None=None) -> None:
        if battle != None:
            self.battle = battle
        else:
            self.battle = Battle()

    def set_battle_mode(self, battle_mode: int) -> None:
        self.battle_mode = battle_mode

    def is_valid_tournament(self, tournament_str: str) -> bool:
        if "(" in tournament_str:
            return False
        else:
            return True

    def is_balanced_tournament(self, tournament_str: str) -> bool:
        # 1054 only
        raise NotImplementedError()

    def start_tournament(self, tournament_str: str) -> None:
        tournaments = tournament_str.split('+')
        participant_names = []
        for element in tournaments:
            if element == " ":
                tournaments.remove(element)
            else:
                participant_names.append(element.split())
        participants = []
        for participant in participant_names:
            counter = 0
            while counter < 2:
                participants.append(PokeTeam.random_team(participant[counter],self.battle_mode))
                counter += 1        

    def advance_tournament(self) -> tuple[PokeTeam, PokeTeam, int] | None:
        pass

    def linked_list_of_games(self) -> LinkedList[tuple[PokeTeam, PokeTeam]]:
        l = LinkedList()
        while True:
            res = self.advance_tournament()
            if res is None:
                break
            l.insert(0, (res[0], res[1]))
        return l
    
    def linked_list_with_metas(self) -> LinkedList[tuple[PokeTeam, PokeTeam, list[str]]]:
        raise NotImplementedError()
    
    def flip_tournament(self, tournament_list: LinkedList[tuple[PokeTeam, PokeTeam]], team1: PokeTeam, team2: PokeTeam) -> None:
        # 1054
        raise NotImplementedError()

if __name__ == "__main__":
    t = Tournament(Battle(verbosity=0))
    t.set_battle_mode(0)
    t.start_tournament("Roark Gardenia + Maylene Crasher_Wake + Fantina Byron + + + Candice Volkner + +")
