import os
import sys
import random
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
    screen.blit(sc, (484, 14))  # отрисовка поля боя

    characters_of_choice = [pygame.image.load('перс1/1.png'), pygame.image.load('перс2/1.png'),
                            pygame.image.load('перс3/1.png'), pygame.image.load('перс4/1.png'),
                            pygame.image.load('перс5/1.png'), pygame.image.load('перс6/1.png'),
                            pygame.image.load('перс7/1.png'), pygame.image.load('перс8/1.png')]  # список персонажей

    characters_of_choice_1 = [pygame.image.load('перс1/2.png'), pygame.image.load('перс2/2.png'),
                            pygame.image.load('перс3/2.png'), pygame.image.load('перс4/2.png'),
                            pygame.image.load('перс5/2.png'), pygame.image.load('перс6/2.png'),
                            pygame.image.load('перс7/2.png'), pygame.image.load('перс8/2.png')]

    enemies_of_choice = [pygame.image.load('злодей1/1.png'), pygame.image.load('злодей2/1.png'),
                         pygame.image.load('злодей3/1.png'), pygame.image.load('злодей4/1.png')]  # список врагов

    to_attack = [pygame.image.load('перс1/для атаки/1.png'), pygame.image.load('перс2/для атаки/1.png'),
                 pygame.image.load('перс3/для атаки/1.png'), pygame.image.load('перс4/для атаки/1.png'),
                 pygame.image.load('перс5/для атаки/1.png'), pygame.image.load('перс6/для атаки/1.png'),
                 pygame.image.load('перс7/для атаки/1.png'), pygame.image.load('перс8/для атаки/1.png')]

    attack_1 = [pygame.image.load('перс1/для атаки/1.png'), pygame.image.load('перс1/для атаки/2.png'),
                pygame.image.load('перс1/для атаки/3.png'), pygame.image.load('перс1/для атаки/4.png'),
                pygame.image.load('перс1/для атаки/5.png'), pygame.image.load('перс1/для атаки/6.png'),
                pygame.image.load('перс1/для атаки/7.png')]

    to_attack_enemy = [pygame.image.load('злодей1/для атаки/1.png')]

    selected_characters = []  # список выбранных персонажей

    finish = pygame.image.load('галочка.png')  # галочка

    choice_button_rect_1 = pygame.draw.rect(screen, (246, 143, 255), (16, 388, 104, 19))  # первая клетка выбора
    left_button_rect_1 = pygame.draw.rect(screen, (246, 143, 255), (16, 232, 28, 17))
    right_button_rect_1 = pygame.draw.rect(screen, (246, 143, 255), (92, 232, 28, 17))
    f1 = pygame.font.Font(None, 22)
    f2 = pygame.font.Font(None, 27)
    f3 = pygame.font.Font(None, 27)
    text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
    text2 = f2.render('<-', True, (255, 255, 255))
    text3 = f3.render('->', True, (255, 255, 255))
    screen.blit(text1, (30, 390))
    screen.blit(text2, (22, 230))
    screen.blit(text3, (97, 230))



    choice_button_rect_2 = pygame.draw.rect(screen, (246, 143, 255), (124, 388, 117, 19))  # вторая клетка выбора
    left_button_rect_2 = pygame.draw.rect(screen, (246, 143, 255), (124, 232, 28, 17))
    right_button_rect_2 = pygame.draw.rect(screen, (246, 143, 255), (213, 232, 28, 17))
    f1 = pygame.font.Font(None, 22)
    f2 = pygame.font.Font(None, 27)
    f3 = pygame.font.Font(None, 27)
    text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
    text2 = f2.render('<-', True, (255, 255, 255))
    text3 = f3.render('->', True, (255, 255, 255))
    screen.blit(text1, (145, 390))
    screen.blit(text2, (130, 230))
    screen.blit(text3, (220, 230))

    choice_button_rect_3 = pygame.draw.rect(screen, (246, 143, 255), (245, 388, 117, 19))  # третья клетка выбора
    left_button_rect_3 = pygame.draw.rect(screen, (246, 143, 255), (245, 232, 28, 17))
    right_button_rect_3 = pygame.draw.rect(screen, (246, 143, 255), (334, 232, 28, 17))
    f1 = pygame.font.Font(None, 22)
    f2 = pygame.font.Font(None, 27)
    f3 = pygame.font.Font(None, 27)
    text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
    text2 = f2.render('<-', True, (255, 255, 255))
    text3 = f3.render('->', True, (255, 255, 255))
    screen.blit(text1, (265, 390))
    screen.blit(text2, (251, 230))
    screen.blit(text3, (340, 230))

    choice_button_rect_4 = pygame.draw.rect(screen, (246, 143, 255), (366, 388, 107, 19))  # четвёртая клетка выбора
    left_button_rect_4 = pygame.draw.rect(screen, (246, 143, 255), (366, 232, 28, 17))
    right_button_rect_4 = pygame.draw.rect(screen, (246, 143, 255), (445, 232, 28, 17))
    f1 = pygame.font.Font(None, 22)
    f2 = pygame.font.Font(None, 27)
    f3 = pygame.font.Font(None, 27)
    text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
    text2 = f2.render('<-', True, (255, 255, 255))
    text3 = f3.render('->', True, (255, 255, 255))
    screen.blit(text1, (380, 390))
    screen.blit(text2, (372, 230))
    screen.blit(text3, (450, 230))

    pygame.draw.rect(screen, (107, 66, 189), (335, 605, 134, 31))  # конпка улучшить
    f4 = pygame.font.Font(None, 25)
    text1 = f4.render('УЛУЧШИТЬ', True, (245, 255, 255))
    screen.blit(text1, (355, 615))

    left_button_rect_5 = pygame.draw.rect(screen, (107, 66, 189), (27, 429, 47, 30))  # конпка улучшить
    right_button_rect_5 = pygame.draw.rect(screen, (107, 66, 189), (410, 429, 47, 30))
    f5 = pygame.font.Font(None, 42)
    f6 = pygame.font.Font(None, 42)
    text1 = f5.render('<-', True, (245, 255, 255))
    text2 = f6.render('->', True, (245, 255, 255))
    screen.blit(text1, (38, 429))
    screen.blit(text2, (419, 429))

    current_image_1 = 0
    current_image_2 = 0
    current_image_3 = 0
    current_image_4 = 0
    current_image_5 = 0


    selection_button_1 = True  # флаги разрешение на тыкание кнопок
    selection_button_2 = False
    selection_button_3 = False
    selection_button_4 = False

    selection_button_flag1 = False  # флаг для вывода на экран изображений после их выбора
    selection_button_flag2 = False
    selection_button_flag3 = False
    selection_button_flag4 = False

    selection_finish_1 = False  # флаг для отслеживания вывода на экран галочек
    selection_finish_2 = False
    selection_finish_3 = False
    selection_finish_4 = False

    displaying_enemies_on_the_screen = []  # список врагов для вывода на экран
    displaying_enemies_on_the_screen = random.choices(enemies_of_choice, k=4)  # выбор 4 врагов

    screen.blit(displaying_enemies_on_the_screen[0], (16, 44))  # вывод врагов на экран
    screen.blit(displaying_enemies_on_the_screen[1], (125, 44))
    screen.blit(displaying_enemies_on_the_screen[2], (245, 44))
    screen.blit(displaying_enemies_on_the_screen[3], (364, 44))

    count_anim = 0

    clock = pygame.time.Clock()


    flag = True
    while flag:

        if count_anim == 7:
            count_anim = 0
        else:
            count_anim += 1

        pygame.display.update()
        screen.blit(characters_of_choice_1[current_image_5], (15, 419))
        if selection_button_flag1:
            screen.blit(selected_characters[0], (19, 254))  # выводим изображение из списка выбранных персонажей
        else:
            screen.blit(characters_of_choice[current_image_1], (19, 254))  # на момент ввыбора прокручиваются все изображения
        if selection_button_flag2:
            screen.blit(selected_characters[1], (132, 254))
        else:
            screen.blit(characters_of_choice[current_image_2], (132, 254))
        if selection_button_flag3:
            screen.blit(selected_characters[2], (253, 254))
        else:
            screen.blit(characters_of_choice[current_image_3], (253, 254))
        if selection_button_flag4:
            screen.blit(selected_characters[3], (370, 254))
        else:
            screen.blit(characters_of_choice[current_image_4], (370, 254))

        if selection_finish_1:  # вывод на экран галочек после выбора персонажей
            screen.blit(finish, (19, 254))
        if selection_finish_2:
            screen.blit(finish, (132, 254))
        if selection_finish_3:
            screen.blit(finish, (253, 254))
        if selection_finish_4:
            screen.blit(finish, (370, 254))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsRunning = False
                pygame.quit()
                flag = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if left_button_rect_5.collidepoint(mouse_pos):
                    current_image_5 -= 1
                    if current_image_5 < 0:
                        current_image_5 = len(characters_of_choice_1) - 1
                elif right_button_rect_5.collidepoint(mouse_pos):
                    current_image_5 += 1
                    if current_image_5 >= len(characters_of_choice_1):
                        current_image_5 = 0
                if selection_button_1:
                    if left_button_rect_1.collidepoint(mouse_pos):  # если нажимают на "<-" в первой клетке выбора
                        current_image_1 -= 1
                        if current_image_1 < 0:
                            current_image_1 = len(characters_of_choice) - 1
                    elif right_button_rect_1.collidepoint(mouse_pos):  # если нажимают на "->" в первой клетке выбора
                        current_image_1 += 1
                        if current_image_1 >= len(characters_of_choice):
                            current_image_1 = 0
                    elif choice_button_rect_1.collidepoint(mouse_pos):  # если нажимают на "выбрать" в первой клетке выбора
                        selected_characters.append(characters_of_choice[current_image_1])  # добавление 1 персонажа в список выбора
                        selection_button_flag1 = True
                        selection_button_1 = False
                        selection_button_2 = True
                        selection_finish_1 = True
                        del characters_of_choice[current_image_1]  # удаление выбранного персонажа из общего списка

                if selection_button_2:
                    if left_button_rect_2.collidepoint(mouse_pos):  # если нажимают на "<-" во второй клетке выбора
                        current_image_2 -= 1
                        if current_image_2 < 0:
                            current_image_2 = len(characters_of_choice) - 1
                    elif right_button_rect_2.collidepoint(mouse_pos):  # если нажимают на "->" во второй клетке выбора
                        current_image_2 += 1
                        if current_image_2 >= len(characters_of_choice):
                            current_image_2 = 0
                    elif choice_button_rect_2.collidepoint(mouse_pos):  # если нажимают на "выбрать" во второй клетке выбора
                        selected_characters.append(characters_of_choice[current_image_2])  # добавление 2 персонажа в список выбора
                        selection_button_flag2 = True
                        selection_button_2 = False
                        selection_button_3 = True
                        selection_finish_2 = True
                        del characters_of_choice[current_image_2]  # удаление выбранного персонажа из общего списка

                if selection_button_3:
                    if left_button_rect_3.collidepoint(mouse_pos):  # если нажимают на "<-" в третьей клетке выбора
                        current_image_3 -= 1
                        if current_image_3 < 0:
                            current_image_3 = len(characters_of_choice) - 1
                    elif right_button_rect_3.collidepoint(mouse_pos):  # если нажимают на "->" в третьей клетке выбора
                        current_image_3 += 1
                        if current_image_3 >= len(characters_of_choice):
                            current_image_3 = 0
                    elif choice_button_rect_3.collidepoint(mouse_pos):  # если нажимают на "выбрать" в третьей клетке выбора
                        selected_characters.append(characters_of_choice[current_image_3])  # добавление 3 персонажа в список выбора
                        selection_button_flag3 = True
                        selection_button_3 = False
                        selection_button_4 = True
                        selection_finish_3 = True
                        del characters_of_choice[current_image_3]  # удаление выбранного персонажа из общего списка

                if selection_button_4:
                    if left_button_rect_4.collidepoint(mouse_pos):  # если нажимают на "<-" в четвёртой клетке выбора
                        current_image_4 -= 1
                        if current_image_4 < 0:
                            current_image_4 = len(characters_of_choice) - 1
                    elif right_button_rect_4.collidepoint(mouse_pos):  # если нажимают на "->" в четвёртой клетке выбора
                        current_image_4 += 1
                        if current_image_4 >= len(characters_of_choice):
                            current_image_4 = 0
                    elif choice_button_rect_4.collidepoint(mouse_pos):  # если нажимают на "выбрать" в четвёртой клетке
                        selected_characters.append(characters_of_choice[current_image_4])  # добавление 4 персонажа в список выбора
                        selection_button_flag4 = True
                        selection_button_4 = False
                        selection_finish_4 = True
                        del characters_of_choice[current_image_4]  # удаление выбранного персонажа из общего списка
                    if selection_button_1 != True and selection_button_2 != True and selection_button_3 != True and selection_button_4 != True:
                        screen.blit(attack_1[count_anim], (951, 141))
                        screen.blit(to_attack_enemy[0], (515, 45))
    clock.tick(20)

    print(selected_characters)

    pygame.quit()
