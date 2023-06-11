import pygame

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (47,79,47)

# Inicialização do Pygame
pygame.init()

# Configuração da janela do jogo
largura_janela = 650
altura_janela = 650
tamanho_quadrado = min(int(largura_janela * 0.95)  // 8, int(altura_janela  * 0.95)// 8)

tamanho_janela = (largura_janela, altura_janela)
tela = pygame.display.set_mode(tamanho_janela)
pygame.display.set_caption("Jogo de Damas")

# Números das linhas e letras das colunas
numeros_linhas = ['1', '2', '3', '4', '5', '6', '7', '8']
letras_colunas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Posições Iniciais das Peças de damas
pos_iniciais_brancas = [
    (0,1), (0,3), (0,5), (0,7),
    (1,0), (1,2), (1,4), (1,6),
    (2,1), (2,3), (2,5), (2,7),
]

pos_iniciais_pretas = [
    (5,0), (5,2), (5,4), (5,6),
    (6,1), (6,3), (6,5), (6,7),
    (7,0), (7,2), (7,4), (7,6),
]

# Loop principal do jogo e estado do jogo
no_menu = True
executando = True
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F2):
            executando = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            no_menu = True

    if no_menu:
        # Lógica do menu
        tela.fill(PRETO)

        fonte_titulo = pygame.font.Font(None, 48)
        fonte_texto = pygame.font.Font(None, 26)

        texto_titulo = fonte_titulo.render("Jogo de Damas", True, BRANCO)
        texto_novo = fonte_texto.render("NOVO JOGO (ENTER)", True, BRANCO)
        texto_salvar = fonte_texto.render("SALVAR PARTIDA (IMPLEMENTAR)", True, BRANCO)
        texto_historico = fonte_texto.render("HISTÓRICO DE PARTIDAS (IMPLEMENTAR)", True, BRANCO)
        texto_sair = fonte_texto.render("SAIR (F2)", True, BRANCO)

        ret_titulo = texto_titulo.get_rect(center=(largura_janela // 2, altura_janela // 2 - 50))
        ret_novo = texto_novo.get_rect(center=(largura_janela // 2, altura_janela // 2))
        ret_salvar = texto_salvar.get_rect(center=(largura_janela // 2, altura_janela // 2 + 50))
        ret_historico = texto_historico.get_rect(center=(largura_janela // 2, altura_janela // 2 + 100))
        ret_sair = texto_sair.get_rect(center=(largura_janela // 2, altura_janela // 2 + 150))

        tela.blit(texto_titulo, ret_titulo)
        tela.blit(texto_novo, ret_novo)
        tela.blit(texto_salvar, ret_salvar)
        tela.blit(texto_historico, ret_historico)
        tela.blit(texto_sair, ret_sair)

        # Verifica se o jogador pressionou a tecla ENTER para iniciar o jogo
        teclas_pressionadas = pygame.key.get_pressed()
        if teclas_pressionadas[pygame.K_RETURN]:
            no_menu = False

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
            tela.blit(texto, (i * tamanho_quadrado + 30 , altura_janela - 25))

        # Desenhaar peças BRANCAS
        tamanho_peca = tamanho_quadrado // 3
        for linha, coluna in pos_iniciais_brancas:
            x = (coluna * tamanho_quadrado + 40)
            y = (linha * tamanho_quadrado + 40)
            pygame.draw.circle(tela, BRANCO, (x,y), tamanho_peca)
        
        # Desenhaar peças BRANCAS
        for linha, coluna in pos_iniciais_pretas:
            x = (coluna * tamanho_quadrado + 40)
            y = (linha * tamanho_quadrado + 40)
            pygame.draw.circle(tela, PRETO, (x,y), tamanho_peca)
        
        

    # Atualização da tela
    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()
