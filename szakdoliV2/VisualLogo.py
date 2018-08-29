# -*- coding: utf-8 -*-

import os, os.path
import shutil
import pygame
if not pygame.font: print 'Warning, fonts disabled'

from Drawable import *
from System.Constants import COLOR as Color, IMAGE_PATHS as img
from Drawable.LogoModule.Turtle import Turtle
from System.SupportFunctions import CreateZip

class ApplicationCore:

    def __init__(self):
        self.SCREEN_WIDHT = 1100
        self.SCREEN_HEIGHT = 720

        self.CreateUserData()

        pygame.init()


        self.background_color = Color.LIGHTGRAY
        self.background_color_index = 7

        self.screen = pygame.display.set_mode((self.SCREEN_WIDHT, self.SCREEN_HEIGHT))
        self.screen.fill(self.background_color)

        pygame.display.init()
        pygame.display.update()

        icon = pygame.image.load(os.getcwd() + img.ICON)
        pygame.display.set_caption("Visual Logo 1.2.3")
        pygame.display.set_icon(icon)

        self.logoCore = Turtle()
        self.logoCore.SetBoundaries((20, 20), (650, 620))

        self.gui = GUI(self)

        self.clock = pygame.time.Clock()

        self.gameExit = False

    def Exit(self):
        self.gameExit = True

    def Run(self):
        while not self.gameExit:
            pygame.display.update()
            self.screen.fill(self.background_color)

            self.gui.DrawGUI(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Exit()

                if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]:
                    self.gui.MainEventHandler(event)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.Exit()
                    if event.key == pygame.K_a:
                        self.gui.button_down["a"] = False
                    if event.key == pygame.K_s:
                        self.gui.button_down["s"] = False
                    if event.key == pygame.K_d:
                        self.gui.button_down["d"] = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.gui.scrollplane.MoveSourcePanel(1)
                    if event.key == pygame.K_DOWN:
                        self.gui.scrollplane.MoveSourcePanel(-1)
                    if event.key == pygame.K_a:
                        self.gui.button_down["a"] = True
                        self.gui.button_down["s"] = False
                        self.gui.button_down["d"] = False
                    if event.key == pygame.K_s:
                        self.gui.button_down["a"] = False
                        self.gui.button_down["s"] = True
                        self.gui.button_down["d"] = False
                    if event.key == pygame.K_d:
                        self.gui.button_down["a"] = False
                        self.gui.button_down["s"] = False
                        self.gui.button_down["d"] = True

            self.clock.tick(60)

        pygame.quit()

    def debug(self):
        self.logoCore.debug()
        self.logoCore.forward()
        self.logoCore.forward()
        self.logoCore.debug()


    def ChangeBackgroundColor(self):
        self.background_color_index = (self.background_color_index + 1) % len(Color.COLOR_LIST)
        self.background_color = Color.COLOR_LIST[self.background_color_index]


    def CreateUserData(self):
        files = []
        if not os.path.exists("UserData"):
            os.makedirs("UserData")
        for (dirpath, dirnames, filenames) in os.walk("UserData"):
            files.extend(filenames)
        for i in range(21):
            if "data" + str(i) + ".zip" not in filenames:
                shutil.copyfile(os.getcwd() + os.path.join(os.sep, "Resources", "data.jpg"),
                                    os.getcwd() + os.path.join(os.sep, "UserData", "data" + str(i) + ".jpg"))
                open(os.getcwd() + os.path.join(os.sep, "UserData", "data" + str(i) + ".dat"), "w")

                CreateZip(i)

core = ApplicationCore()
core.Run()