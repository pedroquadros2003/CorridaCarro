from controlador import*

class Jogador():

    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0
        self.x = x0
        self.y = y0
        self.car_image = pygame.image.load("assets\carro_rosa.png")

    def update(self):
        if pygame.key.get_pressed()[DIREITA]:
            self.x = self.x + 3
        if pygame.key.get_pressed()[ESQUERDA]:
            self.x = self.x - 3

    def render(self, screen):
        #self.car_image = pygame.transform.scale(self.car_image, (50, 100))
        screen.blit(self.car_image, (self.x, self.y))