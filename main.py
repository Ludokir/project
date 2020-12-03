import pygame
import random
import sys
import os
import random

os.environ['SDL_VIDEO_WINDOW_POS'] = '0,30'

pygame.init()
FPS = 60
clock = pygame.time.Clock()

Info = pygame.display.Info()
W_S, H_S = Info.current_w, Info.current_h

BG = (25, 25, 25)
GAME_BG = (170, 200, 15)

max_bricks = 50
game_size = w, h = (W_S // 2), H_S  # размер игрового окна
game_pos = ((W_S - w) // 2), 0  # положение игрового окна
i = 0
speed_x = random.randint(5, 7)
speed_y = speed_y_start = random.randint(-8, -6)
block = 100

platform = pygame.image.load('img/platform1.png')
platform_rect = platform_rect_start = platform.get_rect(
    center=((W_S // 2), (H_S - 100)))
platform_rect.top = H_S - 100

ball = pygame.image.load('img/ball.png')
ball_rect = ball.get_rect(center=((W_S // 2), (H_S - 100)))
ball_rect = ball_rect_start = ball.get_rect(
    center=((W_S // 2), (H_S - 101 - (ball_rect.h // 2))))

print(platform_rect)


class Bricks(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.img_num = random.randint(0, 5)
        self.image_filename = f'img/brick{self.img_num}.png'
        self.image_orig = pygame.image.load(self.image_filename)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        global ball_rect, speed_y
        if ball_rect.colliderect(self.rect):
            self.rect = self.image.get_rect(center=(5000, 5000))
            speed_y = -speed_y


def init_bricks(max_bricks):
    for _ in range(max_bricks):
        brick = Bricks(random.randint(
            (w - (w // 2)), (w + (w // 2))), random.randint(0, H_S))
        all_brick.add(brick)


# начальные установки для платформы и шара
def init():
    global i, ball_rect, platform_rect
    if i == 0:
        ball_rect = ball_rect_start = ball.get_rect(
            center=((W_S // 2), (H_S - 101 - (ball_rect.h // 2))))
        platform_rect = platform_rect_start = platform.get_rect(
            center=((W_S // 2), (H_S - 100)))
        platform_rect.top = H_S - 100


# движение шара
def move():
    global ball_rect, i, speed_x, speed_y, speed_y_start, block, platform_rect
    if i <= block:
        ball_rect = ball_rect
    else:
        ball_rect = ball_rect.move(speed_x, speed_y)
    if ball_rect.top <= 0:
        speed_y = -speed_y
    if ball_rect.right >= (w + (w // 2)) or ball_rect.left <= (w - (w // 2)):
        speed_x = -speed_x
    if ball_rect.bottom >= platform_rect.top and \
        ball_rect.right <= platform_rect.right and \
            ball_rect.left >= platform_rect.left:
        speed_y = -speed_y
    else:
        speed_y = speed_y
    if ball_rect.bottom >= H_S:
        i = 0
        ball_rect = ball_rect_start
        platform_rect = platform_rect_start
        speed_y = speed_y_start


# основные команды
def run():
    global platform_rect, i, block
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
                e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION and i >= block:
            platform_rect.center = e.pos
            platform_rect.top = H_S - 100
            if platform_rect.right >= (w + (w // 2)):
                platform_rect.right = (w + (w // 2))
            if platform_rect.left <= (w - (w // 2)):
                platform_rect.left = (w - (w // 2))


'____________________________ MAIN ____________________________'

# pygame.display.set_icon(pygame.image.load(''))
pygame.display.set_caption('Cringe Арканоид')
screen = pygame.display.set_mode((W_S, H_S))
pygame.mouse.set_visible(True)

all_brick = pygame.sprite.Group()
init_bricks(max_bricks)

while True:
    i += 1  # задержка
    run()
    all_brick.update()
    screen.fill(BG)
    # игровое поле
    game = pygame.draw.rect(screen, GAME_BG, (game_pos, game_size))
    screen.blit(platform, platform_rect)
    screen.blit(ball, ball_rect)
    all_brick.draw(screen)
    move()
    init()
    pygame.display.update()
    clock.tick(FPS)
