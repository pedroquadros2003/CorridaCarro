import pygame
from settings import *

class HUD:

    def __init__(self):
        self.__hud_font = pygame.font.SysFont(None, 35)


    def render(self, screen, carros_ultrapassados):
        texto_ultrapassados = self.__hud_font.render("Ultrapassou: " + str(carros_ultrapassados), True, (255, 255, 128))
        texto_score = self.__hud_font.render("Score: " + str(carros_ultrapassados*10), True, (253, 231, 32))
        screen.blit(texto_ultrapassados, (0, 50))
        screen.blit(texto_score, (0, 100))


        