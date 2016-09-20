from Rectangle import Rect
from Util import Color


class GUI():

    def __init__(self):
        self.items = []
        self.initilize()

    def DrawGUI(self, screen):
        for item in self.items:
            item.DrawObject(screen)

    def initilize(self):
        drawingWindow = Rect(50, 50, 600, 500, "Drawingwindow", Color.BLACK, 1)
        self.items.append(drawingWindow)