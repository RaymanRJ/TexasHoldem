from src.Classes.Game import Game

# TODO: Review turn order - something's off.

game = Game(num_players=4)
game.deal(2)
game.betting_round()    # Pre-flop betting

game.advance_stage()    # Entering FLOP
game.community_deal()
game.betting_round()    # Flop betting

game.advance_stage()    # Entering RIVER
game.community_deal()
game.betting_round()    # River betting

game.advance_stage()    # Entering Turn
game.community_deal()
game.betting_round()    # Final betting




listy = [0, 4, 5, 6, 2, 1, 3]
print(listy[-1])
print(listy[-5])