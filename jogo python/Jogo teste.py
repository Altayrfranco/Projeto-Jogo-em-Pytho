import pygame
from data.confijogo import *




mapa = [
        'pppppppppppppppppppppppppppppppppppppppp',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'p                                      p',
        'pppppppppppppppppppppppppppppppppppppppp',
]

mapa_obj = [

        '                                        ',
        '                           AAAAAA       ',
        '                          v          K  ',
        '          v                             ',
        '                              AAAAAA    ',
        '                                        ',
        '   AAA                                  ',
        '   AAA                                  ',
        '            AA              v           ',
        '           A A A                        ',
        '        v                               ',
        '                                        ',
        '                                        ',
        '                    v                   ',
        '                                        ',
        '                     C    C             ',
        '                        p               ',
        ' MMMMMM    AA AAA    C    C             ',
        ' MMMMMM                                 ',
        '                                        ',

]



tiles = pygame.image.load('img/basictiles.png').convert_alpha()
characters = pygame.image.load('img/characters.png').convert_alpha()
img_vaso = load_image(tiles, 48, 48)
img_grama = load_image(tiles, 16, 128)
img_parede = load_image(tiles, 48, 0)
img_arvore = load_image(tiles, 64, 144)
img_coluna = load_image(tiles, 48, 176)
img_poço = load_image(tiles, 112, 48)
img_mont = load_image(tiles, 112, 112)
img_castel = load_image(tiles, 48, 80)

def desenhar_mapa(map, caracter_imagem):
        for id_linha, linha in enumerate(map):
           for id_coluna, caracter in enumerate(linha):
                  if caracter in caracter_imagem:
                          x = id_coluna * BLK_WIDTH
                          y = id_linha * BLK_HEIGHT
                          img = caracter_imagem[caracter]
                          tela.blit(img, (x, y))

def colisao_mapa(personagem, map, lista_caracteres):
        colisoes = []
        for id_linha, linha in enumerate(map):
                for id_coluna, caracter in enumerate(linha):
                        if caracter in lista_caracteres:
                                x = id_coluna * BLK_WIDTH
                                y = id_linha * BLK_HEIGHT
                                r = pygame.Rect((x, y), (BLK_WIDTH, BLK_HEIGHT))
                                r2 = personagem.rect.copy()
                                r2.move_ip(personagem.vel_x, personagem.vel_y)
                                if r.colliderect(r2):
                                        colisao = {'linha': id_linha, 'coluna': id_coluna, 'caracteres': caracter}
                                        colisoes.append(colisao)
        return colisoes


class Personagem(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.vel_x = 0.0
                self.vel_y = 0.0
                car_img_1 = load_image(characters, 48, 0)
                car_img_2 = load_image(characters, 64, 0)
                car_img_3 = load_image(characters, 80, 0)
                car_img_4 = load_image(characters, 32, 48)
                car_img_5 = load_image(characters, 32, 64)
                car_img_6 = load_image(characters, 32, 80)
                self.lista_imagens = [car_img_1, car_img_2, car_img_3]
                self.image_idx = 0
                self.image = car_img_1
                self.rect = pygame.Rect((32, 32), (BLK_WIDTH, BLK_HEIGHT))

        def update(self):
                self.image = self.lista_imagens[self.image_idx]
                self.image_idx += 1
                if self.image_idx >= len(self.lista_imagens):
                        self.image_idx = 0

                colisoes = colisao_mapa(self, mapa, ['p'])
                if len(colisoes) == 0:
                        self.rect.move_ip(self.vel_x, self.vel_y)

                colisoes = colisao_mapa(self, mapa_obj, ['V'])

        def processar_evento(self, e):
                if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_d:
                                self.vel_x = 1.0
                        if e.key == pygame.K_a:
                                self.vel_x = -1.0
                        if e.key == pygame.K_w:
                                self.vel_y = -1.0
                        if e.key == pygame.K_s:
                                self.vel_y = 1.0

                if e.type == pygame.KEYUP:
                        if e.key in [pygame.K_a, pygame. K_d]:
                                self.vel_x = 0.0
                        if e.key in [pygame.K_w, pygame. K_s]:
                                self.vel_y = 0.0




heroi = Personagem()
grupo_heroi = pygame.sprite.Group(heroi)

while True:
        desenhar_mapa(mapa, {'p': img_parede, ' ' : img_grama})
        desenhar_mapa(mapa_obj, {'v': img_vaso, 'A': img_arvore, 'C': img_coluna, 'p': img_poço, 'M': img_mont, 'K': img_castel})



        grupo_heroi.draw(tela)
        pygame.display.update()

        grupo_heroi.update()

        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                        exit()
                heroi.processar_evento(e)