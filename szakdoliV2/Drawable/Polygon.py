# -*- coding: utf-8 -*-

import pygame

from Base import AbstractDrawable
from System.Constants import COLOR as Color

class Polygon(AbstractDrawable):

    def __init__(self, cooridantes, color=Color.BLACK, width = 0):
        self.coordinates = cooridantes
        self.color = color
        self.width = width
        self.accentColor = Color.WHITE
        self.transparent = False
        self.base = { "coords" : self.coordinates }

    def DrawObject(self, screen):
        if not self.transparent:
            pygame.draw.polygon(screen, self.accentColor, self.coordinates, 0)
        pygame.draw.polygon(screen, self.color, self.coordinates, self.width)

    def IsInside(self, position):
        pass

    def ResetPosition(self):
        self.coordinates = self.base["coords"]

    def GetParameters(self):
        pass