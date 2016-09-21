from Rectangle import Rect
from Util import Color
from Button import Button

class GUI():

    def __init__(self):
        self.items = []
        self.initilize()

    def DrawGUI(self, screen):
        for item in self.items:
            item.DrawObject(screen)

    def initilize(self):
        drawingWindow = Rect(20, 20, 630, 600, "Drawingwindow", Color.BLACK, 1)
        self.items.append(drawingWindow)
        buttonPlay = Button(452,642,55,55, "\Resources\play.png")
        self.items.append(buttonPlay)
        buttonsquircle = Rect(450,640,60,60,"l", width=1)
        self.items.append(buttonsquircle)
