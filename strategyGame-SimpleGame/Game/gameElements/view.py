import pygame
from Game.gameElements.sprite import sprite

class view:
    BLACK = pygame.Color(255, 255, 255)

    def __init__(self, model):
        self.model = model
    
    def update(self):
        sprite.screen.fill(view.BLACK)
        for sprt in self.model.sprites:
            sprt.draw()
        pygame.display.update()