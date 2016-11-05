# -*- coding: utf-8 -*-

from Constants import COLOR as Color
import pygame


class Line:

    def __init__(self, vec2start=None, vec2end=None, color=Color.BLACK, width=1, pen_down=True):
        self.vec2start = vec2start
        self.vec2end = vec2end
        self.color = color
        self.pen_width = width
        self.pen_down = pen_down

    def DrawLine(self, screen):
        if self.pen_down:
            pygame.draw.line(screen, self.color, self.vec2start, self.vec2end, self.pen_width)
