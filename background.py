import pygame
from settings import *
import os


class BackGround:

    def __init__(self):
        self.__grama = pygame.image.load(f"assets{os.sep}grama.jpg")
        self.__faixa_amarela = pygame.image.load(f"assets{os.sep}faixa_amarela.jpg")
        self.__faixa = pygame.image.load(f"assets{os.sep}faixa.jpg")

        # Esta lista contém a posição, em formato de lista, de todas faixas amarelas
        self.__lista_posicao_das_faixas = [[WIDTH / 2, -800 + 100 * i] for i in range(0, 14)]

        self.__vel_faixas = VELOCIDADE_FAIXAS

    def __get_lista_posicao_das_faixas(self):
        return self.__lista_posicao_das_faixas

    def __get_elemento_lista_posicao_das_faixas(self, i, j):
        return self.__lista_posicao_das_faixas[i][j]

    def __get_vel_faixas(self):
        return self.__vel_faixas

    def __get_grama(self):
        return self.__grama

    def __get_faixa(self):
        return self.__faixa

    def __get_faixa_amarela(self):
        return self.__faixa_amarela

    def __sum_posicao_faixa(self, posicao_faixa, value):
        posicao_faixa[1] += value

    def __create_screen_blit(self, screen, variable, lista_posicao):
        screen.blit(variable, tuple(lista_posicao))

    def update(self):
        for posicao_faixa in self.__get_lista_posicao_das_faixas():
            self.__sum_posicao_faixa(posicao_faixa, self.__get_vel_faixas())

        if self.__get_elemento_lista_posicao_das_faixas(0, 1) > 0:
            for posicao_faixa in self.__get_lista_posicao_das_faixas():
                self.__sum_posicao_faixa(posicao_faixa, -800)

    def render(self, screen):
        screen.fill((119, 119, 119))

        lista_posicao_blit = [[self.__get_grama(), 0], [self.__get_grama(), 700], [self.__get_faixa(), 120], [self.__get_faixa(), 680]]

        for list in lista_posicao_blit:
            self.__create_screen_blit(screen, list[0], [list[1], 0])

        for lista_posicao in self.__get_lista_posicao_das_faixas():
            self.__create_screen_blit(screen, self.__get_faixa_amarela(), lista_posicao)

