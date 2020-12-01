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
game_size = w, h = (W_S // 2), H_S
game_pos = ((W_S - w) // 2), 0
platform_speed = 8

platform = pygame.image.load('platform.png')
platform_rect = platform.get_rect(center=((W_S // 2), (H_S - 100)))

print(platform_rect)


def run():
    global platform_rect
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
                e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            platform_rect.center = e.pos
            platform_rect.top = H_S - 100
            if platform_rect.right >= (w + (w // 2)):
                platform_rect.right = (w + (w // 2))
            if platform_rect.left <= (w - (w // 2)):
                platform_rect.left = (w - (w // 2))


'____________________________ MAIN ____________________________'

# pygame.display.set_icon(pygame.image.load(''))
pygame.display.set_caption('Арканоид')
screen = pygame.display.set_mode((W_S, H_S))
pygame.mouse.set_visible(False)


while True:
    run()
    screen.fill(BG)
    game = pygame.draw.rect(screen, GAME_BG, (game_pos, game_size))
    screen.blit(platform, platform_rect)
    pygame.display.update()
    clock.tick(FPS)
