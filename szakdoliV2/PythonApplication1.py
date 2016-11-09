# -*- coding: utf-8 -*-

import pygame
if not pygame.font: print 'Warning, fonts disabled'

from Drawable import *
from System.Constants import COLOR as Color
from Drawable.LogoModule.Turtle import Turtle

class ApplicationCore:

    def __init__(self):
        self.SCREEN_WIDHT = 1100
        self.SCREEN_HEIGHT = 720

        pygame.init()

        self.screen = pygame.display.set_mode((self.SCREEN_WIDHT, self.SCREEN_HEIGHT))
        self.screen.fill(Color.WHITE)

        pygame.display.init()
        pygame.display.update()

        self.logoCore = Turtle()
        self.logoCore.SetBoundaries((20, 20), (650, 620))

        self.gui = GUI(self)

        self.clock = pygame.time.Clock()
        self.currentRect = None

        self.gameExit = False

    def Exit(self):
        self.gameExit = True

    def Run(self):
        while not self.gameExit:
            pygame.display.update()
            self.screen.fill(Color.LIGHTGRAY)

            self.gui.DrawGUI(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Exit()

                if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]:
                    self.gui.MainEventHandler(event)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.Exit()
                    if event.key == pygame.K_KP_PLUS:
                        pass
            self.clock.tick(60)

        pygame.quit()

    def debug(self):
        self.logoCore.debug()
        self.logoCore.forward()
        self.logoCore.forward()
        self.logoCore.debug()

core = ApplicationCore()
core.Run()