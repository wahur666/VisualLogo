# -*- coding: utf-8 -*-

from System.Constants import COLOR as Color
from Polygon import Polygon

from math import radians, sin, cos

class DrawingIcon(Polygon):

    def __init__(self, x, y, w, h, color=Color.BLACK, width=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.base_coordiantes = self.CalculatePoints()
        self.coordinates = self.CalculatePoints()
        self.base_rotation = 0
        self.color = color
        self.width = width
        self.transparent = True
        self.base = {
            "x": self.x,
            "y": self.y,
            "h": self.h,
            "w": self.w
        }


    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        self.UpdatePoints()

    def DrawObject(self, screen, rot):
        self.RotateToAngle(rot)
        super(DrawingIcon, self).DrawObject(screen)


    def ResetPosition(self):
        self.x = self.base["x"]
        self.y = self.base["y"]
        self.base_rotation = 0
        self.UpdatePoints()

    def IsInside(self, position):
        return False

    def UpdatePoints(self):
        self.base_coordiantes = self.CalculatePoints()

    def CalculatePoints(self):
        points = []

        origo = (self.x, self.y)
        p1 = (self.x + self.w / 2, self.y)
        p2 = (self.x - self.w / 2, self.y - self.h / 2)
        p3 = (self.x - self.w / 2, self.y + self.h / 2)

        points.append(origo)
        points.append(p3)
        points.append(p1)
        points.append(p2)


        return points

    def RotateToAngle(self, angle):
        rot_dif = angle - self.base_rotation
        self.coordinates = []
        for x, y in self.base_coordiantes:
            sf = sin(radians(rot_dif))
            cf = cos(radians(rot_dif))
            x -= self.base_coordiantes[0][0]
            y -= self.base_coordiantes[0][1]
            new_x = int(round(x * cf - y * sf)) + self.base_coordiantes[0][0]
            new_y = int(round(x * sf + y * cf)) + self.base_coordiantes[0][1]
            self.coordinates.append((new_x, new_y))