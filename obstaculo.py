import pygame
from settings import *
import os

class Obstaculo (pygame.sprite.Sprite):

    def __init__(self, tipo_obstaculo, posic_midbottom):
        super().__init__()
        self.image = pygame.image.load(f"assets{os.sep}{tipo_obstaculo}.png")
        self.rect = self.image.get_rect(midbottom = posic_midbottom)
        self.__vel_obstaculo = VELOCIDADE_OBS
        self.__esta_morto = False

    def update(self):
        self.rect.bottom += self.__vel_obstaculo

        if self.rect.top > HEIGHT*1.5:
            self.kill()

    ## Função que retorna True somente no primeiro momento em que se percebe que o obstáculo saiu da tela
    ## Importante para o cálculo de carros ultrapassados
    def checar_momento_morte(self):
        if not self.__esta_morto:
            if self.rect.top > HEIGHT:
                self.__esta_morto = True
                return True
        return False
