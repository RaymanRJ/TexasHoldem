from Deck import Deck
from enum import Enum
from HandRankings import Rank

Stage = Enum('Stage', 'PRE_FLOP FLOP RIVER TURN')

for rank in Rank:
    print(rank)