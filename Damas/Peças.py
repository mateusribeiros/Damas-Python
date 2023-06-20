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
    def movimento(self,linha,coluna):
        self.linha = linha
        self.coluna = coluna
        self.posição()
    def ajuda(self,surface):
        if selecionado and pos_selecionada:
            casas_disponiveis = obter_casas_disponiveis(pos_selecionada[0], pos_selecionada[1])
            for linha, coluna in casas_disponiveis:
                x = (coluna * tamanho_quadrado)
                y = (linha * tamanho_quadrado)
                pygame.draw.circle(surface,(0,0,255),(self.x,self.y),10)