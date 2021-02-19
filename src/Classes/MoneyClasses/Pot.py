from typing import Dict, List

from src.Classes.ActorClasses.Player import Player
from src.Classes.MoneyClasses.Chip import Chip


class Pot:
    """
    The Pot object represents the entire Pot for the current round. It is made of smaller __Pot objects
    which are instantiated either at the beginning of a round, or when a player goes "all in".

    This is because when a player goes "all in" there needs to be some way to differentiate the "other" pots
    that the other players continue with, while locking in the current pot's values.
    """

    class __Pot:

        class __PlayerPot:
            __chips: List[Chip]
            __owner: Player

            def __init__(self, owner: Player, *chips: Chip):
                self.__owner = owner
                self.__chips = [*chips]

            @property
            def value(self) -> int:
                return sum(chip.value for chip in self.__chips)

            @value.setter
            def value(self, *chips: Chip) -> None:
                self.__chips.extend([*chips])

            @property
            def owner(self) -> Player:
                return self.__owner

        __player_pot: Dict[Player, __PlayerPot]
        __players_all_in: List[Player]

        def __init__(self, *players: Player):
            self.__players_all_in = list()
            self.__player_pot = dict()
            for player in players:
                self.__player_pot[player] = self.__PlayerPot(player)

        def add_player_bet(self, player: Player, *chips: Chip) -> None:
            self.__player_pot[player].value = chips  # TODO: This prob doesn't work.

        def is_player_all_in(self, player: Player) -> bool:
            return player in self.__players_all_in

        def player_goes_all_in(self, player: Player) -> None:
            self.__players_all_in.append(player)

        @property
        def value(self) -> int:
            return sum(pot.value for pot in self.__player_pot.values())

    __pots: List[__Pot]
    __players: List[Player]

    def __init__(self, *players: Player):
        self.__pots = [self.__Pot(*players)]

    def player_bet(self, player: Player, all_in: bool = False, *chips: Chip):
        current_pot = self.__pots[-1]

        if all_in:
            # TODO: This logic.
            pass
        else:
            current_pot.add_player_bet(player, *chips)

    @property
    def pot_value(self) -> int:
        return sum(pot.value for pot in self.__pots)
