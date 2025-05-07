import pygame
from settings import *
import os

class BackGround:

    def __init__(self):
        self.grama = pygame.image.load(f"assets{os.sep}grama.jpg")
        self.faixa_amarela = pygame.image.load(f"assets{os.sep}faixa_amarela.jpg")
        self.faixa = pygame.image.load(f"assets{os.sep}faixa.jpg")
        
        self.posicao_lista_faixas = [ [WIDTH/2, -800 + 100*i] for i in range(0, 14) ]
        self.vel_faixas = 1

    def update(self):
        
        for lista_posicao in self.posicao_lista_faixas:
            lista_posicao[1] += self.vel_faixas

        if self.posicao_lista_faixas[0][1]>0:
            for lista_posicao in self.posicao_lista_faixas:
                lista_posicao[1] -= 800


    def render(self, screen):
        screen.fill((119, 119, 119))
        screen.blit(self.grama, (0, 0))
        screen.blit(self.grama, (700, 0))
        screen.blit(self.faixa, (120, 0))  
        screen.blit(self.faixa, (680, 0))  #

        for lista_posicao in self.posicao_lista_faixas:
            screen.blit(self.faixa_amarela, tuple(lista_posicao))

