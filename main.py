#---------------------------modules------------------------------------------------------------
import pygame as pg 
import socket as s
from loginpage import n,umsg
import datetime
import webbrowser as w
#----------------------------every time stuff-------------------------------------------------
lemo=''
for i in range(130):
	lemo += ' '
pg.init() 
screen = pg.display.set_mode((1000,500))
pg.display.set_caption(lemo+'TextEdit')
#-------------------------------variables-----------------------------------------------------
y = 500
x = 30
kop = False
normalized = False
xupin = 1000
xupine = 1000
yep = 10
ordinal = False
kop1 = False
kop2 = False
hbg = True
kj = 0
click = 0
clicky = 20
sedanis = -200
gaylussac = False
jap = False
semboy = False
lbg2 = True
cbg = False
sbg = False
setbux = False
sednom = 500
desmosin = False
xupyne = 1000
xupynee = 1000
wbg = False
wbg1 = False
nbg = False
learn = False
key = False
actu = False
acty = False
hud = False
lbg = False
flipine = 600
desmosin2 = False
seminarin = False
activate = False
flipiny = 230
activate_b1 = False
activate_b2 = False
activate_b3 = False
activate_b4 = False
activate_b5 = False
activate_b6 = False
activate_b7 = False
activate_b8 = False
activate_b9 = False
angre = False
angri = False
done = False
actuvatedbox21 = False
messages = True
coloring = False
flipin = 600
#----------------------------------------NAV_BOX----------------------------------------------------------------------------------
text = 'Type in your suggestions...'
text1 = 'Home'
text2 = 'Chatroom'
text3 = 'Notes'
text4 = 'Goals'
text5 = 'Codex'
text6 = 'Notifications'
text7 = 'News'
text8 = 'Settings'
text9 = 'About Us'
text10 = 'Users active'
text11 = 'Learn more'
text12 = 'type here...'
text13 = 'Profile'
text14 = 'Edit'
text15 = 'Create a new note'
#---------------------------------------messages-----------------------------------------------------------------------------------
msg = ''
smsg = ''
lmsg = ''
youn = 100
sednim = 1000
showcase = ''
namelist = ['Sai','Safwan','Vishvesh','Moin','Harish','Bishben','Jonathan','Sumith','Rick','Morty','Shakespeare','Salvador','Samba','Rayvanth','Jatin']
#-----------------------------pygame variables------------------------------------------------
sem = pg.surface.Surface((200,500))
suf = pg.surface.Surface((220,185))
saf = pg.surface.Surface((550,440))
sof = pg.surface.Surface((770,440))
syf = pg.surface.Surface((530,440))
sif = pg.surface.Surface((160,360))
swf = pg.surface.Surface((550,10000))
safepin = pg.surface.Surface((400,150))
daferw = pg.surface.Surface((800,10000))
font = pg.font.Font(None, 20)
fonty = pg.font.Font(None, 30)
fontz = pg.font.Font(None, 40)
#---------------------------------------images---------------------------------------------------
imag = pg.image.load('newlogo.png')
logo = pg.image.load('poke'+str(n)+'.jpg')
imagm = pg.image.load('pokea'+str(n)+'.jpg')
imagh = pg.image.load('datebox.png')
imagf = pg.image.load('weblogo.png')
#----------------------------------------functions-----------------------------------------------
def reper2():
	rep()
	if not key:
		txt_surface = font.render(text, True, (95,97,100))
		screen.blit(txt_surface,(750,y+10))
	elif key:
		txt_surface = font.render(msg, True, (95,97,100))
		screen.blit(txt_surface,(750,y+10))
	if nbg:
		pg.time.delay(1)
	elif hbg:
		pg.time.delay(1)
	elif cbg:
		pg.time.delay(1)
	elif lbg:
		pg.time.delay(0)
	elif wbg:
		pg.time.delay(1)
	else:
		pg.time.delay(0)
	pg.display.flip()
def rep():
	reper4()
	reper5(255,255,255)
	reper6(255,255,255)
	reper7(255,255,255)
	reper8(255,255,255)
	reper9(255,255,255)
	reper10(255,255,255)
	reper11(255,255,255)
	reper12(255,255,255)
	reper13(255,255,255)
def reper3(t,x,y,r,g,b):
	txt_sem = fonty.render(t, True, (r,g,b))
	sem.blit(txt_sem,(x,y))
def reper4():
	screen.blit(sem,(0,0))
def reper5(r,g,b):
	pg.draw.rect(sem,(52,58,64),(0,0,250,56))
	reper3(text1,45,18,r,g,b)
def reper6(r,g,b):
	pg.draw.rect(sem,(52,58,64),(0,56,250,56))
	reper3(text2,45,74,r,g,b)
def reper7(r,g,b):
	pg.draw.rect(sem,(52,58,64),(0,112,250,56))
	reper3(text3,45,130,r,g,b)
def reper8(r,g,b):
	pg.draw.rect(sem,(52,58,64),(0,168,250,56))
	reper3(text4,45,186,r,g,b)
def reper9(r,g,b):
	pg.draw.rect(sem,(52,58,64),(0,224,250,56))
	reper3(text5,45,242,r,g,b)
def reper10(r,g,b):
	pg.draw.rect(sem,(52,58,64),(0,280,250,56))
	reper3(text6,45,298,r,g,b)
def reper11(r,g,b):
	pg.draw.rect(sem,(52,58,64),(0,336,250,56))
	reper3(text7,45,354,r,g,b)
def reper12(r,g,b):
	pg.draw.rect(sem,(52,58,64),(0,392,250,56))
	reper3(text8,45,410,r,g,b)
def reper13(r,g,b):
	pg.draw.rect(sem,(52,58,64),(0,448,250,56))
	reper3(text9,45,466,r,g,b)
def reper14(r,g,b):
	pg.draw.rect(screen,(64,65,66),(495,450,150,50))
	txt_in = fonty.render(text11, True, (r,g,b))
	screen.blit(txt_in,(500,450))
#-----------------------------------------whole program in main loop is rewritten--------------------------
def reper():
	screen.fill((64,65,66))
	if hbg == True:
		screen.blit(imag,(350,20))
		pg.draw.rect(screen,(52,58,64),(750,20,240,250))
		pg.draw.line(screen,(0,255,0),[760,80],[980,80])
		txt_up = fonty.render(text10, True, (255,255,255))
		screen.blit(txt_up,(800,40))
		screen.blit(suf,(760,85))
		suf.fill((52,58,64))
		namey = nameo
		for i in namelist:
			txto = font.render(i,True, (255,255,255))
			suf.blit(txto,(0,namey))
			namey += 20
		if learn:
			reper14(255,0,0)
		else:
			reper14(255,255,255)
	elif cbg:
		pg.draw.rect(screen,(186,189,191),(240,440,460,50))
		pg.draw.circle(screen,(186,189,191),(240,465),25)
		pg.draw.circle(screen,(186,189,191),(700,465),25)
		if not acty:
			txt_sud = fonty.render(text12,True,(95,97,100))
		else:
			txt_sud = fonty.render(smsg,True,(95,97,100))
		screen.blit(txt_sud,(250,455))
		pg.draw.rect(screen,(52,58,64),(750,0,230,500))
		txt_sam = fontz.render(text13, True, (255,255,255))
		screen.blit(txt_sam,(820,20))
		txt_sum = fonty.render(umsg, True, (255,255,255))
		screen.blit(txt_sum,(820,210))
		pg.draw.circle(screen,(64,65,66),(870,130),70)
		screen.blit(imagm,(820,80))
		pg.draw.rect(screen,(12,236,164),(820,240,100,30))
		pg.draw.circle(screen,(0,207,140),(820,255),15)
		pg.draw.circle(screen,(0,255,0),(920,255),15)

		newbox(52,58,64)
		txt_sim = font.render(text14, True, (255,255,255))
		screen.blit(txt_sim,(855,247))
		screen.blit(saf,(200,0))
		if not semboy:
			saf.fill((64,65,66))
			swf.fill((64,65,66))
		saf.blit(swf,(0,kj))
	elif nbg:
		box12 = pg.Rect(780,390,150,30)
		pg.draw.rect(screen,(52,58,64),(760,20,200,400))
		screen.blit(syf,(210,30))
		screen.blit(sif,(780,20))
		'''if hud:
									click += 1
									textem = fonty.render('note'+str(click),True,(255,255,255))
									sif.blit(textem,(50,clicky))
									clicky += 40
									hud = False'''
		pg.draw.rect(screen,(12,236,164),(780,390,150,30))
		pg.draw.circle(screen,(0,207,140),(780,405),15)
		pg.draw.circle(screen,(0,255,0),(930,405),15)
		newbox2(52,58,64)
		txt_sud = font.render(text15,True,(255,255,255))
		screen.blit(txt_sud,(800,396))
	elif sbg:
		text_into = fontz.render(text6+' Panel',True,(255,255,255))
		screen.blit(text_into,(220,10))
		screen.blit(sof,(210,50))
		sof.blit(imagh,(500,0))
		txt_uhm = font.render('TODAY', True, (255,255,255))
		sof.blit(txt_uhm,(550,10))
		txt_sym = font.render(f'{now.strftime("%Y-%m-%d %H:%M")}', True, (255,255,255))
		sof.blit(txt_sym,(550,25))
	elif lbg:
		if lbg2:
			flipin = 600
			flipine = 600
			flipiny = 230
			sednom = 500
			sednim = 1000
			sedanis = -200
			boxybox = pg.Rect(250,465,80,20)
			text_macho = fontz.render('News Column',True,(255,255,255))
			screen.blit(text_macho,(490,15))
			if not normalized:
				text_mach = font.render('View more',True,(255,255,255))
				screen.blit(text_mach,(250,465))
			else:
				text_mach = font.render('View more',True,(255,0,0))
				screen.blit(text_mach,(250,465))
			sportstuff = pg.image.load('sportin.png')
			techno = pg.image.load('techno.png')
			health = pg.image.load('WHO.png')
			screen.blit(sportstuff,(600,30+70))
			screen.blit(techno,(230,30+70))
			screen.blit(health,(600,100+180))
		else:
			smbua = 0
			health = pg.image.load('WHO.png')
			techno = pg.image.load('techno.png')
			sportstuff = pg.image.load('sportin.png')
			trade = pg.image.load('trade.png')
			fashion = pg.image.load('fashion.png')
			politics = pg.image.load('politics.png')
			if not jap:
				text_mach = font.render('back',True,(255,255,255))
				screen.blit(text_mach,(250,450))
			else:
				text_mach = font.render('back',True,(255,0,0))
				screen.blit(text_mach,(250,450))
			boxibox = pg.Rect(250,450,100,50)
			screen.blit(trade,(600,99))
			screen.blit(fashion,(599,279))
			screen.blit(politics,(229,100))
	elif wbg:
		imagimag = pg.image.load('back1.png')
		alien = pg.image.load('safwan.png')
		mainon = pg.image.load('boxin2.png')
		profiler120 = pg.image.load('safprofile.png')
		project120 = pg.image.load('safproject.png')
		alien2 = pg.image.load('saip.png')
		profiler220 = pg.image.load('saiprofile.png')
		project220 = pg.image.load('saiproject.png')
		if not wbg1:
			box20 = pg.Rect(500,295,100,50)
			box22 = pg.Rect(485,245,130,40)
			screen.blit(imagf,(500,100))
			if not seminarin:
				colred(64,65,66)
			else:
				colred(0,207,140)
			txt_sudden = font.render('Visit our website.',True,(255,255,255))
			screen.blit(txt_sudden,(500,257))
			if not coloring:
				txt_suddim = font.render('Discover more',True,(255,255,255))
				pg.draw.rect(screen,(64,65,66),(495,300,100,50))
				screen.blit(txt_suddim,(505,300))
			else:
				txt_suddim = font.render('Discover more',True,(0,255,0))
				pg.draw.rect(screen,(64,65,66),(495,300,100,50))
				screen.blit(txt_suddim,(505,300))
			txt_suddof = font.render('Get Source code on github',True,(0,255,255))
			screen.blit(txt_suddof,(470,400+50))
			txt_lines = font.render('------------------------------------------',True,(0,255,255))
			screen.blit(txt_lines,(470,410+50))
		else:
			actuvatedbox21 = True
			sambar = 7
			box21 = pg.Rect(920,0,50,50)
			screen.blit(imagimag,(930,0))
			screen.blit(mainon,(300,130+200))
			screen.blit(mainon,(300,130))
			screen.blit(alien,(220,50+200))	
			screen.blit(alien2,(220,50))
			text_inf = font.render('Co-Founder',True,(255,255,255))
			screen.blit(text_inf,(340,140+200))	
			text_into = font.render('Syed Safwan',True,(255,255,255))
			screen.blit(text_into,(340,155+200))
			text_ink = font.render('Founder',True,(255,255,255))
			screen.blit(text_ink,(340,140))	
			text_inko = font.render('Sai Sumith',True,(255,255,255))
			screen.blit(text_inko,(340,155))
			if desmosin:
				screen.blit(project120,(710,350))
				screen.blit(profiler120,(710,50))
			elif desmosin2:
				screen.blit(project220,(710,350))
				screen.blit(profiler220,(710,50))
	pg.draw.rect(screen,(255,243,243),(750,y,200,36))
	pg.draw.circle(screen,(255,243,243),(750,y+18),18)
	pg.draw.circle(screen,(255,243,243),(950,y+18),18)
def tcolor(x,y):
	if x == True:
		reper4()
		y(255,0,0)
	else:
		reper4()
		y(255,255,255)
def newbox(r,g,b):
	pg.draw.rect(screen,(r,g,b),(820,243,100,24))
	pg.draw.circle(screen,(r,g,b),(820,255),12)
	pg.draw.circle(screen,(r,g,b),(920,255),12)
def newbox2(r,g,b):
	pg.draw.rect(screen,(r,g,b),(780,393,150,24))
	pg.draw.circle(screen,(r,g,b),(780,405),12)
	pg.draw.circle(screen,(r,g,b),(930,405),12)
def notificationboxes(message):
	global youn
	nem = datetime.datetime.now()
	temin = fonty.render(message,True,(255,255,255))
	pg.draw.rect(sof,(152,149,149),(50,youn,670,40))
	pg.draw.circle(sof,(152,149,149),(50,youn+20),20)
	pg.draw.circle(sof,(152,149,149),(720,youn+20),20)
	sof.blit(temin,(50,youn+10))
	temin2 = fonty.render(f'{nem.hour}:{nem.minute}:{nem.second}',True,(255,255,255))
	sof.blit(temin2,(600,youn+10))
	youn += 50
def colred(r,g,b):
	pg.draw.rect(screen,(12,236,164),(500,245,100,40))
	pg.draw.circle(screen,(0,207,140),(500,265),20)
	pg.draw.circle(screen,(0,255,0),(600,265),20)
	pg.draw.rect(screen,(r,g,b),(500,250,100,30))
	pg.draw.circle(screen,(r,g,b),(500,265),15)
	pg.draw.circle(screen,(r,g,b),(600,265),15)
#------------------------------------------boxes--------------------------------------------------
input_box = pg.Rect(750,440,200,36)
box1 = pg.Rect(0,0,200,56)
box2 = pg.Rect(0,56,200,56)
box3 = pg.Rect(0,112,200,56)
box4 = pg.Rect(0,168,200,56)
box5 = pg.Rect(0,224,200,56)
box6 = pg.Rect(0,280,200,56)
box7 = pg.Rect(0,336,200,56)
box8 = pg.Rect(0,392,200,56)
box9 = pg.Rect(0,448,200,56)
box24 = pg.Rect(300,130+200,200,60)
box25 = pg.Rect(300,130,200,60)
sockstr = pg.Rect(500,440,110,30)
afnet = pg.Rect(760,85,220,185)
sur = pg.Rect(0,0,50,50)
#----------------------------------------Game loop------------------------------------------------
namey = 0
nameo = 0
while True:
	now = datetime.datetime.now()
	if not activate and not actu:
		screen.fill((64,65,66))
	if (activate_b1 == False) and (activate_b2 == False) and (activate_b3 == False) and (activate_b4 == False) and (activate_b5 == False) and (activate_b6 == False) and (activate_b7 == False) and (activate_b8 == False) and (activate_b9 == False):
		rep()
	if hbg:
		screen.blit(imag,(350,20))
		pg.draw.rect(screen,(52,58,64),(750,20,240,250))
		pg.draw.line(screen,(0,255,0),[760,80],[980,80])
		txt_up = fonty.render(text10, True, (255,255,255))
		screen.blit(txt_up,(800,40))
		screen.blit(suf,(760,85))
		suf.fill((52,58,64))
		namey = nameo
		for i in namelist:
			txto = font.render(i,True, (255,255,255))
			suf.blit(txto,(0,namey))
			namey += 20
		if learn:
			reper14(255,0,0)
		else:
			reper14(255,255,255)
	elif cbg:
		box10 = pg.Rect(240,440,460,50)
		box11 = pg.Rect(820,240,100,30)
		if not activate:
			pg.draw.rect(screen,(52,58,64),(750,0,230,500))
			txt_sam = fontz.render(text13, True, (255,255,255))
			screen.blit(txt_sam,(820,20))
			txt_sum = fonty.render(umsg, True, (255,255,255))
			screen.blit(txt_sum,(820,210))
			pg.draw.circle(screen,(64,65,66),(870,130),70)
			screen.blit(imagm,(820,80))
			pg.draw.rect(screen,(12,236,164),(820,240,100,30))
			pg.draw.circle(screen,(0,207,140),(820,255),15)
			pg.draw.circle(screen,(0,255,0),(920,255),15)
			if not angre:
				newbox(52,58,64)
			else:
				newbox(0,207,140)
			txt_sim = font.render(text14, True, (255,255,255))
			screen.blit(txt_sim,(855,247))
		if not acty:
			screen.blit(saf,(200,0))
			if not semboy:
				saf.fill((64,65,66))
				swf.fill((64,65,66))
			txt_sud = fonty.render(text12,True,(95,97,100))
			saf.blit(swf,(0,kj))
			pg.draw.rect(screen,(186,189,191),(240,440,460,50))
			pg.draw.circle(screen,(186,189,191),(240,465),25)
			pg.draw.circle(screen,(186,189,191),(700,465),25)
			screen.blit(txt_sud,(250,455))
		else:
			screen.blit(saf,(200,0))
			saf.blit(swf,(0,kj))
			txt_sud = fonty.render(showcase,True,(95,97,100))
			pg.draw.rect(screen,(186,189,191),(240,440,460,50))
			pg.draw.circle(screen,(186,189,191),(240,465),25)
			pg.draw.circle(screen,(186,189,191),(700,465),25)
			screen.blit(txt_sud,(250,455))
	elif nbg:
		box12 = pg.Rect(780,390,150,30)
		pg.draw.rect(screen,(52,58,64),(760,20,200,400))
		screen.blit(syf,(210,30))
		screen.blit(sif,(780,20))
		if hud:
			click += 1
			textem = fonty.render('note'+str(click),True,(255,255,255))
			sif.blit(textem,(50,clicky))
			clicky += 40
			hud = False
		pg.draw.rect(screen,(12,236,164),(780,390,150,30))
		pg.draw.circle(screen,(0,207,140),(780,405),15)
		pg.draw.circle(screen,(0,255,0),(930,405),15)
		if not angri:
			newbox2(52,58,64)
		else:
			newbox2(20,207,140)
		txt_sud = font.render(text15,True,(255,255,255))
		screen.blit(txt_sud,(800,396))
	elif sbg:
		text_into = fontz.render(text6+' Panel',True,(255,255,255))
		screen.blit(text_into,(220,10))
		screen.blit(sof,(210,50))
		sof.blit(imagh,(500,0))
		txt_uhm = font.render('TODAY', True, (255,255,255))
		sof.blit(txt_uhm,(550,10))
		txt_sym = font.render(f'{now.strftime("%Y-%m-%d %H:%M")}', True, (255,255,255))
		sof.blit(txt_sym,(550,25))
		if messages:
			sof.fill((64,65,66))
			notificationboxes('testing')
			notificationboxes('same here')
			messages = False
		if activate:
			pg.draw.rect(screen,(255,243,243),(750,y,200,36))
			pg.draw.circle(screen,(255,243,243),(750,y+18),18)
			pg.draw.circle(screen,(255,243,243),(950,y+18),18)
			if not key:
				txt_surface = font.render(text, True, (95,97,100))
				screen.blit(txt_surface,(750,y+10))
			elif key:
				txt_surface = font.render(msg, True, (95,97,100))
				screen.blit(txt_surface,(750,y+10))
	elif wbg:
		imagimag = pg.image.load('back1.png')
		alien = pg.image.load('safwan.png')
		mainon = pg.image.load('boxin2.png')
		profiler120 = pg.image.load('safprofile.png')
		project120 = pg.image.load('safproject.png')
		alien2 = pg.image.load('saip.png')
		profiler220 = pg.image.load('saiprofile.png')
		project220 = pg.image.load('saiproject.png')
		if not wbg1:
			box20 = pg.Rect(500,295,100,50)
			box22 = pg.Rect(485,245,130,40)
			screen.blit(imagf,(500,100))
			if not seminarin:
				colred(64,65,66)
			else:
				colred(0,207,140)
			txt_sudden = font.render('Visit our website.',True,(255,255,255))
			screen.blit(txt_sudden,(500,257))
			if not coloring:
				txt_suddim = font.render('Discover more',True,(255,255,255))
				pg.draw.rect(screen,(64,65,66),(495,300,100,50))
				screen.blit(txt_suddim,(505,300))
			else:
				txt_suddim = font.render('Discover more',True,(0,255,0))
				pg.draw.rect(screen,(64,65,66),(495,300,100,50))
				screen.blit(txt_suddim,(505,300))
			txt_suddof = font.render('Get Source code on github',True,(0,255,255))
			screen.blit(txt_suddof,(470,400+50))
			txt_lines = font.render('------------------------------------------',True,(0,255,255))
			screen.blit(txt_lines,(470,410+50))
		else:
			actuvatedbox21 = True
			sambar = 7
			box21 = pg.Rect(920,0,50,50)
			screen.blit(imagimag,(930,0))
			screen.blit(mainon,(300,130+200))
			screen.blit(mainon,(300,130))
			screen.blit(alien,(220,50+200))	
			screen.blit(alien2,(220,50))
			text_inf = font.render('Co-Founder',True,(255,255,255))
			screen.blit(text_inf,(340,140+200))	
			text_into = font.render('Syed Safwan',True,(255,255,255))
			screen.blit(text_into,(340,155+200))
			text_ink = font.render('Founder',True,(255,255,255))
			screen.blit(text_ink,(340,140))	
			text_inko = font.render('Sai Sumith',True,(255,255,255))
			screen.blit(text_inko,(340,155))
			if desmosin:
				while xupin != 700:
					screen.blit(profiler120,(xupin,50))
					xupin -= 10
					pg.display.flip()
					pg.time.delay(sambar)
					sambar += 1
				sambar = 0
				while xupyne != 700:
					screen.blit(project120,(xupyne,350))
					xupyne -= 10
					pg.display.flip()
					pg.time.delay(sambar)
					sambar += 1
				screen.blit(project120,(710,350))
				screen.blit(profiler120,(710,50))
				sambar = 0
			else:
				while xupyne != 1000:
					screen.fill((64,65,66))
					rep()
					box21 = pg.Rect(920,0,50,50)
					screen.blit(imagimag,(930,0))
					screen.blit(mainon,(300,130+200))
					screen.blit(mainon,(300,130))
					screen.blit(alien,(220,50+200))	
					screen.blit(alien2,(220,50))
					text_inf = font.render('Co-Founder',True,(255,255,255))
					screen.blit(text_inf,(340,140+200))	
					text_into = font.render('Syed Safwan',True,(255,255,255))
					screen.blit(text_into,(340,155+200))
					text_ink = font.render('Founder',True,(255,255,255))
					screen.blit(text_ink,(340,140))	
					text_inko = font.render('Sai Sumith',True,(255,255,255))
					screen.blit(text_inko,(340,155))
					screen.blit(project120,(xupyne,350))
					xupyne += 10
					screen.blit(profiler120,(710,50))
					pg.display.flip()
					pg.time.delay(sambar)
					sambar += 1
				sambar = 0
				while xupin != 1000:
					screen.fill((64,65,66))
					rep()
					box21 = pg.Rect(920,0,50,50)
					screen.blit(imagimag,(930,0))
					screen.blit(mainon,(300,130+200))
					screen.blit(mainon,(300,130))
					screen.blit(alien,(220,50+200))	
					screen.blit(alien2,(220,50))
					text_inf = font.render('Co-Founder',True,(255,255,255))
					screen.blit(text_inf,(340,140+200))	
					text_into = font.render('Syed Safwan',True,(255,255,255))
					screen.blit(text_into,(340,155+200))
					text_ink = font.render('Founder',True,(255,255,255))
					screen.blit(text_ink,(340,140))	
					text_inko = font.render('Sai Sumith',True,(255,255,255))
					screen.blit(text_inko,(340,155))
					screen.blit(profiler120,(xupin,50))
					xupin += 10
					pg.display.flip()
					pg.time.delay(sambar)
					sambar += 1
				screen.blit(project120,(xupin,350))
				screen.blit(profiler120,(xupin,50))
				sambar = 0
			if desmosin2:
				while xupine != 700:
					screen.blit(profiler220,(xupine,50))
					xupine -= 10
					pg.display.flip()
					pg.time.delay(sambar)
					sambar += 1
				sambar = 0
				while xupynee != 700:
					screen.blit(project220,(xupynee,350))
					xupynee -= 10
					pg.display.flip()
					pg.time.delay(sambar)
					sambar += 1
				screen.blit(project220,(710,350))
				screen.blit(profiler220,(710,50))
				sambar = 0
			else:
				while xupynee != 1000:
					screen.fill((64,65,66))
					rep()
					box21 = pg.Rect(920,0,50,50)
					screen.blit(imagimag,(930,0))
					screen.blit(mainon,(300,130+200))
					screen.blit(mainon,(300,130))
					screen.blit(alien,(220,50+200))
					screen.blit(alien2,(220,50))	
					text_inf = font.render('Co-Founder',True,(255,255,255))
					screen.blit(text_inf,(340,140+200))	
					text_into = font.render('Syed Safwan',True,(255,255,255))
					screen.blit(text_into,(340,155+200))
					text_ink = font.render('Founder',True,(255,255,255))
					screen.blit(text_ink,(340,140))	
					text_inko = font.render('Sai Sumith',True,(255,255,255))
					screen.blit(text_inko,(340,155))
					screen.blit(project220,(xupynee,350))
					xupynee += 10
					screen.blit(profiler220,(710,50))
					pg.display.flip()
					pg.time.delay(sambar)
					sambar += 1
				sambar = 0
				while xupine != 1000:
					screen.fill((64,65,66))
					rep()
					box21 = pg.Rect(920,0,50,50)
					screen.blit(imagimag,(930,0))
					screen.blit(mainon,(300,130+200))
					screen.blit(mainon,(300,130))
					screen.blit(alien,(220,50+200))
					screen.blit(alien2,(220,50))	
					text_inf = font.render('Co-Founder',True,(255,255,255))
					screen.blit(text_inf,(340,140+200))	
					text_into = font.render('Syed Safwan',True,(255,255,255))
					screen.blit(text_into,(340,155+200))
					text_ink = font.render('Founder',True,(255,255,255))
					screen.blit(text_ink,(340,140))	
					text_inko = font.render('Sai Sumith',True,(255,255,255))
					screen.blit(text_inko,(340,155))
					screen.blit(profiler220,(xupine,50))
					xupine += 10
					pg.display.flip()
					pg.time.delay(sambar)
					sambar += 1
				screen.blit(project120,(xupine,350))
				screen.blit(profiler120,(xupine,50))
				sambar = 0
		if activate:
			pg.draw.rect(screen,(255,243,243),(750,y,200,36))
			pg.draw.circle(screen,(255,243,243),(750,y+18),18)
			pg.draw.circle(screen,(255,243,243),(950,y+18),18)
			if not key:
				txt_surface = font.render(text, True, (95,97,100))
				screen.blit(txt_surface,(750,y+10))
			elif key:
				txt_surface = font.render(msg, True, (95,97,100))
				screen.blit(txt_surface,(750,y+10))
	elif lbg:
		if lbg2:
			flipin = 600
			flipine = 600
			flipiny = 230
			sednom = 500
			sednim = 1000
			sedanis = -200
			boxybox = pg.Rect(250,465,80,20)
			text_macho = fontz.render('News Column',True,(255,255,255))
			screen.blit(text_macho,(490,15))
			if not normalized:
				text_mach = font.render('View more',True,(255,255,255))
				screen.blit(text_mach,(250,465))
			else:
				text_mach = font.render('View more',True,(255,0,0))
				screen.blit(text_mach,(250,465))
			sportstuff = pg.image.load('sportin.png')
			techno = pg.image.load('techno.png')
			health = pg.image.load('WHO.png')
			screen.blit(sportstuff,(600,30+70))
			screen.blit(techno,(230,30+70))
			screen.blit(health,(600,100+180))
		else:
			smbua = 0
			health = pg.image.load('WHO.png')
			techno = pg.image.load('techno.png')
			sportstuff = pg.image.load('sportin.png')
			trade = pg.image.load('trade.png')
			fashion = pg.image.load('fashion.png')
			politics = pg.image.load('politics.png')
			if not jap:
				text_mach = font.render('back',True,(255,255,255))
				screen.blit(text_mach,(250,450))
			else:
				text_mach = font.render('back',True,(255,0,0))
				screen.blit(text_mach,(250,450))
			boxibox = pg.Rect(250,450,100,50)
			while flipin != 1000:
				screen.blit(techno,(230,30+70))
				screen.blit(health,(flipin,100+180))
				screen.blit(sportstuff,(600,30+70))
				flipin += 4
				pg.display.flip()
				pg.time.delay(smbua)
			while flipine != 1000:
				screen.fill((64,65,66))
				rep()
				screen.blit(techno,(230,30+70))
				screen.blit(sportstuff,(flipine,30+70))
				pg.display.flip()
				pg.time.delay(smbua)
				flipine += 4
			while flipiny > -200:
				screen.fill((64,65,66))
				rep()
				screen.blit(techno,(flipiny,30+70))
				rep()
				pg.display.flip()
				pg.time.delay(smbua)
				flipiny -= 4
			smbua = 10
			while sednom != 100:
				screen.fill((64,65,66))
				rep()
				screen.blit(trade,(600,sednom))
				sednom -= 4
				pg.display.flip()
				pg.time.delay(smbua)
				smbua -= 1
			screen.blit(trade,(600,99))
			smbua = 10
			while sednim != 600:
				screen.blit(fashion,(sednim,279))
				sednim -= 2
				pg.display.flip()
				pg.time.delay(smbua)
				smbua -= 1
			screen.blit(fashion,(599,279))
			smbua = 1
			while sedanis < 230:
				screen.fill((64,65,66))
				screen.blit(politics,(sedanis,100))
				rep()
				screen.blit(fashion,(599,279))
				screen.blit(trade,(600,99))
				sedanis += 7
				rep()
				pg.display.flip()
				pg.time.delay(smbua)
				smbua -= 1
			screen.blit(politics,(229,100))
			if activate:
				pg.draw.rect(screen,(255,243,243),(750,y,200,36))
				pg.draw.circle(screen,(255,243,243),(750,y+18),18)
				pg.draw.circle(screen,(255,243,243),(950,y+18),18)
				if not key:
					txt_surface = font.render(text, True, (95,97,100))
					screen.blit(txt_surface,(750,y+10))
				elif key:
					txt_surface = font.render(msg, True, (95,97,100))
					screen.blit(txt_surface,(750,y+10))
	elif setbux:
		pg.draw.rect(screen,(192,192,192),(420,60,300,30))
		pg.draw.circle(screen,(192,192,192),(420,75),15)
		pg.draw.circle(screen,(192,192,192),(720,75),15)
		verset = pg.image.load('setpro.png')
		screen.blit(verset,(300,170))
		verlock = pg.image.load('setlock.png')
		screen.blit(verlock,(550,173))
		verphone = pg.image.load('setphone.png')
		screen.blit(verphone,(800,173))
		vercode = pg.image.load('setcode.png')
		screen.blit(vercode,(300,330))
		verper = pg.image.load('setper.png')
		screen.blit(verper,(550,330))
		vergame = pg.image.load('setgame.png')
		screen.blit(vergame,(800,330))
		txt_settin = fontz.render('Settings', True, (197,197,197))
		screen.blit(txt_settin,(500,20))
		txt_settin2 = font.render('type to search', True, (95,97,100))
		screen.blit(txt_settin2,(420,67))
	elif kop:
		imagimag = pg.image.load('back1.png')
		txt_settin2 = fontz.render('Codex', True, (197,197,197))
		screen.blit(txt_settin2,(550,50))
		metax = pg.image.load('metagamer.png')
		screen.blit(metax,(300,150))
		builboi = pg.Rect(900,10,100,100)
		if not kop1:
			bixup = pg.Rect(300,150,100,100)
		if not kop2:
			bixup2 = pg.Rect(300,270,100,100)
		txt_settin3 = fonty.render('Metagamer', True, (197,197,197))
		screen.blit(txt_settin3,(300,270))
		setcodeeditor = pg.image.load('icode.png')
		screen.blit(setcodeeditor,(550,150))
		txt_settin3 = fonty.render('Code Editors', True, (197,197,197))
		screen.blit(txt_settin3,(530,270))
		setnetin = pg.image.load('netin.png')
		screen.blit(setnetin,(800,150))
		txt_settin4 = fonty.render('Webapps', True, (197,197,197))
		screen.blit(txt_settin4,(805,270))
		setprof = pg.image.load('projo.png')
		screen.blit(setprof,(400,320))
		txt_settin4 = fonty.render('Professional', True, (197,197,197))
		screen.blit(txt_settin4,(390,430))
		setenter = pg.image.load('enterboss.png')
		screen.blit(setenter,(670,320))
		txt_settin5 = fonty.render('Entertainment', True, (197,197,197))
		screen.blit(txt_settin5,(660,430))
		if kop1:
			screen.fill((64,65,66))
			screen.blit(imagimag,(900,10))
	done = False
#-----------------------------events in program-------------------------------------------------------
	for i in pg.event.get():
		activate_b1 = False
		activate_b2 = False
		activate_b3 = False
		activate_b4 = False
		activate_b5 = False
		activate_b6 = False
		activate_b7 = False
		activate_b8 = False
		activate_b9 = False
		learn = False
		angre = False
		angri = False
		normalized = False
		jap = False
		if i.type == pg.QUIT:
			quit()
		if i.type == pg.MOUSEMOTION:
			if input_box.collidepoint(i.pos):
				activate = True
				while y > 440:
					reper()
					if cbg:
						y-=2
					elif lbg:
						y-=4
					elif wbg:
						y-=4
					else:
						y-=1
					reper2()
			elif box1.collidepoint(i.pos):
				activate_b1 = True
			elif box2.collidepoint(i.pos):
				activate_b2 = True
			elif box3.collidepoint(i.pos):
				activate_b3 = True
			elif box4.collidepoint(i.pos):
				activate_b4 = True
			elif box5.collidepoint(i.pos):
				activate_b5 = True
			elif box6.collidepoint(i.pos):
				activate_b6 = True
			elif box7.collidepoint(i.pos):
				activate_b7 = True
			elif box8.collidepoint(i.pos):
				activate_b8 = True
			elif box9.collidepoint(i.pos):
				activate_b9 = True
			elif sockstr.collidepoint(i.pos):
				learn = True
			elif not input_box.collidepoint(i.pos):
				activate = False
				while y<501:
					reper()
					if cbg:
						y+=2
					elif lbg:
						y+=4
					elif wbg:
						y+=4
					else:
						y+=1
					reper2()
			if cbg:
				if box11.collidepoint(i.pos):
					angre = True
			elif nbg:
				if box12.collidepoint(i.pos):
					angri = True
			elif wbg:
				if box20.collidepoint(i.pos):
					coloring = True
				elif box22.collidepoint(i.pos):
					seminarin = True
				else:
					coloring = False
					seminarin = False
			elif lbg:
				if lbg2:
					if boxybox.collidepoint(i.pos):
						normalized = True
				else:
					if boxibox.collidepoint(i.pos):
						jap = True
		if i.type == pg.MOUSEBUTTONDOWN:
			if box1.collidepoint(i.pos):
				hbg = True
				cbg = False
				acty = False
				nbg = False
				sbg = False
				wbg = False
				lbg = False
				setbux = False
				kop = False
			elif box2.collidepoint(i.pos):
				hbg = False
				cbg = True
				nbg = False
				sbg = False
				wbg = False
				lbg = False
				setbux = False
				kop = False
			elif box3.collidepoint(i.pos):
				hbg = False
				cbg = False 
				nbg = True
				sbg = False
				wbg = False
				lbg = False
				setbux = False
				kop = False
				try:
					sif.fill((52,58,64))
				except Exception as e:
					print(e)
			elif box5.collidepoint(i.pos):
				kop = True
				hbg = False
				cbg = False 
				nbg = False
				sbg = False
				wbg = False
				lbg = False
				setbux = False
			elif box6.collidepoint(i.pos):
				hbg = False
				cbg = False
				sbg = True
				nbg = False
				wbg = False
				lbg = False
				setbux = False
				kop = False
			elif box7.collidepoint(i.pos):
				hbg = False
				cbg = False
				sbg = False
				nbg = False
				wbg = False
				lbg = True
				setbux = False
				kop = False
			elif box8.collidepoint(i.pos):
				hbg = False
				cbg = False
				sbg = False
				nbg = False
				wbg = False
				lbg = False
				setbux = True
				kop = False
			elif box9.collidepoint(i.pos):
				hbg = False
				cbg = False
				sbg = False
				nbg = False
				wbg = True
				lbg = False
				setbux = False
				kop = False
			elif i.button == 5:
				if nameo+len(namelist)*20 != 180 and afnet.collidepoint(i.pos):
					nameo -= 10
				elif cbg == True:
					kj -= 10
				elif sbg:
					 youn -= 1
			elif i.button == 4:
				if nameo <= 0 and afnet.collidepoint(i.pos):
					nameo += 10
				elif cbg == True and kj<0:
					kj += 10
				elif sbg:
					youn += 1
			elif cbg:
				if box10.collidepoint(i.pos):
					acty = not acty
			elif nbg:
				if box12.collidepoint(i.pos):
					hud = True
			elif wbg:
				if box20.collidepoint(i.pos):
					wbg1 = True
				if actuvatedbox21:
					if box21.collidepoint(i.pos):
						wbg1 = False
				if wbg1:
					if box24.collidepoint(i.pos):
						desmosin = True
						desmodin2 = False
						xupine = 1000
						xupynee = 1000
					else:
						desmosin = False
					if box25.collidepoint(i.pos):
						desmosin2 = True
						desmodin = False
						xupin = 1000
						xupyne = 1000
					else:
						desmosin2 = False
			elif lbg:
				if boxybox.collidepoint(i.pos):
					lbg2 = False
				elif boxibox.collidepoint(i.pos):
					lbg2 = True
			elif kop:
				if bixup.collidepoint(i.pos):
					kop1 = True
					if builboi.collidepoint(i.pos):
						kop1 = False
				elif bixup2.collidepoint(i.pos):
					kop2 = True
		if i.type == pg.KEYDOWN:
			countr = 1
			if activate:
				key = True
				if i.key == pg.K_BACKSPACE:
					msg = msg[:-1]
				elif i.key == pg.K_RETURN:
					if msg != '':
						print('sent',msg)
						msg = ''
						key = False
					else:
						continue
				else:
					msg += i.unicode
				reper()
				reper2()
			elif acty:
				if i.key == pg.K_BACKSPACE:
					gaylussac = True
				elif i.key == pg.K_RETURN:
					if smsg != '':
						semboy = True
						print('sent',smsg)
						masg = ''
						countc = 0
						for i in smsg:
							if ord(i)<97 and ord(i)>65:
								countc += 5
						while len(smsg) > 30:
							ordinal = True
							masg += smsg[0:31]
							smsg = smsg[31:]
							pg.draw.rect(swf,(95,97,100),(50,yep,350,30))
							fyup = fonty.render(masg,True,(255,255,255))
							swf.blit(fyup,(50,yep+4))
							masg = ''
							yep += 30
							countr += 1
						else:
							if not ordinal:
								tent = len(smsg)*12
								masg += smsg
								pg.draw.rect(swf,(95,97,100),(50,yep,tent,30))
								pg.draw.circle(swf,(95,97,100),(50+tent,yep+15),15)
								fyup = fonty.render(masg,True,(255,255,255))
								swf.blit(fyup,(50,yep+4))
								swf.blit(logo,(10,yep))
								yep += 30
								ordinal = False
							else:
								tent = len(smsg)*12
								masg += smsg
								pg.draw.rect(swf,(95,97,100),(50,yep,350,30))
								fyup = fonty.render(masg,True,(255,255,255))
								swf.blit(fyup,(50,yep+4))
								yep += 30
						smsg = ''
						yep += 20
						if ordinal:
							swf.blit(logo,(10,yep-(countr*30)-20))
						ordinal = False
					else:
						continue
				else:
					smsg += i.unicode
		if gaylussac == True:
			if i.type == pg.KEYUP:
				gaylussac = False
	if msg == '':
		key = False
	if gaylussac:
		smsg = smsg[:-1]
		pg.time.delay(120)
	tcolor(activate_b1,reper5)
	tcolor(activate_b2,reper6)
	tcolor(activate_b3,reper7)
	tcolor(activate_b4,reper8)
	tcolor(activate_b5,reper9)
	tcolor(activate_b6,reper10)
	tcolor(activate_b7,reper11)
	tcolor(activate_b8,reper12)
	tcolor(activate_b9,reper13)
	if len(smsg)>42:
		showcase = smsg[len(smsg)-40:]
	else:
		showcase = smsg
	pg.display.flip()