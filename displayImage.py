import os
import pygame
import urllib
import urllib.request
import time

pygame.init()

display_width = 1000
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('this statement is false')
black = (0,0,0)
white = (255,255,255)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

clock = pygame.time.Clock()
crashed = False
#want this to be a random image from that website
def getFace():
    pygame.draw.rect(gameDisplay,(0,0,255),(100,500,200,50))
    textsurface = myfont.render('Wait...!', False, (255, 255, 255))
    gameDisplay.blit(textsurface,(120,500))
    pygame.display.update()
    f = open('face.png', 'wb')
    f.write(urllib.request.urlopen(urllib.request.Request('https://thispersondoesnotexist.com/image')).read())
    f.close()
    faceImage = pygame.image.load('face.png')

    x =  0#(display_width * 0.2)
    y = 0#(display_height * 0.2)
    image(x, y, faceImage)
    time.sleep(5)

def image(x, y, imageFile):
    if type(imageFile)==str:
        img = pygame.image.load(imageFile)
        img = pygame.transform.scale(img,(500,200))
        gameDisplay.blit(img, (x,y))
    else:
        gameDisplay.blit(imageFile, (x, y))
    pygame.display.update()

gameDisplay.fill(white)
x = display_width/5
y = display_height/5
image(x,y, 'Welcome.jpg')
pygame.display.update()
time.sleep(2)
image(x,y, 'Welcome2.jpg')
pygame.display.update()
time.sleep(0.5)
image(x,y, 'Welcome3.jpg')
pygame.display.update()
time.sleep(1)
def drawButtons():
    pygame.draw.rect(gameDisplay,(0,0,255),(100,500,200,50))
    textsurface = myfont.render('Make a face!', False, (255, 255, 255))
    gameDisplay.blit(textsurface,(120,500))
    pygame.draw.rect(gameDisplay,(0,255,0),(700,500,200,50))
    textsurface = myfont.render('Make a call!', False, (255, 255, 255))
    gameDisplay.blit(textsurface,(720,500))
    pygame.draw.rect(gameDisplay,(255,0,0),(400,600,200,50))
    textsurface = myfont.render('UNKNOWN!', False, (255, 255, 255))
    gameDisplay.blit(textsurface,(420,600))
drawButtons()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0] > 100 and pos[0] < 300 and pos[1] > 500 and pos[1] < 550:
                getFace()
                pygame.display.update()
                image(x,y, 'Welcome3.jpg')
                drawButtons()
            if pos[0] > 700 and pos[0] < 900 and pos[1] > 500 and pos[1] < 550:
                os.system('python ./combined.py')
            if pos[0] > 400 and pos[0] < 600 and pos[1] > 600 and pos[1] < 650:
                exit()
    
    #image(x + 200,y + 300, faceImage)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
