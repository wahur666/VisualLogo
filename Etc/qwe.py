import pygame, sys
from pygame.locals import *

pygame.init()

# Create the window, assigning it to variable 'surface'.
surface = pygame.display.set_mode((350, 250), pygame.RESIZABLE)

pygame.display.set_caption("Resizing test")

while True:
    surface.fill((255,255,255))

    # Draw a red rectangle that resizes with the window as a test.
    pygame.draw.rect(surface, (200,0,0), (100,100,100,100))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == VIDEORESIZE:
            # The main code that resizes the window:
            # (recreate the window with the new size)
            surface = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)