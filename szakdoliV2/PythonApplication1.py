# -*- coding: utf-8 -*-

import pygame

from Drawable import *
from System.Constants import COLOR as Color

SCREEN_WIDHT = 1100
SCREEN_HEIGHT = 720

gui = GUI()

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
screen.fill(Color.WHITE)

pygame.display.init()
pygame.display.update()
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
            gameExit = True

        if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]:
            gui.MainEventHandler(event)
        '''if event.type == pygame.MOUSEBUTTONDOWN:

        gui.OnClick()
        if event.button == 1:
            touching = True
            for rect in rects:
                insite = rect.isInside(event.pos)
                if insite and rect.isMovable():
                    #print 'There is my boi boo ', name
                    #print 'Delta pos' , rect.deltapos(event.pos)
                    currentRect = rect
                    currentRect.setDelta(event.pos)
                else:
                    pass
                    #print 'njet komrad'
            #print event.pos

        if event.type == pygame.MOUSEMOTION:
            pass
            #if touching and currentRect:
            #    #print 'DAGGING'
            #    currentRect.drag(event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            pass
            #if event.button == 1:
            #    touching = False
            #    currentRect = None
            #    #print "Released"
        '''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                gameExit = True
            if event.key == pygame.K_KP_PLUS:
                pass
    clock.tick(60)

pygame.quit()
