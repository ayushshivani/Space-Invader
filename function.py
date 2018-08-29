import pygame
from classes import *
import random
import time
from pygame.locals import *
ali = False
miss = False
misarr1 = []
misarr2 = []
alienarr1 = []
score = [0]


def shoot1(left, top):
    shot = Mis1(left, top - 100)
    misarr1.append(shot)


def shoot2(left, top):
    shot = Mis2(left, top - 100)
    misarr2.append(shot)


def createalien():
    x = random.randint(1, 8) * 100
    y = random.randint(0, 1) * 100
    z = time.time()
    alien = Alien1(x, y, z)
    alienarr1.append(alien)


def delalien():
    z = time.time()
    for x in alienarr1:
        if z - x.time > 7:
            alienarr1.pop(alienarr1.index(x))


def collision():
    for x in alienarr1:
        for y in misarr1:
            if x.left == y.left and x.top == y.top:
                score[0] += 10
                if x not in alienarr1:
                    pass
                else:
                    alienarr1.remove(x)
                    misarr1.remove(y)

    for x in alienarr1:
        for y in misarr2:
            if x.left == y.left and x.top >= y.top:
                x.image = pygame.image.load("alien2.jpg")
                x.time += 5
                misarr2.pop(misarr2.index(y))
