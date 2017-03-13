# Initial Start of the chess board
# Starting from top left corner(a8)
# Finishing at bottom right corner (h1)
# r/R ==> Black/White ROOK
# n/N ==> Black/White KNIGHT
# b/B ==> Black/White BISHOP
# q/Q ==> Black/White QUEEN
# k/K ==> Black/White KING
# p/P ==> Black/White PAWN

initial_start = ['rnbqkbnr',
                 'pppppppp',
                 '8', '8', '8', '8',
                 'PPPPPPPP',
                 'RNBQKBNR']

from enums import Piece
from board import Board

print (Board(initial_start))
