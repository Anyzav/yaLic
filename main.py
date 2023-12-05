import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 650))
screen.fill((0, 0, 0))
pygame.display.set_caption("Game")
pygame.draw.rect(screen, (237, 145, 47), (13, 12, 462, 23))  # оранжевый квадрат слева
a = pygame.draw.rect(screen, (224, 56, 73), (13, 42, 462, 183), 2)  # красная сетка слева
pygame.draw.line(screen, (224, 56, 73), [121, 42], [121, 225], 2)
pygame.draw.line(screen, (224, 56, 73), [242, 42], [242, 225], 2)
pygame.draw.line(screen, (224, 56, 73), [363, 42], [363, 225], 2)
pygame.draw.rect(screen, (137, 224, 56), (13, 228, 462, 181), 2)  # зелёная сетка слева
pygame.draw.line(screen, (137, 224, 56), [121, 228], [121, 408], 2)
pygame.draw.line(screen, (137, 224, 56), [242, 228], [242, 408], 2)
pygame.draw.line(screen, (137, 224, 56), [363, 228], [363, 408], 2)
b = int(input())
if b == 0:
    a = 0
clock = pygame.time.Clock()
pygame.display.update()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
