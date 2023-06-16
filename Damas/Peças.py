import pygame
from Variaveis import preto,Tamanho,branco

class Pieces:

    def __init__(self,linha,coluna,cor):
        self.linha = linha
        self.coluna = coluna
        self.cor = cor
        if self.cor == preto:
            self.direção = -1
        else:
            self.direção = 1
        self.x = 0
        self.y = 0
        self.posição()
    def posição(self):
        self.x = Tamanho * self.coluna + Tamanho//2
        self.y = Tamanho * self.linha + Tamanho // 2
    def desenhar(self,surface):
        pygame.draw.circle(surface, self.cor, (self.x,self.y), 20)
        pygame.draw.circle(surface, self.cor, (self.x,self.y), 20)
    def movimento(self,linha,coluna):
        self.linha = linha
        self.coluna = coluna
        self.posição()