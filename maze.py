from pygame import *

win_width = 700
win_height = 500


window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

class Sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 625:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 510-80:
            self.rect.y += self.speed

class Enemy(Sprite):
    direction = 'left'

    def move(self):
        if self.rect.x < 10:
            self.direction = 'right'
        if self.rect.x > 160:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed


        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, rgb, x,y,w,h):
        super().__init__()
        self.rgb = rgb
        self.width = w
        self.height = h
        self.wall = Surface((w,h))
        self.wall.fill(rgb)

        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.wall, (self.rect.x, self.rect.y))


player = Player('hero.png', 5, 65, 4)
monster = Enemy('cyborg.png', 80, 280, 2)
final = Sprite('treasure.png', 570,430, 0)

w1 = Wall((2,4,55), 50,50, 600, 10)
w2 = Wall((2,4,55), 650,50, 10, 800)
w3 = Wall((2,4,55), 550,130, 10, 200)
w4 = Wall((2,4,55), 220,420, 440, 10)
w5 = Wall((2,4,55), 310,330, 250, 10)
w6 = Wall((2,4,55), 300,130, 10, 210)
w7 = Wall((2,4,55), 10,130, 550, 10)
w8 = Wall((2,4,55), 210,230, 10, 200)
w9 = Wall((2,4,55), 10,140, 10, 370)

game = True
clock = time.Clock()
FPS = 60

#музика
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

font.init()

font = font.Font(None,500)
winer = font.render("win",True,(255,255,0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0, 0))
    w1.draw()
    player.reset()
    player.move()

    if sprite.collide_rect(player, monster) \
        or sprite.collide_rect(player, w1) \
            or sprite.collide_rect(player, w2) \
                 or sprite.collide_rect(player, w3) \
                     or sprite.collide_rect(player, w4)\
                        or sprite.collide_rect(player, w5) \
                            or sprite.collide_rect(player, w6)\
                                or sprite.collide_rect(player, w7) \
                                     or sprite.collide_rect(player, w8) \
                                        or sprite.collide_rect(player, w9):
                                
        player.rect.x = 5
        player.rect.y = 65

    monster.reset()
    monster.move()
    w1.draw()
    w2.draw()
    w3.draw()
    w4.draw()
    w5.draw()
    w6.draw()
    w7.draw()
    w8.draw()
    w9.draw()

    if sprite.collide_rect(player, final):
        window.blit(winer,(50,80))
        
    final.reset()
    display.update()
    clock.tick(FPS)