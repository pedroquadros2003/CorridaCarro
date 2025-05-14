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

        self.jogador = Jogador(300, 450)

        self.grupo_obstaculos = pygame.sprite.Group()
        self.tamanho_gp_obstaculos = 0

        self.__temp_obstaculos = 0
        self.__max_temp_obstaculos = 200

        self.__carros_ultrapassados = 0

    def __get_temp_obstaculos(self):
        return self.__temp_obstaculos

    def __set_temp_obstaculos(self, value):
        self.__temp_obstaculos = value

    def __get_max_temp_obstaculos(self):
        return self.__max_temp_obstaculos

    def __set_max_temp_obstaculos(self, value):
        self.__max_temp_obstaculos = value

    def __get_carros_ultrapassados(self):
        return self.__carros_ultrapassados

    def __set_carros_ultrapassados(self, value):
        self.__carros_ultrapassados = value

    def run(self):

        while not self.__game_over:
            # se fechar a janela, o jogo para
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # adicionar obstáculos
            self.adicionar_obstaculos()

            # dar update em tudo
            self.update()

            # dar blit nos elementos, em ordem
            self.render()

            # Mensagem de derrota movimento lateral do carro
            self.derrota_acostamento()

            # Mensagem de derrota batida do carro
            self.derrota_batida()

            # Atualizando a tela
            pygame.display.update()
            self.clock.tick(100)

    def adicionar_obstaculos(self):
        self.__set_temp_obstaculos(self.__get_temp_obstaculos() + 1)

        if self.__get_temp_obstaculos() >= self.__get_max_temp_obstaculos():
            self.__set_temp_obstaculos(0)

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
                self.__set_carros_ultrapassados(self.__get_carros_ultrapassados() + 1)

    def render(self):
        self.background.render(self.screen)
        self.grupo_obstaculos.draw(self.screen)
        self.HUD.render(self.screen, self.__get_carros_ultrapassados())
        self.jogador.render(self.screen)

    def derrota_acostamento(self):
        if self.jogador.get_x() < 125 or self.jogador.get_x() > 660:
            self.HUD.derrota_acostamento(self.screen)
            time.sleep(2)
            self.reiniciar_jogo()
            self.run()
            self.__game_over = True

    def derrota_batida(self):
        for obstaculo in self.grupo_obstaculos:
            if self.jogador.rect.colliderect(obstaculo.rect):
                self.HUD.derrota_carro(self.screen)
                time.sleep(2)
                self.__game_over = True

    def reiniciar_jogo(self):
        self.grupo_obstaculos.empty()
        self.__set_carros_ultrapassados(0)
        self.__set_temp_obstaculos(0)
        self.__set_max_temp_obstaculos(200)
        self.jogador.set_x(300)
        self.jogador.set_y(450)
