import pygame
from settings import *

class BackGround:

    def init(self, screen):
        self.__screen = screen

        self.__grama = pygame.image.load("grama.jpg")
        self.__faixa_amarela = pygame.image.load("faixa_amarela.jpg")
        self.__faixa = pygame.image.load("faixa.jpg")
        
        self.__posicao_lista_faixas = [ [WIDTH, -800 + 100*i] for i in range(0, 14) ]
        self.__vel_faixas = 2

    def update(self):
        for lista_posicao in self.__posicao_lista_faixas:
            lista_posicao += [0, self.__vel_faixas]

    def render(self):
        self.__screen.blit(self.__grama, (0, 0))
        self.__screen.blit(self.__grama, (700, 0))
        self.__screen.blit(self.__faixa, (120, 0))  # 20 depois da primeira grama
        self.__screen.blit(self.__faixa, (680, 0))  # 20 antes da segunda grama

        for lista_posicao in self.__posicao_lista_faixas:
            self.__screen.blit(self.__faixa_amarela, tuple(lista_posicao))

