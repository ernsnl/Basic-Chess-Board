# Initial Start of the chess board
# Starting from top left corner(a8)
# Finishing at bottom right corner (h1)
# r/R ==> Black/White ROOK
# n/N ==> Black/White KNIGHT
# b/B ==> Black/White BISHOP
# q/Q ==> Black/White QUEEN
# k/K ==> Black/White KING
# p/P ==> Black/White PAWN
import sys
from helper import parse_lichess
from enums import Piece, Color
from board import Board

def main(argv):
    if len(argv) != 2:
        print ('Number of arguments must be two.')
    else:
        if not argv[1].isdigit() and int(argv[1]) != 0 and int(argv[1]) != 1 :
            print ('Color value must be a integer that is either 0 (Black) or 1(White)')
        else:
            color_value = int(argv[1])
            board = Board(parse_lichess(argv[0]))
            board.possible_moves(Color.WHITE if color_value == 1 else Color.BLACK)

if __name__ == "__main__":
   main(sys.argv[1:])
