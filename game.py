import pygame
from pygame.locals import *
from sys import exit

pygame.init()
#pygame.mixer.init()

pygame.mixer.music.load('sounds\BoxCat Games - Against the Wall.mp3')
pygame.mixer.music.play(-1)

largura = 640
altura = 480

PRETO = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('heroi/sprite_0.png'))
        self.sprites.append(pygame.image.load('heroi/sprite_1.png'))
        self.sprites.append(pygame.image.load('heroi/sprite_2.png'))
        self.sprites.append(pygame.image.load('heroi/sprite_3.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (512 / 4, 512 / 4))

        self.rect = self.image.get_rect()
        self.rect.topleft = 256, 360
        self.up = False
        self.left = False
        self.right = False
        self.down = False
        self.jump = False

    def cima(self):
        self.up = True

    def esquerda(self):
        self.left = True

    def direita(self):
        self.right = True

    def baixo(self):
        self.down = True

    def pula(self):
        self.jump = True

    def update(self):
        if self.up == True:
            if self.rect.y <= 480:
                self.up = False
            self.rect.y -= 13
        
        if self.left == True:
            if self.rect.x <= 640:
                self.left  = False
            self.rect.x -= 13

        if self.right == True:
            if self.rect.x >= - 640:
                self.right = False
            self.rect.x += 13

        if self.down == True:
            if self.rect.y >= -480:
                self.down = False
            self.rect.y += 13

# Qualquer erro associado a movimentação do personagem, está associada a condição abaixo

        if self.jump == True:
            if self.rect.y <= 368 & self.rect.y >= 367:
                self.jump = False
            self.rect.y -= 35

# Dimensionamento de movimentação linhas 70 a 80          
        
        if self.rect.y >= 369:
            self.rect.y = 369

        if self.rect.y <= -19:
            self.rect.y = -19
        
        if self.rect.x >= 539:
            self.rect.x = 539
        
        if self.rect.x <= -29:
            self.rect.x = -29
        
        self.atual = self.atual + 0.5
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (512 / 4, 512 / 4))

todas_as_sprites = pygame.sprite.Group()
personagem = Personagem()
todas_as_sprites.add(personagem)

imagem_fundo = pygame.image.load('fundo.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((PRETO))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                personagem.pula()

#        if event.type == KEYDOWN:
#            if event.key == K_w:
#                personagem.cima()
#            if event.key == K_a:
#                personagem.esquerda()
#            if event.key == K_d:
#                personagem.direita()
#            if event.key == K_s:
#                personagem.baixo()
         
    if pygame.key.get_pressed()[K_w]:
        personagem.cima()

    if pygame.key.get_pressed()[K_a]:
        personagem.esquerda()

    if pygame.key.get_pressed()[K_d]:
        personagem.direita()

    if pygame.key.get_pressed()[K_s]:
        personagem.baixo()
    
    tela.blit(imagem_fundo, (0, 0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()


# Caso a movimentação esteja muito fluida e a necessidade seja algo mais
# limitado, basta descomentar as linhas 91 a 99, e comentar as linhas 101
# a 111. Lembre-se que os blocos possuem identações diferentes. 