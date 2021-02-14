from src.Classes.ActorClasses.Actor import Actor
from src.Classes.CardClasses.Deck import Deck
from typing import List
from src.Classes.ActorClasses.Player import Player
from enum import Enum
from src.Classes.ActorClasses.CommunityCards import CommunityCards


class Stage(Enum):
    PRE_FLOP = 1
    FLOP = 2
    RIVER = 3
    TURN = 4

    def next(self):
        current = self.value
        return Stage(current + 1)

    def get_stage_copy(self):
        return Stage(self.value)


class Game(Actor):
    __players: List[Player] = []
    __community_cards: Actor
    __game_stage: Stage

    def __init__(self, num_players: int, name: str = "Game", ):
        super().__init__(name, Deck.create_new_deck())

        self.__game_stage = Stage.PRE_FLOP

        # Setup Community Cards:
        self.__community_cards = CommunityCards()

        # Setup Players:
        for player in range(num_players):
            self.__players.append(Player(f"Player {str(player)}", self.__community_cards))

    def community_deal(self):
        if self.__game_stage is Stage.FLOP:
            for _ in range(3):
                self.__community_cards.add_card(self.deck.draw_card())
        else:
            self.__community_cards.add_card(self.deck.draw_card())
        self.__community_cards.deck.print()

    def deal(self, num_cards: int = 1) -> None:
        for i in range(num_cards):
            for player in self.__players:
                player.add_card(self.deck.draw_card())

    def betting_round(self) -> None:
        for player in self.__players:
            player.bet()
            #TODO: Implement a pot system

    def advance_stage(self) -> None:
        current = Stage.get_stage_copy(self.__game_stage)
        self.__game_stage = Stage.next(self.__game_stage)
        print(f"Advancing from {current.name} to {self.__game_stage.name}")

    @property
    def players(self) -> List[Player]:
        return self.__players
