from Button import Button

from Drawable.Rectangle import Rect
from Util.Constants import COLOR as Color, MOUSE

class GUI:

    def __init__(self):
        self.items = []
        self.initilize()

    def DrawGUI(self, screen):
        for item in self.items:
            item.DrawObject(screen)

    def initilize(self):
        drawingWindow = Rect(20, 20, 630, 600, "Drawingwindow", Color.BLACK, 1)
        self.Add(drawingWindow)

        buttonPlay = Button(450,640,60,60, "\\Resources\\play.png")
        buttonPlay.bind(self.OnClickPlay)
        self.Add(buttonPlay)

        buttonStepOver = Button(520, 640, 60, 60)
        buttonStepOver.bind(self.OnClickStepOver)
        self.Add(buttonStepOver)

        buttonStop = Button(590, 640, 60, 60, "\\Resources\\stop.png")
        buttonStop.bind(self.OnClickStop)
        self.Add(buttonStop)

        buttonSettings = Button(20, 660, 40, 40, "\\Resources\\cogs.png")
        buttonSettings.bind(self.OnClickSettings)
        self.Add(buttonSettings)

        buttonLoad = Button(67, 660, 40, 40)
        buttonLoad.bind(self.OnClickLoad)
        self.Add(buttonLoad)

        buttonSave = Button( 110, 660, 40, 40)
        buttonSave.bind(self.OnClickSave)
        self.Add(buttonSave)

        buttonScreenshot = Button(154, 660, 40, 40, "\\Resources\\camera.png")
        buttonScreenshot.bind(self.OnClickScreenshot)
        self.Add(buttonScreenshot)

        buttonExit = Button(197, 660, 40,40)
        buttonExit.bind(self.OnClickExit)
        self.Add(buttonExit)


    def OnClick(self, event_type, event_pos):
        for item in self.items:
            if item.IsInside(event_pos):
                if isinstance(item, Rect):
                    pass
                if isinstance(item, Button):
                    item.OnClick(event_type)

    def Add(self, item):
        self.items.append(item)

    # ------ Event handlerek -------

    def OnClickPlay(self, evet_type):
        if evet_type == MOUSE.LMB:
            print "Play"
        else:
            print "Valami", evet_type

    def OnClickStop(self, event_type):
        print "Stop"

    def OnClickStepOver(self, event_type):
        print "StepOver"

    def OnClickSettings(self, event_type):
        print "Settings"

    def OnClickLoad(self, event_type):
        print "Load"

    def OnClickSave(self, event_type):
        print "Save"

    def OnClickScreenshot(self, event_type):
        print "Screenshot"

    def OnClickExit(self, event_type):
        print "Exit"