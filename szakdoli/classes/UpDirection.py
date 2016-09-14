from Command import Command
from Tkinter import PhotoImage

class UpDirection(Command):

    def __init__(self, X, Y, H, L, indetLevel):
        super(Command, self).__init__(X, Y, H, L, indetLevel)
        self.images = []
        self.commandName = "UpDirection"

    def runCommand(self):
        Command.runCommand()

    def drawrect(self, canvas):
        base = canvas.create_rectangle(self.X + self.indentLevel * 15, self.Y, self.X + self.L + self.indentLevel * 15,
                                       self.Y + self.H, fill="#ffffff")

        self.itemList.append((base, 'base'))
        #text = canvas.create_text(self.X + 30 + self.indentLevel * 15, self.Y + 30, text=base, fill="#ff0000")
        #self.itemList.append((text, 'text'))
        image = PhotoImage(file="resources/Up-Arrow.gif")
        canvasimage = canvas.create_image(self.X + self.L / 2,self.Y + self.H /2,image=image)
        self.images.append(image)
        self.itemList.append((canvasimage,"image"))
        print(self.itemList)

