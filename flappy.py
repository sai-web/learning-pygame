import pygame as pg 
import random
pg.init()
screen = pg.display.set_mode((640,320))
pg.display.set_caption('flappy bird')
bg = pg.image.load('back.jpg')
pipe = pg.image.load('pipe.png')
pipe2 = pg.image.load('pipe2.png')
base = pg.image.load('flap.jpg')
bird = pg.image.load('bird2.png')
start = pg.image.load('start.png')
x = 0
xu = -210
xm = -420
y = 200
yu = 130
ym = 170
l = [200,170,130,150]
yt = 30
act = False
altered = False
score = 0
font = pg.font.Font(None,20)
def clash(x,y):
    bird_mask = pg.mask.from_surface(bird)
    top_mask = pg.mask.from_surface(pipe)
    bottom_mask = pg.mask.from_surface(pipe2)
    bottom_offset = (640-x-200,y-yt)
    top_offset = (640-x-200,y-400-yt)
    b_point = bird_mask.overlap(bottom_mask, bottom_offset)
    t_point = bird_mask.overlap(top_mask,top_offset)
    if t_point or b_point:
        return True 
    return False
runnin = True
while True:
    runnin = True
    if runnin == True:
        stat = pg.Rect(290,120,70,40)
    while runnin:
        screen.blit(bg,(0,0))
        screen.blit(start,(290,120))
        if score != 0:
            sc = font.render('Score:',True,(255,255,255))
            screen.blit(sc,(540,10))
            sco = font.render(str(score+1),True,(255,255,255))
            screen.blit(sco,(590,10))
        for i in pg.event.get():
            if i.type == pg.QUIT:
                quit()
            if i.type == pg.MOUSEBUTTONDOWN:
                if stat.collidepoint(i.pos):
                    score = 0
                    runnin = False
        pg.display.flip()
    while True:
        screen.blit(bg,(0,0))
        screen.blit(pipe,(640-x,y))
        screen.blit(pipe,(640-xu,yu))
        screen.blit(pipe,(640-xm,ym))
        screen.blit(pipe2,(640-x,y-400))
        screen.blit(pipe2,(640-xu,yu-400))
        screen.blit(pipe2,(640-xm,ym-400))
        screen.blit(bird,(200,yt))
        for i in pg.event.get():
            if i.type == pg.QUIT:
                quit()
            if i.type == pg.KEYDOWN:
                if (i.key == pg.K_UP) or (i.key == pg.K_SPACE):
                    act = True
            if i.type == pg.KEYUP:
                act = False
        if x > 700:
            altered = False
            y = l[random.randint(0,3)]
            x = 0
        if xu > 700:
            altered = False
            yu = l[random.randint(0,3)]
            xu = 0
        if xm > 700:
            altered = False
            ym = l[random.randint(0,3)]
            xm = 0
        x += 1
        xu += 1
        xm += 1
        if not act and yt < 250:
            yt += 2
        else:
            if yt > 0:
                yt-=2
        if (x > 400 or xu > 400 or xm > 400) and not altered:
            altered = True
            score += 1
        screen.blit(base,(0,280))
        sc = font.render('Score:',True,(255,255,255))
        screen.blit(sc,(540,10))
        sco = font.render(str(score),True,(255,255,255))
        screen.blit(sco,(590,10))
        if clash(x,y) or clash(xu,yu) or clash(xm,ym):
            x,xu,xm,y,yu,ym = 0,-210,-420,200,130,170
            break
        pg.display.flip()
        pg.time.delay(7)