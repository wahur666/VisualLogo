import tkinter as tk
import os
import pygame

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.canvasSize = 580
        self.initFrames()

    def _initMenuFrame(self):
        self.frame4 = tk.Frame(self.root, height=100, width=1000)
        self.photo = tk.PhotoImage(file="resources/play-button.gif")
        self.button1 = tk.Button(self.frame4, width=50, height=50, image=self.photo, command=self.play)
        self.button1.image = self.photo
        self.button1.pack(padx=25, pady=25, side='left')
        self.frame4.pack(side='top', fill='x')

    def _initFunctuinonsFrame(self):
        self.frame1 = tk.LabelFrame(self.root, height=600, width=200, text="Parancsok")
        self.canvas1 = tk.Canvas(self.frame1, bg="white", width=200, height=580)
        self.canvas1.config(scrollregion=[0, 0, 200, 900])

        self.canvas1.create_text(100, 600, text="Alma")

        self.canvas1.grid(row=0, column=0)

        self.wbar1 = tk.Scrollbar(self.frame1, orient='vertical', command=self.canvas1.yview)
        self.wbar1.grid(row=0, column=1, sticky='ns')
        self.canvas1.config(yscrollcommand=self.wbar1.set)

        self.frame1.pack(side='left', fill='y')

    def _initStoryboardFrame(self):
        self.frame2 = tk.LabelFrame(self.root, height=600, width=200, text="Storybord")
        self.canvas2 = tk.Canvas(self.frame2, bg="white", width=200, height=580)
        self.canvas2.grid(row=0, column=0)

        self.wbar2 = tk.Scrollbar(self.frame2, orient='vertical', command=self.canvas2.yview)
        self.wbar2.grid(row=0, column=1, sticky='ns')
        self.canvas2.config(yscrollcommand=self.wbar2.set)

        self.frame2.pack(side='left', fill='y')

    def _initPygameFrame(self):
        self.frame3 = tk.Frame(self.root, height=600, width=600)
        os.environ['SDL_WINDOWID'] = str(self.frame3.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        self.screen = pygame.display.set_mode((560, 560))
        self.screen.fill(pygame.Color(255, 255, 255))
        pygame.display.init()
        pygame.display.update()
        self.frame3.pack(side='left', fill='y', pady=20, padx=20)

    def initFrames(self):
        self.root.geometry("1050x710")
        self.root.resizable(width=False, height=False)
        self.root.title("Logo rajzolo")


        self._initMenuFrame()
        self._initFunctuinonsFrame()
        self._initStoryboardFrame()
        self._initPygameFrame()

    def runMainLoop(self):
        self.root.mainloop()

    def play(self):
        self.canvasSize += 100
        self.canvas2.config(scrollregion=[0, 0, 200, self.canvasSize])
        pygame.draw.rect(self.screen, (0,0,0), (0,0,560,560))
        pygame.display.update()
        # print(canvasSize)