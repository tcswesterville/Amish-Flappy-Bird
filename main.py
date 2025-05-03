from random import randint, random

import pygame
import sys
# RUNS SOUND IN CODE
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Sound nice/hi song.mp3")
pygame.mixer.music.play(-1)
#SIZE OF THE GAME
WINDOW_HEIGHT=1080
WINDOW_WIDTH=1920

# the code loads the images( the backgroundImage,pipeImage,birdImage)
backgroundImage = "images/sky.png"
pipeImage = "images/pipe.png"
birdImage = "images/bird.png"

background=pygame.image.load(backgroundImage) # loads image path
bird=pygame.image.load(birdImage) # loads image

bird = pygame.transform.scale(bird,(150,150)) # the size of the bird
# position the bird
playerPosition = bird.get_rect()
playerPosition.y = WINDOW_HEIGHT/2
playerPosition.x = WINDOW_WIDTH/6


pipe_list=[]

screen=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("bum bum bum bum bum")


running = True

class Pipe:
    def __init__(self):
        gap = 390
        random_pipe_length = randint(100, WINDOW_HEIGHT - gap - 100)
        pipe_image = pygame.image.load("images/pipe.png")
        self.scaled_pipe_image = pygame.transform.scale(pipe_image, (130, random_pipe_length))

        bottom_pipe_height = WINDOW_HEIGHT - random_pipe_length - gap
        flipped_pipe_image = pygame.transform.scale(pipe_image,(130,bottom_pipe_height))
        self.flipped_pipe_image = pygame.transform.flip(flipped_pipe_image,False,True )

        self.top_pipe= self.scaled_pipe_image.get_rect()
        self.bottom_pipe = self.flipped_pipe_image.get_rect()

        self.top_pipe.y = 0
        self.bottom_pipe.y = WINDOW_HEIGHT - bottom_pipe_height

        self.top_pipe.x = WINDOW_WIDTH
        self.bottom_pipe.x = WINDOW_WIDTH

        self.made_next_pipe = False

    def make_pipe(self):
        pipe_list.append(self)

    def move_pipe(self):
        self.bottom_pipe.x -= 5
        self.top_pipe.x -= 5
        if playerPosition.colliderect(self.top_pipe) or playerPosition.colliderect(self.bottom_pipe):
            gameoverfont = pygame.font.Font('Lobster-Regular.ttf', 40)
            text =  gameoverfont.render('GAME OVER', True,(255,255,255),(0,0,0))
            text.get_rect().center =(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

            #pygame.quit()

        if self.bottom_pipe.x < WINDOW_WIDTH / 2 and not self.made_next_pipe:
            new_pipe = Pipe()
            pipe_list.append(new_pipe)
            self.made_next_pipe = True

        if self.bottom_pipe.x < 0:
            pipe_list.remove(self)

first_pipe = Pipe()
first_pipe.make_pipe()

while running:
    pygame.time.Clock().tick(30)
    screen.blit(background, background.get_rect())
    screen.blit(bird, playerPosition)
    if playerPosition.y < 0 or playerPosition.y > WINDOW_HEIGHT:
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



