from const import *
from move import Move
from square import Square
from piece import *

class Board:
    def __init__(self, ):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(Cols)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):
        for row in range(Rows):
            for col in range(Cols):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6,7) if color == 'white' else (1,0)
        
        #Pawns
        for col in range(Cols):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        #Knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        #Bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        #Rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        #Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        #King
        self.squares[row_other][4] = Square(row_other, 4, King(color))


    def calculate_moves(self, piece, row, col):
        #Calculate all possible moves for a piece
        if isinstance(piece, Pawn):
            return piece.calculate_moves(self.squares, row, col)
        elif isinstance(piece, Knight):
            return knight_moves()
        elif isinstance(piece, Bishop):
            return piece.calculate_moves(self.squares, row, col)
        elif isinstance(piece, Rook):
            return piece.calculate_moves(self.squares, row, col)
        elif isinstance(piece, Queen):
            return piece.calculate_moves(self.squares, row, col)
        elif isinstance(piece, King):
            return piece.calculate_moves(self.squares, row, col)
        
        def knight_moves():
            possible_moves = [
                (row-2, col-1), (row-2, col+1),
                (row-1, col-2), (row-1, col+2), 
                (row+1, col-2), (row+1, col+2),
                (row+2, col-1), (row+2, col+1)
            ]
            for move in possible_moves:
                pos_row, pos_col = move
                if Square.is_valid_square(pos_row, pos_col):
                    if self.squares[pos_row][pos_col].is_empty_or_enemy(piece.color):
                        intial = Square(row,col)
                        final = Square(pos_row,pos_col)
                        move = Move(intial, final)
                        piece.add_move(move)
        def pawn_moves():
            possible_moves = [(row-1, col), (row-2, col)] if piece.color == 'white' else [(row+1, col), (row+2, col)]
            for move in possible_moves:
                pos_row, pos_col = move
                if Square.is_valid_square(pos_row, pos_col):
                    if self.squares[pos_row][pos_col].is_empty():
                        intial = Square(row,col)
                        final = Square(pos_row,pos_col)
                        move = Move(intial, final)
                        piece.add_move(move)