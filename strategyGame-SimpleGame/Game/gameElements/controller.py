import pygame

class controller:
    
    def __init__(self, model):
        self.model = model
        pygame.key.set_repeat(60)

    def update(self):
        # Does not allow diagonal movements
    ## If diagonals movements desired, pygamey.key.get_pressed() tuple can be used instead
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.model.quitGame()
            elif event.type == pygame.KEYDOWN:
                # Unit movement
                if event.key == pygame.K_w:
                    pass
                elif event.key == pygame.K_s:
                    pass
                elif event.key == pygame.K_a:
                    pass
                elif event.key == pygame.K_d:
                    pass
                elif event.key == pygame.K_SPACE:
                    self.model.player.perfAttack()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.model.checkClick(event.pos[0], event.pos[1])