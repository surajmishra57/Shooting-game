import pygame
import time
import random
pygame.init()
pygame.mixer.init()
Screen=pygame.display.set_mode((400,500))
pygame.display.set_caption("Shooting War")
pygame.display.update()

def chack():
    global X
    if shootx>=X-25 and shootx<=X+30 and shooty>=Y and shooty<=Y+30:
        Screen.fill(white)
        EnemyDead(X,Y)
        Player()
        pygame.display.update()
        time.sleep(1)
        X=random.randint(10,370)
    if EshootX>=playerX-15 and EshootX<=playerX+30 and EshootY>=playerY and EshootY<=playerY+20:
        Screen.fill(white)
        EnemyDead(playerX,playerY)
        Enemy()
        pygame.display.update()
        time.sleep(1)
    if EshootX+20>=playerX-15 and EshootX<=playerX+30 and EshootY>=playerY and EshootY<=playerY+20:
        Screen.fill(white)
        EnemyDead(playerX,playerY)
        Enemy()
        pygame.display.update()
        time.sleep(1)
def Enemy():
    pygame.draw.rect(Screen,red,(X,Y,Z+15,Z))
    pygame.draw.rect(Screen,red,(X-10,Y+5,Z+35,Z))
    pygame.draw.rect(Screen,red,(X-15,Y+10,Z+45,Z+10))
    pygame.draw.rect(Screen,red,(X-10,Y+25,Z+35,Z))
    pygame.draw.rect(Screen,blue,(X-5,Y+30,Z+5,Z+5))
    pygame.draw.rect(Screen,blue,(X+15,Y+30,Z+5,Z+5))
    pygame.draw.rect(Screen,black,(X-5,Y+10,Z+5,Z+5))
    pygame.draw.rect(Screen,black,(X+15,Y+10,Z+5,Z+5))

def Player():
    pygame.draw.rect(Screen,red,(playerX,playerY,10,30))
    pygame.draw.rect(Screen,orange,(playerX-10,playerY+10,30,25))
    pygame.draw.rect(Screen,blue,(playerX-5,playerY+10,20,25))

def EnemyGun():
    pygame.draw.rect(Screen,blue,(EshootX,EshootY,10,10))
    pygame.draw.rect(Screen,blue,(EshootX+20,EshootY,10,10))

def PlayerGun():
     pygame.draw.rect(Screen,red,(shootx,shooty,10,10))

def GameSound(x):
    if x==1:
         pygame.mixer.music.load("Rifle.mp3")
         pygame.mixer.music.play()
    if x==2:
         pygame.mixer.music.load("Ak47.mp3")
         pygame.mixer.music.play()
def EnemyDead(X,Y):
    pygame.draw.rect(Screen,red,(X,Y,15,15))
    pygame.draw.rect(Screen,red,(X,Y+40,15,15))
    pygame.draw.rect(Screen,red,(X+20,Y+20,15,15))
    pygame.draw.rect(Screen,red,(X-20,Y+20,15,15))
    pygame.draw.rect(Screen,Yellow,(X,Y+20,15,15))
#colour
green=(0,255,0)
black=(0,0,0)
orange=(225,124,0)
red=(225,0,0)
blue=(0,0,255)
Yellow=(255,255,0)
white=(0,0,0)
#spacific variables
Dead=0
start=0
StepX=20
fps=7
X,Y,Z=300,20,5
playerX,playerY=200,450
clock=pygame.time.Clock()  
left,right,end=None,True,True
Xright,Xleft=True,False
shootx,shooty=200,399
EshootX,EshootY=295,60

while end :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            end=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                if playerX==380:
                    continue
                playerX+=20

            if event.key==pygame.K_LEFT:
                if playerX==20:
                    continue
                playerX-=20
                
            if event.key==pygame.K_SPACE:
                  start=1
                  if shooty==399:
                      GameSound(0)#1
    if Xright:
        X+=10
        if X>360:
            Xright=False
            Xleft=True
    if Xleft:
        X-=10
        if  X<10:
            Xright=True
            Xleft=False
    if start==1:        
        shooty=shooty-20
        if shooty==-1:
            shooty=399
            start=0
    if start==0:
        shootx=playerX
    if EshootY==60:
       GameSound(0)#2

    EshootY=EshootY+20

    if EshootY==520:
        EshootX,EshootY=X-5,60
  
    Screen.fill(white)
    if start==1:
        PlayerGun()
    Enemy()
    EnemyGun()
    Player()
    pygame.display.update()
    clock.tick(fps)
    chack()
pygame.quit()
