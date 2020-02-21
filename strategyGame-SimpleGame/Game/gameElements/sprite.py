import pygame
import os
import random
pygame.mixer.init()


class sprite:
	screen = None
	clock = None
	sWidth = 0
	sHeight = 0
	
	def __init__(self, x, y, w, h, sprtPath = None,  type = -1, color = None):
		self.rect = pygame.Rect(x, y, w, h)
		#------------------------------------------------
		# RECTANGLE COLOR = GREEN BY DEFAULT
		if(color == None): self.rectColor = pygame.Color(95, 111, 58)
		#-----------------------------------------------
		self.img = None
		self.type = type
		if(sprtPath != None): self.img = self.loadImg(sprtPath)
		self.animationCount = 0
		self.lastAnimation = pygame.time.get_ticks()


	
	@staticmethod
	def init(width, height, caption):
		pygame.init()
		print("Sprite init")
		sprite.screen = pygame.display.set_mode((width,height))
		print("Sprite in sprite " + str(sprite.screen))
		pygame.display.set_caption(caption)
		sprite.sHeight = height
		sprite.sWidth = width
		sprite.clock = pygame.time.Clock()
		print("Sprite initialized")

	def collide(self, collideSprite):
		# Returns True if collition takes place
		return self.rect.colliderect(collideSprite.rect)
	
	def restorePos(self, prevRect):
                print("Restoring Position")
                self.rect = prevRect.copy()
                
	def loadImg(self, imgPath):
		# Turns image path into an absolute path using the current working directory
		# Loads image and rescale using the dimension defined in self.rect
		imgPath = os.getcwd() + imgPath
		img = pygame.image.load(imgPath).convert_alpha()
		img = pygame.transform.scale(img, (self.rect.w, self.rect.h))
		return img

	def loadsnd(self, sndpath):
		# Turns sound path into an absolute path using the current working directory
		sndpath = os.getcwd() + sndpath
		snd = pygame.mixer.Sound(sndpath)
		return snd

	def nextAnimation(self, spriteLimit, animationSpeed):
                if(pygame.time.get_ticks() - self.lastAnimation >= animationSpeed):
                        if(self.animationCount == spriteLimit):
                                self.animationCount = 0
                        else: self.animationCount += 1
                        self.lastAnimation = pygame.time.get_ticks()
                        return True
                return False
	
	def getX(self):
		return self.rect.x

	def mouseInIt(self, x, y):
		return self.rect.collidepoint(x,y)
	
	def getY(self):
		return self.y

	def drawSquare(self, color = None, width = 0):
		if color == None: color = self.rectColor 
		pygame.draw.rect(sprite.screen, color, self.rect, width)

	def drawImg(self):
		if(self.img != None): sprite.screen.blit(self.img, self.rect)
		
	def draw(self):
		self.drawImg()

	def update(self):
                pass
	
	def printData(self):
		print("SpriteData: \nX: " + str(self.rect.x) + "\nY: " + str(self.rect.y) + "\nW:" + str(self.rect.w) + "\nH: " + str(self.rect.h))
