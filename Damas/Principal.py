import time
from Variaveis import largura, altura, Tamanho, branco, preto, LARANJA
from Peças import Pieces
from Tela import Tabuleiro
import pygame
from Jogo import Jogo
from IA import IA

pygame.init()
tela = pygame.display.set_mode((largura + 180, altura))
pygame.display.set_caption('Jogo de damas')
clock = pygame.time.Clock()


def mouse(pos):
    x, y = pos
    linha = y // Tamanho
    coluna = x // Tamanho
    return linha, coluna


tabuleiro = Tabuleiro()
jogo = Jogo(tela)
jogo_pausado = False

def obter_estado_inicial():
    global pos_iniciais_brancas, pos_iniciais_pretas, vez_pretas

    pos_iniciais_brancas = [
        (0, 1), (0, 3), (0, 5), (0, 7),
        (1, 0), (1, 2), (1, 4), (1, 6),
        (2, 1), (2, 3), (2, 5), (2, 7),
    ]

    pos_iniciais_pretas = [
        (5, 0), (5, 2), (5, 4), (5, 6),
        (6, 1), (6, 3), (6, 5), (6, 7),
        (7, 0), (7, 2), (7, 4), (7, 6),
    ]

    vez_pretas = True


obter_estado_inicial()
no_menu = True
executando = True

while executando:

    if jogo.rodada == branco and not jogo_pausado:
        valor, novo_tabuleiro = IA().minimax(jogo.pegar_tabuleiro(), 3, branco,jogo)
        jogo.movimento_ia(novo_tabuleiro)
        vez_pretas = False
    if jogo.rodada == preto and not jogo_pausado:
        vez_pretas = True
    if jogo.ganhador() is not None:
        print(jogo.ganhador())
        executando = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F2):
            executando = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            jogo_pausado = not jogo_pausado
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            tabuleiro.salvar_jogo(novo_tabuleiro)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            tabuleiro.carregar_jogo_salvo(jogo)

    if no_menu:
        imagem = pygame.image.load("../Imagem/chessboard.jpg")
        imagem_redimensionada = pygame.transform.scale(imagem, (1000, 800))
        tela.blit(imagem_redimensionada, (0, 0))

        fonte_titulo = pygame.font.Font(None, 86)
        fonte_texto = pygame.font.Font(None, 35)

        texto_titulo = fonte_titulo.render("JOGO DE DAMAS", True, branco)
        texto_novo = fonte_texto.render("NOVO JOGO (ENTER)", True, branco)
        texto_salvar = fonte_texto.render("SALVAR PARTIDA (S)", True, branco)
        texto_buscar = fonte_texto.render("BUSCAR SALVAMENTO (B)", True, branco)
        texto_sair = fonte_texto.render("SAIR (F2)", True, branco)

        ret_titulo = texto_titulo.get_rect(center=(largura // 1.65, altura // 2 - 100))
        ret_novo = texto_novo.get_rect(center=(largura // 1.70, altura // 2))
        ret_salvar = texto_salvar.get_rect(center=(largura // 1.70, altura // 2 + 40))
        ret_buscar = texto_buscar.get_rect(center=(largura // 1.70, altura // 2 + 80))
        ret_sair = texto_sair.get_rect(center=(largura // 1.70, altura // 2 + 120))

        tela.blit(texto_titulo, ret_titulo)
        tela.blit(texto_novo, ret_novo)
        tela.blit(texto_salvar, ret_salvar)
        tela.blit(texto_buscar, ret_buscar)
        tela.blit(texto_sair, ret_sair)

        teclas_pressionadas = pygame.key.get_pressed()
        if teclas_pressionadas[pygame.K_RETURN]:
            no_menu = False
    else:
        if not jogo_pausado:
            tela.fill(preto)
            tabuleiro.desenhar_quadrados(tela)
            tabuleiro.desenhar(tela)
            jogo.update()

    if not tabuleiro.jogo_encerrado:
        if jogo.ganhador() is not None:
            resultado = jogo.ganhador()
            tela.fill(preto)
            fonte_msg = pygame.font.Font(None, 80)
            texto_msg = fonte_msg.render(resultado, True, branco)
            ret_msg = texto_msg.get_rect(center=(largura // 2, altura // 2 - 125))
            tela.blit(texto_msg, ret_msg)
            no_menu = True
    if event.type == pygame.MOUSEBUTTONDOWN and not jogo_pausado:
        pos = pygame.mouse.get_pos()
        linha, coluna = mouse(pos)
        jogo.selecionar(linha, coluna)
    if jogo_pausado and not no_menu:
        fonte_texto = pygame.font.Font(None, 100)
        texto_ps = fonte_texto.render("PAUSADO", True, LARANJA)
        ret_ps = texto_ps.get_rect(center=(largura // 2, altura // 2))
        tela.blit(texto_ps, ret_ps)

    pygame.display.flip()
    clock.tick(30)
time.sleep(5)
pygame.quit()
