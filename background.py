import pygame
from settings import *
import os

class BackGround:

    def __init__(self):
        self.__grama = pygame.image.load(f"assets{os.sep}grama.jpg")
        self.__faixa_amarela = pygame.image.load(f"assets{os.sep}faixa_amarela.jpg")
        self.__faixa = pygame.image.load(f"assets{os.sep}faixa.jpg")
        
        # Esta lista contém a posição, em formato de lista, de todas faixas amarelas 
        self.__lista_posicao_das_faixas = [ [WIDTH/2, -800 + 100*i] for i in range(0, 14) ]

        self.__vel_faixas = VELOCIDADE_FAIXAS

    def update(self):
        
        for posicao_faixa in self.__lista_posicao_das_faixas:
            posicao_faixa[1] += self.__vel_faixas

        if self.__lista_posicao_das_faixas[0][1]>0:
            for posicao_faixa in self.__lista_posicao_das_faixas:
                posicao_faixa[1] -= 800


    def render(self, screen):
        screen.fill((119, 119, 119))
        screen.blit(self.__grama, (0, 0))
        screen.blit(self.__grama, (700, 0))
        screen.blit(self.__faixa, (120, 0))  
        screen.blit(self.__faixa, (680, 0))  #

        for lista_posicao in self.__lista_posicao_das_faixas:
            screen.blit(self.__faixa_amarela, tuple(lista_posicao))

