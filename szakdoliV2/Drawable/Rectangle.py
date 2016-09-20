import pygame
from Util import Color
from DrawableInterface import DrawableInterface

class Rect(DrawableInterface):

    def __init__(self, x, y, w, h, name, color=Color.BLACK, width=0, movable = False):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.name = name
        self.delta = 0, 0
        self.color = color
        self.width = width
        self.movable = movable

    def jobb(self):
        self.x += 1

    def bal(self):
        self.x -= 1

    def fel(self):
        self.y += 1

    def le(self):
        self.y -= 1

    def DrawObject(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), self.width)

    def print_name(self):
        print self.name + " Clicked"

    def IsInside(self, position):
        return self.x <= position[0] and self.x + self.h >= position[0] and self.y <= position[1] and self.y + self.w >= \
               position[1], self.name

    def deltapos(self, position):
        return position[0] - self.x, position[1] - self.y

    def drag(self, mouseposition):
        self.x = mouseposition[0] - self.delta[0]
        self.y = mouseposition[1] - self.delta[1]

    def setDelta(self, mouseposition):
        self.delta = self.deltapos(mouseposition)

    def isMovable(self):
        return self.movable