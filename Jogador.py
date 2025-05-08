from Controlador import*

class Jogador():

    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0

    def update(self):
        if pygame.key.get_pressed()[DIREITA]:
            self.x = self.x + 3
        if pygame.key.get_pressed()[ESQUERDA]:
            self.x = self.x - 3
    
    car_image = pygame.image.load("imagens\carro_rosa.png")