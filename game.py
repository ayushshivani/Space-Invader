import pygame
import sys
from function import *
from classes import *
from pygame.locals import *
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Space Invader")
background = pygame.image.load("5.jpg")
myFont = pygame.font.SysFont("Times New Roman", 28)
displayscore = myFont.render("Score\n" + str(score[0]), False, (255, 255, 255))


movemissile = pygame.USEREVENT + 1
newalien = pygame.USEREVENT + 2
deletealien = pygame.USEREVENT + 3
pygame.time.set_timer(movemissile, 1000)
pygame.time.set_timer(newalien, 10000)
pygame.time.set_timer(deletealien, 1000)

ship = Spaceship()
screen.blit(ship.image, (ship.left, ship.top))
while True:
    clock.tick(60)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit()
            if event.key == pygame.K_a:
                if ship.left > 0:
                    ship.left -= 100
            if event.key == pygame.K_d:
                if ship.left < 700:
                    ship.left += 100
            if event.key == pygame.K_SPACE:
                shoot1(ship.left, ship.top)
                miss = True
            if event.key == pygame.K_s:
                shoot2(ship.left, ship.top)
        elif event.type == pygame.QUIT:
            sys.exit()
        elif event.type == movemissile:
            for x in misarr1:
                x.top -= 100
                if x.top < 0:
                    misarr1.pop(misarr1.index(x))
            for x in misarr2:
                x.top -= 200
                if x.top < 0:
                    misarr2.pop(misarr2.index(x))
        elif event.type == newalien:
            createalien()
        elif event.type == deletealien:
            delalien()
    collision()

    for x in misarr1:
        screen.blit(x.image, (x.left, x.top))
    for x in misarr2:
        screen.blit(x.image, (x.left, x.top))

    for x in alienarr1:
        screen.blit(x.image, (x.left, x.top))
    displayscore = myFont.render("Score" + ":" +
                                 str(score[0]), True, (255, 255, 255))
    screen.blit(ship.image, (ship.left, ship.top))
    screen.blit(displayscore, (350, 450))
    pygame.display.update()
