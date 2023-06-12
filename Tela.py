import pygame
pygame.init()
white=(255,255,255)
tela = pygame.display.set_mode((500,500))
pygame.display.set_caption('Jogo de damas')
coordenadasb = [(92, 28), (218, 28), (344, 28), (470, 28),(32, 92), (155, 92), (280, 92), (405, 92),(92, 156), (218, 156), (344, 156), (470, 156)]
coordenadasp = [(32, 342), (155, 342), (280, 342), (405, 342),(92, 404), (218, 404), (344, 404), (470, 404),(32, 468), (155, 468), (280, 468), (405, 468)]
while True:
    for linha in range(8):
        for coluna in range(8):
            x = coluna * 62.5
            y = linha * 62.5
            if (linha + coluna) % 2 == 0:
                pygame.draw.rect(tela, (255, 255, 255), (x, y, 62.5, 62.5))
            else:
                pygame.draw.rect(tela, (50, 50, 50), (x, y, 62.5, 62.5))
    for i in coordenadasb:
        pygame.draw.circle(tela, (255, 255, 255), (int(i[0]), int(i[1])), 20)
    for j in coordenadasp:
        pygame.draw.circle(tela, (0,0,0), (int(j[0]), int(j[1])), 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
