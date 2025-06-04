
class Square:
    def __init__(self, row, col, piece = None):
        self.row = row
        self.col = col
        self.piece = piece
    
    def has_piece(self):
        return self.piece is not None
    
    def is_empty(self):
        return self.piece is None
    
    def is_enemy(self, color):
        return self.has_piece() and self.piece.color != color

    def is_empty_or_enemy(self, color):
        return self.is_empty() or self.is_enemy()

    @staticmethod
    def is_valid_square(*args):
        for arg in args:
            if 0 > arg or arg > 7:
                return False
        return True
        
