from settings import *
from background import BackGround
from obstaculo import Obstaculo
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
        self.tamanho_gp_obstaculos = 0

        self.temp_obstaculos = 0
        self.max_temp_obstaculos = 200

        self.carros_ultrapassados = 0

    def run(self):

        while True:
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




    def adicionar_obstaculos(self):
        self.temp_obstaculos+=1

        if self.temp_obstaculos>=self.max_temp_obstaculos:
            self.temp_obstaculos=0

            novo_obst = Obstaculo(VETOROBSTACULOSIMG[random.randrange(0, 6)], (random.randrange(125, 660), 0), self)
            
            self.grupo_obstaculos.add(novo_obst)


    def update(self):
        self.background.update()
        self.grupo_obstaculos.update()

    def render(self):
        self.background.render(self.screen)
        self.grupo_obstaculos.draw(self.screen)
        self.HUD.render(self.screen, self.carros_ultrapassados)
    
    def derrota_acostamento(self):
        pass

    def derrota_batida(self):
        pass



if __name__=="__main__":
    c = Controlador()
    c.run()