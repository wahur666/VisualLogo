# -*- coding: utf-8 -*-

from Base import AbstractDrawable
from Drawable.Rectangle import Rect
from Drawable.Tab import Tab


class ScrollingPlane(AbstractDrawable):

    def __init__(self, x, y, w, h, tabs=2, descriptor="", vec2_pos=None, size=None):
        super(ScrollingPlane, self).__init__(x=x, y=y, w=w, h=h, vec2_pos=vec2_pos, size=size, descriptor=descriptor)
        self.tabs = tabs
        self.items = []

        self.clicked = None
        self.plateitems = []             # Ez egy lista ami listákat tárol majd #Listacpetion
        self.currentActivePlane = 0
        self.InitAfter()
        self.GenerateWindow()

    def IsInside(self, position):
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

    def GenerateWindow(self):
        tabwidth = self.w/self.tabs
        tabhight = 30
        for i in range(self.tabs):
            tab = Tab(self.x + i * tabwidth, self.y, tabwidth, tabhight, id=i, width=1)
            self.Add(tab)
        rect = Rect(self.x, self.y + tabhight, self.w, self.h, width=1)
        self.Add(rect)

        rect1 = Rect(self.x+10, self.y + tabhight + 20, 20, 30, width=1)
        self.AddItemToCurrentPlane(rect1)

    def Add(self, elem):
        self.items.append(elem)

    def CLICKED(self):
        if isinstance(self.clicked, Tab):
            id = self.clicked.GetId()
            print id
            self.currentActivePlane = id
        else:
            print self.clicked

    def AddItemToCurrentPlane(self, item, plane=None):
        if plane:
            self.plateitems[plane].append(item)
        else:
            self.plateitems[self.currentActivePlane].append(item)


    def InitAfter(self):
        for i in range(self.tabs):
            self.plateitems.append([])