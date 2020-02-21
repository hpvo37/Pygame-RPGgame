import pygame
from Game.gameElements.sprite import sprite

LFHEIGTH = 10
RED = pygame.Color(222, 25, 25)
YELLOW = pygame.Color(252, 237, 31)
GREEN =  pygame.Color(67, 198, 93)
BLACK = pygame.Color(0, 0, 0)

class lifeBar():
    def __init__(self, spriteRect, initialHP):
        self.rectLife = pygame.Rect(spriteRect.x,
                                    spriteRect.y - LFHEIGTH - 5,
                                    spriteRect.w, LFHEIGTH)
        self.border = self.rectLife.copy()
        self.color = GREEN
        self.fullWidth = self.rectLife.w
        self.initialHP = initialHP
        

    def update(self, spriteRect, currentHP):
        self.rectLife.x = spriteRect.x
        self.rectLife.y = spriteRect.y - LFHEIGTH - 5
        self.border.x = spriteRect.x
        self.border.y = self.rectLife.y 

        percentage = currentHP/self.initialHP
        self.rectLife.w = self.border.w * percentage
        if(percentage >= 0.50):
            self.color = GREEN
        elif(percentage >= 0.30):
            self.color = YELLOW
        else:
            self.color =  RED
        
    def draw(self):
        pygame.draw.rect(sprite.screen, self.color, self.rectLife)
        pygame.draw.rect(sprite.screen, BLACK, self.border, 2)
