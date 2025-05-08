import pygame 

"""
    Configurações de jogo como velocidade dos carros, tamanho da tela e nome da janela.
    
"""

#variavei de movimento do jogador
DIREITA = pygame.K_RIGHT
ESQUERDA = pygame.K_LEFT

#tamanho da tela
WIDTH = 800
HEIGHT = 600

#nome da janela de jogo
TITULO = "Corrida de Carro" 

#fonte utilizada no jogo
FONTE = "Fonte4.ttf"

#velocidade dos obstáculos
VELOCIDADE_OBS = 3

#velocidade das faixas
VELOCIDADE_FAIXAS=1

#arquivos de obstáculos (carros)
VETOROBSTACULOSIMG = ["carro_verde", "moto_preta", "carro_pink", "carro_branco", "carro_preto", "moto_azul"]
