# -*- coding: utf-8 -*-

from Base import AbstractDrawable
from System.Constants import COLOR as Color
from System.Constants import FONT_AWESOME as fa

import pygame

class TextIcon(AbstractDrawable):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, keycode=u"\uf071", color = Color.BLACK):
        super(TextIcon, self).__init__(x, y, w, h, vec2_pos, size)
        self.keycode = keycode
        self.font = None
        self.text = None
        self.pad_x = 0
        self.color = color
        #self.textpos = (self.x + self.w / 2, self.y + self.h / 2)
        self.LoadFont()

    def IsInside(self, position):
        return self.x <= position[0] and self.x + self.h >= position[0] and self.y <= position[1] and self.y + self.w >= \
               position[1]


    def DrawObject(self, screen):
        screen.blit(self.text, (self.x + 3 + self.pad_x, self.y + 3))


    def LoadFont(self):
        self.font = pygame.font.Font(fa.FONT_PATH, self.h - 6 )
        self.text = self.font.render(self.keycode, 1, self.color)

    def SetPaddning(self, x):
        self.pad_x = x

    def SetColor(self, color):
        self.color = color