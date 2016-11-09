# -*- coding: utf-8 -*-

import pygame

from Drawable.Base.AbstractDrawable import AbstractDrawable
from System.Constants import COLOR as Color


class Rect(AbstractDrawable):

    def __init__(self, x=None, y=None, w=None, h=None, descriptor="", color=Color.BLACK, width=0, movable = False, vec2_pos=None, size=None, transparent = True):
        super(Rect, self).__init__(x=x, y=y, w=w, h=h, vec2_pos=vec2_pos, size=size, descriptor=descriptor)
        self.delta = 0, 0
        self.color = color
        self.width = width
        self.movable = movable
        self.transparent = transparent
        self.accentColor = Color.WHITE
        self.checkMove()
        self.Clickable = True

    def checkMove(self):
        self.move('UP')
        self.move('DOWN')
        self.move('LEFT')
        self.move('RIGHT')

    def move(self, direction ,tick = 1):
        if direction == 'UP':
            self.y += 1
        elif direction == 'DOWN':
            self.y -= 1
        elif direction == 'RIGHT':
            self.x += tick
        elif direction == 'LEFT':
            self.x -= 1
        else:
            raise NameError(direction + " : direction not defined")

    def DrawObject(self, screen):
        if not self.transparent:
            pygame.draw.rect(screen, self.accentColor, (self.x, self.y, self.w, self.h), 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), self.width)

    def print_name(self):
        print self.descriptor + " Clicked"

    def IsInside(self, position):
        if self.Clickable:
            return self.x <= position[0] and self.x + self.w >= position[0] and self.y <= position[1] and self.y + self.h >= position[1]
        else:
            return False

    def deltapos(self, position):
        return position[0] - self.x, position[1] - self.y

    def drag(self, mouseposition):
        self.x = mouseposition[0] - self.delta[0]
        self.y = mouseposition[1] - self.delta[1]

    def setDelta(self, mouseposition):
        self.delta = self.deltapos(mouseposition)

    def isMovable(self):
        return self.movable

    def SetClickable(self, state):
        self.Clickable = state

    def SetColor(self, color):
        self.color = color

    def Extend(self, y, h):
        self.h = h
        self.y = y