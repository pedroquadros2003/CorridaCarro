import pygame
from settings import *
import os

class Obstaculo (pygame.sprite.Sprite):

    def __init__(self, tipo_obstaculo, posic_midbottom, controlador):
        super().__init__()
        self.image = pygame.image.load(f"assets{os.sep}{tipo_obstaculo}.png")
        self.rect = self.image.get_rect(midbottom = posic_midbottom)
        self.__vel_obstaculo = 3
        self.controlador = controlador


    def update(self):
        self.rect.bottom += self.__vel_obstaculo

        if self.rect.top > HEIGHT:
            self.controlador.carros_ultrapassados+=1
            self.kill()
        

#git remote add origin git@github.com:<pedroquadros2003>/CorridaCarro.git
