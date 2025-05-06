import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()


    def show_bg(self, surface):
        for col in range(Cols):
            for row in range(Rows):
                if (col + row) % 2 == 0:
                    color = (234, 235, 200)  # Light Green
                else:
                    color = (119, 154, 88) # Dark Green
                rect = (row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for col in range(Cols):
            for row in range(Rows):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size = 80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2
                        piece.piece_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.piece_rect)



    