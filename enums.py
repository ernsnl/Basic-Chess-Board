from enum import Enum

# Contains the ASCII difference between black and white pieces
class Color(Enum):
    WHITE = 0
    BLACK = 6

# Contains the ASCII values for the chess pieces
class Piece(Enum):
    KING = 9812
    QUEEN = 9813
    ROOK = 9814
    BISHOP = 9815
    NIGHT = 9816
    PAWN = 9817
