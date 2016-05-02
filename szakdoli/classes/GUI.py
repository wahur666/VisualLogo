import tkinter as tk
import os
import pygame
from classes import UpDirection, DownDirection, RotateLeft, RotateRight
import time

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.canvasSize = 560
        self.commands = []
        self.initFrames()
        self.source = []


    def _initMenuFrame(self):
        self.frame4 = tk.LabelFrame(self.root, height=100, width=1000,text="Stuff")

        photo_play = tk.PhotoImage(file="resources/play-button.gif")
        self.button1 = tk.Button(self.frame4, width=50, height=50, image=photo_play, command=self.play)
        self.button1.image = photo_play
        self.button1.pack(padx=10, pady=25, side='left')

        self.button2 = tk.Button(self.frame4, text="DrawRectPygame", command=self.DrawOnPygame)
        self.button2.pack(side='left')

        photo_new = tk.PhotoImage(file="resources/new-doc-128.gif")
        self.button3 = tk.Button(self.frame4, text="DrawRectCanvas", command=self.clearCanvas, image=photo_new)
        self.button3.image = photo_new
        self.button3.pack(side='left')

        #self.button4 = tk.Button(self.frame4, text="Extend canvas", command=self.extendCanvas)
        #self.button4.pack(side='left')

        photo_cogs = tk.PhotoImage(file="resources/cogs.gif")
        self.button5 = tk.Button(self.frame4, width=50, height=50, image=photo_cogs)
        self.button5.image = photo_cogs
        self.button5.pack(padx=10, pady=25,side='left')

        self.button6 = tk.Button(self.frame4, text="Hidden Command")
        self.button6.pack(side='left')

        self.visibity = True

        self.frame4.pack(side='top', fill='x')

    def _initFunctuinonsFrame(self):
        self.frame1 = tk.LabelFrame(self.root, height=600, width=200, text="Parancsok")
        self.canvas1 = tk.Canvas(self.frame1, bg="white", width=200, height=580)
        #self.canvas1.config(scrollregion=[0, 0, 200, 900])
        self.canvas1.grid(row=0, column=0)

        tk.Grid.rowconfigure(self.frame1, 0, weight=1)
        tk.Grid.columnconfigure(self.frame1, 0, weight=1)

        self.wbar1 = tk.Scrollbar(self.frame1, orient='vertical', command=self.canvas1.yview)
        self.wbar1.grid(row=0, column=1, sticky='ns')
        self.canvas1.config(yscrollcommand=self.wbar1.set)

        self.frame1.pack(side='left', fill='both', expand='yes')

        self.PrepareFunctions()

    def _initStoryboardFrame(self):
        self.frame2 = tk.LabelFrame(self.root, height=600, width=200, text="Storybord")

        self.canvas2 = tk.Canvas(self.frame2, bg="white", width=200, height=580)
        self.canvas2.grid(row=0, column=0)

        tk.Grid.rowconfigure(self.frame2, 0, weight=1)
        tk.Grid.columnconfigure(self.frame2, 0, weight=1)

        self.wbar2 = tk.Scrollbar(self.frame2, orient='vertical', command=self.canvas2.yview)
        self.wbar2.grid(row=0, column=1, sticky='ns')
        self.canvas2.config(yscrollcommand=self.wbar2.set)

        self.frame2.pack(side='left', fill='both', expand='yes')

        self.X = 20
        self.Y = 20
        self.H = 60
        self.L = 60

    def _initPygameFrame(self):
        self.frame3 = tk.Frame(self.root, height=600, width=600)
        os.environ['SDL_WINDOWID'] = str(self.frame3.winfo_id())
        from platform import system
        if system() == "Windows":
            os.environ['SDL_VIDEODRIVER'] = 'windib'

        #self.root.update()
        self.screen = pygame.display.set_mode((560, 560))
        self.screen.fill(pygame.Color(255, 255, 255))
        pygame.display.init()
        pygame.display.update()
        self.frame3.pack(side='left', fill='y', pady=20, padx=20, expand='yes')

    def initFrames(self):
        self.root.geometry("1050x710")
        #self.root.resizable(width=False, height=False)
        self.root.title("Logo rajzolo")


        self._initMenuFrame()
        self._initFunctuinonsFrame()
        self._initStoryboardFrame()
        self._initPygameFrame()

        self.root.update()

        self._initBinds()
        self._print()

    def runMainLoop(self):
        self.root.mainloop()

    def extendCanvas(self):
        self.canvasSize += 80
        self.canvas2.config(scrollregion=[0, 0, 200, self.canvasSize])
        #pygame.draw.rect(self.screen, (0,0,0), (0,0,560,560))
        #pygame.display.update()
        # print(canvasSize)

    def DrawOnPygame(self):
        pygame.draw.rect(self.screen, (0,0,0), (10,10,400,400))
        pygame.display.update()

    def DrawOnCanvas(self, command):
        if self.canvasSize < self.Y + 80:
            self.extendCanvas()
        #rect1 = command.__init__(self.X, self.Y, self.H, self.L, 0)
        command.drawrect(self.canvas2)
        #rect1 = Command.Command(self.X,self.Y,self.H, self.L, 0)
        #rect1.drawrect(self.canvas2)
        self.Y += 80
        self.canvas2.yview_moveto(1.0)

    def PrepareFunctions(self):
        X = Y = 20
        H = L = 60
        rect1 = UpDirection.UpDirection(X,Y,H,L,0)
        rect1.drawrect(self.canvas1)
        self.commands.append(rect1)
        Y += 80
        rect1 = DownDirection.DownDirection(X, Y, H, L, 0)
        rect1.drawrect(self.canvas1)
        self.commands.append(rect1)
        Y += 80
        rect1 = RotateLeft.RotateLeft(X, Y, H, L, 0)
        rect1.drawrect(self.canvas1)
        self.commands.append(rect1)
        Y += 80
        rect1 = RotateRight.RotateRight(X, Y, H, L, 0)
        rect1.drawrect(self.canvas1)
        self.commands.append(rect1)
        Y += 80

    def _initBinds(self):
        self.button5.bind("<Shift-1>", self._print)
        self.canvas1.bind("<Button-1>", self.canvas1Bind)
        self.canvas2.bind("<Button-1>", self.canvas2Bind)

    def _print(self, event=None):
        print("Valami")
        if self.visibity :
            self.button6.pack_forget()
            self.visibity = False
        else:
            self.button6.pack(side='left')
            self.visibity = True

    def _print2(self):
        print("Nincs nyomva a shift")

    def canvas1Bind(self, event=None):
        print("Canvas1")
        for elem in self.commands:
            if elem.returnList()[1][0] == self.canvas1.find_withtag("current")[0]:
                name = elem.returnCommandName()
                if name == "UpDirection":
                    temp = UpDirection.UpDirection(self.X,self.Y,self.H,self.L,0)
                    self.DrawOnCanvas(temp)
                    self.source.append(temp)
                if name == "RotateLeft":
                    temp = RotateLeft.RotateLeft(self.X, self.Y, self.H, self.L, 0)
                    self.DrawOnCanvas(temp)
                    self.source.append(temp)
                if name == "DownDirection":
                    temp = DownDirection.DownDirection(self.X, self.Y, self.H, self.L, 0)
                    self.DrawOnCanvas(temp)
                    self.source.append(temp)
                if name == "RotateRight":
                    temp = RotateRight.RotateRight(self.X, self.Y, self.H, self.L, 0)
                    self.DrawOnCanvas(temp)
                    self.source.append(temp)
        print(self.canvas1.find_withtag("current")[0])

    def canvas2Bind(self, event=None):
        print("Canvas2")

    def play(self):
        self.canvas2.yview_moveto(0.0)
        currentSize = 560
        X = 10
        Y = 50
        for i in range(len(self.source)):
            temp = self.canvas2.create_rectangle(X,Y,X+5,Y+5)
            Y+=80
            if Y - 80> currentSize:
                print("Haho")
                diff = (currentSize - 160)/self.canvasSize
                if diff > 1:
                    diff=1.0
                self.canvas2.yview_moveto(diff)
                currentSize += 400
                self.canvas2.update()
                self.root.after(2000, None)

            self.canvas2.update()
            self.root.after(1000, None)
            #time.sleep(1)

            print("wait")
            self.canvas2.delete(temp)


    def clearCanvas(self):
        self.canvas2.delete("all")
        self.source.clear()
        self.canvasSize = 560
        self.canvas2.config(scrollregion=[0, 0, 200, self.canvasSize])
        self.Y = 20