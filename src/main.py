import sys
import pygame
from const import *
from game import Game
class Main:
    def __init__(self):
        pygame.init()
        self.Screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.Game = Game()
        pygame.display.set_caption("Chess")


    

    def mainloop(self):
        screen = self.Screen
        game = self.Game
        
        while True:
            game.show_bg(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()
main.mainloop()