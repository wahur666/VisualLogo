# -*- coding: utf-8 -*-

from Drawable.Base.AbstractDrawable import AbstractDrawable
from Rectangle import Rect
from Sprite import Spirte
from TextIcon import TextIcon
from System.Constants import IMAGE_PATHS as C_IMG
from System.Constants import FONT_AWESOME as C_FA
from System.Constants import COLOR as Color

class Button(AbstractDrawable):

    def __init__(self, x=None, y=None, w=None, h=None, imgpath = C_IMG.PLACEHOLDER, descriptor="", size = None, vec2_pos = None, keycode=u"\uf071", padding=0):
        super(Button, self).__init__(x=x, y=y, w=w, h=h, size=size, vec2_pos=vec2_pos, descriptor=descriptor)

        self.imgpath = imgpath
        self.sprite = None

        self.keycode = keycode
        self.icon_padding = padding
        self.texticon = None

        self.texticon_color = Color.BLACK

        self.buttonsquircle = Rect(self.x  , self.y , self.w , self.h, width=1, transparent=False)

    def DrawObject(self, screen):
        if not self.texticon:
            self.LoadImage()
        self.buttonsquircle.DrawObject(screen)      #BASE
        if self.sprite:
            self.sprite.DrawObject(screen)          #IMAGE
        if self.texticon:
            self.texticon.DrawObject(screen)        #FontAwesome

    def IsInside(self, position):
        return self.x <= position[0] and self.x + self.h >= position[0] and self.y <= position[1] and self.y + self.w >= \
               position[1]

    def bind(self, funcpointer):
        self.OnClick = funcpointer

    def OnClick(self, event_type):
        raise RuntimeError("Undobund button")

    def LoadImage(self):
        if self.imgpath != C_IMG.PLACEHOLDER:
            self.sprite = Spirte(self.x + 2, self.y + 2, self.w - 5, self.h - 5, self.imgpath)
        elif self.keycode != C_FA.PLACEHOLDER:
            self.texticon = TextIcon(self.x + 2 + self.icon_padding, self.y + 2, self.w - 5, self.h - 5, keycode=self.keycode, color=self.texticon_color)
        else:
            self.texticon = TextIcon(self.x + 2, self.y + 2, self.w - 5, self.h - 5, keycode=C_FA.PLACEHOLDER)

    def SetAccentColor(self, accent):
        self.buttonsquircle.SetAccentColor(accent)

    def SetTextIconColor(self, color):
        self.texticon_color = color