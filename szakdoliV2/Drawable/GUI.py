# -*- coding: utf-8 -*-

from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION

from Button import Button
from Drawable.Rectangle import Rect
from Drawable.ScrollingPlane import ScrollingPlane
from System.Constants import COLOR as Color, MOUSE
from Tab import Tab

class GUI:

    def __init__(self, exit_func_pointer):
        self.exit_func = exit_func_pointer
        self.items = []
        self.settings_buttons = []
        self.show_settings = False
        self.initilize()

    def DrawGUI(self, screen):
        for item in self.items:
            item.DrawObject(screen)

        if self.show_settings:
            for item in self.settings_buttons:
                item.DrawObject(screen)

    def initilize(self):
        drawingWindow = Rect(20, 20, 630, 600, "Drawingwindow", Color.BLACK, 1, transparent=False)
        self.Add(drawingWindow)

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

        scrollplane = ScrollingPlane(820, 20, 263, 600, 3)
        self.Add(scrollplane)

        self.mouseDown = False

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
            print "Play"
        else:
            print "Valami", event.button

    def OnClickStop(self, event):
        print "Stop"

    def OnClickStepOver(self, event):
        print "StepOver"

    def OnClickSettings(self, event):
        self.show_settings = not self.show_settings

    def OnClickLoad(self, event):
        print "Load"

    def OnClickSave(self, event):
        print "Save"

    def OnClickScreenshot(self, event):
        print "Screenshot"

    def OnClickExit(self, event):
        self.exit_func()