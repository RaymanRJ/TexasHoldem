from Game import Game




game = Game(4)
game.deal(2)
game.betting_round()

game.advance_stage()    # Entering FLOP
game.community_deal()
game.betting_round()

game.deal()
game.betting_round()
game.betting_round()

game.advance_stage()    # ENTERING RIVER
game.deal()
game.community_deal()
game.betting_round()

game.advance_stage()    # ENTERING TURN
game.deal()
game.community_deal()
game.betting_round()



