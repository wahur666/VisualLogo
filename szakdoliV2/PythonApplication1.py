# -*- coding: utf-8 -*-

import pygame
if not pygame.font: print 'Warning, fonts disabled'

from Drawable import *
from System.Constants import COLOR as Color

def Exit():
    global gameExit
    gameExit = True

SCREEN_WIDHT = 1100
SCREEN_HEIGHT = 720

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
screen.fill(Color.WHITE)

pygame.display.init()

pygame.display.update()

gui = GUI(Exit)

clock = pygame.time.Clock()
touching = False
currentRect = None

gameExit = False
while not gameExit:
    pygame.display.update()
    screen.fill(Color.LIGHTGRAY)

    gui.DrawGUI(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit()

        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]:
            gui.MainEventHandler(event)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                Exit()
            if event.key == pygame.K_KP_PLUS:
                pass
    clock.tick(60)

pygame.quit()
