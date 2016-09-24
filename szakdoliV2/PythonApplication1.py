import pygame

from Util.ConfigiParser import parse_config
from Util.Constants import COLOR as Color
from Drawable import *



Configuration = parse_config()



#rect1 = Rect(5,5,90,20, "ALak1")
#rect2 = Rect(100, 100, 100, 100, "ALMA", Color.RED, 1)


rects = []
#rects.append(rect1)
#rects.append(rect2)

gui = GUI()

screen = pygame.display.set_mode((int(Configuration['Display']['width']),int(Configuration['Display']['height'])))
screen.fill(Color.WHITE)


pygame.display.init()
pygame.display.update()
clock = pygame.time.Clock()
touching = False
currentRect = None

gameExit = False
while not gameExit:
    pygame.display.update()
    screen.fill(Color.WHITE)
    for r in rects:
        r.drawRect(screen)

    gui.DrawGUI(screen)

    #rect1.drawRect(screen)
    #rect.jobb()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            gui.OnClick(event.button, event.pos)
            if event.button == 1:
                touching = True
                for rect in rects:
                    insite, name = rect.isInside(event.pos)
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
            if touching and currentRect:
                #print 'DAGGING'
                currentRect.drag(event.pos)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                touching = False
                currentRect = None
                #print "Released"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                gameExit = True
            if event.key == pygame.K_KP_PLUS :
                rects[0].w += 10
                rects[0].y -= 5
                #print "Itt kellene tortenni valaminek"
    clock.tick(60)
        

pygame.quit()