import pygame
import random

pygame.init()

sprite_event=pygame.USEREVENT+1
background_event=pygame.USEREVENT+2

Blue=pygame.Color('blue')
Yellow=pygame.Color('yellow')
Orange=pygame.Color('orange')
White=pygame.Color('white')

LightBlue=pygame.Color('LightBlue')
DarkBlue=pygame.Color('darkblue')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]
    
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit=False
        if self.rect.left<=0 or self.rect.right>=400:
            self.velocity[0]=-1*self.velocity[0]
            boundary_hit=True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.velocity[1]=-1*self.velocity[1]
            boundary_hit=True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_event))
            pygame.event.post(pygame.event.Event(background_event))
    
    def change_color(self):
        self.image.fill(random.choice([Blue,Yellow, Orange, White]))

def change_bg():
    global bg_color
    bg_color=random.choice([LightBlue,DarkBlue])

all_sprites = pygame.sprite.Group()

sp1=Sprite(White,20,30)
sp1.rect.x=random.randint(0,380)
sp1.rect.y=random.randint(0,370)

all_sprites.add(sp1)

screen=pygame.display.set_mode((400,400))
bg_color=Blue
screen.fill(bg_color)
exit = False

clock=pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==sprite_event:
            sp1.change_color()
        elif event.type==background_event:
            change_bg()
    
    all_sprites.update()
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()