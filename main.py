import configparser
import pygame
import sys
import os


FPS = 10
IsLoad=False
Games = []
GImg=[]
GBack=[]
GName=[]
GPath=[]
State=0
Colum=0

stateG=1
power=""
Enter=False

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

pygame.display.toggle_fullscreen()
pygame.joystick.init()

#joystick init
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

#Game loading
def Start():
    m=[]
    config = configparser.ConfigParser()
    config.sections()
    files = os.listdir("Games/")
    images = filter(lambda x: x.endswith('.ini'), files)
    f = []
    g = []
    for i in images:
        t=i.partition('.')
        config.read(f'Games/{t[0]}.ini')
        print(config["Game"]["name"])
        g.append(config["Game"]["name"] + ";"+config["Game"]["ico"]+";"+config["Game"]["path"] +";"+config["Game"]["back"])
    for x in g:
        f=(x.replace('"', ''))
        Games.append(f)
    for n in Games:
        t=(n.split(';'))
        m.append(t)
    for n in m:
        GName.append(n[0])
        GImg.append(n[1])
        GPath.append(n[2])
        GBack.append(n[3])

#Drawing
def show():
        bg=pygame.image.load(GBack[stateG-1])
        bg=pygame.transform.scale(bg, (1920, 1080))
        screen.blit(bg, (0,0))


        g1 = pygame.image.load(GImg[0]).convert_alpha()
        g1 = pygame.transform.scale(g1, (250, 320))
        screen.blit(g1, (120, 400))

        if(len(GName)>1):
            g2 = pygame.image.load(GImg[1]).convert_alpha()
            g2 = pygame.transform.scale(g2, (250, 320))
            screen.blit(g2, (520, 400))
            if(len(GName)>2):
                g3 = pygame.image.load(GImg[2]).convert_alpha()
                g3 = pygame.transform.scale(g3, (250, 320))
                screen.blit(g3, (1020, 400))
                if(len(GName)>3):
                    g3 = pygame.image.load(GImg[3]).convert_alpha()
                    g3 = pygame.transform.scale(g3, (250, 320))
                    screen.blit(g3, (1520, 400))
        if Colum==0:
            if stateG == 1:
                pygame.draw.rect(screen, (64, 128, 255),
                        (120, 400, 250, 320), 8)
            if stateG == 2:
                pygame.draw.rect(screen, (64, 128, 255),
                        (520, 400, 250, 320), 8)
            if stateG == 3:
                pygame.draw.rect(screen, (64, 128, 255),
                        (1020, 400, 250, 320), 8)
            if stateG == 4:
                pygame.draw.rect(screen, (64, 128, 255),
                        (1520, 400, 250, 320), 8)

#Inputs
def Inputs():
    global stateG
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    if pygame.joystick.get_init() and len(joysticks)>0:
        if joysticks[0].get_numaxes() >= 2:
            axis_x = joysticks[0].get_axis(0)
            axis_y = joysticks[0].get_axis(1)
        if joysticks[0].get_button(0):
            if Colum==0:
                os.system(GPath[stateG-1])
        if axis_x > 0.7:
            if stateG < 5 and Colum==0:
                stateG = stateG + 1
            if stateG == 5 and Colum==0:
                stateG=1
            sound1.play()
        if axis_x < -0.7 and Colum==0:
            if stateG > 0:
                stateG = stateG - 1
            if stateG == 0 and Colum==0:
                stateG=4
            sound1.play()
    else:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            os.system(GPath[stateG-1])
        if keys[pygame.K_LEFT]:
            if stateG > 0:
                stateG = stateG - 1
            if stateG == 0 and Colum==0:
                stateG=4
        if keys[pygame.K_RIGHT]:
            if stateG < 5 and Colum==0:
                stateG = stateG + 1
            if stateG == 5 and Colum==0:
                stateG=1

#Gray Bar
def Bar():
    bar=pygame.image.load("Data/Bar/barg.png")
    screen.blit(bar, (0,0))

Start()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        if event.type == pygame.VIDEOEXPOSE:
            IsLoad = False
        else:
            IsLoad = True
    if IsLoad:
        Inputs()
        show()
        Bar()
    pygame.display.update()
