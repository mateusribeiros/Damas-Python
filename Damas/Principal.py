import pygame
from Damas.Variaveis import largura,altura, Tamanho
from Peças import Pieces
from Damas.Tela import Tabuleiro

pygame.init()
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo de damas')
clock = pygame.time.Clock()

def mouse(pos):
    x,y = pos
    linha = y // Tamanho
    coluna = x // Tamanho
    return  linha, coluna
def main():
    tabuleiro = Tabuleiro()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                linha,coluna = mouse(pos)
                peça = tabuleiro.pegar_peça(linha,coluna)
                tabuleiro.movimentos(peça,4,3)
        tabuleiro.desenhar(tela)
        pygame.display.update()
        clock.tick(30)
main()

