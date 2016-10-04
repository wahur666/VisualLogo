# -*- coding: utf-8 -*-

from Drawable.Base.Command import Command

class Forward(Command):

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Forward, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Forward, self).execture_command()

    def DrawObject(self, screen):
        super(Forward, self).DrawObject(screen)

    def IsInside(self, position):
        return  super(Forward, self).IsInside(position)

class Backward(Command):
    def IsInside(self, position):
        return super(Backward, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Backward, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Backward, self).execture_command()

    def DrawObject(self, screen):
        super(Backward, self).DrawObject(screen)

class Right(Command):
    def IsInside(self, position):
        return super(Right, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Right, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Right, self).execture_command()

    def DrawObject(self, screen):
        super(Right, self).DrawObject(screen)

class Left(Command):
    def IsInside(self, position):
        return super(Left, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Left, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Left, self).execture_command()

    def DrawObject(self, screen):
        super(Left, self).DrawObject(screen)

class Home(Command):
    def IsInside(self, position):
        return super(Home, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Home, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Home, self).execture_command()

    def DrawObject(self, screen):
        super(Home, self).DrawObject(screen)

class PenDown(Command):
    def IsInside(self, position):
        return super(PenDown, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(PenDown, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(PenDown, self).execture_command()

    def DrawObject(self, screen):
        super(PenDown, self).DrawObject(screen)

class PenUp(Command):
    def IsInside(self, position):
        return super(PenUp, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(PenUp, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(PenUp, self).execture_command()

    def DrawObject(self, screen):
        super(PenUp, self).DrawObject(screen)


class PenWidth(Command):
    def IsInside(self, position):
        return super(PenWidth, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(PenWidth, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(PenWidth, self).execture_command()

    def DrawObject(self, screen):
        super(PenWidth, self).DrawObject(screen)


class PenColor(Command):
    def IsInside(self, position):
        return super(PenColor, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(PenColor, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(PenColor, self).execture_command()

    def DrawObject(self, screen):
        super(PenColor, self).DrawObject(screen)

class FloodFill(Command):
    def IsInside(self, position):
        return super(FloodFill, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(FloodFill, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(FloodFill, self).execture_command()

    def DrawObject(self, screen):
        super(FloodFill, self).DrawObject(screen)

class Reset(Command):
    def IsInside(self, position):
        return super(Reset, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Reset, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Reset, self).execture_command()

    def DrawObject(self, screen):
        super(Reset, self).DrawObject(screen)

class Clear(Command):
    def IsInside(self, position):
        return super(Clear, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Clear, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Clear, self).execture_command()

    def DrawObject(self, screen):
        super(Clear, self).DrawObject(screen)

class ShowTurtle(Command):
    def IsInside(self, position):
        return super(ShowTurtle, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(ShowTurtle, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(ShowTurtle, self).execture_command()

    def DrawObject(self, screen):
        super(ShowTurtle, self).DrawObject(screen)

class HideTurlte(Command):
    def IsInside(self, position):
        return super(HideTurlte, self).IsInside(position)

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(HideTurlte, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(HideTurlte, self).execture_command()

    def DrawObject(self, screen):
        super(HideTurlte, self).DrawObject(screen)

class Loop(Command):
    def IsInside(self, position):
        pass #mivel ez több darabból fog állni ezért nem lehet csak úgy az örököltet használni

    def __init__(self, x=None, y=None, w=None, h=None, vec2_pos=None, size=None, descriptor=""):
        super(Loop, self).__init__(x, y, w, h, vec2_pos, size, descriptor)

    def execture_command(self):
        super(Loop, self).execture_command()

    def DrawObject(self, screen):
        super(Loop, self).DrawObject(screen)