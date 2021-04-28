# from exceptions import *
from module import *
from player import Player as _Player
from game import XOGame as _XOGame

pl1 = _Player("Reza", "x")
pl2 = _Player("Reza", "o")

game = _XOGame(pl1, pl2)

game.mark(5, 'x')
game.mark(6, 'o')
game.mark(2, 'x')

# duplicate round error
# game.mark(8, 'x')

# invalid cell error
# game.mark(12, 'o')

game.mark(1, 'o')

# unfinished error
# print(game.winner.name)

game.mark(8, 'x')

# finished error
# game.mark(3, 'o')

print(game)

winner = game.winner
print(winner.name, winner.sign)