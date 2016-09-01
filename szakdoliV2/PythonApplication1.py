import pygame
import Color

class Rect:
    def __init__(self,x,y,h,w, name):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.name = name
        self.delta = 0,0
    
    def jobb(self):
        self.x += 1

    def bal(self):
        self.x -= 1

    def fel(self):
        self.y += 1

    def le(self):
        self.y -= 1

    def drawRect(self, screen):
        pygame.draw.rect(screen, Color.black, (self.x, self.y, self.h, self.w))

    def print_name(self):
        print self.name + " Clicked"

    def isInside(self, position):
        return self.x <= position[0] and self.x + self.h >= position[0] and self.y <= position[1] and self.y + self.w >= position[1], self.name

    def deltapos(self, position):
        return position[0]-self.x, position[1] - self.y

    def drag(self, mouseposition):
        self.x = mouseposition[0] - self.delta[0]
        self.y = mouseposition[1] - self.delta[1]

    def setDelta(self, mouseposition):
        self.delta = self.deltapos(mouseposition)

rect1 = Rect(5,5,90,20, "ALak1")
rect2 = Rect(100,100,100,100, "ALMA")

rects = []
rects.append(rect1)
rects.append(rect2)


screen = pygame.display.set_mode((500,500))
screen.fill(Color.white)


pygame.display.init()
pygame.display.update()
clock = pygame.time.Clock()
touching = False
currentRect = None

gameExit = False
while not gameExit:
    pygame.display.update()
    screen.fill(Color.white)
    for r in rects:
        r.drawRect(screen)
    #rect1.drawRect(screen)
    #rect.jobb()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            touching = True
            for rect in rects:
                insite, name = rect.isInside(event.pos)
                if insite:
                    print 'There is my boi boo ', name
                    print 'Delta pos' , rect.deltapos(event.pos)
                    currentRect = rect
                    currentRect.setDelta(event.pos)
                else:
                    print 'njet komrad'
            print event.pos
        if event.type == pygame.MOUSEMOTION:
            if touching and currentRect:
                #print 'DAGGING'
                currentRect.drag(event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            touching = False
            currentRect = None

            print 'released'
    clock.tick(60)
        

pygame.quit()