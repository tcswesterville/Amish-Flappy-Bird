import pygame
import sys

pygame.init()

WINDOW_HEIGHT=1080

WINDOW_WIDTH=1920

clock=pygame.time.Clock()

backgroundImage = "images/sky.png"
pipeImage = "images/pipe.png"
birdImage = "images/bird.png"

background=pygame.image.load(backgroundImage)
pipe=pygame.image.load(pipeImage)
bird=pygame.image.load(birdImage)

bird = pygame.transform.scale(bird,(100,100))
pipe = pygame.transform.scale(pipe,(100,100))

playerPosition = bird.get_rect()
playerPosition.y = WINDOW_HEIGHT/2
playerPosition.x = WINDOW_WIDTH/4

screen=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("bum bum bum bum bum")

running = True

while running:
    screen.blit(background, background.get_rect())
    screen.blit(pipe, pipe.get_rect())
    screen.blit(bird, playerPosition)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
            sys.exit()
        pressed = pygame.key.get_pressed()


        if pressed[pygame.K_ESCAPE]:
            pygame.quit()
    playerPosition.y += 5
    pygame.display.flip()

    if pressed[pygame.Space]: playerPosition.y += 5
