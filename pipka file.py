#Создай собственный Шутер!
from pygame import *
from time import time as timer
from time import *
from random import*
#создай окно игры
finish = False
window = display.set_mode((700, 500))
display.set_caption("бедная курица...")
background = transform.scale(image.load("cbble.jpg"), (700, 500))
#задай фон сцены
font.init()
fonts1 = font.SysFont("Arial", 20)
font2 = font.SysFont("Arial", 50)
win = font2.render("ПОБедАААА", True, (255, 200, 100))
#num_fire = 0
#mixer.init()
#kick = mixer.Sound('fire.ogg')
#mixer.music.load('space.ogg')
#mixer.music.play()
#clock = time.Clock()
FPS = 10
x1 = 20
y1 = 250
x2 = 600
y2 = 250
x3 = 3
y3 = 3
speed = 10
game = True
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y  -= self.speed
        if keys[K_DOWN] and self.rect.y < 695:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y  -= self.speed
        if keys[K_s] and self.rect.y < 695:
            self.rect.y += self.speed
        
player1 = Player("CTR.png", x2, y2, speed, 70, 90)
player2 = Player2("t.png", x1, y1, speed,70, 90)
ball = GameSprite("chkn.png", 350, 250, 3, 40, 40)

while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    ball.rect.x += x3
    ball.rect.y += y3
    if ball.rect.x > 650 or ball.rect.x < 0:
        game = False
    if ball.rect.y > 450 or ball.rect.y < 0:
        y3 *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        x3 *= -1
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    ball.reset()
    ball.update()
    display.update()
  #  clock.tick(FPS)
