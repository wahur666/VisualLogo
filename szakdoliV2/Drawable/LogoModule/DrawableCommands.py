# -*- coding: utf-8 -*-

from Drawable.Base.Command import Command
from Drawable.Rectangle import Rect
from System.Constants import FONT_AWESOME as fa
from System.Constants import IMAGE_PATHS as img
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
            self.keycode = fa.UP
        elif self.mul == 2:
            self.keycode = fa.LONG_UP



class Backward(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None, mul = 1):
        super(Backward, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        #self.imagePath = "\\Resources\\arrow-down.png"
        self.imagePath = imgpath
        self.mul = mul
        if self.mul == 1:
            self.keycode = fa.DOWN
        elif self.mul == 2:
            self.keycode = fa.LONG_DOWN



class Right(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None, mul = 1):
        super(Right, self).__init__(x, y, w, h, vec2_pos, size, descriptor)


        #self.imagePath = imgpath
        self.mul = mul
        if self.mul == 1:
            self.imagePath = img.BEND_RIGHT
        elif self.mul == 2:
            self.imagePath = img.TURN_RIGHT



class Left(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None, mul = 1):
        super(Left, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        #self.imagePath = imgpath
        self.mul = mul
        if self.mul == 1:
            self.imagePath = img.BEND_LEFT
        elif self.mul == 2:
            self.imagePath = img.TURN_LEFT



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

        self.pen_width = 0

        self.width_rect = Rect(self.x, self.y, self.w, self.h, color=Color.BLACK)

    def DrawObject(self, screen):
        self.mainRect.DrawObject(screen)
        self.width_rect.Extend(y=self.y + self.h / 2 - self.pen_width * 5, h=self.pen_width * 10)
        self.width_rect.DrawObject(screen)

    def Extend(self):
        self.pen_width = (self.pen_width + 1) % 4

    def SetPosition(self, x, y):
        super(PenWidth, self).SetPosition(x, y)
        self.width_rect.SetPosition(x, y)

class PenColor(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(PenColor, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        self.keycode = fa.PLACEHOLDER


        self.colorlist = Color.COLOR_LIST
        self.current_color_index = 1

        self.pen_color = self.colorlist[self.current_color_index]

        self.color_rect = Rect(self.x + 10, self.y + 10, self.w - 20, self.h - 20, color=self.pen_color)

    def DrawObject(self, screen):
        self.mainRect.DrawObject(screen)
        self.color_rect.DrawObject(screen)

    def ChangeColor(self):
        self.current_color_index = (self.current_color_index + 1) % len(self.colorlist)
        self.pen_color = self.colorlist[self.current_color_index]
        self.color_rect.SetColor(self.pen_color)

    def SetPosition(self, x, y):
        super(PenColor, self).SetPosition(x, y)
        self.color_rect.SetPosition(x + 10, y + 10)

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

        self.keycode = fa.EYE_SEE


class HideTurlte(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", imgpath=None):
        super(HideTurlte, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

        self.keycode = fa.EYE_NOT_SEE



class Loop(Command):

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

        self.running = False

        self.InitCycleDisplayMatrix()

    def InitCycleDisplayMatrix(self):
        self.cycle_display_matrix = []
        matix_number = [0, 0, 0,
                        0, 0, 0,
                        0, 0, 0]
        self.cycle_display_matrix.append(matix_number) #0

        matix_number = [0, 0, 0,
                        0, 1, 0,
                        0, 0, 0]
        self.cycle_display_matrix.append(matix_number) #1

        matix_number = [1, 0, 0,
                        0, 0, 0,
                        0, 0, 1]
        self.cycle_display_matrix.append(matix_number) #2

        matix_number = [1, 0, 0,
                        0, 1, 0,
                        0, 0, 1]
        self.cycle_display_matrix.append(matix_number) #3

        matix_number = [1, 0, 1,
                        0, 0, 0,
                        1, 0, 1]
        self.cycle_display_matrix.append(matix_number) #4

        matix_number = [1, 0, 1,
                        0, 1, 0,
                        1, 0, 1]
        self.cycle_display_matrix.append(matix_number) #5

        matix_number = [1, 0, 1,
                        1, 0, 1,
                        1, 0, 1]
        self.cycle_display_matrix.append(matix_number) #6

        matix_number = [1, 0, 1,
                        1, 1, 1,
                        1, 0, 1]
        self.cycle_display_matrix.append(matix_number) #7

        matix_number = [1, 1, 1,
                        1, 0, 1,
                        1, 1, 1]
        self.cycle_display_matrix.append(matix_number) #8

        matix_number = [1, 1, 1,
                        1, 1, 1,
                        1, 1, 1]
        self.cycle_display_matrix.append(matix_number) #9


    def DrawObject(self, screen):
        super(Loop, self).DrawObject(screen)
        self.DrawRemainingCycleMatrix(screen)

    def DrawRemainingCycleMatrix(self, screen):
        if self.running:
            amount = self.remaining_cycle
        else:
            amount = self.cycle_nubmer
        for i in range(3):
            for j in range(3):
                if self.cycle_display_matrix[amount][i * 3 + j]:
                    pos_x = 8 + j * 16 + self.x + 55
                    pos_y = 8 + i * 16 + self.y + 1
                    pygame.draw.circle(screen, Color.MAGENTA, (pos_x, pos_y), 5, 0)

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

    def ChangeCycleNumber(self):
        self.cycle_nubmer = (self.cycle_nubmer + 1) % 10
        if not self.running and not self.cycle_nubmer:
            self.cycle_nubmer = 1
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

