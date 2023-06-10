import pygame

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (47,79,47)

# Inicialização do Pygame
pygame.init()

# Configuração da janela do jogo
largura_janela = 900
altura_janela = 650
tamanho_quadrado = largura_janela // 12

# Números e Letras das casas
numeros_linhas = ['1', '2', '3', '4', '5', '6', '7', '8']
letras_colunas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

tamanho_janela = (largura_janela, altura_janela)
tela = pygame.display.set_mode(tamanho_janela)
pygame.display.set_caption("Jogo de Damas")

# Loop principal do jogo
executando = True
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F2):
            executando = False

    # Lógica do jogo e desenho do tabuleiro
    tela.fill(PRETO)

    for linha in range(8):
        for coluna in range(8):
            cor = BRANCO if (linha + coluna) % 2 == 0 else VERDE
            pygame.draw.rect(tela, cor, (coluna * tamanho_quadrado, linha * tamanho_quadrado, tamanho_quadrado, tamanho_quadrado))

    # Desenhar número de linhas
    for i, numero in enumerate(numeros_linhas):
        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(numero, True, BRANCO)
        tela.blit(texto, (largura_janela - 295, i * tamanho_quadrado + tamanho_quadrado // 2))

    # Desenhar letras das colunas
    for i, letra  in enumerate(letras_colunas):
        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(letra, True, BRANCO)
        tela.blit(texto, (i * tamanho_quadrado + tamanho_quadrado // 2, altura_janela - 40))
    # Atualização da tela
    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()
