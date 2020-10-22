import pygame as pg
#----------------------------every time stuff-------------------------------------------------
lemo=''
for i in range(130):
	lemo += ' '
pg.init() 
screen = pg.display.set_mode((1000,500))
pg.display.set_caption(lemo+'TextEdit')
#------------------------------variables-----------------------------------------------------
n = 1
text = 'Login page'
text2 = 'Username'
text3 = 'Password'
text4 = 'sign in'
text5 = 'sign up'
text6 = 'Choose your profile photo'
text7 = 'Next'
font = pg.font.Font(None, 50)
fontx = pg.font.Font(None, 25)
fonty = pg.font.Font(None, 30)
fonta = pg.font.Font(None, 35)
text_b = font.render(text,True,(255,255,255))
text_e = fontx.render(text4,True,(255,255,255))
text_f = fontx.render(text5,True,(255,255,255))
umsg = ''
pmsg = ''
sambo = True
sembo = True
gay = False
bay = False
tay = False
say = False
may = False 
day = False 
imago = pg.image.load('profile photo.png')
imagi = pg.image.load('back.png')
#------------------------------functions-----------------------------------------------------
def colorpat(r,g,b):
	pg.draw.rect(screen,(r,g,b),(450,325,100,20))
	pg.draw.circle(screen,(r,g,b),(450,335),10)
	pg.draw.circle(screen,(r,g,b),(550,335),10)
def colorpat2(r,g,b):
	pg.draw.rect(screen,(r,g,b),(450,365,100,20))
	pg.draw.circle(screen,(r,g,b),(450,375),10)
	pg.draw.circle(screen,(r,g,b),(550,375),10)
def txtcolor(r,g,b):
	if not day and umsg == '':
		text_c = fonty.render(text2,True,(r,g,b))
		screen.blit(text_c,(450,185))
	else:
		if len(umsg) < 18:
			text_c = fonty.render(umsg,True,(255,255,255))
			screen.blit(text_c,(400,185))
		else:
			if len(umsg) < 18:
				text_c = fonty.render(umsg,True,(255,255,255))
				screen.blit(text_c,(400,185))
			else:
				kj = umsg[-18:]
				text_c = fonty.render(kj,True,(255,255,255))
				screen.blit(text_c,(400,185))
def txtcolor2(r,g,b):
	if not may and pmsg == '':
		text_c = fonty.render(text3,True,(r,g,b))
		screen.blit(text_c,(450,255))
	else:
		if len(pmsg) < 18:
			lj = len(pmsg)*'*'
			if not sembo:
				text_c = fonty.render(pmsg,True,(255,255,255))
				screen.blit(text_c,(400,255))
			else:
				text_c = fonta.render(lj,True,(255,255,255))
				screen.blit(text_c,(400,258))
		else:
			if not sembo:
				kj = pmsg[-18:]
				text_c = fonty.render(kj,True,(255,255,255))
				screen.blit(text_c,(400,255))
			else:
				kj = pmsg[-18:]
				lj = len(kj)*'*'
				text_c = fonta.render(lj,True,(255,255,255))
				screen.blit(text_c,(400,258))
#------------------------------boxes----------------------------------------------------------
t1 = pg.Rect(450,360,100,30)
t2 = pg.Rect(450,320,100,30)
t3 = pg.Rect(400,240,200,50)
t4 = pg.Rect(400,170,200,50)
t5 = pg.Rect(900,400,100,100)
t6 = pg.Rect(550,400,100,30)
#-----------------------------game loop-----------------------------------------------------
run = True
while run:
	imagm = pg.image.load('pokea'+str(n)+'.jpg')
	screen.fill((64,65,66))
	if sambo:
		pg.draw.rect(screen,(52,58,64),(250,50,500,370))
		pg.draw.line(screen,(0,255,0),[270,130],[730,130])

		pg.draw.rect(screen,(12,236,164),(400,165,200,60))
		pg.draw.circle(screen,(0,207,140),(400,195),30)
		pg.draw.circle(screen,(0,255,0),(600,195),30)

		pg.draw.rect(screen,(12,236,164),(400,235,200,60))
		pg.draw.circle(screen,(0,207,140),(400,265),30)
		pg.draw.circle(screen,(0,255,0),(600,265),30)

		pg.draw.rect(screen,(52,58,64),(400,170,200,50))
		pg.draw.rect(screen,(52,58,64),(400,240,200,50))
		pg.draw.rect(screen,(12,236,164),(450,320,100,30))
		pg.draw.rect(screen,(12,236,164),(450,360,100,30))

		pg.draw.circle(screen,(52,58,64),(400,195),25)
		pg.draw.circle(screen,(52,58,64),(600,195),25)
		pg.draw.circle(screen,(52,58,64),(400,265),25)
		pg.draw.circle(screen,(52,58,64),(600,265),25)

		pg.draw.circle(screen,(0,207,140),(450,335),15)
		pg.draw.circle(screen,(0,255,0),(550,335),15)

		pg.draw.circle(screen,(0,207,140),(450,375),15)
		pg.draw.circle(screen,(0,255,0),(550,375),15)

		if not gay:
			colorpat2(52,58,64)
		else:
			colorpat2(0,207,140)

		if not bay:
			colorpat(52,58,64)
		else:
			colorpat(0,207,140)

		screen.blit(text_b,(400,70))
		if not say:
			txtcolor(255,255,255)
		else:
			txtcolor(0,255,0)
		if not tay:
			txtcolor2(255,255,255)
		else:
			txtcolor2(0,255,0)
		screen.blit(text_e,(470,327))
		screen.blit(text_f,(470,367))
	else:
		pg.draw.rect(screen,(52,58,64),(350,50,300,400))
		pg.draw.line(screen,(0,255,0),[360,170],[640,170])
		pg.draw.circle(screen,(100,103,102),(500,110),50)
		pg.draw.circle(screen,(64,65,66),(500,310),70)
		if n!=5:
			screen.blit(imagm,(450,270))
		else:
			screen.blit(imagm,(460,270))
		text_go = fontx.render(text7,True,(255,255,255))
		screen.blit(imago,(478,80))
		screen.blit(imagi,(900,400))
		text_q = fonty.render(text6,True,(255,255,255))
		screen.blit(text_q,(370,185))
		screen.blit(text_go,(550,400))
	for i in pg.event.get():
		gay,bay,tay,say = False,False,False,False
		if i.type == pg.QUIT:
			quit()
		if i.type == pg.MOUSEMOTION:
			if t1.collidepoint(i.pos):
				gay = True
			elif t2.collidepoint(i.pos):
				bay = True	
			elif t3.collidepoint(i.pos):
				tay = True	
			elif t4.collidepoint(i.pos):
				say = True	
		if i.type == pg.MOUSEBUTTONDOWN:
			if t3.collidepoint(i.pos):
				may = not may
				day = False	
			elif t4.collidepoint(i.pos):
				day = not day
				may = False	
			elif t2.collidepoint(i.pos) and umsg!=''  and pmsg!='':
				sambo = False
			elif t5.collidepoint(i.pos):
				sambo = True
			elif t6.collidepoint(i.pos):
				if sambo == False:
					run = False
		if i.type == pg.KEYDOWN:
			if i.key == pg.K_BACKSPACE:
				if may:
					pmsg = pmsg[:-1]
				elif day:
					umsg = umsg[:-1]
			elif i.key == pg.K_RIGHT:
				if not sambo and n!=5:
					n+=1
			elif i.key == pg.K_LEFT:
				if not sambo and n!=1:
					n-=1
			else:
				if may:
					pmsg += i.unicode
				elif day:
					umsg += i.unicode
	pg.display.flip()