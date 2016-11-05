# -*- coding: utf-8 -*-

from Drawable.Base.Command import Command
from System.Constants import FONT_AWESOME as fa
import os.path
import pygame
from System.Constants import COLOR as Color

class Forward(Command):

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None, mul = 1):
        super(Forward, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        #self.imagePath = "\\Resources\\arrow-up.png"
        self.imagePath = imgpath
        self.mul = mul
        if self.mul == 1:
            self.keycode = fa.ANGLE_UP
        elif self.mul == 2:
            self.keycode = fa.ANGLE_DOUBLE_UP



class Backward(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None, mul = 1):
        super(Backward, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        #self.imagePath = "\\Resources\\arrow-down.png"
        self.imagePath = imgpath
        self.mul = mul
        if self.mul == 1:
            self.keycode = fa.ANGLE_DOWN
        elif self.mul == 2:
            self.keycode = fa.ANGLE_DOUBLE_DOWN



class Right(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None, mul = 1):
        super(Right, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        #self.imagePath = "\\Resources\\turnright.png"

        self.imagePath = imgpath
        self.mul = mul
        if self.mul == 1:
            self.keycode = fa.ANGLE_RIGHT
        elif self.mul == 2:
            self.keycode = fa.ANGLE_DOUBLE_RIGHT



class Left(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None, mul = 1):
        super(Left, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        #self.imagePath = "\\Resources\\turnleft.png"

        self.imagePath = imgpath
        self.mul = mul
        if self.mul == 1:
            self.keycode = fa.ANGLE_LEFT
        elif self.mul == 2:
            self.keycode = fa.ANGLE_DOUBLE_LEFT



class Home(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(Home, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        self.imagePath = imgpath
        self.keycode = fa.HOME



class PenDown(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(PenDown, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        self.imagePath = os.path.join(os.path.sep,"Resources", "pencil2.png")

        #self.imagePath = imgpath
        #self.keycode = fa.PEN


class PenUp(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(PenUp, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        #self.imagePath = "\\Resources\\pencil.png"

        self.imagePath = imgpath
        self.keycode = fa.PEN



class PenWidth(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(PenWidth, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        self.keycode = fa.PLACEHOLDER


class PenColor(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(PenColor, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        self.keycode = fa.PLACEHOLDER



class FloodFill(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(FloodFill, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        self.imagePath = imgpath
        self.keycode = fa.FLOODFILL



class Reset(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(Reset, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        self.imagePath = imgpath
        self.keycode = fa.RESET



class Clear(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(Clear, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        self.imagePath = imgpath
        self.keycode = fa.CLEAR



class ShowTurtle(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(ShowTurtle, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        self.keycode = fa.PLACEHOLDER


class HideTurlte(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(HideTurlte, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        self.keycode = fa.PLACEHOLDER



class Loop(Command):
    # mivel ez több darabból fog állni ezért nem lehet csak úgy az örököltet használni
    #def IsInside(self, position):
    #   pass

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(Loop, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        self.keycode = fa.LOOP
        self.loopend = None

        self.cycle_nubmer = 3
        self.remaining_cycle = self.cycle_nubmer

        self.compile_information = {
            "compiled" : False,
            "pre_test" : False,
            "loopend_index" : -1
        }

    def DrawObject(self, screen):
        super(Loop, self).DrawObject(screen)


    def SetLoopend(self, loopend):
        self.loopend = loopend

    def DrawLoopend(self, screen):
        if self.loopend:
            #self.loopend.DrawObject(screen)
            pygame.draw.line(screen, Color.BLUE, (int(self.x + self.w * 0.75), int(self.y + self.h / 2)),
                      (int(self.loopend.x + self.loopend.w / 2),int(self.loopend.y + self.loopend.h / 2)),1)


    def SetCompileInfo(self, pre_test, loopend_index):
        self.compile_information["compiled"] = True
        self.compile_information["pre_test"] = pre_test
        self.compile_information["loopend_index"] = loopend_index

    def ResetCompileInfo(self):
        self.compile_information["compiled"] = False

    def CountDown(self):
        self.remaining_cycle -= 1

    def ResetCycleCounter(self):
        self.remaining_cycle = self.cycle_nubmer

class LoopEnd(Command):
    def __init__(self, vec2_pos=None, size=None):
        super(LoopEnd, self).__init__(vec2_pos=vec2_pos, size=size)

        self.compile_information = {
            "compiled": False,
            "pre_test": False,
            "loopbase_index": -1
        }

    def DrawObject(self, screen):
        self.mainRect.DrawObject(screen)

    def SetCompileInfo(self, pre_test, loopbase_index):
        self.compile_information["compiled"] = True
        self.compile_information["pre_test"] = pre_test
        self.compile_information["loopbase_index"] = loopbase_index

    def ResetCompileInfo(self):
        self.compile_information["compiled"] = False

