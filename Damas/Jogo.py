import pygame
from Variaveis import preto, Tamanho, branco
from Peças import Pieces
from Tela import Tabuleiro

class Jogo:
    def __init__(self, superficie):
        self.selecionar = None
        self.tabuleiro = Tabuleiro()
        self.rodada = preto
        self.valido_mov = {}
        self.superficie = superficie

    def update(self):
        self.tabuleiro.desenhar(self.superficie)
        pygame.display.update()

    def resetar(self):
        self.selecionar = None
        self.tabuleiro = Tabuleiro()
        self.rodada = preto
        self.valido_mov = {}

    def realizar_selecao(self, linha, coluna):
        if self.selecionar:
            result = self._movimento(linha, coluna)
            if not result:
                self.selecionar = None
                self.realizar_selecao(linha, coluna)
        peca = self.tabuleiro.criar_peças(linha, coluna)
        if peca != 0 and peca.cor == self.rodada:
            self.selecionar = peca
            self.valido_mov = self.tabuleiro.pegar_validos_mov(peca)
            return True
        return False

    def _movimento(self, linha, coluna):
        peca = self.tabuleiro.pegar_peça(linha, coluna)
        if self.selecionar and peca == 0 and (linha, coluna) in self.valido_mov:
            self.tabuleiro.movimentos(self.selecionar, linha, coluna)
            self.mudar_rodada()
        else:
            return False
        return True

    def mudar_rodada(self):
        if self.rodada == preto:
            self.rodada = branco
        else:
            self.rodada = preto
