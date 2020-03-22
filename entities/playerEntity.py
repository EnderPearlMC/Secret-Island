import pygame


# class which stores the main player
class PlayerEntity(pygame.sprite.Sprite):

    # construct method
    # @param game : instance of the class Game
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load("assets/images/entities/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.velocity_x = 0
        self.velocity_y = 0

        self.game = game

    def change_velocity(self, vel_x, vel_y):
        if 7 > self.velocity_x > -7:
            self.velocity_x += vel_x
        if 7 > self.velocity_y > -7:
            self.velocity_y += vel_y

    def reset_velocity(self):
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self):

        """self.rect.x += self.velocity_x

        block_hit_list = pygame.sprite.spritecollide(self, self.game.dungeons.get(self.game.current_dungeon).blocks_collision_group, False)
        for b in block_hit_list:
            if self.velocity_x > 0:
                self.rect.right = b.rect.left
            else:
                self.rect.left = b.rect.right

        self.rect.y += self.velocity_y

        block_hit_list = pygame.sprite.spritecollide(self, self.game.dungeons.get(self.game.current_dungeon).blocks_collision_group, False)
        for b in block_hit_list:
            if self.velocity_y > 0:
                self.rect.bottom = b.rect.top
            else:
                self.rect.top = b.rect.bottom"""