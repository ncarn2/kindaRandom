import pygame
import urllib
import urllib.request

pygame.init()

display_width = 1000
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('this statement is false')
black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
#want this to be a random image from that website

urllib.request.urlretrieve("https://thispersondoesnotexist.com/image", "face.png")
f = open('face.png', 'wb')
f.write(urllib.request.urlopen('https://thispersondoesnotexist.com/image').read())
f.close()
faceImage = pygame.image.load('face.png')

x =  (display_width * 0.2)
y = (display_height * 0.2)

def image(x, y):
    gameDisplay.blit(faceImage, (x, y))


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    image(x,y)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
