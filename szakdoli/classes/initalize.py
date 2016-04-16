import tkinter as tk
import pygame
'''
def play():
    global canvasSize
    canvasSize += 100
    canvas1.config(scrollregion=[0, 0, 200, canvasSize])
    # print(canvasSize)
'''

def _initMenuFrame(root):
    frame4 = tk.LabelFrame(root, height=100, width=1000, text="Menu")
    photo = tk.PhotoImage(file="resources/play-button.gif")
    button1 = tk.Button(frame4, width=50, height=50, image=photo)
    button1.image=photo
    button1.pack(padx=25, pady=25, side='left')
    frame4.pack(side='top', fill='x')


def _initFunctuinonsFrame(root):
    frame1 = tk.LabelFrame(root, height=600, width=200, text="Parancsok")
    canvas1 = tk.Canvas(frame1, bg="white", width=200, height=580)
    canvas1.config(scrollregion=[0, 0, 200, 900])

    canvas1.create_text(100, 600, text="Alma")

    canvas1.grid(row=0, column=0)

    wbar1 = tk.Scrollbar(frame1, orient='vertical', command=canvas1.yview)
    wbar1.grid(row=0, column=1, sticky='ns')
    canvas1.config(yscrollcommand=wbar1.set)

    frame1.pack(side='left', fill='y')

def _initStoryboardFrame(root):
    frame2 = tk.LabelFrame(root, height=600, width=200, text="Storybord")
    canvas2 = tk.Canvas(frame2, bg="white", width=200, height=580)
    canvas2.grid(row=0, column=0)

    wbar2 = tk.Scrollbar(frame2, orient='vertical', command=canvas2.yview)
    wbar2.grid(row=0, column=1, sticky='ns')
    canvas2.config(yscrollcommand=wbar2.set)

    frame2.pack(side='left', fill='y')

def _initPygameFrame(root):
    frame3 = tk.LabelFrame(root, height=600, width=600, text="DrawingBoard")

    frame3.pack(side='left', fill='y')

def initFrames(root):
    root.geometry("1000x705")
    root.resizable(width=False, height=False)
    root.title("Logo rajzolo")
    #canvasSize = 580

    _initMenuFrame(root)
    _initFunctuinonsFrame(root)
    _initStoryboardFrame(root)
    _initPygameFrame(root)









