from controlador import*

class Jogador():

    def __init__(self, x0, y0):
        self.__x0 = x0
        self.__y0 = y0
        self.__x = x0
        self.__y = y0
        self.__car_image = pygame.image.load("assets\\carro_rosa.png")
        self.rect = self.__car_image.get_rect(midtop=(self.__x, self.__y))

    def get_x(self):
        return self.__x

    def __get_y(self):
        return self.__y

    def __get_car_image(self):
        return self.__car_image

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def __set_rect_x(self, x):
        self.rect.x = x

    def update(self):
        if pygame.key.get_pressed()[DIREITA]:
            self.set_x(self.get_x() + 3)
            self.__set_rect_x(self.get_x())
        if pygame.key.get_pressed()[ESQUERDA]:
            self.set_x(self.get_x() - 3)
            self.__set_rect_x(self.get_x())

    def render(self, screen):
        #self.car_image = pygame.transform.scale(self.car_image, (50, 100))
        screen.blit(self.__get_car_image(), (self.get_x(), self.__get_y()))