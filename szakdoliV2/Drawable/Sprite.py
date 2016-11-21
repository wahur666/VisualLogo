# -*- coding: utf-8 -*-


from os import getcwd
from System.Constants import IMAGE_PATHS as img
import PIL
from PIL import Image

import pygame

from Base.AbstractDrawable import AbstractDrawable


class Spirte(AbstractDrawable):

    def __init__(self, x = None, y = None, w = None, h = None, imgpath = img.PLACEHOLDER, descriptor="", vec2_pos = None, size = None):
        super(Spirte, self).__init__(x=x, y=y, w=w, h=h, vec2_pos=vec2_pos, size=size, descriptor=descriptor)
        self.imgpath = imgpath
        self.image = None
        self.base_rotation = 0


        self.LoadImage()

    def DrawObject(self, screen, rotation = None):
        if rotation:
            self.RotateTo(rotation)
        screen.blit(self.image, (self.x, self.y))
        self.base_rotation = rotation


    def IsInside(self, position):
        return self.x <= position[0] and self.x + self.h >= position[0] and self.y <= position[1] and self.y + self.w >= \
               position[1]


    def LoadImage(self):
        f = getcwd()+self.imgpath
        image = Image.open(f)
        image_w, image_h =  image.size
        if self.w is None:
            self.w = image_w
        if self.h is None:
            self.h = image_h

        image = image.resize((self.w, self.h), PIL.Image.ANTIALIAS)
        self.image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
        self.image = self.image.convert_alpha()

    def RotateTo(self, angle):
        rot_dif = self.base_rotation - angle
        self.image = pygame.transform.rotate(self.image, rot_dif)