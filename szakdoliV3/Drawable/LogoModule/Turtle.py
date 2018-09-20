# -*- coding: utf-8 -*-

from math import sin, cos, radians

from Drawable.RenderItems import Line, Flood
from System.Constants import COLOR as Color


class Turtle:

    def __init__(self):
        self.pos_x , self.pos_y = (315, 300)
        self.base = {
            "x" : self.pos_x,
            "y" : self.pos_y
        }
        self.rotation = 0
        self.show_turtle = True
        self.pen_color = Color.BLACK
        self.pen_down = True
        self.pen_witdh = 1
        self.distorsion = 0

        self.lines = [] # <instance Class : Line >

        self.boundaries = {
            "top" : None,
            "bot" : None
        }


    def forward(self, distance = 20):
        start_x, start_y = self.pos_x, self.pos_y
        self.pos_x, self.pos_y = self.move(1, distance)
        self.NormalizeMovement()
        end_x, end_y = self.pos_x, self.pos_y
        line_o = Line((start_x + self.distorsion, start_y + self.distorsion), (end_x + self.distorsion, end_y + self.distorsion),
                      self.pen_color, self.pen_witdh, self.pen_down)
        self.lines.append(line_o)

    def backward(self, distance = 20):
        start_x, start_y = self.pos_x, self.pos_y
        self.pos_x, self.pos_y = self.move(-1, distance)
        self.NormalizeMovement()
        end_x, end_y = self.pos_x, self.pos_y
        line_o = Line((start_x, start_y), (end_x, end_y), self.pen_color, self.pen_witdh, self.pen_down)
        self.lines.append(line_o)

    def right(self, angle = 90):
        self.rotation += angle
        self.rotation %= 360

    def left(self, angle = 90):
        self.rotation -= angle
        self.rotation %= 360

    def home(self):
        start_x, start_y = self.pos_x, self.pos_y
        self.pos_x, self.pos_y = self.base["x"], self.base["y"]
        end_x, end_y = self.pos_x, self.pos_y
        line_o = Line((start_x + self.distorsion, start_y + self.distorsion), (end_x + self.distorsion, end_y + self.distorsion),
                      self.pen_color, self.pen_witdh, self.pen_down)
        self.lines.append(line_o)

    def pendown(self):
        self.pen_down = True

    def penup(self):
        self.pen_down = False

    def width(self, size):
        self.pen_witdh = size

    def color(self, color):
        self.pen_color = color

    def fill(self):
        flood = Flood((self.pos_x, self.pos_y), self.pen_color)
        self.lines.append(flood)

    def reset(self):
        self.pos_x, self.pos_y = self.base["x"], self.base["y"]
        self.lines = []
        self.rotation = 0
        self.pen_color = Color.BLACK
        self.pen_witdh = 3
        self.pen_down = True
        self.show_turtle = True

    def clear(self):
        self.lines = []

    def showturtle(self):
        self.show_turtle = True

    def hideturtle(self):
        self.show_turtle = False


    def move(self, direction, distance):
        return int(round(self.pos_x + (distance * cos(radians(self.rotation))) * direction)),\
               int(round(self.pos_y + (distance * sin(radians(self.rotation))) * direction))

    def debug(self):
        print (self.pos_x, self.pos_y)
        print (self.rotation)

    def GetTurtleInformationToRender(self):
        return (self.pos_x, self.pos_y), self.rotation, self.show_turtle

    def GetLinesForRenderer(self):
        return self.lines

    def SetDistorsion(self, amount):
        self.distorsion = amount

    def SetBoundaries(self, top, bot):
        self.boundaries["top"] = top
        self.boundaries["bot"] = bot

    def NormalizeMovement(self):
        if self.boundaries["top"] is not None and self.boundaries["bot"] is not None:

            if self.pos_x < self.boundaries["top"][0]:
                self.pos_x = self.boundaries["top"][0]
            if self.pos_x > self.boundaries["bot"][0]:
                self.pos_x = self.boundaries["bot"][0]

            if self.pos_y < self.boundaries["top"][1]:
                self.pos_y = self.boundaries["top"][1]
            if self.pos_y > self.boundaries["bot"][1]:
                self.pos_y = self.boundaries["bot"][1]