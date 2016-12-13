# -*- coding: utf-8 -*-

from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
import pygame
import time

from Button import Button
from Drawable.Rectangle import Rect
from Drawable.ScrollingPlane import ScrollingPlane
from System.Constants import COLOR as Color, MOUSE, FONT_AWESOME as FA
from System.Timer import Timer
from Drawable.DrawingIcon import DrawingIcon
from System.SupportFunctions import SerializeCommands, LoadSerializedCommands, CreateZip
from DataManagementScreen import DataManagementScreen

from Tab import Tab
import os.path, os


class GUI:

    def __init__(self, parent):
        self.parent = parent
        self.items = []
        self.settings_buttons = []
        self.show_settings = False
        self.initilize()

    def DrawGUI(self, screen):
        self.timer.tick()
        for item in self.items:
            item.DrawObject(screen)

        if self.show_settings:
            for item in self.settings_buttons:
                item.DrawObject(screen)

        if self.running:
            self.RunCode(self.skip_wait)

        if self.show_run_pointer:
            self.scrollplane.DrawRunPointer(screen)

        pos, rot, show = self.parent.logoCore.GetTurtleInformationToRender()
        for line in self.parent.logoCore.GetLinesForRenderer():
            line.DrawObject(screen)
        if show:
            self.drawing_arrow.SetPosition(pos[0], pos[1])
            self.drawing_arrow.DrawObject(screen, rot)

        if self.show_data_management_panel:
            self.DataManagmentWindow.DrawObject(screen)

        if self.wait_next_draw:
            self.CreateDataScreenshot()
            self.data_index = None
            self.wait_next_draw = False
            self.disable_input = False


    def initilize(self):
        self.drawingWindow = Rect(20, 20, 630, 600, Color.BLACK, 1, transparent=False)
        self.Add(self.drawingWindow)

        buttonPlay = Button(380,640,60,60, keycode=FA.PLAY, padding=5)
        buttonPlay.bind(self.OnClickPlay)
        buttonPlay.SetAccentColor(Color.HATTER_1)
        self.Add(buttonPlay)

        buttonStepOver = Button(450, 640, 60, 60, keycode=FA.STEPOVER, padding=10)
        buttonStepOver.bind(self.OnClickStepOver)
        buttonStepOver.SetAccentColor(Color.HATTER_4)
        self.Add(buttonStepOver)

        buttonStop = Button(520, 640, 60, 60, keycode=FA.STOP, padding=4)
        buttonStop.bind(self.OnClickStop)
        buttonStop.SetAccentColor(Color.HATTER_7)
        self.Add(buttonStop)

        buttonReset = Button(590, 640, 60, 60, keycode=FA.RESET, padding=4)
        buttonReset.bind(self.OnClickReset)
        buttonReset.SetAccentColor(Color.HATTER_8)
        self.Add(buttonReset)

        buttonSettings = Button(65, 660, 40, 40, keycode=FA.SETTINGS, padding=-1)
        buttonSettings.bind(self.OnClickSettings)
        self.Add(buttonSettings)

        buttonLoad = Button(110, 660, 40, 40, keycode=FA.LOAD)
        buttonLoad.bind(self.OnClickLoad)
        self.AddToSettings(buttonLoad)

        buttonSave = Button( 155, 660, 40, 40, keycode=FA.SAVE, padding=2)
        buttonSave.bind(self.OnClickSave)
        self.AddToSettings(buttonSave)

        buttonScreenshot = Button(200, 660, 40, 40, keycode=FA.CAMERA)
        buttonScreenshot.bind(self.OnClickScreenshot)
        self.AddToSettings(buttonScreenshot)

        buttonBackground = Button(20, 660, 40,40, keycode=FA.BACKGROUND_PICTURE, padding=-1)
        buttonBackground.bind(self.OnClickBackground)
        self.Add(buttonBackground)

        self.DataManagmentWindow = DataManagementScreen(100,100, 900, 550, parent=self)

        self.scrollplane = ScrollingPlane(820, 20, 263, 600, 3, parent=self)
        self.Add(self.scrollplane)

        self.mouseDown = False
        self.timer = Timer()
        self.running = False
        self.reset = True
        self.compile_needed = True
        self.global_counter = 0
        self.drawing_arrow = DrawingIcon(0, 0, 30, 30, color=Color.RED, width=0)
        self.show_run_pointer = False
        self.step_over_mode = False
        self.show_data_management_panel = False
        self.skip_wait = False
        self.data_index = None
        self.wait_next_draw = False
        self.disable_input = False
        self.button_down = {
            "a" : False,
            "s" : False,
            "d" : False
        }


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

        if not self.disable_input:
            if not self.show_data_management_panel:

                if self.show_settings:
                    for item in self.settings_buttons:
                        if item.IsInside(event.pos):
                            item.OnClick(event)


                for item in self.items:
                    if item.IsInside(event.pos):
                        if isinstance(item, Rect):
                            return
                        elif isinstance(item, Button):
                            item.OnClick(event)
                            return
                        elif isinstance(item, Tab):
                            return
                        elif isinstance(item, ScrollingPlane):
                            if self.running:
                                return
                            item.OnClick(event)
                            return
                        else:
                            print "Undefine click", type(item)
                            return
            else:
                if self.DataManagmentWindow.IsInside(event.pos):
                    self.DataManagmentWindow.OnClick(event)
        else:
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
        if not self.running:
            if event.button == MOUSE.LMB:
                if self.button_down["s"]:
                    self.skip_wait = True
                self.StartRunningCode()
            elif event.button == MOUSE.RMB:
                self.skip_wait = True
                self.StartRunningCode()

    def OnClickStop(self, event):
        self.running = False
        self.show_run_pointer = False
        self.step_over_mode = False
        self.skip_wait = False
        self.scrollplane.EnableSidepanel(True)
        self.scrollplane.StopRunning()
        print "Stop"

    def OnClickStepOver(self, event):
        if not self.running and not self.step_over_mode:
            self.global_counter = 0
            self.OnClickPlay(event)
            self.scrollplane.EnableSidepanel(False)
        if self.show_run_pointer:
            self.running = False
            self.skip_wait = False
            self.StepOver()

    def OnClickSettings(self, event):
        if event.button == MOUSE.RMB or event.button == MOUSE.LMB and self.button_down["s"]:
            self.show_settings = not self.show_settings

    def OnClickLoad(self, event):
        self.show_data_management_panel = True
        self.DataManagmentWindow.SetMode("Load")

    def OnClickSave(self, event):
        self.OnClickStop(event)
        self.show_data_management_panel = True
        self.DataManagmentWindow.SetMode("Save")

    def OnClickScreenshot(self, event):
        rect = pygame.Rect(self.drawingWindow.GetParameters())
        sub = self.parent.screen.subsurface(rect)
        pygame.image.save(sub, os.path.join( "Screenshots", "screenshot" + time.strftime("_%Y_%m_%d_%H_%M_%S") + ".jpg"))

    def OnClickBackground(self, event):
        self.parent.ChangeBackgroundColor()

    def OnClickReset(self, event):
        self.OnClickStop(event)
        self.parent.logoCore.reset()

    def RunCode(self, skip_wait=False):
        if self.reset:
            self.global_counter = 0
            self.reset =  False
            self.timer.wait(.5)
            self.scrollplane.runpointer.SetPosition(-50, -50)

        if self.scrollplane.HasNext(self.global_counter):
            self.scrollplane.EnableSidepanel(False)
            if self.timer.is_waiting():
                return
            self.global_counter = self.scrollplane.Play(self.global_counter)
            if not skip_wait:
                self.timer.wait(.5)
        else:
            if self.timer.is_waiting():
                return
            self.running = False
            self.scrollplane.EnableSidepanel(True)
            self.scrollplane.StopRunning()
            self.show_run_pointer = False
            self.skip_wait = False
            if skip_wait:
                self.wait_next_draw = True



    def StepOver(self):
        self.step_over_mode = True
        if self.scrollplane.HasNext(self.global_counter):
            self.global_counter = self.scrollplane.Play(self.global_counter)
        else:
            self.scrollplane.EnableSidepanel(True)
            self.show_run_pointer = False
            self.step_over_mode = False

    def Compile(self):
        self.scrollplane.CompileLoops()
        print "Compiled"

    def NeedCompile(self):
        self.compile_needed = True

    def CloseDataManagementWindow(self):
        self.show_data_management_panel = False

    def LoadData(self, index):
        commands = LoadSerializedCommands(index)
        if commands:
            self.scrollplane.SetCurrentActiveCommandList(commands)
            self.scrollplane.ResetPosition()
            self.scrollplane.RearrangeCommands()
            self.scrollplane.ResizeSourceBlock()


    def SaveData(self, index):
        active_list = self.scrollplane.GetCurrentActiveCommandList()
        SerializeCommands(active_list, index)
        self.StartRunningCode()
        self.skip_wait = True
        self.data_index = index
        self.disable_input = True

    def CreateDataScreenshot(self):
        if self.data_index is not None:
            rect = pygame.Rect(self.drawingWindow.GetParameters())
            sub = self.parent.screen.subsurface(rect)
            pygame.image.save(sub, os.path.join("UserData", "data" + str(self.data_index) + ".jpg"))
            CreateZip(self.data_index)

    def StartRunningCode(self):
        if self.step_over_mode:
            self.step_over_mode = False
            self.running = True
            return
        self.parent.logoCore.reset()
        self.reset = True
        self.running = True
        self.show_run_pointer = True
        if self.compile_needed:
            self.Compile()
            self.compile_needed = False

