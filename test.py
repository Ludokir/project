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
print()
