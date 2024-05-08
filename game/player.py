import random

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.scene = pygame.display.get_surface().get_rect()
        self.rect.x = self.scene.width // 2
        self.rect.y = self.scene.height - self.rect.height

