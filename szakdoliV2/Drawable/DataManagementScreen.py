from Drawable.Base import AbstractDrawable
from Rectangle import Rect
from System.Constants import *
from Button import Button
from Sprite import Spirte
from System.SupportFunctions import LoadZip_Image

import os, os.path
import pygame.font

class DataManagementScreen(AbstractDrawable):

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", parent=None):
        super(DataManagementScreen, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        self.radiobuttons = []
        self.button_ok = Button(self.x + 325, self.y + 450, 75, 75, keycode=FONT_AWESOME.CHECK)
        self.button_ok.SetTextIconColor(COLOR.GREEN)
        self.button_cancel = Button(self.x + 500, self.y + 450, 75, 75, keycode=FONT_AWESOME.CLOSE, padding=8)
        self.button_cancel.SetTextIconColor(COLOR.RED)
        self.main_rect = Rect(self.x, self.y, self.w, self.h, color=COLOR.BLACK, width=1, transparent=False)
        self.PrepareCheckboxes()
        self.text = None
        self.font = None
        self.text_load = None
        self.text_save = None
        self.selected = None
        self.parent = parent

    def IsInside(self, position):
        if self.x <= position[0] and self.x + self.w >= position[0] and self.y <= position[1] and self.y + self.h >= position[1]:
            for elem in self.radiobuttons:
                if elem.IsInside(position):
                    self.selected = elem
                    return True
            if self.button_ok.IsInside(position):
                self.selected = self.button_ok
                return True
            if self.button_cancel.IsInside(position):
                self.selected = self.button_cancel
                return True
            return False
        else:
            return False

    def DrawObject(self, screen):
        self.main_rect.DrawObject(screen)
        for elem in self.radiobuttons:
            elem.DrawObject(screen)
        screen.blit(self.text, (self.x + 415, self.y + 10))
        self.button_ok.DrawObject(screen)
        self.button_cancel.DrawObject(screen)



    def PrepareCheckboxes(self):
        for i in range(3):
            for j in range(7):
                pos_x = self.main_rect.x + 25 + j * 125
                pos_y = self.main_rect.y + 75 + i * 125
                checkbox = CheckboxRect(pos_x, pos_y,size=(100,100), index=int(i * 7 + j))
                self.radiobuttons.append(checkbox)

    def SetMode(self, mode):
        self.mode = mode
        if not self.font:
            self.LoadFont()
        if mode == "Save":
            self.text = self.text_save
        elif mode == "Load":
            self.text = self.text_load
        self.LoadAllImages()
        self.DeselectAllRadioButtons()

    def LoadFont(self):
        font = os.path.join("Resources", "nimbus-roman-no9-l.regular.otf")
        self.font = pygame.font.Font(font, 38)
        self.text_save = self.font.render("Save", 1, COLOR.BLACK)
        self.text_load = self.font.render("Load", 1, COLOR.BLACK)

    def OnClick(self, event):
        if isinstance(self.selected, CheckboxRect):
            for elem in self.radiobuttons:
                if elem is self.selected:
                    elem.SetSelected(True)
                else:
                    elem.SetSelected(False)
        elif isinstance(self.selected, Button):
            if self.selected is self.button_ok:
                index = -1
                for elem in self.radiobuttons:
                    if elem.GetSelected():
                        index = elem.index
                if index > -1:
                    if self.mode == "Save":
                        self.parent.CloseDataManagementWindow()
                        self.parent.SaveData(index)
                        print "Saved", index
                    else:
                        self.parent.LoadData(index)
                        print  "Loaded", index
                else:
                    print "no elem selected"

            else:
                print "cancel"

            self.parent.CloseDataManagementWindow()

    def DeselectAllRadioButtons(self):
        for elem in self.radiobuttons:
            elem.SetSelected(False)

    def LoadAllImages(self):
        for elem in self.radiobuttons:
            elem.LoadImage()


class CheckboxRect(AbstractDrawable):

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor="", color=COLOR.BLACK, index = None):
        super(CheckboxRect, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        self.main_rect = Rect(self.x, self.y, self.w, self.h, color=color, width=1, transparent=False)
        self.selected = False
        self.index = index
        self.imgpath = LoadZip_Image(index)
        self.sprite = None

    def DrawObject(self, screen):
        if self.selected:
            self.main_rect.width = 3
            self.main_rect.color = COLOR.GREEN
        else:
            self.main_rect.width = 1
            self.main_rect.color = COLOR.RED
        self.main_rect.DrawObject(screen)
        self.sprite.DrawObject(screen)

    def IsInside(self, position):
        return self.main_rect.IsInside(position)

    def SetSelected(self, state):
        self.selected = state

    def LoadImage(self):
        self.sprite = Spirte(self.x + 2, self.y + 2, self.w - 5, self.h - 5, self.imgpath, mode=1, index = self.index)

    def GetSelected(self):
        return self.selected