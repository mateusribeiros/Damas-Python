import pygame
from pygame.locals import *
from sys import exit

pygame.init()
white=(255, 255, 255)
tela = pygame.display.set_mode((540,780))
pygame.display.set_caption('Image')

# Carregar a imagem usando o Pygame
imagem = pygame.image.load(".\\Damas\\tabuleiro.jpg")
pygame.display.set_caption('Jogo de damas')

while True:
    tela.fill(white)
    tela.blit(imagem,(0,0))
    pygame.font.init()
    font1 = pygame.font.Font(None, 30)
    text = font1.render("    1          2          3          4           5            6          7            8", True, (0, 0, 0))
    tela.blit(text, (10, 490))
    font1 = pygame.font.Font(None, 30)
    text = font1.render("A", True, (0, 0, 0))
    tela.blit(text, (510, 20))
    font1 = pygame.font.Font(None, 30)
    text = font1.render("B", True, (0, 0, 0))
    tela.blit(text, (510, 80))
    font1 = pygame.font.Font(None, 30)
    text = font1.render("C", True, (0, 0, 0))
    tela.blit(text, (510, 140))
    font1 = pygame.font.Font(None, 30)
    text = font1.render("D", True, (0, 0, 0))
    tela.blit(text, (510, 200))
    font1 = pygame.font.Font(None, 30)
    text = font1.render("E", True, (0, 0, 0))
    tela.blit(text, (510, 260))
    font1 = pygame.font.Font(None, 30)
    text = font1.render("F", True, (0, 0, 0))
    tela.blit(text, (510, 320))
    font1 = pygame.font.Font(None, 30)
    text = font1.render("G", True, (0, 0, 0))
    tela.blit(text, (510, 380))
    font1 = pygame.font.Font(None, 30)
    text = font1.render("H", True, (0, 0, 0))
    tela.blit(text, (510, 440))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # VERMELHAS
    # Primeiras casas Vermelhas
    pygame.draw.circle(tela, (255, 0, 0), (100, 30), (20)) # 125 distancia das casas
    pygame.draw.circle(tela, (255, 0, 0), (225, 30), (20))
    pygame.draw.circle(tela, (255, 0, 0), (350, 30), (20))
    pygame.draw.circle(tela, (255, 0, 0), (475, 30), (20))

    # Segundas Casas Vermelhas
    pygame.draw.circle(tela, (255, 0, 0), (35, 90), (20))
    pygame.draw.circle(tela, (255, 0, 0), (160, 90), (20))
    pygame.draw.circle(tela, (255, 0, 0), (285, 90), (20))
    pygame.draw.circle(tela, (255, 0, 0), (410, 90), (20))

    # Terceiras Casas Vermelhas
    pygame.draw.circle(tela, (255, 0, 0), (100, 150), (20))
    pygame.draw.circle(tela, (255, 0, 0), (225, 150), (20))
    pygame.draw.circle(tela, (255, 0, 0), (350, 150), (20))
    pygame.draw.circle(tela, (255, 0, 0), (475, 150), (20))


    # BRANCAS
    # Primeiras Casas Brancas
    pygame.draw.circle(tela, (255, 255, 255), (35, 455), (20))
    pygame.draw.circle(tela, (255, 255, 255), (160, 455), (20))
    pygame.draw.circle(tela, (255, 255, 255), (285, 455), (20))
    pygame.draw.circle(tela, (255, 255, 255), (410, 455), (20))

    pygame.draw.circle(tela, (255, 255, 255), (100, 395), (20))
    pygame.draw.circle(tela, (255, 255, 255), (225, 395), (20))
    pygame.draw.circle(tela, (255, 255, 255), (350, 395), (20))
    pygame.draw.circle(tela, (255, 255, 255), (475, 395), (20))

    pygame.draw.circle(tela, (255, 255, 255), (35, 335), (20))
    pygame.draw.circle(tela, (255, 255, 255), (160, 335), (20))
    pygame.draw.circle(tela, (255, 255, 255), (285, 335), (20))
    pygame.draw.circle(tela, (255, 255, 255), (410, 335), (20))

    pygame.display.update()