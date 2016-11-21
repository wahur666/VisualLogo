# -*- coding: utf-8 -*-

from Polygon import Polygon
from System.Constants import COLOR as Color


class RunPointer(Polygon):
    def __init__(self, x, y, w, h, color=Color.BLACK, width=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.base_coordiantes = self.CalculatePoints()
        self.coordinates = self.CalculatePoints()
        self.color = color
        self.transparent = True
        self.width = 0
        self.base = {
            "x": self.x,
            "y": self.y,
            "h": self.h,
            "w": self.w
        }

    def CalculatePoints(self):
        points = []

        p1 = (self.x + self.w / 2, self.y)
        p2 = (self.x - self.w / 2, self.y - self.h / 2)
        p3 = (self.x - self.w / 2, self.y + self.h / 2)

        points.append(p3)
        points.append(p1)
        points.append(p2)


        return points

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        self.UpdatePoints()

    def IsInside(self, position):
        return False

    def UpdatePoints(self):
        self.coordinates = self.CalculatePoints()