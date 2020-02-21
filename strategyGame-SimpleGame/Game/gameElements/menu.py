
from Game.gameElements.button import button
from Game.gameElements.sprite import sprite
import pygame

class menu(sprite):
    LIGHTGREY = pygame.Color(190, 193, 198)
    BLACK = pygame.Color(0,0,0)
    WHITE = pygame.Color(255,255,255)
    DARKGREY = pygame.Color(77, 77, 77)
    
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, r"\resources\sprites\menu\background.png")
        self.action = None
        self.gameTitle = pygame.font.SysFont('Berlin Sans FB', 80).render("Monster Hunter", True, menu.WHITE)
        self.titleLocation = self.gameTitle.get_rect()
        self.titleLocation.x = 275
        self.titleLocation.y = 250
        self.go = button(465, 350, 150, "S", "Start Game", self.goFunct, menu.LIGHTGREY)
        self.quit = button(465, 450, 150, "S", "Quit", self.quitFunct, menu.LIGHTGREY)

    def draw(self):
        self.drawImg()
        sprite.screen.blit(self.gameTitle, self.titleLocation)
        
    def goFunct(self):
        self.action = "G"

    def quitFunct(self):
        self.action = "Q"

    def getButtons(self):
        return (self.go, self.quit)
