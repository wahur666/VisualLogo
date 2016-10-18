# -*- coding: utf-8 -*-

import copy

from Base import AbstractDrawable

from Drawable.Rectangle import Rect
from Drawable.Tab import Tab
from Drawable.Base.Command import Command
from LogoModule.DrawableCommands import *

from System.Vector2 import Vector2
from System.SupportFunctions import MoveListElement

import Drawable.LogoModule.DrawableCommands as logo

class ScrollingPlane(AbstractDrawable):

    def __init__(self, x, y, w, h, tabs=2, descriptor="", vec2_pos=None, size=None):
        super(ScrollingPlane, self).__init__(x=x, y=y, w=w, h=h, vec2_pos=vec2_pos, size=size, descriptor=descriptor)
        self.tabs = tabs
        self.items = []

        self.clicked = None
        self.plateitems = []             # Ez egy lista ami listákat tárol majd #Listacpetion
        self.currentActivePlane = 0
        self.InitBefore()
        self.GenerateWindow()
        self.InitAfter()
        self.selectedCommand = None

    def IsInside(self, position):
        for item in self.grid:
            if item.IsInside(position):
                self.clicked = item
                return True

        for item in self.plateitems[self.currentActivePlane]:
            if item.IsInside(position):
                self.clicked = item
                return True

        for item in self.items:
            if item.IsInside(position):
                self.clicked = item
                return True
        return False


    def DrawObject(self, screen):
        for elem in self.items:
            elem.DrawObject(screen)

        for elem in self.plateitems[self.currentActivePlane]:
            elem.DrawObject(screen)

        for elem in self.grid:
            elem.DrawObject(screen)

        if self.selectedCommand:
            self.selectedCommand.DrawObject(screen)

    def GenerateWindow(self):
        tabwidth = self.w/self.tabs
        tabhight = 30
        for i in range(self.tabs):
            tab = Tab(self.x + i * tabwidth, self.y, tabwidth, tabhight, id=i, width=1, transparent=False)
            self.Add(tab)

        sidepanel = Rect(vec2_pos=Vector2(700, 75), size=(121, 520), width=1, transparent=False)
        #sidepanel.SetClickable(False)
        self.Add(sidepanel)

        self.PrepareSidePanelForLogo()

        self.mainpanel = Rect(self.x, self.y + tabhight, self.w, self.h, width=1, transparent=False)
        self.Add(self.mainpanel)

        #rect1 = Rect(self.x+10, self.y + tabhight + 20, 20, 30, width=1)
        #self.AddItemToCurrentPlane(rect1)



    def Add(self, elem):
        self.items.append(elem)

    def OnDrag(self, event):
        if self.selectedCommand:
            self.selectedCommand.drag(event.pos)
            if self.selectedCommand not in self.plateitems[self.currentActivePlane] and self.mainpanel.IsInside((self.selectedCommand.x, self.selectedCommand.y)):
                self.AddItemToCurrentPlane(self.selectedCommand)
            if self.selectedCommand in self.plateitems[self.currentActivePlane] and not self.mainpanel.IsInside((self.selectedCommand.x, self.selectedCommand.y)):
                self.plateitems[self.currentActivePlane].remove(self.selectedCommand)
                self.RearrangeCommands()
            if self.selectedCommand in self.plateitems[self.currentActivePlane]:
                for item in self.plateitems[self.currentActivePlane]:
                    if self.selectedCommand is not item:
                        if item.y - item.h / 2 < self.selectedCommand.y:
                            MoveListElement(self.plateitems[self.currentActivePlane], self.selectedCommand, self.plateitems[self.currentActivePlane].index(item))
                            self.RearrangeCommands(ignore=self.selectedCommand)


    def OnRelease(self, event):
        if self.selectedCommand:
            if self.mainpanel.IsInside(event.pos):
                self.SetCommandPosition()
                if not self.selectedCommand in self.plateitems[self.currentActivePlane]:
                    self.AddItemToCurrentPlane(self.selectedCommand)
            else:
                if self.selectedCommand in self.plateitems[self.currentActivePlane]:
                    self.plateitems[self.currentActivePlane].remove(self.selectedCommand)
                del self.selectedCommand
                self.RearrangeCommands()
        self.selectedCommand = None

    def OnClick(self, event):
        if isinstance(self.clicked, Tab):
            id = self.clicked.GetId()
            self.RepaintTabs(id)
            print id
            self.currentActivePlane = id
        elif isinstance(self.clicked, Command):
            if not self.mainpanel.IsInside(event.pos):
                self.selectedCommand = copy.deepcopy(self.clicked)
                #DeepCopy Eseten muszaly ujra betolteni a kepet!!!
                self.selectedCommand.LoadSprite()
            else:
                self.selectedCommand = self.clicked

            self.selectedCommand.setDelta(event.pos)
            print "Copied"
        else:
            print self.clicked

    def SetCommandPosition(self):
        if not self.selectedCommand in self.plateitems[self.currentActivePlane]:
            self.selectedCommand.SetPosition(self.mainpanel.x + self.mainpanel.w / 2 - 25, self.mainpanel.y + 5 + len(self.plateitems[self.currentActivePlane]) * 55)
        else:
            self.selectedCommand.SetPosition(self.mainpanel.x + self.mainpanel.w / 2 - 25, self.mainpanel.y + 5 + self.plateitems[self.currentActivePlane].index(self.selectedCommand) * 55)

    def RearrangeCommands(self, ignore=None):
        for item in self.plateitems[self.currentActivePlane]:
            if item is not ignore:
                item.SetPosition(self.mainpanel.x + self.mainpanel.w / 2 - 25, self.mainpanel.y + 5 + self.plateitems[self.currentActivePlane].index(item) * 55)

    def AddItemToCurrentPlane(self, item, plane=None):
        if plane:
            self.plateitems[plane].append(item)
        else:
            self.plateitems[self.currentActivePlane].append(item)


    def InitBefore(self):
        for i in range(self.tabs):
            self.plateitems.append([])

    def RepaintTabs(self, id):
        for item in self.items:
            if isinstance(item, Tab):
                if id == item.GetId():
                    item.selected = True
                else:
                    item.selected = False

    def InitAfter(self):
        self.RepaintTabs(0)

    def PrepareSidePanelForLogo(self):
        self.grid = []

        # Sidepanel elemei
        command = logo.Forward(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.Backward(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.Left(vec2_pos=Vector2(0, 0), size=(50, 50))
        self.grid.append(command)

        command = logo.Right(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.PenDown(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.PenUp(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.PenWidth(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.PenColor(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.Home(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.FloodFill(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.Reset(vec2_pos=Vector2(0, 0), size=(50, 50))
        self.grid.append(command)

        command = logo.Clear(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.ShowTurtle(vec2_pos=Vector2(0, 0), size=(50, 50))
        self.grid.append(command)

        command = logo.HideTurlte(vec2_pos=Vector2(0, 0), size=(50, 50))
        self.grid.append(command)

        #TO BE IMPLEMENTED
        '''command = logo.Loop(vec2_pos=Vector2(0, 0), size=(50, 50))
        self.Add(self.command)'''

        self.DrawGrid()

        #self.items.extend(self.grid)

    def DrawGrid(self):
        from math import ceil
        base_x = 708
        base_y = 88
        delta_x = delta_y = 55
        for i in range(int(ceil(len(self.grid)/2.))):
            for j in range(2):
                counter = i * 2 + j
                if counter == len(self.grid):
                    return
                self.grid[counter].SetPosition(base_x + delta_x * j, base_y + delta_y * i)

