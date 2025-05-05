import pygame
from const import *


class Game:
    def __init__(self):
        pass

    def show_bg(self, surface):
        for col in range(Cols):
            for row in range(Rows):
                if (col + row) % 2 == 0:
                    color = (234, 235, 200)  # Light Green
                else:
                    color = (119, 154, 88) # Dark Green
                rect = (row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE)
                pygame.draw.rect(surface, color, rect)



    