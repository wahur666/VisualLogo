# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from System.Vector2 import Vector2

class AbstractDrawable:
    __metaclass__ = ABCMeta

    def __init__(self, x = None, y = None, w = None, h = None, vec2_pos = None, size = None, descriptor = ""):
        if x is not None and y is not None:
            self.x = x
            self.y = y
        elif x is None and y is None and vec2_pos is not None:
            if not isinstance(vec2_pos, Vector2):
                raise TypeError("vec2_pos is not Vector2 type")
            self.x = vec2_pos.x
            self.y = vec2_pos.y
        else:
            raise ValueError("Not enough parameter, give X and Y, or Vec2_pos")

        if w is not None and h is not None:
            self.w = w
            self.h = h
        elif w is None and h is None and size is not None:
            if type(size) != tuple:
                raise TypeError("size is not tuple(int, int) type")
            self.w = size[0]
            self.h = size[1]
        else:
            raise ValueError("Not enough parameter, give W and H, or size=tuple(int,int)")

        self.descriptor = descriptor

        self.base = {
            "x" : self.x,
            "y" : self.y,
            "h" : self.h,
            "w" : self.w
        }

    @abstractmethod
    def DrawObject(self, screen):
        pass

    @abstractmethod
    def IsInside(self, position):
        pass

    def SetPosition(self, x, y):
        self.x = x
        self.y = y

    def ResetPosition(self):
        self.x = self.base['x']
        self.y = self.base['y']
        self.h = self.base['h']
        self.w = self.base['w']

    def GetParameters(self):
        return self.x, self.y, self.w, self.h
