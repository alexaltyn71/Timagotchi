import os
import sys
import pygame
import random
import time

kill_pillow = False
FOOD = 100
WATER = 100
SLEEP = 1
LOVE = 100
COINS = 0
start_time = round(time.time(), 1)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def indicators():
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    _food = my_font.render(str(FOOD), False, (0, 0, 0))
    screen.blit(_food, (45, 33))
    water = my_font.render(str(WATER), False, (0, 0, 0))
    screen.blit(water, (45, 68))
    sleep = my_font.render(str(SLEEP), False, (0, 0, 0))
    screen.blit(sleep, (45, 103))
    love = my_font.render(str(LOVE), False, (0, 0, 0))
    screen.blit(love, (45, 138))


def coins():
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    coin = my_font.render(str(COINS), False, (0, 0, 0))
    screen.blit(coin, (665, 35))


def gameLoop():
    global tima, tv, pillow, food, dis, COINS, running
    pygame.display.set_mode(size, pygame.NOFRAME)

    def our_snake(snake_list):
        for x in snake_list:
            screen.blit(tima_cur, (x[0], x[1]))

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 8, dis_height / 2])

    dis_width, dis_height = 720, 480
    dis = pygame.display.set_mode((dis_width, dis_height))

    back = (194, 255, 147)
    text = (48, 104, 10)
    snake_block = 10
    coin = load_image('coin.png')
    tima_cur = load_image('cursor.png')
    font_style = pygame.font.SysFont("Comic Sans MS", 22)
    clock = pygame.time.Clock()

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(back)
            square = load_image('square.png')
            screen.blit(square, (0, 0))
            indicators()
            coins()
            message("GAME OVER! Нажми C (начать заново) или Q (выйти)", text)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        dis = Home()
                        tima = Tima()
                        tv = TV()
                        pillow = SPillow()
                        food = Food()
                        ex = Exit()
                        return
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(back)
        screen.blit(coin, (foodx, foody))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        our_snake(snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            COINS += 1

        clock.tick(20)


def game_exit():
    pygame.init()

    screen.fill('black')
    exit_tima = load_image('tima_lie_7.png')
    button = load_image('game_exit.png')
    screen.blit(exit_tima, (0, 0))
    screen.blit(button, (0, 0))
    pygame.time.delay(60)


def over():
    pygame.init()

    screen.fill('black')
    exit_tima = load_image('game_over.png')
    screen.blit(exit_tima, (0, 0))
    pygame.time.delay(60)


class Home(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('room.png')
        self.rect = self.image.get_rect()


class Exit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('exit.png')
        self.rect = self.image.get_rect()

    def update(self, *args):
        global dis, tima, tv, pillow, food
        area = pygame.Rect(618, 444, 100, 34)

        if args and args[0].type == pygame.MOUSEBUTTONDOWN and area.collidepoint(event.pos):
            dis.kill()
            pillow.kill()
            tima.kill()
            food.kill()
            tv.kill()
            self.kill()

            game_exit()


class Tima(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('tima_sit_1.png')
        self.rect = self.image.get_rect()

    def update(self, *args):
        global LOVE
        area = pygame.Rect(250, 300, 130, 155)

        indicators()

        if args and args[0].type == pygame.MOUSEBUTTONDOWN and area.collidepoint(event.pos):
            images = ['tima_care_1.png', 'tima_care_2.png']
            ind = 0
            for i in range(6):
                self.image = load_image(images[ind])
                ind = (ind + 1) % 2
                all_sprites.draw(screen)
                all_sprites.update()
                pygame.display.flip()
                pygame.time.delay(350)
            self.image = load_image('tima_sit_1.png')

            LOVE += 10
            if LOVE > 100:
                LOVE = 100


class SPillow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('small_pillow.png')
        self.rect = self.image.get_rect()

    def update(self, *args):
        global dis, tima, tv, pillow, food
        area = pygame.Rect(440, 320, 210, 85)

        if args and args[0].type == pygame.MOUSEBUTTONDOWN and area.collidepoint(event.pos):
            dis = Pillow()
            tima = Sleep()
            food.kill()
            tv.kill()
            self.kill()


class Pillow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('pillow.png')
        self.rect = self.image.get_rect()

    def update(self, *args):
        global kill_pillow, tima, tv, pillow, food, dis, ex
        if kill_pillow:
            kill_pillow = False
            dis = Home()
            food = Food()
            tv = TV()
            pillow = SPillow()
            tima = Tima()
            ex = Exit()
            self.kill()


class Sleep(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('big_tima_sleep_1.png')
        self.rect = self.image.get_rect()

    def update(self, *args):
        area = pygame.Rect(270, 70, 250, 300)

        indicators()

        if args and args[0].type == pygame.MOUSEBUTTONDOWN and area.collidepoint(event.pos):
            images = ['big_tima_sleep_1.png', 'big_tima_sleep_2.png', 'big_tima_sleep_3.png', 'big_tima_sleep_4.png',
                      'big_tima_sleep_5.png', 'big_tima_sleep_6.png', 'big_tima_sleep_7.png', 'big_tima_sleep_8.png']

            for i in range(5):
                self.image = load_image(images[i])
                self.rect = self.image.get_rect()

                all_sprites.draw(screen)
                all_sprites.update()
                pygame.display.flip()
                pygame.time.delay(150)

            ind = 6
            global SLEEP, kill_pillow
            while SLEEP < 100:
                self.image = load_image(images[ind])
                self.rect = self.image.get_rect()
                ind = (ind + 1) % 2 + 6

                all_sprites.draw(screen)
                all_sprites.update()
                pygame.display.flip()
                pygame.time.delay(350)

                SLEEP += 1
                if SLEEP > 100:
                    SLEEP = 100
            else:
                kill_pillow = True
                self.kill()


class TV(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('tv_1.png')
        self.rect = self.image.get_rect()

    def update(self, *args):
        global dis, tima, tv, pillow, food
        area = pygame.Rect(371, 78, 167, 120)

        images = ['tv_2.png', 'tv_1.png']
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and area.collidepoint(event.pos):
            for i in range(2):
                for j in range(2):
                    self.image = load_image(images[j])

                    all_sprites.draw(screen)
                    all_sprites.update()
                    pygame.display.flip()
                    pygame.time.delay(350)

            tima.kill()
            tv.kill()
            pillow.kill()
            food.kill()
            ex.kill()
            gameLoop()


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('food.png')
        self.rect = self.image.get_rect()

    def update(self, *args):
        global dis, tima, tv, pillow
        area = pygame.Rect(85, 330, 155, 65)

        if args and args[0].type == pygame.MOUSEBUTTONDOWN and area.collidepoint(event.pos):
            shop = Shop()
            food.kill()
            tima.kill()
            tv.kill()
            pillow.kill()
            ex.kill()


class Shop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('shop.png')
        self.rect = self.image.get_rect()

    def update(self, *args):
        coins()
        indicators()

        def up():
            global tv, tima, pillow, food, ex
            self.kill()
            tima = Tima()
            tv = TV()
            pillow = SPillow()
            food = Food()
            ex = Exit()

        global COINS, FOOD, WATER
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and pygame.Rect(640, 384, 48, 44).collidepoint(event.pos):
            up()
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and pygame.Rect(230, 54, 121, 44).collidepoint(event.pos):
            if COINS >= 2:
                FOOD += 1
                if FOOD > 100:
                    FOOD = 100
                COINS -= 2
                up()
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and pygame.Rect(230, 147, 121, 44).collidepoint(event.pos):
            if COINS >= 5:
                FOOD += 3
                if FOOD > 100:
                    FOOD = 100
                COINS -= 5
                up()
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and pygame.Rect(230, 248, 121, 44).collidepoint(event.pos):
            if COINS >= 10:
                FOOD += 5
                if FOOD > 100:
                    FOOD = 100
                COINS -= 10
                up()
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and pygame.Rect(230, 341, 121, 44).collidepoint(event.pos):
            if COINS >= 20:
                FOOD += 15
                if FOOD > 100:
                    FOOD = 100
                COINS -= 20
                up()
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and pygame.Rect(474, 54, 121, 44).collidepoint(event.pos):
            if COINS >= 1:
                WATER += 1
                if WATER > 100:
                    WATER = 100
                COINS -= 2
                up()
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and pygame.Rect(474, 147, 121, 44).collidepoint(event.pos):
            if COINS >= 5:
                WATER += 3
                if WATER > 100:
                    WATER = 100
                COINS -= 5
                up()
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and pygame.Rect(474, 248, 121, 44).collidepoint(event.pos):
            if COINS >= 10:
                WATER += 5
                if WATER > 100:
                    WATER = 100
                COINS -= 10
                up()
        elif args and args[0].type == pygame.MOUSEBUTTONDOWN and pygame.Rect(474, 341, 121, 44).collidepoint(event.pos):
            if COINS >= 20:
                WATER += 15
                if WATER > 100:
                    WATER = 100
                COINS -= 20
                up()


all_sprites = pygame.sprite.Group()

size = width, height = 720, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Timagotchi')

dis = Home()
tima = Tima()
tv = TV()
pillow = SPillow()
food = Food()
ex = Exit()

cur = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)
        if event.type == pygame.MOUSEMOTION and cur:
            all_sprites.update(event)

    now = round(time.time() + 0.05, 1)
    if (now - start_time) % 5 == 0:
        SLEEP -= 1
    if (now - start_time) % 100 == 0:
        FOOD -= 1
    if (now - start_time) % 60 == 0:
        WATER -= 1
    if (now - start_time) % 30 == 0:
        LOVE -= 1

    if SLEEP == 0 or FOOD == 0 or WATER == 0 or LOVE == 0:
        dis.kill()
        tima.kill()
        tv.kill()
        pillow.kill()
        ex.kill()
        food.kill()
        over()

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    pygame.time.delay(60)

pygame.quit()
