from Game.gameElements.sprite import sprite

class item(sprite):
    def __init__(self, enemyR, w = 34, h = 34):
        super().__init__(enemyR.center[0] - w//2,
                         enemyR.center[1] - h//2,
                         w, h, r"\resources\sprites\items\redPotion.png")
    def heallingEffect(self):
        return 20

    def update(self):
        pass
    

