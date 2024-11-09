import pygame
import sys

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Sound nice/hi song.mp3")
pygame.mixer.music.play(-1)
WINDOW_HEIGHT=1080

WINDOW_WIDTH=1920

clock=pygame.time.Clock()

backgroundImage = "images/sky.png"
pipeImage = "images/pipe.png"
birdImage = "images/bird.png"

background=pygame.image.load(backgroundImage)
pipe=pygame.image.load(pipeImage)
bird=pygame.image.load(birdImage)

bird = pygame.transform.scale(bird,(150,150))
pipe = pygame.transform.scale(pipe,(199,199))
pipeupsidedown=pygame.transform.flip(pipe,False,True)
playerPosition = bird.get_rect()
playerPosition.y =WINDOW_HEIGHT/2
playerPosition.x = WINDOW_WIDTH/6

pipePosition = pipe.get_rect()
pipePosition.y = WINDOW_HEIGHT/2
pipePosition.x = WINDOW_WIDTH/1

pipelist=[pipePosition]

screen=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("bum bum bum bum bum")

gameoverfont=pygame.font.Font('Lobster-Regular.ttf', 40)
running = True

while running:
    for sigmapipe in pipelist:
        sigmapipe.x-=3
        if playerPosition.colliderect(sigmapipe):
            print(playerPosition,pipePosition)
            running =False
    pygame.time.Clock().tick(30)
    screen.blit(background, background.get_rect())
    screen.blit(pipeupsidedown, pipePosition)
    screen.blit(bird, playerPosition)
    if playerPosition.y <0 or playerPosition.y>WINDOW_HEIGHT :
        running=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
            sys.exit()
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            pygame.quit()
        if pressed[pygame.K_SPACE]:
            playerPosition.y-=42.9
    playerPosition.y +=5.2

    pygame.display.flip()


