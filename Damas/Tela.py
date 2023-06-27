import pygame
from Variaveis import branco, cinza, Linhas, Colunas, preto,Tamanho
from Peças import Pieces

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = []
        self.criar_tela()
        self.preto_esquerda = self.branco_esquerda = 12
    def desenhar_quadrados(self, surface):
        for linha in range(Linhas):
            for coluna in range(Colunas):
                x = coluna * Tamanho
                y = linha * Tamanho
                if (linha + coluna) % 2 == 0:
                    pygame.draw.rect(surface, branco, (x, y, Tamanho, Tamanho))
                else:
                    pygame.draw.rect(surface, cinza, (x, y, Tamanho, Tamanho))

    def criar_tela(self):
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
        self.desenhar_quadrados(surface)
        for linha in range(Linhas):
            for coluna in range(Colunas):
                peca = self.tabuleiro[linha][coluna]
                if peca != 0:
                    peca.desenhar(surface)

    def mov(self, peca, linha, coluna):
        self.tabuleiro[peca.linha][peca.coluna], self.tabuleiro[linha][coluna] = self.tabuleiro[linha][coluna], self.tabuleiro[peca.linha][peca.coluna]
        peca.mov(linha, coluna)

    def pegar_peca(self, linha, coluna):
        return self.tabuleiro[linha][coluna]

    def remover(self, pecas):
        for peca in pecas:
            self.tabuleiro[peca.linha][peca.coluna] = 0
            if peca != 0:
                if peca.cor == preto:
                    self.preto_esquerda -= 1
                else:
                    self.branco_esquerda -= 1

    def ganhador(self):
        if self.preto_esquerda <= 0:
            return "VITORIA DO BRANCO"
        elif self.branco_esquerda <= 0:
            return "VITORIA DO PRETO"

        return None

    def pegar_movimento_validos(self, peca):
        movim = {}
        esquerda = peca.coluna - 1
        direita = peca.coluna + 1
        linha = peca.linha

        if peca.cor == preto:
            movim.update(self._transversal_esquerda(linha - 1, max(linha - 3, -1), -1, peca.cor, esquerda))
            movim.update(self._transversal_direita(linha - 1, max(linha - 3, -1), -1, peca.cor, direita))
        if peca.cor == branco:
            movim.update(self._transversal_esquerda(linha + 1, min(linha + 3, Linhas), 1, peca.cor, esquerda))
            movim.update(self._transversal_direita(linha + 1, min(linha + 3, Linhas), 1, peca.cor, direita))

        return movim

    def _transversal_esquerda(self, start, stop, step, cor, esquerda, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if esquerda < 0:
                break

            current = self.tabuleiro[r][esquerda]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, esquerda)] = last + skipped
                else:
                    moves[(r, esquerda)] = last

                if last:
                    if step == -1:
                        linha = max(r - 3, 0)
                    else:
                        linha = min(r + 3, Linhas)
                    moves.update(self._transversal_esquerda(r + step, linha, step, cor, esquerda - 1, skipped=last))
                    moves.update(self._transversal_direita(r + step, linha, step, cor, esquerda + 1, skipped=last))
                break
            elif current.cor == cor:
                break
            else:
                last = [current]

            esquerda -= 1

        return moves

    def _transversal_direita(self, start, stop, step, cor, direita, skipped=[]):
        movim = {}
        last = []
        for r in range(start, stop, step):
            if direita >= Colunas:
                break

            current = self.tabuleiro[r][direita]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    movim[(r, direita)] = last + skipped
                else:
                    movim[(r, direita)] = last

                if last:
                    if step == -1:
                        linha = max(r - 3, 0)
                    else:
                        linha = min(r + 3, Linhas)
                    movim.update(self._transversal_esquerda(r + step, linha, step, cor, direita - 1, skipped=last))
                    movim.update(self._transversal_direita(r + step, linha, step, cor, direita + 1, skipped=last))
                break
            elif current.cor == cor:
                break
            else:
                last = [current]

            direita += 1

        return movim
    def avaliar(self):
        return self.branco_esquerda - self.preto_esquerda
    def contar_pecas(self, cor):
        pecas = []
        for linha in self.tabuleiro:
            for peca in linha:
                if peca != 0 and peca.cor == cor:
                    pecas.append(peca)
        return pecas