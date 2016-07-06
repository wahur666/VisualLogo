import pygame
import Color

class Rect:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.h = 0
        self.w = 0
    
    def jobb(self):
        self.x += 1

    def bal(self):
        self.x -= 1

rect = Rect()

rect.x = 5
rect.y = 6
rect.h = 7
rect.w = 8

def drawRect(screen):
    global rect
    pygame.draw.rect(screen, Color.black, (rect.x, rect.y, rect.h, rect.w))

screen = pygame.display.set_mode((500,500))
screen.fill(Color.white)


pygame.display.init()
pygame.display.update()
clock = pygame.time.Clock()


gameExit = False
while not gameExit:
    pygame.display.update()
    screen.fill(Color.white)
    drawRect(screen)
    rect.jobb()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print event.pos
    clock.tick(60)
        

pygame.quit()