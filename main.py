import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 650))
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Game")
    pygame.draw.rect(screen, (230, 230, 250), (13, 12, 462, 23))  # имя, уровень, выйти из аккаунта
    pygame.draw.rect(screen, (220, 20, 60), (13, 42, 462, 183), 2)  # враги
    pygame.draw.line(screen, (220, 20, 60), [121, 42], [121, 224], 2)
    pygame.draw.line(screen, (220, 20, 60), [242, 42], [242, 224], 2)
    pygame.draw.line(screen, (220, 20, 60), [363, 42], [363, 224], 2)
    pygame.draw.rect(screen, (148, 0, 211), (13, 228, 462, 181), 2)  # выбор персонажа
    pygame.draw.line(screen, (148, 0, 211), [121, 228], [121, 408], 2)
    pygame.draw.line(screen, (148, 0, 211), [242, 228], [242, 408], 2)
    pygame.draw.line(screen, (148, 0, 211), [363, 228], [363, 408], 2)
    pygame.draw.rect(screen, (72, 61, 139), (13, 415, 462, 226), 2)  # описание персонажа
    pygame.draw.rect(screen, (139, 0, 0), (482, 12, 787, 398), 2)  # поле боя
    pygame.draw.rect(screen, (75, 0, 130), (482, 419, 571, 219), 2)  # корзинка
    pygame.draw.rect(screen, (75, 0, 130), (1063, 457, 60, 51), 2)  # набор очков атаки
    pygame.draw.circle(screen, (244, 164, 96), (1199, 485), 63, 2)  # магазин
    pygame.draw.rect(screen, (255, 215, 0), (1063, 564, 207, 43), 2)

    sc = pygame.image.load('сцена.png')
    screen.blit(sc, (484, 14))

    clock = pygame.time.Clock()
    pygame.display.update()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
