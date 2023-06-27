import pygame
from Variaveis import preto,Tamanho,branco #UFG

class Pieces:

    def __init__(self,linha,coluna,cor):
        self.linha = linha
        self.coluna = coluna
        self.cor = cor
        self.x = 0
        self.y = 0
        self.posição()
        self.king = False
    def fazer_ling(self):
        self.king = True
    def posição(self):
        self.x = Tamanho * self.coluna + Tamanho//2
        self.y = Tamanho * self.linha + Tamanho // 2
    def desenhar(self,surface):
        pygame.draw.circle(surface, self.cor, (self.x,self.y), 30)
        pygame.draw.circle(surface, self.cor, (self.x,self.y), 30)
        if self.king:
            surface.blit(UFG,(self.x - UFG.get_width()//2, self.y - UFG.get_height()//2))
    def mov(self,linha,coluna):
        self.linha = linha
        self.coluna = coluna
        self.posição()