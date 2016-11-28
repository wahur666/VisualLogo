# -*- coding: utf-8 -*-

import copy

from Base import AbstractDrawable

from Drawable.Tab import Tab
from RunPointer import RunPointer
from LogoModule.DrawableCommands import *
from Button import Button

from System.Vector2 import Vector2
from System.SupportFunctions import MoveListElement
from System.Constants import MOUSE as Mouse, FONT_AWESOME as fa

import Drawable.LogoModule.DrawableCommands as logo

class ScrollingPlane(AbstractDrawable):

    def __init__(self, x, y, w, h, tabs=2, descriptor="", vec2_pos=None, size=None, parent=None):
        super(ScrollingPlane, self).__init__(x=x, y=y, w=w, h=h, vec2_pos=vec2_pos, size=size, descriptor=descriptor)
        self.parent = parent

        self.tabs = tabs
        self.items = []

        self.clicked = None
        self.plateitems = []             # Ez egy lista ami listákat tárol majd #Listaception
        self.currentActivePlane = 0
        self.InitBefore()
        self.GenerateWindow()
        self.InitAfter()
        self.selectedCommand = None
        self.loopend = None

        self.sidepanel_active = True

        self.base = {
            'height' : self.h,
            'x' : self.x,
            'y' : self.y,
            'width' : self.w
        }
        self.counter = 0

    def __del__(self):
        print "Scrollong plane destruktor lefutott"

    def IsInside(self, position):
        if self.sidepanel_active:
            self.sidepanel.IsInside(position)
            for item in self.grid:
                if item.IsInside(position):
                    self.clicked = item
                    return True
            if self.clearCommandsButton.IsInside(position):
                if self.plateitems[self.currentActivePlane]:
                    self.clicked = self.clearCommandsButton
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

        for elem in self.plateitems[self.currentActivePlane]:
            if isinstance(elem, Loop):
                elem.DrawLoopend(screen)

        if self.sidepanel_active:
            self.sidepanel.DrawObject(screen)
            for elem in self.grid:
                elem.DrawObject(screen)
            if self.plateitems[self.currentActivePlane]:
                self.clearCommandsButton.DrawObject(screen)

        if self.selectedCommand:
            self.selectedCommand.DrawObject(screen)

    def GenerateWindow(self):
        tabwidth = self.w/self.tabs
        tabhight = 30
        for i in range(self.tabs):
            tab = Tab(self.x + i * tabwidth, self.y, tabwidth, tabhight, id=i, width=1, transparent=False)
            self.Add(tab)

        self.sidepanel = Rect(vec2_pos=Vector2(700, 75), size=(121, 520), width=1, transparent=False)
        self.clearCommandsButton = Button(771, 594, 50, 50, keycode=fa.ROUND_X, padding=4)
        self.clearCommandsButton.bind(self.ClearCurrentSource)
        self.clearCommandsButton.SetTextIconColor(Color.RED)

        self.PrepareSidePanelForLogo()

        self.mainpanel = Rect(self.x, self.y + tabhight, self.w, self.h, width=1, transparent=False)
        self.Add(self.mainpanel)

        #rect1 = Rect(self.x+10, self.y + tabhight + 20, 20, 30, width=1)
        #self.AddItemToCurrentPlane(rect1)



    def Add(self, elem):
        self.items.append(elem)

    def OnDrag(self, event):
        adjustment_needed = False
        if self.selectedCommand:
            self.selectedCommand.drag(event.pos)
            if self.selectedCommand not in self.plateitems[self.currentActivePlane] and self.mainpanel.IsInside((event.pos)):
                if isinstance(self.selectedCommand, Loop):
                    self.selectedCommand.loopend.SetPosition(self.selectedCommand.x, self.selectedCommand.y + 55)
                    self.AddItemToCurrentPlane(self.loopend)
                self.AddItemToCurrentPlane(self.selectedCommand)
                self.RearrangeCommands(ignore=self.selectedCommand)
            if self.selectedCommand in self.plateitems[self.currentActivePlane] and not self.mainpanel.IsInside((event.pos)):
                self.plateitems[self.currentActivePlane].remove(self.selectedCommand)
                if isinstance(self.selectedCommand, Loop):
                    if self.selectedCommand.loopend in self.plateitems[self.currentActivePlane]:
                        self.plateitems[self.currentActivePlane].remove(self.selectedCommand.loopend)
                if isinstance(self.selectedCommand, LoopEnd):
                    for item in self.plateitems[self.currentActivePlane]:
                        if isinstance(item, Loop):
                            if item.loopend == self.selectedCommand:
                                self.plateitems[self.currentActivePlane].remove(item)
                                self.selectedCommand = None
                                adjustment_needed = True
                                break
                self.RearrangeCommands()
            self.ResizeSourceBlock()
            if self.selectedCommand in self.plateitems[self.currentActivePlane]:
                for item in self.plateitems[self.currentActivePlane]:
                    if self.selectedCommand is not item and item is not None:
                        if item.y - item.h / 2 < self.selectedCommand.y:
                            MoveListElement(self.plateitems[self.currentActivePlane], self.selectedCommand, self.plateitems[self.currentActivePlane].index(item))
                            self.RearrangeCommands(ignore=self.selectedCommand)
            if self.mainpanel.x < event.pos[0] and event.pos[0] < self.mainpanel.x + self.mainpanel.w:
                if event.pos[1] < 20:
                    self.MoveSourcePanel(1)
                if event.pos[1] > 700:
                    self.MoveSourcePanel(-1)
            if adjustment_needed:
                while self.mainpanel.y + self.mainpanel.h < 700 and self.mainpanel.h > 700:
                    self.MoveSourcePanel(1)



    def OnRelease(self, event):
        if self.selectedCommand:
            if self.mainpanel.IsInside(event.pos):
                self.SetCommandPosition()
                if not self.selectedCommand in self.plateitems[self.currentActivePlane]:
                    self.AddItemToCurrentPlane(self.selectedCommand)
                    if isinstance(self.selectedCommand, Loop):
                        self.AddItemToCurrentPlane(self.selectedCommand.loopend)
            else:
                while self.mainpanel.y + self.mainpanel.h < 700 and self.mainpanel.h > 700:
                    self.MoveSourcePanel(1)
                if self.mainpanel.h < 700:
                    self.ResetPosition()
                    self.ResizeSourceBlock()
                if self.selectedCommand in self.plateitems[self.currentActivePlane]:
                    self.plateitems[self.currentActivePlane].remove(self.selectedCommand)
                for item in self.plateitems[self.currentActivePlane]:
                    if item is None:
                        self.plateitems[self.currentActivePlane].remove(item)

                del self.selectedCommand

                self.RearrangeCommands()
        self.selectedCommand = None

    def OnClick(self, event):
        if event.button in [Mouse.LMB, Mouse.RMB, Mouse.MMB]:
            if isinstance(self.clicked, Tab):
                id = self.clicked.GetId()
                self.currentActivePlane = id
                self.ResetPosition()
                self.RepaintTabs(id)
                self.ResizeSourceBlock()
            elif isinstance(self.clicked, Command):
                if event.button == Mouse.MMB or self.parent.button_down["a"] and event.button == Mouse.LMB:
                    self.CreateACommandCopy()
                    self.AddItemToCurrentPlane(self.selectedCommand)
                    if isinstance(self.selectedCommand, Loop):
                        self.AddItemToCurrentPlane(self.selectedCommand.loopend)
                    self.selectedCommand = None
                    self.RearrangeCommands()
                    self.ResizeSourceBlock()

                elif event.button == Mouse.RMB or self.parent.button_down["s"] and event.button == Mouse.LMB:
                    if isinstance(self.clicked, PenColor):
                        self.clicked.ChangeColor()
                    elif isinstance(self.clicked, PenWidth):
                        self.clicked.Extend()
                    elif isinstance(self.clicked, Loop):
                        self.clicked.ChangeCycleNumber()

                elif event.button == Mouse.LMB and self.parent.button_down["d"]:
                    if self.mainpanel.IsInside(event.pos):
                        self.selectedCommand = self.clicked
                        if isinstance(self.selectedCommand, Loop):
                            self.loopend = self.selectedCommand.loopend
                        self.plateitems[self.currentActivePlane].remove(self.selectedCommand)
                        if self.loopend:
                            self.plateitems[self.currentActivePlane].remove(self.loopend)
                        self.selectedCommand = None
                        self.loopend = None
                        self.RearrangeCommands()
                        self.ResizeSourceBlock()
                        while self.mainpanel.y + self.mainpanel.h < 700 and self.mainpanel.h > 700:
                            self.MoveSourcePanel(1)
                        if self.mainpanel.h < 700:
                            self.ResetPosition()
                            self.ResizeSourceBlock()

                elif event.button == Mouse.LMB:
                    if not self.mainpanel.IsInside(event.pos):
                        self.CreateACommandCopy()
                    else:
                        self.selectedCommand = self.clicked
                        if isinstance(self.selectedCommand, Loop):
                            self.loopend = self.selectedCommand.loopend

                    self.selectedCommand.setDelta(event.pos)



            elif isinstance(self.clicked, Button):
                self.clicked.OnClick()
            else:
                print "Clicked element: ", self.clicked
        elif event.button in [Mouse.SCROLLDOWN, Mouse.SCROLLUP]:
            if self.mainpanel.IsInside(event.pos):
                if self.mainpanel.h > 600:
                    if event.button == Mouse.SCROLLDOWN:
                        self.MoveSourcePanel(-1)
                    else:
                        self.MoveSourcePanel(1)


    def MoveSourcePanel(self, direction = 1,reset=True):
        if self.items[0].y >= 20 and direction > 0:
            return

        if self.mainpanel.y +  self.mainpanel.h <= 700 and direction < 0:
            return

        for item in self.items:
            if item is self.sidepanel:
                continue
            position_y = item.y + 20 * direction
            item.SetPosition(item.x, position_y)
            if isinstance(item, Tab):
                item.UpdatePoints()

        self.RearrangeCommands(needreset=reset)

    def ResetPosition(self):
        for item in self.items:
            if item is self.sidepanel:
                continue
            item.ResetPosition()
        self.RearrangeCommands()

    def SetCommandPosition(self):
        if not self.selectedCommand in self.plateitems[self.currentActivePlane]:
            self.selectedCommand.SetPosition(self.mainpanel.x + self.mainpanel.w / 2 - 25, self.mainpanel.y + 5 + len(self.plateitems[self.currentActivePlane]) * 55)
        else:
            self.selectedCommand.SetPosition(self.mainpanel.x + self.mainpanel.w / 2 - 25, self.mainpanel.y + 5 + self.plateitems[self.currentActivePlane].index(self.selectedCommand) * 55)

    def RearrangeCommands(self, ignore=None, needreset=True):
        if needreset:
            self.parent.NeedCompile()
            self.ResetCompileInfos()
            self.parent.reset = True
        for item in self.plateitems[self.currentActivePlane]:
            if item:
                if item is not ignore:
                    item.SetPosition(self.mainpanel.x + self.mainpanel.w / 2 - 25, self.mainpanel.y + 5 + self.plateitems[self.currentActivePlane].index(item) * 55)


        #Calculate inner loop count
        for item in self.plateitems[self.currentActivePlane]:
            if isinstance(item, Loop):
                item.ark_level = 0

        active_que = []
        for i in range(len(self.plateitems[self.currentActivePlane])):
            item = self.plateitems[self.currentActivePlane][i]
            if isinstance(item, Loop):
                start = self.plateitems[self.currentActivePlane].index(item)
                end = self.plateitems[self.currentActivePlane].index(item.loopend)
                if start < end:
                    active_que.append((start, end, item))
                else:
                    active_que.append((end, start, item))

        for item in active_que:
            for elem in active_que:
                if item == elem:
                    continue
                if item[0] < elem[0] and item[1] > elem[1]:
                    item[2].ark_level += 1


    def AddItemToCurrentPlane(self, item, plane=None):
        if plane:
            self.plateitems[plane].append(item)
        else:
            self.plateitems[self.currentActivePlane].append(item)


    def ResizeSourceBlock(self):
        self.mainpanel.h = max([len(self.plateitems[self.currentActivePlane]) * 55 + 5, self.base['height']])

    def InitBefore(self):
        for i in range(self.tabs):
            self.plateitems.append([])
        self.runpointer = RunPointer(0,0,40,40)

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

        command = logo.Forward(vec2_pos=Vector2(0, 0), size=(50, 50), mul=2)
        self.grid.append(command)

        command = logo.Backward(vec2_pos=Vector2(0, 0), size=(50, 50), mul=2)
        self.grid.append(command)

        command = logo.Left(vec2_pos=Vector2(0, 0), size=(50, 50))
        self.grid.append(command)

        command = logo.Right(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.Left(vec2_pos=Vector2(0, 0), size=(50, 50), mul=6)
        self.grid.append(command)

        command = logo.Right(vec2_pos=Vector2(0, 0), size=(50, 50), mul=6)
        self.grid.append(command)

        command = logo.Home(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.FloodFill(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.PenWidth(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.PenColor(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.PenDown(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.PenUp(vec2_pos=Vector2(0,0), size=(50, 50))
        self.grid.append(command)

        command = logo.ShowTurtle(vec2_pos=Vector2(0, 0), size=(50, 50))
        self.grid.append(command)

        command = logo.HideTurtle(vec2_pos=Vector2(0, 0), size=(50, 50))
        self.grid.append(command)

        '''
        command = logo.Reset(vec2_pos=Vector2(0, 0), size=(50, 50))
        self.grid.append(command)

        command = logo.Clear(vec2_pos=Vector2(0, 0), size=(50, 50))
        self.grid.append(command)
        '''

        command = logo.Loop(vec2_pos=Vector2(0, 0), size=(105, 50))
        self.grid.append(command)

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


    def Play(self, counter):
        i = self.plateitems[self.currentActivePlane][counter]
        self.MoveSourceToShowPointer(i)
        self.runpointer.SetPosition(i.x + 25 - 70, i.y + 25)
        if isinstance(i, Forward):
            self.parent.parent.logoCore.forward(distance=i.mul * 20)
        elif isinstance(i, Backward):
            self.parent.parent.logoCore.backward(distance=i.mul * 20)
        elif isinstance(i, Left):
            self.parent.parent.logoCore.left(angle=15*i.mul)
        elif isinstance(i, Right):
            self.parent.parent.logoCore.right(angle=15*i.mul)
        elif isinstance(i, PenDown):
            self.parent.parent.logoCore.pendown()
        elif isinstance(i, PenUp):
            self.parent.parent.logoCore.penup()
        elif isinstance(i, PenWidth):
            self.parent.parent.logoCore.width((i.pen_width+1)*2 + 1)
        elif isinstance(i, PenColor):
            self.parent.parent.logoCore.color(i.pen_color)
        elif isinstance(i, Home):
            self.parent.parent.logoCore.home()
        elif isinstance(i, FloodFill):
            self.parent.parent.logoCore.fill()
        elif isinstance(i, ShowTurtle):
            self.parent.parent.logoCore.showturtle()
        elif isinstance(i, HideTurtle):
            self.parent.parent.logoCore.hideturtle()
        elif isinstance(i, Reset):
            self.parent.parent.logoCore.reset()
        elif isinstance(i, Clear):
            self.parent.parent.logoCore.clear()
        elif isinstance(i, Loop):
            i.running = True
            if i.compile_information["pre_test"]:
                if i.remaining_cycle == 0:
                    counter = i.compile_information["loopend_index"]
                    i.ResetCycleCounter()
                else:
                    i.CountDown()
            else:
                if i.remaining_cycle == 0:
                    i.ResetCycleCounter()
                else:
                    counter = i.compile_information["loopend_index"]
                    i.CountDown()

        elif isinstance(i, LoopEnd):
            if  i.compile_information["pre_test"]:
                counter = i.compile_information["loopbase_index"] - 1

        counter += 1
        return counter

    def HasNext(self, counter):
        return counter < len(self.plateitems[self.currentActivePlane])

    def EnableSidepanel(self, state):
        self.sidepanel_active = state

    def FindLoopBase(self, loopend):
        for elem in self.plateitems[self.currentActivePlane]:
            if isinstance(elem, Loop):
                if elem.loopend == loopend:
                    return elem

    def FindLoopEnd(self, loopbase):
        for elem in self.plateitems[self.currentActivePlane]:
            if isinstance(elem, LoopEnd):
                if loopbase.loopend == elem:
                    return elem

    def CompileLoops(self):
        for elem in self.plateitems[self.currentActivePlane]:
            if isinstance(elem, Loop):
                if not elem.compile_information["compiled"]:
                    loopend = self.FindLoopEnd(elem)
                    loopend_index = self.plateitems[self.currentActivePlane].index(loopend)
                    loopstart_index = self.plateitems[self.currentActivePlane].index(elem)
                    pre_test = loopend_index > loopstart_index
                    elem.SetCompileInfo(pre_test=pre_test, loopend_index=loopend_index)
                    loopend.SetCompileInfo(pre_test, loopstart_index)
            if isinstance(elem, LoopEnd):
                if not elem.compile_information["compiled"]:
                    loop_base = self.FindLoopBase(elem)
                    loopstart_index = self.plateitems[self.currentActivePlane].index(loop_base)
                    loopend_index = self.plateitems[self.currentActivePlane].index(elem)
                    pre_test = loopend_index > loopstart_index
                    elem.SetCompileInfo(pre_test, loopstart_index)
                    loop_base.SetCompileInfo(pre_test, loopend_index)


    def ResetCompileInfos(self):
        for elem in self.plateitems[self.currentActivePlane]:
            if isinstance(elem, Loop) or isinstance(elem, LoopEnd):
                elem.ResetCompileInfo()

    def StopRunning(self):
        for elem in self.plateitems[self.currentActivePlane]:
            if isinstance(elem, Loop):
                elem.running = False
                elem.ResetCycleCounter()
            elif isinstance(elem, LoopEnd):
                elem.running = False


    def DrawRunPointer(self, screen):
        self.runpointer.DrawObject(screen)

    def MoveSourceToShowPointer(self, i):
        flag = False
        t = False
        while i.y + i.h > 700 and not t:
            flag = True
            self.MoveSourcePanel(-1, False)
        t = flag
        while i.y < 20 and not t:
            self.MoveSourcePanel(1, False)

    def ClearCurrentSource(self):
        self.plateitems[self.currentActivePlane] = []
        self.ResetPosition()
        self.ResizeSourceBlock()

    def CreateACommandCopy(self):
        self.clicked.UnloadIcon()
        self.selectedCommand = copy.deepcopy(self.clicked)
        self.clicked.LoadSprite()
        # DeepCopy Eseten muszaj ujra betolteni a kepet!!!
        self.selectedCommand.LoadSprite()
        if isinstance(self.selectedCommand, Loop):
            self.selectedCommand.RollColor()
            self.loopend = LoopEnd(vec2_pos=Vector2(self.selectedCommand.x, self.selectedCommand.y + 55),
                                   size=(50, 50))
            self.loopend.SetLoopStart(self.selectedCommand)
            self.selectedCommand.SetLoopend(self.loopend)


    def SetCurrentActiveCommandList(self, list):
        self.plateitems[self.currentActivePlane] = list

    def GetCurrentActiveCommandList(self):
        return self.plateitems[self.currentActivePlane]

    def GetCommandLists(self):
        return self.plateitems

    def SetCommandLists(self, list_of_lists):
        self.plateitems = list_of_lists