"""" Jogo de corrida de carros adaptado (figuras) do código-fonte de Asish Raz
(https://www.youtube.com/watch?v=ul-XHW-sTRo&list=PLE_8CZYFlz5bw1iqtvO0IysAN2C6EiLDs&index=3)"""

import pygame
import random
import time
from settings import *


pygame.init()  # inicializar o pygame

DIREITA = pygame.K_RIGHT
ESQUERDA = pygame.K_LEFT

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # tamanho da tela

clock = pygame.time.Clock()

car_image = pygame.image.load("carro_rosa.png")

# definindo a posição do carro
def car(x, y):
    screen.blit(car_image, ((x, y)))

# carregando as imagens
grama = pygame.image.load("grama.jpg")
faixa_amarela = pygame.image.load("faixa_amarela.jpg")
faixa = pygame.image.load("faixa.jpg")

# definindo as posições das faixas amarelas para criar o movimento
def faixaA(faixaA_x, faixaA_y):
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y + 100))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y + 200))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y + 300))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y + 400))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y + 500))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y - 100))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y - 200))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y - 300))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y - 400))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y - 500))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y - 600))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y - 700))
    screen.blit(faixa_amarela, (faixaA_x, faixaA_y - 800))
# adicionando os obstaculos
def obstaculo(obstaculo_x, obstaculo_y, obst):
    if obst == 0:
        obstaculo_imagem = pygame.image.load("carro_verde.png")
    elif obst == 1:
        obstaculo_imagem = pygame.image.load("moto_preta.png")
    elif obst == 2:
        obstaculo_imagem = pygame.image.load("carro_pink.png")
    elif obst == 3:
        obstaculo_imagem = pygame.image.load("carro_branco.png")
    elif obst == 4:
        obstaculo_imagem = pygame.image.load("carro_preto.png")
    elif obst == 5:
        obstaculo_imagem = pygame.image.load("moto_azul.png")

    screen.blit(obstaculo_imagem, (obstaculo_x, obstaculo_y))

pygame.display.set_caption("Corrida")

# definindo o plano de fundo
def background():
    screen.blit(grama, (0, 0))
    screen.blit(grama, (700, 0))
    screen.blit(faixa, (120, 0))  # 20 depois da primeira grama
    screen.blit(faixa, (680, 0))  # 20 antes da segunda grama

# definindo as fontes
my_font = pygame.font.Font("Fonte4.ttf", 100)
render_text_bateulateral = my_font.render("VOCê BATEU!", 0, (255, 255, 255))  # ("texto", opaco/transparente 0/1, cor do texto)
render_text_perdeu= my_font.render("GAME OVER!" , 0, (255, 0, 0))  # ("texto

# função para escrever na tela a quantidade de carros que passaram e a pontuação
def score_card(car_passou, score):
    font = pygame.font.SysFont(None, 35)
    passou = font.render("Passou: " + str(car_passou), True, (255, 255, 128))
    score = font.render("Score: " + str(score), True, (253, 231, 32))
    screen.blit(passou, (0, 50))
    screen.blit(score, (0, 100))

# função que faz o looping do jogo
def game_loop():

    car_passou = 0
    score = 0

    velocidade_obstaculo = 2

    faixaA_x = 375
    faixaA_y = 0
    obst = 0
    obstaculo_x = random.randrange(125, 660)

    inimigo_largura = 55
    inimigo_altura = 120
    obstaculo_y = -500
    fechou = False  # primeiramente, fechou é falso: a tela está aberta

    x = (WIDTH-56)/2
    y = HEIGHT-125

    mudar_x = 0
    while not fechou:
        # se fechar a janela, o jogo para
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                fechou = True
        # se clicar em qualquer tecla, entra no if
        if event.type == pygame.KEYDOWN:
            # se clicar na seta da esquerda, anda 3 para a esquerda no eixo x
            if event.key == ESQUERDA:
                mudar_x = -3
            # se clicar na seta da direita, anda 3 para a direita no eixo x
            if event.key == DIREITA:
                mudar_x = 3
        # se soltar qualquer tecla, não faz nada
        if event.type == pygame.KEYUP:
            if event.key == ESQUERDA or event.key == DIREITA:
                mudar_x = 0

        # alterando a coordenada x do carro de acordo comas mudanças acima para ele se mover
        x = x + mudar_x

        # deixando o fundo cinza
        screen.fill((119, 119, 119))  # cinza em RGB

        # chamando a função background para adicionar as faixas e a grama
        background()

        # adicionando movimento às faixas
        #faixaA_y = faixaA_y + velocidade_obstaculo / 4
        faixaA(faixaA_x, faixaA_y)
        faixaA_y = faixaA_y + velocidade_obstaculo

        # adicionando movimento aos obstaculos
        obstaculo_y = obstaculo_y + velocidade_obstaculo/4
        obstaculo(obstaculo_x, obstaculo_y, obst)
        obstaculo_y = obstaculo_y + velocidade_obstaculo

        car(x, y)

        score_card(car_passou, score)

        # restrições do movimento do carro
        if x > 680 - 56 or x < 120 + 5:
            screen.blit(render_text_bateulateral, (80, 200))
            pygame.display.update()  # atualizar a tela
            time.sleep(3)
            game_loop()
            fechou = True

       # definindo onde o obstaculo vai aparecer, recomeçando a posição do obstaculo e da faixa
        if obstaculo_y > HEIGHT:
            obstaculo_y = 0-inimigo_altura
            faixaA_y = 0
            obstaculo_x = random.randrange(125, 650-inimigo_largura)
            obst = random.randint(0, 5)
            # determinando quantos carros passaram e a pontuação
            car_passou = car_passou + 1
            score = car_passou * 10

        # restrições para o game over
        if y < obstaculo_y + inimigo_altura:
            if x > obstaculo_x or x > obstaculo_x -56:
                if x < obstaculo_x + inimigo_largura or x < obstaculo_x-56:
                    screen.blit(render_text_perdeu, (80, 200))
                    pygame.display.update()
                    time.sleep(3)
                    fechou = True

        # ataualizando a tela
        pygame.display.update()
        clock.tick(100)#(100)

game_loop()
pygame.quit()
quit()
