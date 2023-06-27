import pygame
from Variaveis import preto, Tamanho, branco
from Peças import Pieces
from Tela import Tabuleiro

class Jogo:
    def __init__(self, superficie):
        self.selecionado = None
        self.tabuleiro = Tabuleiro()
        self.rodada = preto
        self.valido_mov = {}
        self.superficie = superficie

    def update(self):
        self.tabuleiro.desenhar(self.superficie)
        self.desenhar_ajuda(self.valido_mov)
        pygame.display.update()

    def resetar(self):
        self.selecionado = None
        self.tabuleiro = Tabuleiro()
        self.rodada = preto
        self.valido_mov = {}
    def ganhador(self):
        return self.tabuleiro.ganhador()
    def selecionar(self, linha, coluna):
        if self.selecionado:
            resultado = self._movimento(linha, coluna)
            if not resultado:
                self.selecionado = None
                self.selecionar(linha, coluna)
        peca = self.tabuleiro.pegar_peca(linha, coluna)
        if peca != 0 and peca.cor == self.rodada:
            self.selecionado = peca
            self.valido_mov = self.tabuleiro.pegar_movimento_validos(peca)
            return True
        return False

    def _movimento(self, linha, coluna):
        peca = self.tabuleiro.pegar_peca(linha, coluna)
        if self.selecionado and peca == 0 and (linha, coluna) in self.valido_mov:
            self.tabuleiro.mov(self.selecionado, linha, coluna)
            passar = self.valido_mov[(linha, coluna)]
            if passar:
                self.tabuleiro.remover(passar)
            self.mudar_rodada()
        else:
            return False
        return True
    def mudar_rodada(self):
        self.valido_mov = {}
        if self.rodada == preto:
            self.rodada = branco
        else:
            self.rodada = preto
    def pegar_tabuleiro(self):
        return self.tabuleiro
    def movimento_ia(self,tabuleiro):
        self.tabuleiro = tabuleiro
        self.mudar_rodada()
    def desenhar_ajuda(self, movimentos):
        for i in movimentos:
            linha, coluna = i
            pygame.draw.circle(self.superficie, (0,255,0),(coluna * Tamanho + Tamanho // 2, linha * Tamanho + Tamanho // 2), 10)