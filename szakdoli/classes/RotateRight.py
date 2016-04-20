from classes.Command import Command
from tkinter import PhotoImage

class RotateRight(Command):

    def __init__(self, X, Y, H, L, indetLevel):
        super().__init__(X, Y, H, L, indetLevel)
        self.images = []

    def runCommand(self):
        super().runCommand()

    def drawrect(self, canvas):
        base = canvas.create_rectangle(self.X + self.indentLevel * 15, self.Y, self.X + self.L + self.indentLevel * 15,
                                       self.Y + self.H, fill="#ffffff")
        self.itemList.append((base, 'base'))
        image = PhotoImage(file="resources/turn-right-arrow.gif")
        canvasimage = canvas.create_image(self.X + self.L / 2,self.Y + self.H /2,image=image)
        self.images.append(image)
        self.itemList.append((canvasimage,"image"))
        print(self.itemList)