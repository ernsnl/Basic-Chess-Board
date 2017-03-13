"""
BoardLocation class
self.row ==> row of the location
self.col ==> column of the location
self.color ==> if a piece is placed on the location, color value of that piece.
self.piece ==> if a piece is placed on the location, type value of that piece.
self.empty ==> whether the location contains a piece or not.
    Calculated by checking the existence of the color and piece values.
"""

class BoardLocation():
    def __init__(self, row, col, color=None, piece=None):
        self.row = row
        self.col = col
        self.color = color
        self.piece = piece
        self.empty = color is None and piece is None

    def __str__(self):
        if self.color and self.piece:
            return str(chr(self.color.value + self.piece.value)) + ' '
        else:
            return '  '
