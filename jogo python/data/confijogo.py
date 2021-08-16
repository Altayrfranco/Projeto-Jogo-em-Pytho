import pygame
from pygame import mixer

AMARELO = (0xFF, 0XFF, 0X00)
PRETO = (0X00, 0X00, 0X00)
TELA_WIDTH = 800
TELA_HEIGHT = 600

BLK_WIDTH = TELA_WIDTH // 40
BLK_HEIGHT = TELA_HEIGHT // 20

pygame.init()

mixer.init()

pygame.mixer.music.load('data\TownTheme.mp3')
pygame.mixer.music.play(-1)


tela = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))

def load_image(img_set, x, y):
        img_orig = img_set.subsurface((x, y), (16, 16))
        img_scaled = pygame.transform.scale(img_orig, (BLK_WIDTH, BLK_HEIGHT))
        return img_scaled
