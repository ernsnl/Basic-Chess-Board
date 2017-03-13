
from enums import Piece, Color

class BoardLocation():
    def __init__(self, color=None, piece=None):
        self.color = color
        self.piece = piece
        self.empty = color and piece

    def __str__(self):
        if self.color and self.piece:
            return str(chr(self.color.value + self.piece.value)) + ' '
        else:
            return '  '


class Board():
    def __init__(self, board):
        self.board_text = board
        self.board_matrix = self.create_board(board)

    def __str__(self):
        print_str = ''
        for row in self.board_matrix:
            for col in row:
                print_str += str(col)
            print_str += '\n'
        return print_str

    def create_board(self, board):
        chess_board = []
        for row in board:
            chess_row = []
            for char in row:
                if char.isdigit():
                    # Empty Spaces in the Chess Board
                    chess_row.extend([BoardLocation() for _ in range(int(char))])
                elif char.islower():
                    # Black Pieces in the Chess Board
                    chess_row.append(assign_piece(char, Color.BLACK))
                else:
                    # White Pieces in the Chess Board
                    chess_row.append(assign_piece(char.lower(), Color.WHITE))
            chess_board.append(chess_row)
        return chess_board

def assign_piece(piece_string, color):
    if piece_string == 'r':
        return BoardLocation(color, Piece.ROOK)
    if piece_string == 'p':
        return BoardLocation(color, Piece.PAWN)
    if piece_string == 'b':
        return BoardLocation(color, Piece.BISHOP)
    if piece_string == 'q':
        return BoardLocation(color, Piece.QUEEN)
    if piece_string == 'n':
        return BoardLocation(color, Piece.KNIGHT)
    if piece_string == 'k':
        return BoardLocation(color, Piece.KING)
