import pygame
from os import getcwd

from AbstractDrawable import AbstractDrawable

class Button(AbstractDrawable):

    def __init__(self, x, y, w, h, imgpath):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.imgpath = imgpath

    def DrawObject(self, screen):
        imageRect = pygame.Rect(self.x, self.y, self.w, self.h)
        f = getcwd()+self.imgpath
        image = pygame.image.load(f)
        image = pygame.transform.scale(image, imageRect.size)
        image = image.convert_alpha()
        screen.blit(image, (self.x, self.y))


    def IsInside(self, position):
        pass

    def OnClick(self):
        pass