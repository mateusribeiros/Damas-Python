import pygame
from Variaveis import branco, cinza, Linhas, Colunas, preto,Tamanho
from Peças import Pieces

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = []
        self.criar_peças()

    def desenhar_tabu(self, surface):
        for linha in range(Linhas):
            for coluna in range(Colunas):
                x = coluna * Tamanho
                y = linha * Tamanho
                if (linha + coluna) % 2 == 0:
                    pygame.draw.rect(surface, branco, (x, y, Tamanho, Tamanho))
                else:
                    pygame.draw.rect(surface, cinza, (x, y, Tamanho, Tamanho))

    def criar_peças(self):
        for linha in range(Linhas):
            self.tabuleiro.append([])
            for coluna in range(Colunas):
                if coluna % 2 == (linha + 1) % 2:
                    if linha < 3:
                        self.tabuleiro[linha].append(Pieces(linha, coluna, branco))
                    elif linha > 4:
                        self.tabuleiro[linha].append(Pieces(linha, coluna, preto))
                    else:
                        self.tabuleiro[linha].append(0)
                else:
                    self.tabuleiro[linha].append(0)

    def desenhar(self, surface):
        self.desenhar_tabu(surface)
        for linha in range(Linhas):
            for coluna in range(Colunas):
                peca = self.tabuleiro[linha][coluna]
                if peca != 0:
                    peca.desenhar(surface)

