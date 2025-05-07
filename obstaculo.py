import pygame
from settings import *

class Obstaculo (pygame.sprite.Sprite):

    def __init__(self, tipo_obstaculo, posic_midbottom):

        self.image = pygame.image.load(f"{tipo_obstaculo}.png")
        self.rect = self.image.get_rect(midbottom = posic_midbottom)
        self.__vel_obstaculo = 3

    def update(self):
        self.rect.bottom += self.__vel_obstaculo

        if self.__rect.top > HEIGHT:
            self.kill()
        

#git remote add origin git@github.com:<pedroquadros2003>/CorridaCarro.git
