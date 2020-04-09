import pygame


# class which stores the main player
class PlayerEntity(pygame.sprite.Sprite):

    # construct method
    # @param game : instance of the class Game
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/entities/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.velocity_x = 0
        self.velocity_y = 0
