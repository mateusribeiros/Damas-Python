import pygame

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (47, 79, 47)
AMARELO = (217, 217, 25)
AZUL = (30, 144, 255)
LARANJA = (255,165,0)
AMARELO_ESVERDEADO = (153,204,50)
ROSA = (255,0,255)
AZUL_MARINHO = (112,147,219)
VERMELHO = (255,0,0)

# Inicialização do Pygame
pygame.init()

# Configuração da janela do jogo
largura_janela = 650
altura_janela = 700
tamanho_quadrado = min(int(largura_janela * 0.95) // 8, int(altura_janela * 0.95) // 8)

tamanho_janela = (largura_janela, altura_janela)
tela = pygame.display.set_mode(tamanho_janela)
pygame.display.set_caption("Jogo de Damas")

# Números das linhas e letras das colunas
numeros_linhas = ['1', '2', '3', '4', '5', '6', '7', '8']
letras_colunas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Função para obter as casas disponíveis para movimento (POSSIVEL MUDANÇA NA IMPLEMENTAÇAO DA ARVORE)
def obter_casas_disponiveis(linha, coluna):
    casa_esq = 0
    casa_dir = 0
    casas_disponiveis = []
    
    if vez_das_brancas:
        casa_esq = (linha + 1, coluna - 1)
        casa_dir = (linha + 1, coluna + 1)
    elif not vez_das_brancas:
        casa_esq = (linha - 1, coluna - 1)
        casa_dir = (linha - 1, coluna + 1)

    if casa_esq not in (pos_iniciais_brancas and pos_iniciais_pretas):
        casas_disponiveis.append(casa_esq)
    if casa_dir not in (pos_iniciais_brancas and pos_iniciais_pretas):
        casas_disponiveis.append(casa_dir)
    return casas_disponiveis

# Estado Inicial da partida
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

# Loop principal do jogo e estado do jogo
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

            texto_reinit = fonte.render("REINICIANDO...", True, LARANJA)
            ret_reinit = texto_reinit.get_rect(center=(largura_janela // 2, altura_janela // 2 )) 

            pygame.draw.rect(tela, PRETO, (0, 0, tamanho_janela[0], tamanho_janela[1]))
            tela.blit(texto_reinit, ret_reinit)

            pygame.display.flip()
            pygame.time.wait(1300)

            obter_estado_inicial()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Botão esquerdo do mouse pressionado
            if not selecionado:
                # Verifica se uma peça foi selecionada
                pos_mouse = pygame.mouse.get_pos()
                coluna = pos_mouse[0] // tamanho_quadrado
                linha = pos_mouse[1] // tamanho_quadrado
                if vez_das_brancas:
                    if (linha, coluna) in pos_iniciais_brancas:
                        selecionado = True
                        pos_selecionada = (linha, coluna)
                else:
                    if (linha, coluna) in pos_iniciais_pretas:
                        selecionado = True
                        pos_selecionada = (linha, coluna)
            else:
                # Movimenta a peça selecionada para a casa diagonalmente adjacente
                pos_mouse = pygame.mouse.get_pos()
                coluna = pos_mouse[0] // tamanho_quadrado
                linha = pos_mouse[1] // tamanho_quadrado
                casas_disponiveis = obter_casas_disponiveis(pos_selecionada[0], pos_selecionada[1])
                if (linha, coluna) in casas_disponiveis:
                    # Verifica se a casa selecionada está vazia
                    if vez_das_brancas:
                        if (linha, coluna) not in pos_iniciais_brancas:
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
                selecionado = False
                pos_selecionada = None

    if no_menu:
        # Lógica do menu
        tela.fill(PRETO)

        fonte_titulo = pygame.font.Font(None, 76)
        fonte_texto = pygame.font.Font(None, 26)
        fonte_desc = pygame.font.Font(None, 16)

        texto_titulo = fonte_titulo.render("Jogo de Damas", True, BRANCO)
        texto_novo = fonte_texto.render("NOVO JOGO (ENTER)", True, BRANCO)
        texto_reiniciar = fonte_texto.render("REINICIAR PARTIDA (R)", True, BRANCO)
        texto_salvar = fonte_texto.render("SALVAR PARTIDA (IMPLEMENTAR)", True, BRANCO)
        texto_historico = fonte_texto.render("HISTÓRICO DE PARTIDAS (IMPLEMENTAR)", True, BRANCO)
        texto_sair = fonte_texto.render("SAIR (F2)", True, BRANCO)
        texto_msg = fonte_desc.render("Durante a partida pressione ESC para retornar ao MENU", True, LARANJA)

        ret_titulo = texto_titulo.get_rect(center=(largura_janela // 2, altura_janela // 2 - 125))
        ret_novo = texto_novo.get_rect(center=(largura_janela // 2, altura_janela // 2))
        ret_reiniciar = texto_reiniciar.get_rect(center=(largura_janela // 2, altura_janela // 2 + 50))
        ret_salvar = texto_salvar.get_rect(center=(largura_janela // 2, altura_janela // 2 + 100))
        ret_historico = texto_historico.get_rect(center=(largura_janela // 2, altura_janela // 2 + 150))
        ret_sair = texto_sair.get_rect(center=(largura_janela // 2, altura_janela // 2 + 200))

        tela.blit(texto_titulo, ret_titulo)
        tela.blit(texto_novo, ret_novo)
        tela.blit(texto_reiniciar, ret_reiniciar) 
        tela.blit(texto_salvar, ret_salvar)
        tela.blit(texto_historico, ret_historico)
        tela.blit(texto_sair, ret_sair)
        tela.blit(texto_msg, (10, 680))

        # Verifica se o jogador pressionou a tecla ENTE R para iniciar o jogo
        teclas_pressionadas = pygame.key.get_pressed()
        if teclas_pressionadas[pygame.K_RETURN]:
            no_menu = False
            vez_das_brancas = True

    else:
        # Lógica do jogo e desenho do tabuleiro
        tela.fill(PRETO)

        for linha in range(8):
            for coluna in range(8):
                cor = BRANCO if (linha + coluna) % 2 == 0 else VERDE
                pygame.draw.rect(tela, cor, (coluna * tamanho_quadrado, linha * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado))

        # Desenhar números das linhas
        for i, numero in enumerate(numeros_linhas):
            fonte = pygame.font.Font(None, 36)
            texto = fonte.render(numero, True, BRANCO)
            tela.blit(texto, (largura_janela - 25, i * tamanho_quadrado + 30))

        # Desenhar letras das colunas
        for i, letra in enumerate(letras_colunas):
            fonte = pygame.font.Font(None, 36)
            texto = fonte.render(letra, True, BRANCO)
            tela.blit(texto, (i * tamanho_quadrado + 30, altura_janela - 80))

        # Desenhar peças BRANCAS
        tamanho_peca = tamanho_quadrado // 3
        for linha, coluna in pos_iniciais_brancas:
            x = (coluna * tamanho_quadrado + 40)
            y = (linha * tamanho_quadrado + 40)
            pygame.draw.circle(tela, BRANCO, (x, y), tamanho_peca)

        # Desenhar peças PRETAS
        for linha, coluna in pos_iniciais_pretas:
            x = (coluna * tamanho_quadrado + 40)
            y = (linha * tamanho_quadrado + 40)
            pygame.draw.circle(tela, PRETO, (x, y), tamanho_peca)

        # Destacar casas disponíveis para movimentação
        if selecionado and pos_selecionada:
            casas_disponiveis = obter_casas_disponiveis(pos_selecionada[0], pos_selecionada[1])
            for linha, coluna in casas_disponiveis:
                x = (coluna * tamanho_quadrado)
                y = (linha * tamanho_quadrado)
                pygame.draw.rect(tela, AMARELO, (x, y, tamanho_quadrado, tamanho_quadrado))

        if vez_das_brancas:
            fonte_vez = pygame.font.Font(None, 30)
            texto_vez = fonte_vez.render("Vez das BRANCAS!", True, LARANJA)
            tela.blit(texto_vez, (10, 10))
        else:
            fonte_vez = pygame.font.Font(None, 30)
            texto_vez = fonte_vez.render("Vez das PRETAS!", True, LARANJA)
            tela.blit(texto_vez, (10, 10))

    pygame.display.flip()

pygame.quit()

