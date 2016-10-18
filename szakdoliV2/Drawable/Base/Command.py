# -*- coding: utf-8 -*-

from abc import abstractmethod
import warnings

from Drawable.Base import AbstractDrawable

from Drawable.Rectangle import Rect
from Drawable.Sprite import Spirte

class Command(AbstractDrawable):

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Command, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        self.mainRect = Rect(self.x, self.y, self.w, self.h, width=1, transparent=False)
        self.sprite = None
        self.imagePath = None

    @abstractmethod
    def execture_command(self):
        pass;

    def IsInside(self, position):
        return self.x <= position[0] and self.x + self.w >= position[0] and self.y <= position[1] and self.y + self.h >= position[1]

    def DrawObject(self, screen):
        if not self.sprite:
            self.LoadSprite()
        self.mainRect.DrawObject(screen)
        self.sprite.DrawObject(screen)

    def LoadSprite(self):
        if self.imagePath is None:
            self.sprite = Spirte(self.x, self.y, self.w, self.h)
            warnings.warn("NO SPTIRE TO LOAD! CHANGE IT")
        else:
            self.sprite = Spirte(self.x, self.y, self.w, self.h, imgpath=self.imagePath)

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        self.mainRect.SetPosition(x,y)
        if self.sprite:
            self.sprite.SetPosition(x,y)

    def deltapos(self, position):
        return position[0] - self.x, position[1] - self.y

    def drag(self, mouseposition):
        x = mouseposition[0] - self.delta[0]
        y = mouseposition[1] - self.delta[1]
        self.SetPosition(x, y)

    def setDelta(self, mouseposition):
        self.delta = self.deltapos(mouseposition)