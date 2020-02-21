import json
import pygame
import os
from Game.gameElements.sprite import sprite
from Game.gameElements.map import map
from Game.gameElements.button import button
from Game.gameElements.menu import menu

from Game.gameElements.player import player
from Game.gameElements.enemy import worm
from Game.gameElements.enemy import dragon
from Game.gameElements.particles import particles


WORM = 0
DRAGON = 1
class model:
    TEXTCOLOR = pygame.Color(255, 255, 255)
    UTEXTCOLOR = pygame.Color(168, 168, 168)
    
    BGCOLOR = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    UBGCOLOR = pygame.Color(70, 66, 50)
    BUTTONMARGIN = 20

    BCOLORUNACTIVE = pygame.Color(0,0,0, 255)

    def __init__(self):
        self.sprites = []
        self.run = True
        self.menuSprites = []
        self.gameSprites = []

        self.enemies = []
        self.tiles = None
        self.stage = "MENU"

        self.setUpGame()
        self.setUpMenu()
        
        self.selectedTile = None
        self.tileControlledUnit = None
        self.tileDefendingUnit = None
        
        self.gameOver =  False
        
    def loadGame(self):
        with open("resources/map.json") as f:
            data = json.load(f)
        self.map = map(data["map"])
        self.tiles = self.map.getTiles()
        self.addSprite(self.map)

        for enemy in data["enemies"]:
            tmpEnemy = None
            if(enemy["type"] == WORM):
                enemyCenter =  self.map.tiles[enemy["x"]][enemy["y"]].getCenter(64, 64)
                tmpEnemy = worm(enemyCenter[0], enemyCenter[1], 64, 64)
            elif(enemy["type"] == DRAGON):
                enemyCenter = self.map.tiles[enemy["x"]][enemy["y"]].getCenter(69, 69)
                tmpEnemy = dragon(enemyCenter[0], enemyCenter[1], 70, 70, self.map)
            self.gameSprites.append(tmpEnemy)
            self.enemies.append(tmpEnemy)

        playerData = data["player"]
        playerCenter = self.map.tiles[playerData["x"]][playerData["y"]].getCenter(50, 37)
        self.player = player(playerCenter[0], playerCenter[1], 10, 100, 100, 1, 0)
        self.gameSprites.append(self.player)
        
        for particle in data["particles"]:
            particleCenter = self.map.tiles[particle["x"]][particle["y"]].getCenter(70, 70)
            tmpParticle = particles(particleCenter[0], particleCenter[1], 70, 70)
            self.gameSprites.append(tmpParticle)
        self.gameSprites += self.map.floatingTiles
            
    def setUpGame(self):
        ## Here Loading can be perform
        self.sprites = self.gameSprites
        self.loadGame()
        self.items = self.map.items

    def setUpMenu(self):
        self.menu = menu(0, 0, 1050, 700)
        self.menuSprites.append(self.menu)
        self.menuSprites += self.menu.getButtons()
        self.sprites =  self.menuSprites
        
    def addSprite(self, sprite):
        self.sprites.append(sprite)

    def removeSprite(self, sprite):
        self.sprites.remove(sprite)

    def loadsnd(self, sndpath):
        # Turns sound path into an absolute path using the current working directory
        sndpath = os.getcwd() + sndpath
        snd = pygame.mixer.Sound(sndpath)
        return snd

    def checkCollision(self):
        #Attacking Enemy
        for tile in self.tiles:
            if(tile.type <= map.COLLIDELIMIT):
                if(self.player.collide(tile)):
                    self.player.restorePos(self.player.prevRect)
                    playerCenter = self.player.rect.center
                    tmpTile = self.map.getTileAt(playerCenter[0], playerCenter[1])
                    center = tmpTile.getCenter(self.player.rect.w, self.player.rect.h)
                    self.player.moveTo(center[0], center[1])
                    self.collidesnd = self.loadsnd(r'\resources\sounds\effects\hitwall.wav')
                    self.collidesnd.play()
                    break
        for enemy in self.enemies:
            if(not enemy.alive):
                item =  enemy.dropItem()
                self.gameSprites.remove(enemy)
                self.enemies.remove(enemy)
                if(item != None):
                    self.items.append(item)

            elif(self.player.collide(enemy) and not enemy.isDying):
                if(enemy.isAttacking and enemy.hitAgain()):
                    self.player.receiveAttack(enemy.attackDamage)
                if(self.player.attacking):
                    enemy.receiveAttack(self.player.attackDamage)
                    
    def checkClick(self, x, y):
        if self.stage == "GAME":
            for item in self.items:
                if(item.mouseInIt(x, y)):
                    self.player.heal(item.heallingEffect())
                    self.items.remove(item)
                    return

            tile = self.map.getSelectedTile(x, y)
            center = tile.getCenter(self.player.rect.w, self.player.rect.h)
            self.player.moveTo(center[0], center[1])


        else: ## Menu is running
            for sprt in self.sprites:
                if (isinstance(sprt, button)):
                    if(sprt.checkClick(x, y)):
                        if(self.menu.action == "G"):
                            self.stage = "GAME"
                            self.sprites = self.gameSprites
                        elif(self.menu.action == "Q"):
                            self.quitGame()

    def quitGame(self):
        self.run = False

    def update(self):
        if(self.stage == "GAME"):
            self.checkCollision()
            for sprite in self.sprites:
                sprite.update()
            if (self.player.hp <= 0 or len(self.enemies) == 0):
                self.gameOver = True
