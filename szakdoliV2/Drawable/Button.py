# -*- coding: utf-8 -*-

import pygame
from os import getcwd
from Rectangle import Rect

from Drawable.Base.AbstractDrawable import AbstractDrawable

class Button(AbstractDrawable):

    def __init__(self, x, y, w, h, imgpath = "\\Resources\\icon-placeholder.png", description=''):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.imgpath = imgpath
        self.desctiption = description
        self.image = None

    def DrawObject(self, screen):
        if not self.image:
            self.LoadImage()
        self.buttonsquircle.DrawObject(screen)      #BASE
                                                    #FEEDBACK
        screen.blit(self.image, (self.x + 2, self.y + 2))   #IMAGE


    def IsInside(self, position):
        return self.x <= position[0] and self.x + self.h >= position[0] and self.y <= position[1] and self.y + self.w >= \
               position[1]

    def bind(self, funcpointer):
        self.OnClick = funcpointer

    def OnClick(self, event_type):
        raise RuntimeError("Undobund button")

    def LoadImage(self):
        imageRect = pygame.Rect(self.x - 2, self.y - 2, self.w - 5, self.h - 5)
        f = getcwd()+self.imgpath
        self.image = pygame.image.load(f)
        self.image = pygame.transform.scale(self.image, imageRect.size)
        self.image = self.image.convert_alpha()
        self.buttonsquircle = Rect(self.x  , self.y , self.w , self.h, width=1)