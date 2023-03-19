import pygame, sys
from settings import Button 


#ecrã
pygame.init()
screen = pygame.display.set_mode((1200,720))#criar a janela
pygame.display.set_caption('Menu') #definir o titulo da janela
clock = pygame.time.Clock() #definir o relogio 

#imagem de fundo
BG = pygame.image.load("bg.jpg")

#função que retorna um objeto de fonte com tamanho especificado
def get_font(size): 
    font =pygame.font.SysFont("8-Bit Madness", size)
    return font

#tela de jogo
def play():
    #definir o titulo da janela
    pygame.display.set_caption("Play")

    while True:
        #obter a posição do mouse
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
       
        #preencher a tela com preto
        screen.fill("black")
        
        #renderizar o texto
        PLAY_TEXT = get_font(45).render("This is the PLAYscreen", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640,260))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        #criar o botão "BACK"
        PLAY_BACK = Button(image =None, pos=(640, 460), 
                           text_input ="BACK", font=get_font(75), base_color="White", hovering_color="Pink")
        
       #Mudar a cor do botão se o rato estiver a passar por cima dele 
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        #loop de eventos eventos
        for event in pygame.event.get():
           #se o utilizador fechar a janela, sair do programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Se o utilizador clicar no botão esquerdo do rato
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Voltar ao menu principal se o botão "BACK" for clicado
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        #atualizar a tela
        pygame.display.update()

#tela de options
def options(): #options screen
    pygame.display.set_caption("Options")

    while True:
        #obter a posição do rato
        OPTIONS_MOUSE_POS= pygame.mouse.get_pos()

       #preencher a tela com branco
        screen.fill("White")

        #texto de options
        OPTIONS_TEXT =get_font(45).render("...", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        #criar o botão "BACK"
        OPTIONS_BACK = Button(image=None, pos=(640,460),
                              text_input= "BACK", font=get_font(75), base_color="Black", hovering_color="Pink")
        
        #mudar a cor do botão se o rtao estiver a passar por cima dele
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
           #sair do jogo se o jogador clicar no botão fechar
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           #se o utilizador clicar no botão esquerdo do rato
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        #atualizar a tela
        pygame.display.update()


def main_menu(): #Main menu screen 
    pygame.display.set_caption("Menu")

    while True:
        screen.blit (BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #texto do titulo do menu principal
        MENU_TEXT = get_font(106).render("MAIN MENU", True, (255, 105, 180))
        
        MENU_RECT = MENU_TEXT.get_rect(center= (600, 100))

        #botões de opções disponiveis no menu principal
        PLAY_BUTTON = Button(image=pygame.image.load("buttons3.jpg"), pos=(600, 250),
                             text_input="PLAY", font=get_font(75), base_color="Pink", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("buttons3.jpg"), pos=(600, 400),
                             text_input="OPTIONS", font=get_font(75), base_color="Pink", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("buttons3.jpg"), pos=(600, 550),
                             text_input="QUIT", font=get_font(75), base_color="Pink", hovering_color="White")
        
        screen.blit(MENU_TEXT, MENU_RECT)

        #atualiza a cor do botão se p mouse estiver em cima dele
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
               #verifica se o botão de play foi pressionado e inicia a tela de jogo
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                #verifica se o botao de opcoes foi pressionado e inicia a tela de opções 
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                #verifica se o botão de sair foi pressionado e encerra o jogo
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        #atualiza a tela
        pygame.display.update()
main_menu()
