# -*- coding: utf-8 -*-

from Drawable.Base.AbstractDrawable import AbstractDrawable
from Rectangle import Rect
from Sprite import Spirte
from System.Vector2 import Vector2

class Button(AbstractDrawable):

    def __init__(self, x=None, y=None, w=None, h=None, imgpath = "\\Resources\\icon-placeholder.png", descriptor="", size = None, vec2_pos = None):
        super(Button, self).__init__(x=x, y=y, w=w, h=h, size=size, vec2_pos=vec2_pos, descriptor=descriptor)
        self.imgpath = imgpath
        self.sprite = None

    def DrawObject(self, screen):
        if not self.sprite:
            self.LoadImage()
        self.buttonsquircle.DrawObject(screen)      #BASE
                                                    #FEEDBACK
        self.sprite.DrawObject(screen)              #IMAGE


    def IsInside(self, position):
        return self.x <= position[0] and self.x + self.h >= position[0] and self.y <= position[1] and self.y + self.w >= \
               position[1]

    def bind(self, funcpointer):
        self.OnClick = funcpointer

    def OnClick(self, event_type):
        raise RuntimeError("Undobund button")

    def LoadImage(self):
        self.sprite = Spirte(self.x + 2, self.y + 2, self.w - 5, self.h - 5, self.imgpath)
        self.buttonsquircle = Rect(self.x  , self.y , self.w , self.h, width=1)