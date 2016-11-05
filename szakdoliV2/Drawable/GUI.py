# -*- coding: utf-8 -*-

from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
import pygame

from Button import Button
from Drawable.Rectangle import Rect
from Drawable.ScrollingPlane import ScrollingPlane
from System.Constants import COLOR as Color, MOUSE
from System.Timer import Timer
from Drawable.DrawingIcon import DrawingIcon

from Tab import Tab
import os.path, os

global_counter = 0


class GUI:

    def __init__(self, parent):
        self.parent = parent
        self.items = []
        self.settings_buttons = []
        self.show_settings = True
        self.initilize()

    def __del__(self):
        print "GUI destruktor lefutott"

    def DrawGUI(self, screen):
        self.timer.tick()
        for item in self.items:
            item.DrawObject(screen)

        if self.show_settings:
            for item in self.settings_buttons:
                item.DrawObject(screen)

        if self.running:
            self.RunCode()

        pos, rot, show = self.parent.logoCore.GetTurtleInformationToRender()
        if show:
            self.drawing_arrow.SetPosition(pos[0], pos[1])
            self.drawing_arrow.DrawObject(screen, rot)
            #self.turtle_image.SetPosition(pos[0], pos[1])
            #self.turtle_image.DrawObject(screen, rot)
        for line in self.parent.logoCore.GetLinesForRenderer():
            line.DrawLine(screen)


    def initilize(self):
        self.drawingWindow = Rect(20, 20, 630, 600, "Drawingwindow", Color.BLACK, 1, transparent=False)
        self.Add(self.drawingWindow)

        buttonPlay = Button(450,640,60,60, keycode=u"\uF04B", padding=5)
        buttonPlay.bind(self.OnClickPlay)
        self.Add(buttonPlay)

        buttonStepOver = Button(520, 640, 60, 60, keycode=u"\uF051", padding=10)
        buttonStepOver.bind(self.OnClickStepOver)
        self.Add(buttonStepOver)

        buttonStop = Button(590, 640, 60, 60, keycode=u"\uF04D", padding=4)
        buttonStop.bind(self.OnClickStop)
        self.Add(buttonStop)

        buttonSettings = Button(20, 660, 40, 40, keycode=u"\uF085", padding=-1)
        buttonSettings.bind(self.OnClickSettings)
        self.Add(buttonSettings)

        buttonLoad = Button(67, 660, 40, 40, keycode=u"\uF115")
        buttonLoad.bind(self.OnClickLoad)
        self.AddToSettings(buttonLoad)

        buttonSave = Button( 110, 660, 40, 40, keycode=u"\uF0C7", padding=2)
        buttonSave.bind(self.OnClickSave)
        self.AddToSettings(buttonSave)

        buttonScreenshot = Button(154, 660, 40, 40, keycode=u"\uF083")
        buttonScreenshot.bind(self.OnClickScreenshot)
        self.AddToSettings(buttonScreenshot)

        buttonExit = Button(197, 660, 40,40, keycode=u"\uF011", padding=2)
        buttonExit.bind(self.OnClickExit)
        self.AddToSettings(buttonExit)

        #poli = Polygon([[50, 75], [65, 60], [135, 60], [150,75], [150,100], [50,100]])
        #self.Add(poli)


        #tab = Tab(100,100,100,50,width=1)
        #self.Add(tab)

        self.scrollplane = ScrollingPlane(820, 20, 263, 600, 3, parent=self)
        self.Add(self.scrollplane)

        self.mouseDown = False
        self.timer = Timer()
        self.running = False
        self.reset = True
        self.compile_needed = True

        self.drawing_arrow = DrawingIcon(0, 0, 30, 30, color=Color.RED, width=1)
        #self.turtle_image = Spirte(x=0,y=0, w=50, h=50, imgpath=img.TURTLE)
        #self.parent.logoCore.SetDistorsion(25)

    def MainEventHandler(self, event):
        if event.type == MOUSEMOTION:
            if self.mouseDown:
                self.OnDrag(event)
        elif event.type == MOUSEBUTTONUP:
            self.OnRelease(event)
        elif event.type == MOUSEBUTTONDOWN:
            self.OnClick(event)
        else:
            from webbrowser import open as webopen
            webopen("https://reposti.com/i/m/bMm.jpg", new=2)

    def OnClick(self, event):
        self.mouseDown = True

        if self.show_settings:
            for item in self.settings_buttons:
                if item.IsInside(event.pos):
                    item.OnClick(event)


        for item in self.items:
            if item.IsInside(event.pos):
                if isinstance(item, Rect):
                    return
                    pass
                elif isinstance(item, Button):
                    item.OnClick(event)
                    return
                elif isinstance(item, Tab):
                    print "Tab"
                    return
                elif isinstance(item, ScrollingPlane):
                    print "Scrolling"
                    item.OnClick(event)
                    return
                else:
                    print "Undefine click", type(item)
                    return


    def OnRelease(self, event):
        self.mouseDown = False
        for item in self.items:
            if isinstance(item, ScrollingPlane):
                item.OnRelease(event)

    def OnDrag(self, event):
        for item in self.items:
            if isinstance(item, ScrollingPlane):
                item.OnDrag(event)

    def Add(self, item):
        self.items.append(item)

    def AddToSettings(self, item):
        self.settings_buttons.append(item)

    # ------ Event handlerek -------

    def OnClickPlay(self, event):
        if event.button == MOUSE.LMB:
            self.parent.logoCore.reset()
            self.reset = True
            self.running = True
            if self.compile_needed:
                self.Compile()
                self.compile_needed = False
        else:
            print "Valami", event.button

    def OnClickStop(self, event):
        global global_counter
        self.running = False
        self.scrollplane.EnableSidepanel(True)
        print "Stop"

    def OnClickStepOver(self, event):
        if not self.reset:
            self.running = False
            self.StepOver()

    def OnClickSettings(self, event):
        self.show_settings = not self.show_settings

    def OnClickLoad(self, event):
        print "Load"

    def OnClickSave(self, event):
        print "Save"

    def OnClickScreenshot(self, event):
        rect = pygame.Rect(self.drawingWindow.GetParameters())
        sub = self.parent.screen.subsurface(rect)
        pygame.image.save(sub, os.path.join("..", "Etc", "screenshot.jpg"))

    def OnClickExit(self, event):
        self.parent.Exit()

    def RunCode(self):
        global global_counter
        if self.reset:
            global_counter = 0
            self.reset =  False

        if self.scrollplane.HasNext(global_counter):
            self.scrollplane.EnableSidepanel(False)
            if self.timer.is_waiting():
                return
            global_counter = self.scrollplane.Play(global_counter)
            print global_counter
            self.timer.wait(.5)
        else:
            self.running = False
            self.scrollplane.EnableSidepanel(True)

    def StepOver(self):
        global global_counter
        if self.scrollplane.HasNext(global_counter):
            global_counter = self.scrollplane.Play(global_counter)
        else:
            self.scrollplane.EnableSidepanel(True)

    def Compile(self):
        self.scrollplane.CompileLoops()
        print "Compiled"

    def NeedCompile(self):
        self.compile_needed = True
