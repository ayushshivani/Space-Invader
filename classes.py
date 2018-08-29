import pygame


class Spaceship:
    def __init__(self):
        self.image = pygame.image.load("index.png")
        self.left = 300
        self.top = 700


class Missiles:
    def __init__(self, left, top):
        self.left = left
        self.top = top


class Mis1(Missiles):
    def __init__(self, left, top):
        Missiles.__init__(self, left, top)
        self.image = pygame.image.load("bullet.png")


class Mis2(Missiles):
    def __init__(self, left, top):
        Missiles.__init__(self, left, top)
        self.image = pygame.image.load("bullet2.png")


class Alien:
    def __init__(self, left, top, time):
        self.left = left
        self.top = top
        self.time = time


class Alien1(Alien):
    def __init__(self, left, top, time):
        Alien.__init__(self, left, top, time)
        self.image = pygame.image.load("alien1.jpg")


class Alien2(Alien):
    def __init__(self, left, top, time):
        Alien.__init__(self, left, top, time)
        self.image = pygame.image.load("alien2.jpg")
