# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARKGREY = (40, 40, 40)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BGCOLOUR = BLACK

#game settings
WIDTH = 1100 #largura da janela
HEIGHT = 641 #altura da janela
FPS= 60 #frames por segundo
title = "PuzzlePacked IQ Games"#título da janela
TILESIZE = 50 #tamanho de cada peça do puzzle
GAME_SIZE = 4 #tamanho do jogo

#buttons para menu
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos [0]
        self.y_pos = pos [1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image= self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect =self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update (self, screen):
        #atualiza o botão na tela
        if self.image is not None:
            screen.blit(self.image, self.rect)    
        screen.blit(self.text, self.text_rect)

    def checkForInput(self,position):
        #verifica se a posição passada como parâmetro esta dentro do botão
        if position [0] in range (self.rect.left, self.rect.right) and position [1] in range (self.rect.top, self.rect.bottom):
            return True
        return False
    def changeColor(self, position):
        #muda a cor  do botão para a cor "hovering" se o cursor do rato estiver por cima dele
        if position [0] in range (self.rect.left, self.rect.right) and position [1] in range (self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text= self.font.render(self.text_input, True, self.base_color)













