from random import randint, random

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

pipeupsidedown=pygame.transform.flip(pipe,False,True)
playerPosition = bird.get_rect()
playerPosition.y = WINDOW_HEIGHT/2
playerPosition.x = WINDOW_WIDTH/6


pipe_list=[]

screen=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("bum bum bum bum bum")

gameoverfont=pygame.font.Font('Lobster-Regular.ttf', 40)
running = True

class Pipe:
    def __init__(self):
        gap = 250
        random_pipe_length = randint(100, WINDOW_HEIGHT - gap - 100)
        pipe_image = pygame.image.load("images/pipe.png")
        self.scaled_pipe_image = pygame.transform.sca

        self.top_pipe.y = 0
        self.bottom_pipe.y = WINDOW_HEIGHT - bottom_pipe_height

        self.top_pipe.x = 0
        self.bottom_pipe.x=WINDOW_WIDTH

        self.made_next_pipe =False

    def make_pipe(self):le(pipe_image, (200, random_pipe_length))

        bottom_pipe_height = WINDOW_HEIGHT - random_pipe_length - gap
        flipped_pipe_image =pygame.transform.scale(pipe_image,(200,bottom_pipe_height))
        self.flipped_pipe_image =pygame.transform.flip(flipped_pipe_image,False,True )

        self.top_pipe= self.scaled_pipe_image.get_rect()
        self.bottom_pipe = self.flipped_pipe_image.get_rect()
        pipe_list.append(self)

    def move_pipe(self):
        self.bottom_pipe.x -= 3
        self.top_pipe.x -= 3
        if playerPosition.colliderect(self.top_pipe) or playerPosition.colliderect(self.bottom_pipe):
            pygame.quit()
        if self.bottom_pipe.x < WINDOW_WIDTH / 2 and not self.made_next_pipe:
            new_pipe = Pipe()
            pipe_list.append(new_pipe)
            self.made_next_pipe = True

        if self.bottom_pipe.x < 0:
            pipe_list.remove(self)
pipe_list =[]

first_pipe = Pipe()
first_pipe.make_pipe()

while running:
    pygame.time.Clock().tick(30)
    screen.blit(background, background.get_rect())
    screen.blit(bird, playerPosition)
    if playerPosition.y < 0 or playerPosition.y > WINDOW_HEIGHT :
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

    for pipe in pipe_list:
        screen.blit(pipe.scaled_pipe_image, pipe.top_pipe)
        screen.blit(pipe.flipped_pipe_image, pipe.bottom_pipe)
        pipe.move_pipe()

    pygame.display.update()



