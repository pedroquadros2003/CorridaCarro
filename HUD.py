import pygame
from settings import *

class HUD:

    def init(self, screen):
        self.__carros_ultrapassados = 0
        self.__score = 0
        self.__screen = screen
        self.__hud_font = pygame.font.SysFont(None, 35)
    
    def set_carros_ultrapassados(self, novo_valor):
        self.__carros_ultrapassados = novo_valor

    def render(self):
        texto_ultrapassados = self.__hud_font.render("Ultrapassou: " + str(self.__carros_ultrapassados), True, (255, 255, 128))
        texto_score = self.__hud_font.render("Score: " + str(self.__score), True, (253, 231, 32))
        self.__screen.blit(texto_ultrapassados, (0, 50))
        self.__screen.blit(texto_score, (0, 100))


        