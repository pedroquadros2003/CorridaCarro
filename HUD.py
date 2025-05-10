import pygame
from settings import *

class HUD:

    def __init__(self):
        self.__hud_font = pygame.font.SysFont(None, 35)

        #fontes para as mensagens de derrota
        self.__perda_font = pygame.font.Font("assets\\Fonte4.ttf", 100)
        self.text_bateulateral = self.__perda_font.render("VOCê BATEU!", 0, (255, 255, 255))  # ("texto", opaco/transparente 0/1, cor do texto)
        self.text_perdeu = self.__perda_font.render("GAME OVER!" , 0, (255, 0, 0))


    def render(self, screen, carros_ultrapassados):
        texto_ultrapassados = self.__hud_font.render("Ultrapassou: " + str(carros_ultrapassados), True, (255, 255, 128))
        texto_score = self.__hud_font.render("Score: " + str(carros_ultrapassados*10), True, (253, 231, 32))
        screen.blit(texto_ultrapassados, (0, 50))
        screen.blit(texto_score, (0, 100))

    def derrota_acostamento(self, screen):
        # Mensagem de derrota movimento lateral do carro
        screen.blit(self.text_bateulateral, (WIDTH//2-310, HEIGHT//2-100))
        pygame.display.update()
    
    def derrota_carro(self, screen):
        # Mensagem de derrota movimento do carro
        screen.blit(self.text_perdeu, (WIDTH//2-310, HEIGHT//2-100))
        pygame.display.update()
    


        