from board_location import BoardLocation
from enums import Piece


def chess_location_row(row):
    """Return the row numbering in a chess board.
    Assuming a8 is located in top left corner

    >> chess_location_row(0)
    8
    >> chess_location_row(7)
    1
    """
    return str(8 - row)


def chess_location_col(col):
    """Return the col value in a chess board.
    Assuming a8 is located in top left corner

    >> chess_location_col(0)
    a
    >> chess_location_col(7)
    g
    """
    return chr(col + 97)

def append_list(move, move_list):
    """Returns a tuple contaning a list and condition for break.
    depending of the move type, it adds to the list and calculates the value of break"""
    if move is None:
        return (move_list, False)
    if len(move) == 3:
        move_list.append(move)
        return (move_list, False)
    else:
        move_list.append(move)
        return (move_list, True)

def print_possible_moves(piece_info, possible_moves):
    """Prints all the possible moves of a piece
    takes piece_info ==> It is an instance of BoardLocation
    takes possible_moves ==> List of moves that can be played by piece

    possible_moves are list of tuples that contains 2 or 3 element.
    2 element move means piece can move freely.
    3 element move means piece can take another piece which has different color than the main piece.
    """
    if len(possible_moves) > 0:
        print (piece_info.piece.name + ' at ' +
               chess_location_col(piece_info.col) + chess_location_row(piece_info.row))
        for move in possible_moves:
            _buffer = 'x' if len(move) == 3 else ''
            print(piece_info.piece.name[0] + _buffer + chess_location_col(move[1]) +
                  chess_location_row(move[0]), end=' ')
        print('\n----')


def assign_piece(row, col, piece_string, color):
    """Take row, col, string value and color parameter for piece
       Returns a BoardLocation instance contaning that value of information.
    """
    if piece_string == 'r':
        return BoardLocation(row, col, color, Piece.ROOK)
    if piece_string == 'p':
        return BoardLocation(row, col, color, Piece.PAWN)
    if piece_string == 'b':
        return BoardLocation(row, col, color, Piece.BISHOP)
    if piece_string == 'q':
        return BoardLocation(row, col, color, Piece.QUEEN)
    if piece_string == 'n':
        return BoardLocation(row, col, color, Piece.NIGHT)
    if piece_string == 'k':
        return BoardLocation(row, col, color, Piece.KING)

def parse_lichess(value):
    """Return a array that can be utilized for board creation"""
    split_string = value.split(' ')
    chess_array = []
    chess_row = ""
    for board in split_string[0]:
        if board == '/':
            chess_array.append(chess_row)
            chess_row = ""
        else:
            chess_row += board

    chess_array.append(chess_row)
    return chess_array
