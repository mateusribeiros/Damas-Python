import pygame
from Variaveis import branco, Linhas, Colunas, preto,Tamanho, largura, laranja, MARROM, BRANCO, CINZA, LARANJA
from Peças import Pieces
import time

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = []
        self.criar_tela()
        self.preto_esquerda = self.branco_esquerda = 12
        self.jogo_encerrado = False
        self.preto_kings = self.branco_kings = 0

    def desenhar_quadrados(self, surface):
        for linha in range(Linhas):
            for coluna in range(Colunas):
                x = coluna * Tamanho
                y = linha * Tamanho
                if (linha + coluna) % 2 == 0:
                    pygame.draw.rect(surface, MARROM, (x, y, Tamanho, Tamanho))
                else:
                    pygame.draw.rect(surface, BRANCO, (x, y, Tamanho, Tamanho))

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

        fonte_texto = pygame.font.Font(None, 48)
        texto_ps = fonte_texto.render("PRETAS", True, CINZA)
        ret_ps = pygame.draw.rect(surface, preto, (largura, 0, Tamanho * 3, Tamanho))
        text_rect = texto_ps.get_rect(center=ret_ps.center)

        # Adicionando botão
        botao_rect = pygame.draw.rect(surface, MARROM, (largura, 0,  Tamanho * 3, 800))
        surface.blit(texto_ps, text_rect)

        pretas = 12 - len(self.contar_pecas(preto))
        brancas = 12 - len(self.contar_pecas(branco))

        fonte = pygame.font.Font(None, 25)
        fonteCapture = pygame.font.Font(None, 20)

        textoF = fonteCapture.render("PRETAS CAPTURADAS", True, CINZA)
        retanguloF = pygame.draw.rect(surface, MARROM, (largura, 150, Tamanho * 3, Tamanho))
        posF = textoF.get_rect(center=retanguloF.center)

        textoP = fonte_texto.render(str(pretas), True, CINZA)
        retanguloP = pygame.draw.rect(surface, MARROM, (largura, 180, Tamanho * 3, Tamanho))
        posP = textoP.get_rect(center=retanguloP.center)

        textoT = fonteCapture.render("BRANCAS CAPTURADAS", True, CINZA)
        retanguloT = pygame.draw.rect(surface, MARROM, (largura, 300, Tamanho * 3, Tamanho))
        posT = textoT.get_rect(center=retanguloT.center)

        textoB = fonte_texto.render(str(brancas), True, CINZA)
        retanguloB = pygame.draw.rect(surface, MARROM, (largura, 325, Tamanho * 3, Tamanho))
        posB = textoB.get_rect(center=retanguloB.center)

        textoPa = fonte.render("PAUSE(ESC)", True, LARANJA)
        retanguloPa = pygame.draw.rect(surface, MARROM, (largura, 650, Tamanho * 3, Tamanho))
        posPa = textoPa.get_rect(center=retanguloPa.center)

        textoS = fonte.render("SALVAR(S)", True, LARANJA)
        retanguloS = pygame.draw.rect(surface, MARROM, (largura, 700, Tamanho * 3, Tamanho))
        posS = textoS.get_rect(center=retanguloS.center)

        surface.blit(textoPa, posPa)
        surface.blit(textoS, posS)
        surface.blit(textoT, posT)
        surface.blit(textoF, posF)
        surface.blit(textoP, posP)
        surface.blit(textoB, posB)

        surface.blit(texto_ps, text_rect)

    def mov(self, peca, linha, coluna):
        self.tabuleiro[peca.linha][peca.coluna], self.tabuleiro[linha][coluna] = self.tabuleiro[linha][coluna], self.tabuleiro[peca.linha][peca.coluna]
        peca.mov(linha, coluna)
        if linha == Linhas - 1 or linha == 0:
            peca.fazer_king()
            if peca.cor == branco:
                self.branco_kings += 1
            else:
                self.preto_kings += 1

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
        if self.preto_esquerda <= 0 or self.branco_esquerda <= 0:
            self.jogo_encerrado = True
            return "     VITÓRIA DOS BRANCOS!" if self.preto_esquerda <= 0 else "VITÓRIA DOS PRETOS"
        elif len(self.contar_pecas(branco)) == 0:
            time.sleep(10)
            return "     VITÓRIA DOS PRETOS"
            self.jogo_encerrado = True
        elif len(self.contar_pecas(preto)) == 0:
            time.sleep(10)
            return "     VITÓRIA DOS BRANCOS"
            self.jogo_encerrado = True
        else:
            movimentos_possiveis = False
            for linha in self.tabuleiro:
                for peca in linha:
                    if peca != 0 and peca.cor == branco:
                        movimentos = self.pegar_movimento_validos(peca)
                        if len(movimentos) > 0:
                            movimentos_possiveis = True
                            break
                if movimentos_possiveis:
                    break
            if not movimentos_possiveis:
                return "EMPATE - NÃO HÁ MAIS MOVIMENTOS POSSÍVEIS"
                time.sleep(10)
                self.jogo_encerrado = True
            else:
                return None

    def pegar_movimento_validos(self, peca):
        movim = {}
        esquerda = peca.coluna - 1
        direita = peca.coluna + 1
        linha = peca.linha

        if peca.cor == preto or peca.king:
            movim.update(self._transversal_esquerda(linha - 1, max(linha - 3, -1), -1, peca.cor, esquerda))
            movim.update(self._transversal_direita(linha - 1, max(linha - 3, -1), -1, peca.cor, direita))
        if peca.cor == branco or peca.king:
            movim.update(self._transversal_esquerda(linha + 1, min(linha + 3, Linhas), 1, peca.cor, esquerda))
            movim.update(self._transversal_direita(linha + 1, min(linha + 3, Linhas), 1, peca.cor, direita))

        return movim

    def _transversal_esquerda(self, start, stop, step, cor, esquerda, skipped=[]):
        moves = {}
        last = []
        for i in range(start, stop, step):
            if esquerda < 0:
                break

            current = self.tabuleiro[i][esquerda]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(i, esquerda)] = last + skipped
                else:
                    moves[(i, esquerda)] = last

                if last:
                    if step == -1:
                        linha = max(i - 3, 0)
                    else:
                        linha = min(i + 3, Linhas)
                    moves.update(self._transversal_esquerda(i + step, linha, step, cor, esquerda - 1, skipped=last))
                    moves.update(self._transversal_direita(i + step, linha, step, cor, esquerda + 1, skipped=last))
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
        for i in range(start, stop, step):
            if direita >= Colunas:
                break

            current = self.tabuleiro[i][direita]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    movim[(i, direita)] = last + skipped
                else:
                    movim[(i, direita)] = last

                if last:
                    if step == -1:
                        linha = max(i - 3, 0)
                    else:
                        linha = min(i + 3, Linhas)
                    movim.update(self._transversal_esquerda(i + step, linha, step, cor, direita - 1, skipped=last))
                    movim.update(self._transversal_direita(i + step, linha, step, cor, direita + 1, skipped=last))
                break
            elif current.cor == cor:
                break
            else:
                last = [current]

            direita += 1

        return movim
    def avaliar(self):
        return self.branco_esquerda - self.preto_esquerda + (self.branco_kings * 0.5 - (self.preto_kings * 0.5))
    
    def contar_pecas(self, cor):
        pecas = []
        for linha in self.tabuleiro:
            for peca in linha:
                if peca != 0 and peca.cor == cor:
                    pecas.append(peca)
        return pecas