import pygame
import sys

pygame.init()

WIDTH = 500
LENGTH = 400

tela = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption('Teste')

#loop da página 
run = True

while True:
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
           run = False
           pygame.quit()
           sys.exit() 
        
        cor =  (240,230,140)
        tela.fill(cor)       
        pygame.draw.circle(tela, ('red'), (100,265), 50)
        pygame.draw.circle(tela, ('black'), (100,75), 20)


        # APLICAR UM 
        # RETANGULO ** 
        pygame.draw.rect(tela, ('green'),(350,55,100,50))
        # ELIPSE ** 
        pygame.draw.ellipse(tela,('blue'),(350,240,100,50))
        # DOCUMENTAÇÃO 
        # PESQUISA       


        pygame.display.flip()