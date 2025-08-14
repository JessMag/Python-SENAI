# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/




#DEFINIÇÃO DE VARIAVEIS DAS DIMENSOES DE TELA
largura, altura = 400, 400

#CRIACAO DA TELA COM A BIBBLIOTECA PYGAME, SUB MODULO DISPLAY E FUNCAO SET MODE UTILIZANDO AS VARIAVEIS JÁ CRIADAS
tela = pygame.display.set_mode((largura, altura))

#TITULO DO JOGO COM SUBMODULO DISPLAY E FUNÇÃO SET CAPTION
pygame.display.set_caption("Labirinto")

#CRIA CORES COM RGB (SÃO TUPLAS)
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

#CRIA UMA VARIAVEL QUE VAI DEFINIR O TAMANHO DO "JOGADOR" E DE CADA "PIXEL" DO LABIRINTO
tamanho_celula = 40

#CRIA UMA LISTA DENTRO DA LISTA ONDE 1 SERA O LABIRINTO E 0 O ESPAÇO EM BRANCO, CRIA O CENÁRIO ATRAVES DESSA "MATRIZ"
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#QUANDO O "PERSONAGEM" FOR ANDAR X*TAMANHO FARÁ COM QUE ELE PULE AO PROXIMO QUADRADO ANDANDO UMA CASA, MESMO PARA Y
x, y = 1 * tamanho_celula, 1 * tamanho_celula
#VELOCIDADE ALTA FARA COM QUE "PULE" PARA A PROXIMA CASA
velocidade = 40

#AGORA EFETIVAMENTE SERÁ CRIADO O LABIRINTO ATRAVES DA LISTA
#CRIA FUNÇÃO QUE VAI DESENHAR
def desenhar_labirinto():
    #LOOP FOR VARIAVEL LINHA EM DENTRO DO COMPRIMENTO DA LISTA ENTÃO
    for linha in range(len(labirinto)):
        #ENTRA PRA MAIS UM LOOP
        for coluna in range(len(labirinto[linha])):
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))


executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False


    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y


    tela.fill(branco)

    
    desenhar_labirinto()
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))


    pygame.display.flip()


    pygame.time.Clock().tick(10)


pygame.quit()
