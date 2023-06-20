import pygame
from Variaveis import largura, altura, Tamanho, branco, preto
from Peças import Pieces
from Tela import Tabuleiro
from Jogo import Jogo

pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo de damas')
clock = pygame.time.Clock()

def mouse(pos):
    x, y = pos
    linha = y // Tamanho
    coluna = x // Tamanho
    return linha, coluna


def obter_casas_disponiveis(linha, coluna):
    casas_disponiveis = []

    if vez_das_brancas:
        casa_esq = (linha + 1, coluna - 1)
        casa_dir = (linha + 1, coluna + 1)
    else:
        casa_esq = (linha - 1, coluna - 1)
        casa_dir = (linha - 1, coluna + 1)

    if casa_esq not in (pos_iniciais_brancas + pos_iniciais_pretas):
        casas_disponiveis.append(casa_esq)
    if casa_dir not in (pos_iniciais_brancas + pos_iniciais_pretas):
        casas_disponiveis.append(casa_dir)

    if casas_disponiveis:  # Verifica se há casas disponíveis
        return casas_disponiveis
    else:
        return None

def obter_estado_inicial():
    global pos_iniciais_brancas, pos_iniciais_pretas, selecionado, pos_selecionada, vez_das_brancas

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

    selecionado = False
    pos_selecionada = None
    vez_das_brancas = True

def main():
    selecionado = False
    vez_das_brancas = True
    tabuleiro = Tabuleiro()
    jogo = Jogo(tela)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F2):
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                no_menu = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                fonte = pygame.font.Font(None, 80)
                texto_reinit = fonte.render("REINICIANDO...", True, branco)
                ret_reinit = texto_reinit.get_rect(center=(largura // 2, altura // 2 ))
                pygame.draw.rect(tela, preto, (0, 0, largura, altura))
                tela.blit(texto_reinit, ret_reinit)
                pygame.display.flip()
                pygame.time.wait(1300)
                obter_estado_inicial()


            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botão esquerdo do mouse pressionado

                if not selecionado:

                    # Verifica se uma peça foi selecionada

                    pos_mouse = pygame.mouse.get_pos()

                    coluna = pos_mouse[0] // Tamanho

                    linha = pos_mouse[1] // Tamanho

                    if vez_das_brancas:

                        if (linha, coluna) in pos_iniciais_brancas:
                            selecionado = True

                            pos_selecionada = (linha, coluna)  # Atribui pos_selecionada aqui

                    else:

                        if (linha, coluna) in pos_iniciais_pretas:
                            selecionado = True

                            pos_selecionada = (linha, coluna)  # Atribui pos_selecionada aqui

                else:

                    # Movimenta a peça selecionada para a casa diagonalmente adjacente

                    pos_mouse = pygame.mouse.get_pos()

                    coluna = pos_mouse[0] // Tamanho

                    linha = pos_mouse[1] // Tamanho

                    if selecionado:  # Verifica se uma peça está selecionada

                        casas_disponiveis = obter_casas_disponiveis(pos_selecionada[0], pos_selecionada[1])

                        if casas_disponiveis is not None:

                            if (linha, coluna) in casas_disponiveis:
                                # Atualiza a posição da peça para a nova casa
                                pos_iniciais_brancas.remove(pos_selecionada)
                                pos_iniciais_brancas.append((linha, coluna))
                                vez_das_brancas = False
                        else:
                            if (linha, coluna) not in pos_iniciais_pretas:
                                # Atualiza a posição da peça para a nova casa
                                pos_iniciais_pretas.remove(pos_selecionada)
                                pos_iniciais_pretas.append((linha, coluna))
                                vez_das_brancas = True
                    pos_selecionada = None

        jogo.update()
        clock.tick(30)

obter_estado_inicial()
no_menu = True
executando = True
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F2):
            executando = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            no_menu = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            fonte = pygame.font.Font(None, 80)

            texto_reinit = fonte.render("REINICIANDO...", True, branco)
            ret_reinit = texto_reinit.get_rect(center=(largura // 2, altura // 2 ))

            pygame.draw.rect(tela, preto, (0, 0, (largura,altura)[0], (largura,altura)[1]))
            tela.blit(texto_reinit, ret_reinit)

            pygame.display.flip()
            pygame.time.wait(1300)

            obter_estado_inicial()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            no_menu = False
            obter_estado_inicial()
            main()

    if no_menu:
        # Lógica do menu
        tela.fill(preto)

        fonte_titulo = pygame.font.Font(None, 76)
        fonte_texto = pygame.font.Font(None, 26)
        fonte_desc = pygame.font.Font(None, 16)

        texto_titulo = fonte_titulo.render("Jogo de Damas", True, branco)
        texto_novo = fonte_texto.render("NOVO JOGO (ENTER)", True, branco)
        texto_reiniciar = fonte_texto.render("REINICIAR PARTIDA (R)", True, branco)
        texto_salvar = fonte_texto.render("SALVAR PARTIDA (IMPLEMENTAR)", True, branco)
        texto_historico = fonte_texto.render("HISTÓRICO DE PARTIDAS (IMPLEMENTAR)", True, branco)
        texto_sair = fonte_texto.render("SAIR (F2)", True, branco)
        texto_msg = fonte_desc.render("Durante a partida pressione ESC para retornar ao MENU", True, preto)

        ret_titulo = texto_titulo.get_rect(center=(largura // 2, altura // 2 - 125))
        ret_novo = texto_novo.get_rect(center=(largura // 2, altura // 2))
        ret_reiniciar = texto_reiniciar.get_rect(center=(largura // 2, altura // 2 + 50))
        ret_salvar = texto_salvar.get_rect(center=(largura // 2, altura // 2 + 100))
        ret_historico = texto_historico.get_rect(center=(largura // 2, altura // 2 + 150))
        ret_sair = texto_sair.get_rect(center=(largura // 2, altura // 2 + 200))

        tela.blit(texto_titulo, ret_titulo)
        tela.blit(texto_novo, ret_novo)
        tela.blit(texto_reiniciar, ret_reiniciar)
        tela.blit(texto_salvar, ret_salvar)
        tela.blit(texto_historico, ret_historico)
        tela.blit(texto_sair, ret_sair)
        tela.blit(texto_msg, (10, 680))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
