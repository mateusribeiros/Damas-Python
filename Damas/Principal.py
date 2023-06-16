import pygame
from Variaveis import largura, altura, Tamanho, branco, preto
from Peças import Pieces
from Tela import Tabuleiro
from Jogo import Jogo

pygame.init()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo de damas')
clock = pygame.time.Clock()

TEXTO = "ISABELA SUA GOSTOSA!"

def mouse(pos):
    x, y = pos
    linha = y // Tamanho
    coluna = x // Tamanho
    return linha, coluna

def main():
    tabuleiro = Tabuleiro()
    jogo = Jogo(tela)

    texto_impresso = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                linha, coluna = mouse(pos)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                if not texto_impresso:
                    font = pygame.font.Font(None, 50)
                    texto = font.render(TEXTO, True, branco)
                    ret_texto = texto.get_rect(center=(largura // 2, altura // 2))
                    tamanho_janela = (largura, altura)

                    pygame.draw.rect(tela, preto, (0, 0, tamanho_janela[0], tamanho_janela[1]))
                    tela.blit(texto, ret_texto)

                    pygame.display.flip()
                    pygame.time.wait(3000)

                    texto_impresso = True
                else:
                    texto_impresso = False

        jogo.update()
        clock.tick(30)

main()
