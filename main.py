import os
import sys
import random
import pygame
import sqlite3
import time

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 650))
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Game")
    pygame.mixer.music.load("445a6d5c5c7fd4d.mp3")
    pygame.mixer.music.play(-1)
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
    pygame.draw.circle(screen, (244, 164, 96), (1199, 485), 63, 2)  # магазин
    pygame.draw.rect(screen, (255, 215, 0), (1063, 564, 207, 43), 2)

    sc = pygame.image.load('сцена.png')
    screen.blit(sc, (484, 14))  # отрисовка поля боя

    score = 50  # счетчик монет
    f11 = pygame.font.Font(None, 40)

    character_1 = pygame.image.load('перс1/1.png')
    character_2 = pygame.image.load('перс2/1.png')
    character_3 = pygame.image.load('перс3/1.png')
    character_4 = pygame.image.load('перс4/1.png')
    character_5 = pygame.image.load('перс5/1.png')
    character_6 = pygame.image.load('перс6/1.png')
    character_7 = pygame.image.load('перс7/1.png')
    character_8 = pygame.image.load('перс8/1.png')

    enemy_1 = pygame.image.load('злодей1/1.png')
    enemy_2 = pygame.image.load('злодей2/1.png')
    enemy_3 = pygame.image.load('злодей3/1.png')
    enemy_4 = pygame.image.load('злодей4/1.png')

    characters_of_choice = [character_1, character_2, character_3, character_4, character_5,
                            character_6, character_7, character_8]  # список персонажей

    characters_of_choice_2 = [character_1, character_2, character_3, character_4, character_5,
                            character_6, character_7, character_8]

    characters_of_choice_1 = [pygame.image.load('перс1/2.png'), pygame.image.load('перс2/2.png'),
                            pygame.image.load('перс3/2.png'), pygame.image.load('перс4/2.png'),
                            pygame.image.load('перс5/2.png'), pygame.image.load('перс6/2.png'),
                            pygame.image.load('перс7/2.png'), pygame.image.load('перс8/2.png')]

    enemies_of_choice = [enemy_1, enemy_2, enemy_3, enemy_4]  # список врагов

    to_attack = [pygame.image.load('перс1/для атаки/1.png'), pygame.image.load('перс2/для атаки/1.png'),
                 pygame.image.load('перс3/для атаки/1.png'), pygame.image.load('перс4/для атаки/1.png'),
                 pygame.image.load('перс5/для атаки/1.png'), pygame.image.load('перс6/для атаки/1.png'),
                 pygame.image.load('перс7/для атаки/1.png'), pygame.image.load('перс8/для атаки/1.png')]

    attack_1 = [pygame.image.load('перс1/для атаки/1.png'), pygame.image.load('перс1/для атаки/2.png'),
                pygame.image.load('перс1/для атаки/3.png'), pygame.image.load('перс1/для атаки/4.png'),
                pygame.image.load('перс1/для атаки/5.png'), pygame.image.load('перс1/для атаки/6.png'),
                pygame.image.load('перс1/для атаки/7.png')]

    attack_2 = [pygame.image.load('перс2/для атаки/1.png'), pygame.image.load('перс2/для атаки/2.png'),
                pygame.image.load('перс2/для атаки/3.png'), pygame.image.load('перс2/для атаки/4.png'),
                pygame.image.load('перс2/для атаки/5.png')]

    attack_3 = [pygame.image.load('перс3/для атаки/1.png'), pygame.image.load('перс3/для атаки/2.png'),
                pygame.image.load('перс3/для атаки/3.png'), pygame.image.load('перс3/для атаки/4.png'),
                pygame.image.load('перс3/для атаки/5.png'), pygame.image.load('перс3/для атаки/6.png'),
                pygame.image.load('перс3/для атаки/7.png'), pygame.image.load('перс3/для атаки/8.png'),
                pygame.image.load('перс3/для атаки/9.png')]

    attack_4 = [pygame.image.load('перс4/для атаки/1.png'), pygame.image.load('перс4/для атаки/2.png'),
                pygame.image.load('перс4/для атаки/3.png'), pygame.image.load('перс4/для атаки/4.png'),
                pygame.image.load('перс4/для атаки/5.png')]

    attack_5 = [pygame.image.load('перс5/для атаки/1.png'), pygame.image.load('перс5/для атаки/2.png'),
                pygame.image.load('перс5/для атаки/3.png'), pygame.image.load('перс5/для атаки/4.png'),
                pygame.image.load('перс5/для атаки/5.png'), pygame.image.load('перс5/для атаки/6.png'),
                pygame.image.load('перс5/для атаки/7.png'), pygame.image.load('перс5/для атаки/8.png'),
                pygame.image.load('перс5/для атаки/9.png'), pygame.image.load('перс5/для атаки/10.png')]

    attack_6 = [pygame.image.load('перс6/для атаки/1.png'), pygame.image.load('перс6/для атаки/2.png'),
                pygame.image.load('перс6/для атаки/3.png'), pygame.image.load('перс6/для атаки/4.png'),
                pygame.image.load('перс6/для атаки/5.png'), pygame.image.load('перс6/для атаки/6.png'),
                pygame.image.load('перс6/для атаки/7.png'), pygame.image.load('перс6/для атаки/8.png'),
                pygame.image.load('перс6/для атаки/9.png'), pygame.image.load('перс6/для атаки/10.png'),
                pygame.image.load('перс6/для атаки/11.png')]

    attack_7 = [pygame.image.load('перс7/для атаки/1.png'), pygame.image.load('перс7/для атаки/2.png'),
                pygame.image.load('перс7/для атаки/3.png'), pygame.image.load('перс7/для атаки/4.png'),
                pygame.image.load('перс7/для атаки/5.png'), pygame.image.load('перс7/для атаки/6.png'),
                pygame.image.load('перс7/для атаки/7.png'), pygame.image.load('перс7/для атаки/8.png')]

    attack_8 = [pygame.image.load('перс8/для атаки/1.png'), pygame.image.load('перс8/для атаки/2.png'),
                pygame.image.load('перс8/для атаки/3.png'), pygame.image.load('перс8/для атаки/4.png'),
                pygame.image.load('перс8/для атаки/5.png'), pygame.image.load('перс8/для атаки/6.png'),
                pygame.image.load('перс8/для атаки/7.png'), pygame.image.load('перс8/для атаки/8.png')]

    attack_enemy_1 = [pygame.image.load('злодей1/для атаки/1.png'), pygame.image.load('злодей1/для атаки/2.png'),
                      pygame.image.load('злодей1/для атаки/3.png'), pygame.image.load('злодей1/для атаки/4.png'),
                      pygame.image.load('злодей1/для атаки/5.png'), pygame.image.load('злодей1/для атаки/6.png'),
                      pygame.image.load('злодей1/для атаки/7.png')]

    attack_enemy_2 = [pygame.image.load('злодей2/для атаки/1.png'), pygame.image.load('злодей2/для атаки/2.png'),
                      pygame.image.load('злодей2/для атаки/3.png'), pygame.image.load('злодей2/для атаки/4.png'),
                      pygame.image.load('злодей2/для атаки/5.png'), pygame.image.load('злодей2/для атаки/6.png'),
                      pygame.image.load('злодей2/для атаки/7.png')]

    attack_enemy_3 = [pygame.image.load('злодей3/для атаки/1.png'), pygame.image.load('злодей3/для атаки/2.png'),
                      pygame.image.load('злодей3/для атаки/3.png'), pygame.image.load('злодей3/для атаки/4.png'),
                      pygame.image.load('злодей3/для атаки/5.png'), pygame.image.load('злодей3/для атаки/6.png'),
                      pygame.image.load('злодей3/для атаки/7.png')]

    attack_enemy_4 = [pygame.image.load('злодей4/для атаки/1.png'), pygame.image.load('злодей4/для атаки/2.png'),
                      pygame.image.load('злодей4/для атаки/3.png'), pygame.image.load('злодей4/для атаки/4.png'),
                      pygame.image.load('злодей4/для атаки/5.png'), pygame.image.load('злодей4/для атаки/6.png'),
                      pygame.image.load('злодей4/для атаки/7.png')]

    kill = [pygame.image.load('анимация удара/1.png'), pygame.image.load('анимация удара/2.png'),
            pygame.image.load('анимация удара/3.png'), pygame.image.load('анимация удара/4.png'),
            pygame.image.load('анимация удара/5.png')]

    list_to_attack_characters = {character_1: attack_1, character_2: attack_2, character_3: attack_3,
                                 character_4: attack_4, character_5: attack_5, character_6: attack_6,
                                 character_7: attack_7, character_8: attack_8}

    to_attack_enemy = {enemy_1: attack_enemy_1, enemy_2: attack_enemy_2, enemy_3: attack_enemy_3,
                       enemy_4: attack_enemy_4}

    selected_characters = []  # список выбранных персонажей

    finish = pygame.image.load('галочка.png')  # галочка

    choice_button_rect_1 = pygame.draw.rect(screen, (246, 143, 255), (16, 388, 104, 19))  # первая клетка выбора
    left_button_rect_1 = pygame.draw.rect(screen, (246, 143, 255), (16, 232, 28, 17))
    right_button_rect_1 = pygame.draw.rect(screen, (246, 143, 255), (92, 232, 28, 17))
    f1 = pygame.font.Font(None, 22)
    f2 = pygame.font.Font(None, 27)
    text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
    text2 = f2.render('<-', True, (255, 255, 255))
    text3 = f2.render('->', True, (255, 255, 255))
    screen.blit(text1, (30, 390))
    screen.blit(text2, (22, 230))
    screen.blit(text3, (97, 230))

    choice_button_rect_2 = pygame.draw.rect(screen, (246, 143, 255), (124, 388, 117, 19))  # вторая клетка выбора
    left_button_rect_2 = pygame.draw.rect(screen, (246, 143, 255), (124, 232, 28, 17))
    right_button_rect_2 = pygame.draw.rect(screen, (246, 143, 255), (213, 232, 28, 17))
    f1 = pygame.font.Font(None, 22)
    f2 = pygame.font.Font(None, 27)
    text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
    text2 = f2.render('<-', True, (255, 255, 255))
    text3 = f2.render('->', True, (255, 255, 255))
    screen.blit(text1, (145, 390))
    screen.blit(text2, (130, 230))
    screen.blit(text3, (220, 230))

    choice_button_rect_3 = pygame.draw.rect(screen, (246, 143, 255), (245, 388, 117, 19))  # третья клетка выбора
    left_button_rect_3 = pygame.draw.rect(screen, (246, 143, 255), (245, 232, 28, 17))
    right_button_rect_3 = pygame.draw.rect(screen, (246, 143, 255), (334, 232, 28, 17))
    f1 = pygame.font.Font(None, 22)
    f2 = pygame.font.Font(None, 27)
    text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
    text2 = f2.render('<-', True, (255, 255, 255))
    text3 = f2.render('->', True, (255, 255, 255))
    screen.blit(text1, (265, 390))
    screen.blit(text2, (251, 230))
    screen.blit(text3, (340, 230))

    choice_button_rect_4 = pygame.draw.rect(screen, (246, 143, 255), (366, 388, 107, 19))  # четвёртая клетка выбора
    left_button_rect_4 = pygame.draw.rect(screen, (246, 143, 255), (366, 232, 28, 17))
    right_button_rect_4 = pygame.draw.rect(screen, (246, 143, 255), (445, 232, 28, 17))
    f1 = pygame.font.Font(None, 22)
    f2 = pygame.font.Font(None, 27)
    text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
    text2 = f2.render('<-', True, (255, 255, 255))
    text3 = f2.render('->', True, (255, 255, 255))
    screen.blit(text1, (380, 390))
    screen.blit(text2, (372, 230))
    screen.blit(text3, (450, 230))

    list_name = []  # список имён персонажей
    list_hp = []  # список жизней персонажей
    list_hp1 = []
    list_attack_power = []  # список силы атаки персонажей
    list_raising_HP = []  # список повышения единиц жизней
    list_raising_attack = []  # список повышения единиц силы атаки
    list_cost = []  # список стоимосости повышения

    list_name_enemy = []  # список имён врагов
    list_hp_enemy = []  # список жизней врагов
    list_attack_power_enemy = []  # список силы атаки врагов
    list_raising_HP_enemy = []  # список повышения единиц жизней врагов
    list_raising_attack_enemy = []  # список повышения единиц силы атаки врагов

    con = sqlite3.connect('characterization.sqlite')  # подключаем БД
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM pers""").fetchall()
    for elem in result:
        list_name.append(elem[1])
        list_hp.append(elem[2])
        list_hp1.append(elem[2])
        list_attack_power.append(elem[3])
        list_raising_HP.append(elem[4])
        list_raising_attack.append(elem[5])
        list_cost.append(elem[6])

    result_2 = cur.execute("""SELECT * FROM villains""").fetchall()
    for elem in result_2:
        list_name_enemy.append(elem[1])
        list_hp_enemy.append(elem[2])
        list_attack_power_enemy.append(elem[3])
        list_raising_HP_enemy.append(elem[4])
        list_raising_attack_enemy.append(elem[5])


    f7 = pygame.font.Font(None, 18)  # для вывода на экран характеристик


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
    count_kill = 0
    count_enemy = 0
    run = False
    run_flag_enemy = False
    run_flag_character = True
    stop_image = True
    run_image = False


    all_sprites = pygame.sprite.Group()

    basket = pygame.image.load('корзинка.png')

    class Ball(pygame.sprite.Sprite):
        def __init__(self, radius):
            super().__init__(all_sprites)
            self.radius = radius
            self.x = 700
            self.y = 500
            self.image = pygame.image.load('круг.png')
            self.rect = pygame.Rect(self.x, self.y, 2 * radius, 2 * radius)
            self.vx = random.randint(-5, 5)
            self.vy = random.randint(-5, 5)

        def update(self):
            if pygame.sprite.spritecollideany(self, horizontal_borders):
                self.vy = -self.vy
            if pygame.sprite.spritecollideany(self, vertical_borders):
                self.vx = -self.vx
            self.rect = self.rect.move(self.vx, self.vy)

            self.x += self.vx
            self.y += self.vy


            mouse_pos = pygame.mouse.get_pos()
            mouse_clicked = pygame.mouse.get_pressed()[0]
            if self.rect.collidepoint(*mouse_pos) and mouse_clicked:
                self.kill()

    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()

    class Border(pygame.sprite.Sprite):
        def __init__(self, x1, y1, x2, y2):
            super().__init__(all_sprites)
            if x2 == x1:  # вертикальная стенка
                self.add(vertical_borders)
                self.image = pygame.Surface([1, y2 - y1])
                self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
            else:  # горизонтальная стенка
                self.add(horizontal_borders)
                self.image = pygame.Surface([x2 - x1, 1])
                self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

    Border(495, 425, 1040, 425)
    Border(495, 425, 495, 620)
    Border(1040, 425, 1040, 620)
    Border(495, 620, 1040, 620)

    circles = []

    current_image = 0

    block_run = False
    block_stop_3_s = 0


    experience = 0
    f8 = pygame.font.Font(None, 50)

    count_time = 0

    rect1_x = 206
    rect2_x = 206

    def new(e):
        # global exper
        # exper = 0
        pygame.draw.rect(screen, (75, 0, 130), (1063, 457, 60, 51))
        text1 = f8.render(str(round((12 - len(all_sprites.sprites()) + 4) * 100 / 12)), True, (245, 255, 255))
        screen.blit(text1, (1065, 466))
        # exper = e

    def draw_character_anim():
        screen.blit(sc, (484, 14))
        pygame.draw.rect(screen, (139, 0, 0), (560, 25, rect1_x, 22))
        pygame.draw.rect(screen, (139, 0, 0), (941, 61, rect2_x, 22))
        pygame.draw.rect(screen, (255, 255, 255), (558, 25, 208, 24), 2)
        pygame.draw.rect(screen, (255, 255, 255), (939, 61, 208, 24), 2)
        if displaying_enemies_on_the_screen[j] == enemy_1 or displaying_enemies_on_the_screen[j] == enemy_2:
            screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][0], (515, 45))
        elif displaying_enemies_on_the_screen[j] == enemy_3:
            screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][0], (500, 50))
        elif displaying_enemies_on_the_screen[j] == enemy_4:
            screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][0], (500, 100))

    def draw_enemy_anim():
        screen.blit(sc, (484, 14))
        screen.blit(list_to_attack_characters[selected_characters[j]][0], (951, 141))
        pygame.draw.rect(screen, (139, 0, 0), (560, 25, rect1_x, 22))
        pygame.draw.rect(screen, (139, 0, 0), (941, 61, rect2_x, 22))
        pygame.draw.rect(screen, (255, 255, 255), (558, 25, 208, 24), 2)
        pygame.draw.rect(screen, (255, 255, 255), (939, 61, 208, 24), 2)

    def window():
        screen.blit(sc, (484, 14))
        pygame.draw.rect(screen, (139, 0, 0), (560, 25, rect1_x, 22))
        pygame.draw.rect(screen, (139, 0, 0), (941, 61, rect2_x, 22))
        pygame.draw.rect(screen, (255, 255, 255), (558, 25, 208, 24), 2)
        pygame.draw.rect(screen, (255, 255, 255), (939, 61, 208, 24), 2)
        screen.blit(list_to_attack_characters[selected_characters[j]][0], (951, 141))
        if displaying_enemies_on_the_screen[j] == enemy_1 or displaying_enemies_on_the_screen[j] == enemy_2:
            screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][0], (515, 45))
        elif displaying_enemies_on_the_screen[j] == enemy_3:
            screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][0], (500, 50))
        elif displaying_enemies_on_the_screen[j] == enemy_4:
            screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][0], (500, 100))


    winning = [0, 0, 0, 0]
    flag_attack = True
    list_for_j = [0]
    j = 0
    percentages = 100
    percentages2 = 100
    att = len(all_sprites.sprites())
    hp_ch = int(list_hp[list_for_j[j]])
    hp_enemy = int(list_hp_enemy[list_for_j[j]])

    fff = False
    money_win = 0

    flag = True

    while flag:
        print(list_for_j)
        pygame.draw.rect(screen, (255, 215, 0), (1063, 564, 207, 43))
        score_text = f11.render(f"Счет: {score}", True, (255, 255, 255))
        screen.blit(score_text, (1065, 572))
        new(experience)

        level_up = pygame.draw.rect(screen, (107, 66, 189), (335, 605, 134, 31))  # конпка улучшить
        f4 = pygame.font.Font(None, 25)
        text1 = f4.render('УЛУЧШИТЬ', True, (245, 255, 255))
        screen.blit(text1, (355, 615))

        left_button_rect_5 = pygame.draw.rect(screen, (107, 66, 189), (27, 429, 47, 30))
        right_button_rect_5 = pygame.draw.rect(screen, (107, 66, 189), (410, 429, 47, 30))
        f5 = pygame.font.Font(None, 42)
        f6 = pygame.font.Font(None, 42)
        text1 = f5.render('<-', True, (245, 255, 255))
        text2 = f6.render('->', True, (245, 255, 255))
        screen.blit(text1, (38, 429))
        screen.blit(text2, (419, 429))

        pygame.draw.rect(screen, (107, 66, 189), (25, 468, 132, 90))  # вывод на экран характеристик
        name = list_name[current_image_5]
        hp = list_hp1[current_image_5]
        attack_power = list_attack_power[current_image_5]
        cost = list_cost[current_image_5]
        text1 = f7.render(f'Имя: {name}', True, (255, 255, 255))
        screen.blit(text1, (30, 478))
        text1 = f7.render(f'HP: {hp}', True, (255, 255, 255))
        screen.blit(text1, (30, 498))
        text1 = f7.render(f'Сила атаки: {attack_power}', True, (255, 255, 255))
        screen.blit(text1, (30, 518))
        text1 = f7.render(f'Цена повышения: {cost}', True, (255, 255, 255))
        screen.blit(text1, (30, 538))

        if fff:
            screen.blit(sc, (484, 14))
            f9 = pygame.font.Font(None, 80)
            text1 = f9.render(f'Вы выиграли {money_win} монет', True, (255, 255, 255))
            screen.blit(text1, (558, 55))
            f1f1f1 = pygame.draw.rect(screen, (107, 66, 189), (585, 130, 205, 70))
            f10 = pygame.font.Font(None, 30)
            text1 = f10.render(f'Начать новую игру', True, (255, 255, 255))
            screen.blit(text1, (588, 155))

        if run:
            window()
            if stop_image:
                if hp_ch <= 0 or hp_enemy <= 0:
                    if hp_enemy <= 0:
                        winning[j] = 1
                    j += 1
                    if j == 4:
                        stop_image = False
                        run = False
                        fff = True
                        for i in winning:
                            if i == 100:
                                money_win += 15
                                score += 15
                    else:
                        hp_ch = int(list_hp[list_for_j[j]])
                        hp_enemy = int(list_hp_enemy[j])
                        rect1_x = 206
                        rect2_x = 206
                        element_x = 100
                        element_x2 = 100
                        percentages = 100
                        percentages2 = 100
                if j == 4:
                    stop_image = False
                    run = False
                else:
                    window()
                    block_run = True
                    block_stop_3_s += 1



            if run_image:

                if run_flag_enemy:

                    screen.blit(sc, (484, 14))
                    screen.blit(list_to_attack_characters[selected_characters[j]][0], (951, 141))
                    pygame.draw.rect(screen, (139, 0, 0), (560, 25, rect1_x, 22))
                    pygame.draw.rect(screen, (139, 0, 0), (941, 61, rect2_x, 22))
                    pygame.draw.rect(screen, (255, 255, 255), (558, 25, 208, 24), 2)
                    pygame.draw.rect(screen, (255, 255, 255), (939, 61, 208, 24), 2)
                    time.sleep(0.09)


                    if count_enemy != (len(to_attack_enemy[displaying_enemies_on_the_screen[j]]) - 1):
                        count_enemy += 1

                    else:
                        print(hp_ch)
                        hp_ch = int(list_hp[list_for_j[j]]) - list_attack_power_enemy[j]
                        element_x2 = round(hp_ch * percentages2 / int(list_hp[list_for_j[j]]))
                        list_hp[list_for_j[j]] = hp_ch
                        percentages2 = element_x2
                        rect2_x = 2.06 * element_x2


                        count_enemy = 0
                        stop_image = True
                        run_flag_enemy = False
                        run_image = False
                        count_kill = 0
                        window()





                    if displaying_enemies_on_the_screen[j] == enemy_1 or displaying_enemies_on_the_screen[j] == enemy_2:
                        screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][count_enemy], (515, 45))
                    if displaying_enemies_on_the_screen[j] == enemy_3:
                        screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][count_enemy], (500, 50))
                    if displaying_enemies_on_the_screen[j] == enemy_4:
                        screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][count_enemy], (500, 100))

                if run_flag_character:

                    screen.blit(sc, (484, 14))
                    pygame.draw.rect(screen, (139, 0, 0), (560, 25, rect1_x, 22))
                    pygame.draw.rect(screen, (139, 0, 0), (941, 61, rect2_x, 22))
                    pygame.draw.rect(screen, (255, 255, 255), (558, 25, 208, 24), 2)
                    pygame.draw.rect(screen, (255, 255, 255), (939, 61, 208, 24), 2)
                    if displaying_enemies_on_the_screen[j] == enemy_1 or displaying_enemies_on_the_screen[j] == enemy_2:
                        screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][0], (515, 45))
                    if displaying_enemies_on_the_screen[j] == enemy_3:
                        screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][0], (500, 50))
                    if displaying_enemies_on_the_screen[j] == enemy_4:
                        screen.blit(to_attack_enemy[displaying_enemies_on_the_screen[j]][0], (500, 100))
                    time.sleep(0.09)
                    if count_anim == len(list_to_attack_characters[selected_characters[j]]) - 1:
                        hp_enemy = int(list_hp_enemy[j]) - (int(list_attack_power[j]) * round((12 - att + 4) * 100 / 12)) / 100

                        element_x = round(hp_enemy * percentages / list_hp_enemy[j])
                        list_hp_enemy[j] = hp_enemy
                        percentages = element_x

                        rect1_x = 2.06 * element_x

                        count_anim = 0
                        count_time = 0

                        if hp_enemy < 0:
                            run_flag_character = False
                            stop_image = True
                            run_image = False
                        else:
                            run_flag_enemy = True
                            run_flag_character = False

                    if count_anim != len(list_to_attack_characters[selected_characters[j]]) - 1:
                        count_anim += 1
                    screen.blit(list_to_attack_characters[selected_characters[j]][count_anim], (951, 141))
                    if count_kill != len(kill) - 1:
                        count_kill += 1
                    screen.blit(kill[count_kill], (753, 168))


        if block_run:

            screen.blit(basket, (484, 421))
            count_time += 1
            if block_stop_3_s == 1:
                time.sleep(1)
                for i in range(12):
                    circles.append(Ball(20))
            if count_time <= 1:
                for i in circles:
                    i.update()
                    all_sprites.draw(screen)
                    att = len(all_sprites.sprites())
            else:
                for i in circles:
                    all_sprites.remove(i)
                run_image = True
                run_flag_character = True
                block_run = False
                stop_image = False
                block_stop_3_s = 0
                count_time = 0
                circles = []



        pygame.display.update()
        screen.blit(characters_of_choice_1[current_image_5], (152, 419))
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
                flag = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if level_up.collidepoint(mouse_pos):
                    # sql_update_query = """Update pers set Attack_power = 10000 where id = 4"""
                    # cur.execute(sql_update_query)
                    # con.commit()
                    if score >= cost:
                        score -= cost
                        list_hp1[current_image_5] = str(int(list_hp1[current_image_5]) + int(list_raising_HP[current_image_5]))
                        list_hp[current_image_5] = list_hp1[current_image_5]
                        list_attack_power[current_image_5] = str(int(list_attack_power[current_image_5]) + int(list_raising_attack[current_image_5]))

                if fff:
                    if f1f1f1.collidepoint(mouse_pos):
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
                        pygame.draw.circle(screen, (244, 164, 96), (1199, 485), 63, 2)  # магазин
                        pygame.draw.rect(screen, (255, 215, 0), (1063, 564, 207, 43), 2)

                        screen.blit(sc, (484, 14))  # отрисовка поля боя


                        characters_of_choice = [character_1, character_2, character_3, character_4, character_5,
                                                character_6, character_7, character_8]  # список персонажей


                        enemies_of_choice = [enemy_1, enemy_2, enemy_3, enemy_4]  # список врагов


                        list_to_attack_characters = {character_1: attack_1, character_2: attack_2,
                                                     character_3: attack_3,
                                                     character_4: attack_4, character_5: attack_5,
                                                     character_6: attack_6,
                                                     character_7: attack_7, character_8: attack_8}

                        to_attack_enemy = {enemy_1: attack_enemy_1, enemy_2: attack_enemy_2, enemy_3: attack_enemy_3,
                                           enemy_4: attack_enemy_4}

                        selected_characters = []  # список выбранных персонажей

                        choice_button_rect_1 = pygame.draw.rect(screen, (246, 143, 255),
                                                                (16, 388, 104, 19))  # первая клетка выбора
                        left_button_rect_1 = pygame.draw.rect(screen, (246, 143, 255), (16, 232, 28, 17))
                        right_button_rect_1 = pygame.draw.rect(screen, (246, 143, 255), (92, 232, 28, 17))
                        f1 = pygame.font.Font(None, 22)
                        f2 = pygame.font.Font(None, 27)
                        text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
                        text2 = f2.render('<-', True, (255, 255, 255))
                        text3 = f2.render('->', True, (255, 255, 255))
                        screen.blit(text1, (30, 390))
                        screen.blit(text2, (22, 230))
                        screen.blit(text3, (97, 230))

                        choice_button_rect_2 = pygame.draw.rect(screen, (246, 143, 255),
                                                                (124, 388, 117, 19))  # вторая клетка выбора
                        left_button_rect_2 = pygame.draw.rect(screen, (246, 143, 255), (124, 232, 28, 17))
                        right_button_rect_2 = pygame.draw.rect(screen, (246, 143, 255), (213, 232, 28, 17))
                        f1 = pygame.font.Font(None, 22)
                        f2 = pygame.font.Font(None, 27)
                        text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
                        text2 = f2.render('<-', True, (255, 255, 255))
                        text3 = f2.render('->', True, (255, 255, 255))
                        screen.blit(text1, (145, 390))
                        screen.blit(text2, (130, 230))
                        screen.blit(text3, (220, 230))

                        choice_button_rect_3 = pygame.draw.rect(screen, (246, 143, 255),
                                                                (245, 388, 117, 19))  # третья клетка выбора
                        left_button_rect_3 = pygame.draw.rect(screen, (246, 143, 255), (245, 232, 28, 17))
                        right_button_rect_3 = pygame.draw.rect(screen, (246, 143, 255), (334, 232, 28, 17))
                        f1 = pygame.font.Font(None, 22)
                        f2 = pygame.font.Font(None, 27)
                        text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
                        text2 = f2.render('<-', True, (255, 255, 255))
                        text3 = f2.render('->', True, (255, 255, 255))
                        screen.blit(text1, (265, 390))
                        screen.blit(text2, (251, 230))
                        screen.blit(text3, (340, 230))

                        choice_button_rect_4 = pygame.draw.rect(screen, (246, 143, 255),
                                                                (366, 388, 107, 19))  # четвёртая клетка выбора
                        left_button_rect_4 = pygame.draw.rect(screen, (246, 143, 255), (366, 232, 28, 17))
                        right_button_rect_4 = pygame.draw.rect(screen, (246, 143, 255), (445, 232, 28, 17))
                        f1 = pygame.font.Font(None, 22)
                        f2 = pygame.font.Font(None, 27)
                        text1 = f1.render('ВЫБРАТЬ', True, (255, 255, 255))
                        text2 = f2.render('<-', True, (255, 255, 255))
                        text3 = f2.render('->', True, (255, 255, 255))
                        screen.blit(text1, (380, 390))
                        screen.blit(text2, (372, 230))
                        screen.blit(text3, (450, 230))

                        list_name = []  # список имён персонажей
                        list_hp = []  # список жизней персонажей
                        list_attack_power = []  # список силы атаки персонажей
                        list_raising_HP = []  # список повышения единиц жизней
                        list_raising_attack = []  # список повышения единиц силы атаки

                        list_name_enemy = []  # список имён врагов
                        list_hp_enemy = []  # список жизней врагов
                        list_attack_power_enemy = []  # список силы атаки врагов
                        list_raising_HP_enemy = []  # список повышения единиц жизней врагов
                        list_raising_attack_enemy = []  # список повышения единиц силы атаки врагов

                        con = sqlite3.connect('characterization.sqlite')  # подключаем БД
                        cur = con.cursor()
                        result = cur.execute("""SELECT * FROM pers""").fetchall()
                        for elem in result:
                            list_name.append(elem[1])
                            list_hp.append(elem[2])
                            list_attack_power.append(elem[3])
                            list_raising_HP.append(elem[4])
                            list_raising_attack.append(elem[5])

                        result_2 = cur.execute("""SELECT * FROM villains""").fetchall()
                        for elem in result_2:
                            list_name_enemy.append(elem[1])
                            list_hp_enemy.append(elem[2])
                            list_attack_power_enemy.append(elem[3])
                            list_raising_HP_enemy.append(elem[4])
                            list_raising_attack_enemy.append(elem[5])

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
                        count_kill = 0
                        count_enemy = 0
                        run = False
                        run_flag_enemy = False
                        run_flag_character = True
                        stop_image = True
                        run_image = False


                        circles = []

                        current_image = 0

                        block_run = False
                        block_stop_3_s = 0

                        experience = 0
                        f8 = pygame.font.Font(None, 50)

                        count_time = 0

                        rect1_x = 206
                        rect2_x = 206


                        winning = [0, 0, 0, 0]
                        flag_attack = True
                        list_for_j = [0]
                        j = 0
                        percentages = 100
                        percentages2 = 100
                        att = 16
                        hp_ch = int(list_hp[list_for_j[j]])
                        hp_enemy = int(list_hp_enemy[j])

                        fff = False
                        money_win = 0

                        rect1_x = 206
                        rect2_x = 206
                        element_x = 100
                        element_x2 = 100

                        flag = True

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
                        list_for_j[0] = characters_of_choice_2.index(characters_of_choice[current_image_1])
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
                        list_for_j.append(characters_of_choice_2.index(characters_of_choice[current_image_2]))
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
                        list_for_j.append(characters_of_choice_2.index(characters_of_choice[current_image_3]))
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
                        list_for_j.append(characters_of_choice_2.index(characters_of_choice[current_image_4]))
                        del characters_of_choice[current_image_4]  # удаление выбранного персонажа из общего списка
                    if selection_button_1 != True and selection_button_2 != True and selection_button_3 != True and selection_button_4 != True:
                        run = True

    pygame.quit()
    con.close()