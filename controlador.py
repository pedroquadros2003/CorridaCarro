from settings import *
from background import BackGround
from obstaculo import Obstaculo
from HUD import HUD
from jogador import Jogador

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

        self.__game_over = False

        #self.grupo_jogador = pygame.sprite.GroupSingle()
        #self.grupo_jogador.add()
        self.jogador = Jogador(300, 450)

        self.grupo_obstaculos = pygame.sprite.Group()
        self.tamanho_gp_obstaculos = 0

        self.temp_obstaculos = 0
        self.max_temp_obstaculos = 200

        self.carros_ultrapassados = 0

    def run(self):

        while not self.__game_over:
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

            novo_obst = Obstaculo(VETOROBSTACULOSIMG[random.randrange(0, 6)], (random.randrange(125, 660), 0))
            
            self.grupo_obstaculos.add(novo_obst)


    def update(self):
        self.update_carros_ultrapassados()
        self.background.update()
        self.grupo_obstaculos.update()
        self.jogador.update()

    def update_carros_ultrapassados(self):
        for obstaculo in self.grupo_obstaculos:
            if obstaculo.checar_momento_morte():
                self.carros_ultrapassados+=1

    def render(self):
        self.background.render(self.screen)
        self.grupo_obstaculos.draw(self.screen)
        self.HUD.render(self.screen, self.carros_ultrapassados)
        self.jogador.render(self.screen)
    
    def derrota_acostamento(self):
        if self.jogador.x < 125 or self.jogador.x > 660:
            self.HUD.derrota_acostamento(self.screen)
            pygame.display.update()
            time.sleep(2)
            self.reiniciar_jogo()
            self.run()
            self.__game_over = True

    def derrota_batida(self):
        pass
        # for obstaculo in self.grupo_obstaculos:
        #     if dealgumaformachecaracolisaoooo:
        #         self.HUD.derrota_acostamento(self.screen)
        #         pygame.display.update()
        #         time.sleep(2)
        #         self.reiniciar_jogo()
        #         self.run()
        #         self.__game_over = True

    def reiniciar_jogo(self):
        self.grupo_obstaculos.empty()
        self.carros_ultrapassados = 0
        self.temp_obstaculos = 0
        self.max_temp_obstaculos = 200
        self.jogador.x = 300
        self.jogador.y = 450
