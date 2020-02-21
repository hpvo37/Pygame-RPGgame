from Game.gameElements.controller import controller
from Game.gameElements.model import model
from Game.gameElements.view import view
from Game.gameElements.sprite import sprite
from pygame import mixer
import pygame
import sys

mixer.music.load("lastencounter.wav")
mixer.music.set_volume(0.25)
mixer.music.play(-1)

class Game:
	def __init__(self):
		self.model = model()
		self.view = view(self.model)
		self.controller = controller(self.model)

	def run(self):
		while self.model.run:
			self.controller.update()
			self.model.update()
			self.view.update()
			if (self.model.gameOver == True):
				self.gameover()

	def draw_text(self, text, size, color, x, y, align="nw"):
                font = pygame.font.SysFont("comicsansms", size)
                text_surface = font.render(text, True, color)
                text_rect = text_surface.get_rect()
                if align == "nw":
                    text_rect.topleft = (x, y)
                if align == "ne":
                    text_rect.topright = (x, y)
                if align == "sw":
                    text_rect.bottomleft = (x, y)
                if align == "se":
                    text_rect.bottomright = (x, y)
                if align == "n":
                    text_rect.midtop = (x, y)
                if align == "s":
                    text_rect.midbottom = (x, y)
                if align == "e":
                    text_rect.midright = (x, y)
                if align == "w":
                    text_rect.midleft = (x, y)
                if align == "center":
                    text_rect.center = (x, y)
                sprite.screen.blit(text_surface, text_rect)

	def gameover(self):
		pygame.mixer.music.stop()
		sprite.screen.fill(pygame.Color(0, 0, 0))
		self.draw_text("GAME OVER", 100, (255, 0, 0), 1050 / 2, 700 / 2, align="center")
		self.draw_text("Press Any Key to Exit", 75, (255, 255, 255), 1050 / 2, 700 * 3 / 4, align="center")			
		pygame.display.flip()
		self.waitforkey()
	
	def waitforkey(self):
		pygame.event.wait()
		waiting = True
		while waiting:
                        self.clock = pygame.time.Clock()
                        self.clock.tick(60)
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        self.model.run = False
                                        waiting = False
                                if event.type == pygame.KEYUP:
                                        waiting = False
                                        self.model.run = False


