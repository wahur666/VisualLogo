# -*- coding: utf-8 -*-

import pygame

from Base import AbstractDrawable
from System.Constants import COLOR as Color

class Polygon(AbstractDrawable):

    def __init__(self, cooridantes, color=Color.BLACK, width = 0):
        self.coordinates = cooridantes
        self.color = color
        self.width = width

    def DrawObject(self, screen):
        pygame.draw.polygon(screen, self.color, self.coordinates, self.width)

    def IsInside(self, position):
        pass
