# -*- coding: utf-8 -*-

from Polygon import Polygon
from System.Constants import COLOR as Color


#TODO: Tényleg újragondolni az egészet, és az AbstractDrawable osztályból származtatni
class Tab(Polygon):

    def __init__(self, x, y, w, h, color = Color.BLACK , id = None, width = 0, descriptor = "", size = None, vec2_pos = None, transparent=True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.id = id
        self.color = color
        self.darkAccent = Color.GREY
        self.lightAccent = (200, 200, 200)    #implicit szinmegadás, már már a magic number határát karistolja
        self.accentColor = None
        self.width = width
        self.descriptor = descriptor
        self.transparent = transparent
        self.selected = False
        self.coordinates = self.CalculatePoints()

    def IsInside(self, position):
        return self.x <= position[0] and self.x + self.w >= position[0] and self.y <= position[1] and self.y + self.h >= position[1]

    def DrawObject(self, screen):
        #pygame.draw.rect(screen, Color.RED, (self.x, self.y, self.w, self.h))
        if not self.transparent:
            if self.selected:
                self.accentColor = self.darkAccent
            else:
                self.accentColor = self.lightAccent
        super(Tab, self).DrawObject(screen)

    def GetId(self):
        return self.id

    def CalculatePoints(self):
        points = []
        percentofcut = 0.2
        '''
        óra mutatóval megegyezően helyezzük fel a pontokat
        a magasság 20%-a lesz a legvágott rész

            *(p2)--------*(p3)      /\              *(tl) ------------ * (tr)       tl = self.x, self.y
          /                \         | percentofcut |                  |            tr = self.x + self.w, self.y
        *(p1)               *(p4)   \/              |                  |            bl = self.x, self.y + self.h
        |                   |                       |                  |            br = self.x + self.w, self.y + self.h
        |                   |                       |                  |
        |                   |                       |                  |
        *(p6) --------------*(p5)                   *(bl) ------------ * (br)
        '''

        # TODO lehetne 4 részből összerakni, 2 téglalap és 2 ARC

        tl = self.x, self.y
        tr = self.x + self.w, self.y
        bl = self.x, self.y + self.h
        br = self.x + self.w, self.y + self.h
        edgecut = int(self.h * percentofcut)

        #fontos hogy int legyen mert csak egész pontokat lehet megjeleníteni
        #      Coords:  X      Y
        points.append((tl[0] , tl[1] + edgecut )) #p1
        points.append((tl[0] + edgecut, tl[1]))  # p2
        points.append((tr[0] - edgecut, tr[1]  ))  # p3
        points.append((tr[0] , tr[1] + edgecut ))  # p4
        points.append( br )  # p5
        points.append( bl )  # p6

        return points