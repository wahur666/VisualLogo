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

    def DrawObject(self, screen):
        if self.pen_down:
            pygame.draw.line(screen, self.color, self.vec2start, self.vec2end, self.pen_width)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Flood:

    def __init__(self, vec2pos=None, color=Color.BLACK):
        self.vec2pos = vec2pos
        self.color = color
        self.caluclaated = False
        self.surface = None

    def DrawObject(self, screen):
        if not self.caluclaated:
            pa = pygame.PixelArray(screen)
            pa = self.flood_fill(screen, Node(self.vec2pos[0], self.vec2pos[1]), self.color, pa)
            self.surface = pa.make_surface()
            self.caluclaated = True
            del pa
        screen.blit(self.surface, (20,20), (20,20,650,620))


    def flood_fill(self, screen, node, replacement_colour, px):
        current_colour = screen.get_at((self.vec2pos[0], self.vec2pos[1]))

        if replacement_colour == current_colour:
            return px

        q = []
        q.append(node)
        while q:
            n = q.pop()
            if screen.get_at((n.x, n.y)) == current_colour:
                px[n.x, n.y] = replacement_colour
                if n.x - 1 >= 20 and n.y - 1 >= 20 and n.x + 1 < 650 and n.y + 1 < 620:
                    q += [Node(n.x - 1, n.y), Node(n.x + 1, n.y), Node(n.x, n.y - 1), Node(n.x, n.y + 1) ]
        return px