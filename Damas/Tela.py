import pygame
from Damas.Variaveis import branco,cinza,Linhas,Colunas,preto
from Peças import Pieces

class Tabuleiro:

    def __init__(self):
        self.tabuleiro = []
        self.criar_peças()
        #self.selecionada = None
        #self.branca.left = self.preto_left = 12
    def desenhar_tabu(self,surface):
        for linha in range(Linhas):
            for coluna in range(Colunas):
                x = coluna * 62.5
                y = linha * 62.5
                if (linha + coluna) % 2 == 0:
                    pygame.draw.rect(surface, (branco), (x, y, 62.5, 62.5))
                else:
                    pygame.draw.rect(surface, (cinza), (x, y, 62.5, 62.5))
    def criar_peças(self):
        for linha in range(Linhas):
            self.tabuleiro.append([])
            for coluna in range (Colunas):
                if coluna % 2 == ((linha+1) % 2):
                    if linha < 3:
                        self.tabuleiro[linha].append(Pieces(linha,coluna,branco))
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
    def movimentos(self,peça,linha,coluna):
        self.tabuleiro[peça.linha][peça.coluna],self.tabuleiro[linha][coluna] = self.tabuleiro[peça.linha][peça.coluna], self.tabuleiro[linha][coluna]
        peça.movimento(linha,coluna)
    def pegar_peça(self,linha,coluna):
        return self.tabuleiro[linha][coluna]