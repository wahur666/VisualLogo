# -*- coding: utf-8 -*-

from Drawable.Base.Command import Command

class Forward(Command):

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Forward, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        self.imagePath = "\\Resources\\arrow-up.png"

    def execture_command(self):
        super(Forward, self).execture_command()


class Backward(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Backward, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        self.imagePath = "\\Resources\\arrow-down.png"

    def execture_command(self):
        super(Backward, self).execture_command()


class Right(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Right, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        self.imagePath = "\\Resources\\turnright.png"

    def execture_command(self):
        super(Right, self).execture_command()


class Left(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Left, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        self.imagePath = "\\Resources\\turnleft.png"

    def execture_command(self):
        super(Left, self).execture_command()


class Home(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Home, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Home, self).execture_command()


class PenDown(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(PenDown, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        self.imagePath = "\\Resources\\pencil2.png"

    def execture_command(self):
        super(PenDown, self).execture_command()

class PenUp(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(PenUp, self).__init__(x, y, w, h, vec2_pos, size, descriptor)
        self.imagePath = "\\Resources\\pencil.png"

    def execture_command(self):
        super(PenUp, self).execture_command()


class PenWidth(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(PenWidth, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(PenWidth, self).execture_command()


class PenColor(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(PenColor, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(PenColor, self).execture_command()


class FloodFill(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(FloodFill, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(FloodFill, self).execture_command()


class Reset(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Reset, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Reset, self).execture_command()


class Clear(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Clear, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Clear, self).execture_command()


class ShowTurtle(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(ShowTurtle, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(ShowTurtle, self).execture_command()

class HideTurlte(Command):
    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(HideTurlte, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(HideTurlte, self).execture_command()


class Loop(Command):
    # mivel ez több darabból fog állni ezért nem lehet csak úgy az örököltet használni
    def IsInside(self, position):
        pass

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Loop, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Loop, self).execture_command()

    def DrawObject(self, screen):
        pass