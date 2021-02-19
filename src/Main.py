from src.Classes.Game import Game
from multiprocessing import Pool
import time

# TODO: Review turn order - something's off.

num_games = 10000

# Multiprocessing:

start_time = time.time()
games = [Game(num_players=4) for _ in range(num_games)]


def thread_function(game: Game):
    for _ in range(13):
        game.deal()
        game.betting_round()


with Pool(5) as p:
    p.map(thread_function, games)

end_time = time.time()
print(f"Total Multiprocessing time: {end_time - start_time}s.")

# Sequential:

start_time = time.time()
games = [Game(num_players=4) for _ in range(num_games)]

for game in games:
    thread_function(game)

end_time = time.time()
print(f"Total Sequential time: {end_time - start_time}s.")

# game = Game(num_players=4)
# game.deal(2)
# game.betting_round()    # Pre-flop betting
#
# game.advance_stage()    # Entering FLOP
# game.community_deal()
# game.betting_round()    # Flop betting
#
# game.advance_stage()    # Entering RIVER
# game.community_deal()
# game.betting_round()    # River betting
#
# game.advance_stage()    # Entering TURN
# game.community_deal()
# game.betting_round()    # Final betting
