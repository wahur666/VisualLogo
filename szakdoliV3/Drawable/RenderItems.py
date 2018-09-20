# -*- coding: utf-8 -*-

from System.Constants import COLOR as Color
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
        screen.blit(self.surface, (20,20), (20,20,630,600))


    def flood_fill(self, screen, node, replacement_colour, px):
        current_colour = px[node.x, node.y]

        if screen.map_rgb(replacement_colour) == current_colour:
            return px

        q = list()
        q.append(node)
        while q:
            n = q.pop()
            if px[n.x, n.y] == current_colour:
                px[n.x, n.y] = replacement_colour
            else:
                continue

            w = Node(n.x + 1, n.y)
            while w.x <= 650 and px[w.x, w.y] == current_colour:
                px[w.x, w.y] = replacement_colour

                q.append(Node(w.x, w.y - 1))
                q.append(Node(w.x, w.y + 1))

                w.x += 1

            e = Node(n.x - 1, n.y)
            while e.x >= 20 and px[e.x, e.y] == current_colour:
                px[e.x, e.y] = replacement_colour

                q.append(Node(e.x, e.y - 1))
                q.append(Node(e.x, e.y + 1))

                e.x -= 1

        return px
