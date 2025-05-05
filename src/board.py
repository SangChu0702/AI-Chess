from const import *
from square import Square
class Board:
    def __init__(self, ):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(Cols)]
        self._create()

    def _create(self):
        for row in range(Rows):
            for col in range(Cols):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        pass