import pygame
from const import *


class Dragger:
    def __init__(self):
        self.dragging = False
        self.piece = None
        self.mouse_x = 0
        self.mouse_y = 0
        self.intial_row = 0
        self.intial_col = 0


    #Other methods

    #Lấy vị trí chuột
    def update_mouse(self, pos):
        self.mouse_x, self.mouse_y = pos

    #Lưu vị trí ban đầu của quân cờ khi được nhấn chuột
    def save_initial(self, pos):
        self.intial_row = pos[1] // SQ_SIZE
        self.intial_col = pos[0] // SQ_SIZE

    #Lưu quân cờ được trỏ đên
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
    
    #Xoá quân cờ được trỏ đến sau khi xong
    def undrag_piece(self):
        self.piece = None
        self.dragging = False

    #Dragging method
    def update_blit(self, surface):
        self.piece.set_texture(size = 128)
        img = pygame.image.load(self.piece.texture)
        img_center = self.mouse_x, self.mouse_y
        self.piece.piece_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.piece_rect)

