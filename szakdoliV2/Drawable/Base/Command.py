# -*- coding: utf-8 -*-

from abc import abstractmethod
import warnings

from Drawable.Base import AbstractDrawable

from Drawable.Rectangle import Rect
from Drawable.Sprite import Spirte
from Drawable.TextIcon import TextIcon

class Command(AbstractDrawable):

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None):
        super(Command, self).__init__(x, y, w, h, vec2_pos, size)
        self.mainRect = Rect(self.x, self.y, self.w, self.h, width=1, transparent=False)
        self.sprite = None
        self.imagePath = None
        self.texticon = None
        self.keycode = None
        self.keycode_pad = 0

    def execute_command(self):
        raise RuntimeError("Event didn't binded")

    def IsInside(self, position):
        return self.x <= position[0] and self.x + self.w >= position[0] and self.y <= position[1] and self.y + self.h >= position[1]

    def DrawObject(self, screen):
        if not (self.sprite or self.texticon):
            self.LoadSprite()
        self.mainRect.DrawObject(screen)
        if self.sprite:
            self.sprite.DrawObject(screen)
        if self.texticon:
            self.texticon.DrawObject(screen)

    def LoadSprite(self):
        if self.imagePath is None and self.keycode is not None:
            self.texticon = TextIcon(self.x, self.y, self.w, self.h, keycode=self.keycode)
            self.texticon.SetPaddning(self.keycode_pad)
        elif self.imagePath is not None and self.keycode is None:
            self.sprite = Spirte(self.x, self.y, self.w, self.h, imgpath=self.imagePath)
        else:
             self.sprite = Spirte(self.x, self.y, self.w, self.h)
             warnings.warn("Too many argument")

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        self.mainRect.SetPosition(x,y)
        if self.sprite:
            self.sprite.SetPosition(x,y)
        if self.texticon:
            self.texticon.SetPosition(x,y)

    def deltapos(self, position):
        return position[0] - self.x, position[1] - self.y

    def drag(self, mouseposition):
        x = mouseposition[0] - self.delta[0]
        y = mouseposition[1] - self.delta[1]
        self.SetPosition(x, y)

    def setDelta(self, mouseposition):
        self.delta = self.deltapos(mouseposition)

    def UnloadIcon(self):
        self.texticon = None

    def Bind(self, function_pointer):
        self.execute_command = function_pointer

    def SetAccentColor(self, accent):
        self.mainRect.SetAccentColor(accent)

    def SetKeyCodePadding(self, x):
        self.keycode_pad = x