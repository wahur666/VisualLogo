class Rect:
    def __init__(self, X, Y, H, L, indetLevel):
        self.X = X
        self.Y = Y
        self.L = L
        self.H = H
        self.itemList = []
        self.indentLevel = indetLevel

    def drawrect(self, canvas):
        base = canvas.create_rectangle(self.X+self.indentLevel*15, self.Y, self.X+self.L+self.indentLevel*15, self.Y+self.H, fill="#ffffff")
        self.itemList.append((base,'base'))
        text = canvas.create_text(self.X + 30 +self.indentLevel*15, self.Y + 30, text = base, fill="#ff0000")
        self.itemList.append((text,'text'))
        print(self.itemList)

    def returnList(self):
        return self.itemList