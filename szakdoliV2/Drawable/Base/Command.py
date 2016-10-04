# -*- coding: utf-8 -*-

from abc import abstractmethod

from Drawable.Base import AbstractDrawable


class Command(AbstractDrawable):

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Command, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    @abstractmethod
    def execture_command(self):
        pass;

    def IsInside(self, position):
        return self.x <= position[0] and self.x + self.w >= position[0] and self.y <= position[1] and self.y + self.h >= position[1]


