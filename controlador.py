from settings import *
from background import BackGround
from HUD import HUD

import pygame
import random
import time
from settings import *

class Controlador:

    def __init__(self):
        pygame.init()  # inicializar o pygame

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # tamanho da tela

        pygame.display.set_caption("Corrida")

        self.clock = pygame.time.Clock()


        self.background = BackGround()

        self.HUD = HUD()

        #self.grupo_jogador = pygame.sprite.GroupSingle()
        #self.grupo_jogador.add()

        self.grupo_obstaculos = pygame.sprite.Group()


        self.max_timer = 100
        self.timer = 0

    def run(self):

        # se fechar a janela, o jogo para
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #adicionar obstáculos
        self.adicionar_obstaculos()

        #dar update em tudo
        self.update()

        #dar blit nos elementos, em ordem
        self.render()

        # Mensagem de derrota movimento lateral do carro
        self.derrota_acostamento()

        # Mensagem de derrota batida do carro
        self.derrota_batida()

        # Atualizando a tela
        pygame.display.update()
        self.clock.tick(100)

        self.run()


    def adicionar_obstaculos(self):
        pass

    def update(self):
        pass

    def render(self):
        pass
    
    def derrota_acostamento(self):
        pass

    def derrota_batida(self):
        pass



if __name__=="__main__":
    c = Controlador()
    c.run()