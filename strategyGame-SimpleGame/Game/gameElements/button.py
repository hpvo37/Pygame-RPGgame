import pygame
from Game.gameElements.sprite import sprite

class button(sprite):
    TEXTSIZE = None
    TEXTCOLOR = pygame.Color(255, 255, 255)
    UTEXTCOLOR = pygame.Color(168, 168, 168)
    
    BGCOLOR = pygame.Color(0, 0, 0)
    UBGCOLOR = pygame.Color(70, 66, 50)
    BUTTONMARGIN = 20

    BCOLORUNACTIVE = pygame.Color(0,0,0, 255)
    
    
    def __init__(self, x, y, w, size, text, clickFunct, color = None):
        super().__init__(x + button.BUTTONMARGIN//2, y, w - button.BUTTONMARGIN, 0)
        if(button.TEXTSIZE == None): button.TEXTSIZE = {"S": pygame.font.SysFont('Berlin Sans FB', 20)}
        self.text = self.aText = button.TEXTSIZE[size].render(text, True, button.TEXTCOLOR)
        self.uText = button.TEXTSIZE[size].render(text, True, button.UTEXTCOLOR)
        self.textRect = self.aText.get_rect()
        print("String Size: " + str(self.textRect))
        if color == None:
            self.color = button.BGCOLOR
        else:
            self.color = color
            self.regColor = color
            # Color for button when it is unclickable
            self.unClickBColor =  pygame.Color(color[0], color[1] - 10, color[2] -10)

        self.rect.h = self.textRect.h * 2 + button.BUTTONMARGIN

        # Locating text in the center of button
        self.textRect.x =  self.rect.x + (self.rect.w - self.textRect.w)//2
        self.textRect.y =  self.rect.y + (self.rect.h - self.textRect.h)//2

        self.clickCall = clickFunct

        #Click animation
        self.clickTime = 0

        #Controls wheather or not it can be clicked
        #It allows to control if a unit can or not perform certain actions
        self.active = True
        

    def setActive(self, active):
        self.active = active
        if(not self.active):
            self.color = button.UBGCOLOR
            self.text =  self.uText
        else:
            self.color = button.BGCOLOR
            self.text = self.aText
               
    def checkClick(self, x, y):
        if(self.active and self.mouseInIt(x, y)):
            self.color = button.BGCOLOR
            self.clickTime = 0
            self.clickCall()
            return True
        else: return False
        
    def draw(self):
        self.drawSquare(self.color)
        sprite.screen.blit(self.text, self.textRect)

    def update(self):
        # Clicking animation
        if(self.active):
            if(self.color == button.BGCOLOR):
                self.clickTime += 1
                if(self.clickTime == 64):
                    self.color = self.regColor