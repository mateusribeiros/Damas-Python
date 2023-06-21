import pygame
from Variaveis import preto,Tamanho,branco

class Pieces:

    def __init__(self,linha,coluna,cor):
        self.linha = linha
        self.coluna = coluna
        self.cor = cor
        self.x = 0
        self.y = 0
        self.posição()
    def posição(self):
        self.x = Tamanho * self.coluna + Tamanho//2
        self.y = Tamanho * self.linha + Tamanho // 2
    def desenhar(self,surface):
        pygame.draw.circle(surface, self.cor, (self.x,self.y), 30)
        pygame.draw.circle(surface, self.cor, (self.x,self.y), 30)
    def mov(self,linha,coluna):
        self.linha = linha
        self.coluna = coluna
        self.posição()