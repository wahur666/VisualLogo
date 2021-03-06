# -*- coding: utf-8 -*-

import pygame
import random

from Drawable.Base.Command import Command
from Drawable.Rectangle import Rect
from System.Constants import FONT_AWESOME as fa
from System.Constants import IMAGE_PATHS as img
from System.Constants import COLOR as Color


class Forward(Command):

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None,  imgpath=None, mul = 1):
        super(Forward, self).__init__(x, y, w, h, vec2_pos, size)
        self.imagePath = imgpath
        self.mul = mul
        if self.mul == 1:
            self.keycode = fa.UP
            self.SetKeyCodePadding(2)
        elif self.mul == 2:
            self.keycode = fa.LONG_UP
            self.SetKeyCodePadding(13)

        self.mainRect.SetAccentColor(Color.HATTER_1)


class Backward(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None,  imgpath=None, mul = 1):
        super(Backward, self).__init__(x, y, w, h, vec2_pos, size)
        self.imagePath = imgpath
        self.mul = mul
        if self.mul == 1:
            self.keycode = fa.DOWN
            self.SetKeyCodePadding(2)
        elif self.mul == 2:
            self.keycode = fa.LONG_DOWN
            self.SetKeyCodePadding(13)

        self.mainRect.SetAccentColor(Color.HATTER_1)


class Right(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, imgpath=None, mul = 2):
        super(Right, self).__init__(x, y, w, h, vec2_pos, size)

        self.mul = mul
        if self.mul == 2:
            self.imagePath = img.BEND_RIGHT
        elif self.mul == 6:
            self.imagePath = img.TURN_RIGHT

        self.mainRect.SetAccentColor(Color.HATTER_2)


class Left(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None,  imgpath=None, mul = 2):
        super(Left, self).__init__(x, y, w, h, vec2_pos, size)

        self.mul = mul
        if self.mul == 2:
            self.imagePath = img.BEND_LEFT
        elif self.mul == 6:
            self.imagePath = img.TURN_LEFT

        self.mainRect.SetAccentColor(Color.HATTER_2)



class Home(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None,  imgpath=None):
        super(Home, self).__init__(x, y, w, h, vec2_pos, size)

        self.imagePath = imgpath
        self.keycode = fa.HOME
        self.SetKeyCodePadding(2)
        self.mainRect.SetAccentColor(Color.HATTER_3)



class PenDown(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, imgpath=None):
        super(PenDown, self).__init__(x, y, w, h, vec2_pos, size)


        self.keycode = fa.PEN
        self.SetKeyCodePadding(2)
        self.mainRect.SetAccentColor(Color.HATTER_4)

class PenUp(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, imgpath=None):
        super(PenUp, self).__init__(x, y, w, h, vec2_pos, size)
        self.keycode = fa.PEN
        self.mainRect.SetAccentColor(Color.HATTER_4)
        self.SetKeyCodePadding(2)

        self.cross_points = [(self.x + 10, self.y + 5),
                             (self.x + 5, self.y + 10),
                             (self.x + self.w - 10, self.y + self.h - 5),
                             (self.x + self.w - 5, self.y + self.h - 10)]

    def DrawObject(self, screen):
        super(PenUp, self).DrawObject(screen)
        pygame.draw.polygon(screen, Color.RED, self.cross_points, 0)

    def SetPosition(self, x, y):
        super(PenUp, self).SetPosition(x, y)
        self.cross_points = [(self.x + 8, self.y + 5),
                             (self.x + 5, self.y + 8),
                             (self.x + self.w - 8, self.y + self.h - 5),
                             (self.x + self.w - 5, self.y + self.h - 8)]

class PenWidth(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, imgpath=None):
        super(PenWidth, self).__init__(x, y, w, h, vec2_pos, size)

        self.keycode = fa.PLACEHOLDER

        self.pen_width = 0
        self.mainRect.SetAccentColor(Color.HATTER_6)
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

    def SetPenWidth(self, witdh):
        self.pen_width = witdh

class PenColor(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, imgpath=None):
        super(PenColor, self).__init__(x, y, w, h, vec2_pos, size)

        self.keycode = fa.PLACEHOLDER


        self.colorlist = Color.COLOR_LIST
        self.current_color_index = 1
        self.mainRect.SetAccentColor(Color.HATTER_6)
        self.pen_color = self.colorlist[self.current_color_index]

    def DrawObject(self, screen):
        self.mainRect.DrawObject(screen)
        pygame.draw.circle(screen, self.pen_color, (int(self.x + self.w / 2), int(self.y + self.h / 2)), 15, 0 )

    def ChangeColor(self):
        self.current_color_index = (self.current_color_index + 1) % len(self.colorlist)
        self.pen_color = self.colorlist[self.current_color_index]

    def SetPosition(self, x, y):
        super(PenColor, self).SetPosition(x, y)

    def SetColor(self, color):
        self.pen_color = color

class FloodFill(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, imgpath=None):
        super(FloodFill, self).__init__(x, y, w, h, vec2_pos, size)

        self.imagePath = imgpath
        self.keycode = fa.FLOODFILL
        self.mainRect.SetAccentColor(Color.HATTER_3)


class Reset(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None,  imgpath=None):
        super(Reset, self).__init__(x, y, w, h, vec2_pos, size)

        self.imagePath = imgpath
        self.keycode = fa.RESET



class Clear(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, imgpath=None):
        super(Clear, self).__init__(x, y, w, h, vec2_pos, size)

        self.imagePath = imgpath
        self.keycode = fa.CLEAR



class ShowTurtle(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, imgpath=None):
        super(ShowTurtle, self).__init__(x, y, w, h, vec2_pos, size)

        self.keycode = fa.EYE_SEE
        self.mainRect.SetAccentColor(Color.HATTER_4)

class HideTurtle(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None,  imgpath=None):
        super(HideTurtle, self).__init__(x, y, w, h, vec2_pos, size)

        self.keycode = fa.EYE_NOT_SEE
        self.mainRect.SetAccentColor(Color.HATTER_4)



class Loop(Command):

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, imgpath=None):
        super(Loop, self).__init__(x, y, w, h, vec2_pos, size)

        self.keycode = fa.LOOP
        self.loopend = None

        self.cycle_number = 3
        self.remaining_cycle = self.cycle_number

        self.RollColor()

        self.compile_information = {
            "compiled" : False,
            "pre_test" : False,
            "loopend_index" : -1
        }

        self.running = False
        self.mainRect.SetAccentColor(Color.HATTER_5)

        self.InitCycleDisplayMatrix()

        self.loop_id = None
        self.ark_level = 0

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
            amount = self.cycle_number
        for i in range(3):
            for j in range(3):
                if self.cycle_display_matrix[amount][i * 3 + j]:
                    pos_x = 8 + j * 16 + self.x + 55
                    pos_y = 8 + i * 16 + self.y + 1
                    pygame.draw.circle(screen, Color.MAGENTA, (int(pos_x), int(pos_y)), 5, 0)

    def SetLoopend(self, loopend):
        self.loopend = loopend

    def DrawLoopend(self, screen):
        if self.loopend:
            #self.loopend.DrawObject(screen)
            point_list = self.CalclatePointList()
            #pygame.draw.line(screen, Color.BLUE, (int(self.x + self.w * 0.75), int(self.y + self.h / 2)),
            #          (int(self.loopend.x + self.loopend.w / 2),int(self.loopend.y + self.loopend.h / 2)),1)
            pygame.draw.aalines(screen, Color.LOOP_COLORS[self.color], False, point_list, 1)

    def SetCompileInfo(self, pre_test, loopend_index):
        self.compile_information["compiled"] = True
        self.compile_information["pre_test"] = pre_test
        self.compile_information["loopend_index"] = loopend_index

    def ResetCompileInfo(self):
        self.compile_information["compiled"] = False

    def CountDown(self):
        self.remaining_cycle -= 1

    def ResetCycleCounter(self):
        self.remaining_cycle = self.cycle_number

    def ChangeCycleNumber(self):
        self.cycle_number = (self.cycle_number + 1) % 10
        if not self.running and not self.cycle_number:
            self.cycle_number = 1
        self.remaining_cycle = self.cycle_number

    def SetCycleNumber(self, number):
        self.cycle_number = number
        self.remaining_cycle = self.cycle_number

    def CalclatePointList(self):
        point_list = []
        if self.ark_level == 0:
            if self.y < self.loopend.y:
                loop_start = (round(self.x + self.w * .75), round(self.y + self.h))
            else:
                loop_start = (round(self.x + self.w * .75), round(self.y))
            l3 = (round(self.x + self.w * .75), round(self.loopend.y + self.loopend.h / 2))
            point_list.append(loop_start)
            point_list.append(l3)
        elif self.ark_level == 1:
            loop_start = (round(self.x + self.w), round(self.y + self.h / 2))
            l0 = (round(self.x + self.w * 1.25), round(self.y + self.h / 2))
            l3 = (round(self.x + self.w * 1.25), round(self.loopend.y + self.loopend.h / 2))
            point_list.append(loop_start)
            point_list.append(l0)
            point_list.append(l3)
        elif self.ark_level > 1:
            loop_start = (round(self.x + self.w), round(self.y + self.h / 2))
            l0 = (round(self.x + self.w * 1.40), round(self.y + self.h / 2))
        #l1 = (round(self.x + self.w * 1.45) , (round((self.loopend.y + self.loopend.h / 2 ) + round(self.y + self.h / 2)) / 2))
            l3 = (round(self.x + self.w * 1.40), round(self.loopend.y + self.loopend.h / 2))
            point_list.append(loop_start)
            point_list.append(l0)
            point_list.append(l3)

        loop_end = (round(self.loopend.x + self.loopend.w), round(self.loopend.y + self.loopend.h / 2))
        point_list.append(loop_end)
        return point_list

    def RollColor(self):
        self.color = random.randint(0, len(Color.LOOP_COLORS) - 1)


class LoopEnd(Command):
    def __init__(self, vec2_pos=None, size=None):
        super(LoopEnd, self).__init__(vec2_pos=vec2_pos, size=size)

        self.compile_information = {
            "compiled": False,
            "pre_test": False,
            "loopbase_index": -1
        }

        self.loop_id = None
        self.loopstart = None

        self.mainRect.SetAccentColor(Color.HATTER_5)

    def DrawObject(self, screen):
        self.mainRect.DrawObject(screen)

    def SetCompileInfo(self, pre_test, loopbase_index):
        self.compile_information["compiled"] = True
        self.compile_information["pre_test"] = pre_test
        self.compile_information["loopbase_index"] = loopbase_index

    def ResetCompileInfo(self):
        self.compile_information["compiled"] = False

    def SetLoopStart(self, loop):
        self.loopstart = loop