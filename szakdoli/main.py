import tkinter as tk
from tkinter import ttk
import pygame
import cx_Freeze

root = tk.Tk()
root.geometry("1000x705")
root.resizable(width=False, height=False)
root.title("Logo rajzolo")

frame1 = tk.LabelFrame(root, height=600, width=200, text="Parancsok")
frame2 = tk.LabelFrame(root, height=600, width=200, text="Storybord")
frame3 = tk.LabelFrame(root, height=600, width=600, text="DrawingBoard")
frame4 = tk.LabelFrame(root, height=100, width=1000, text="Menu")

canvas1 = tk.Canvas(frame1, bg="white", width=200, height=580)
canvas1.config(scrollregion=[0,0,200,900])

canvas1.create_text(100,600,text="Alma")

canvas2 = tk.Canvas(frame2, bg="white", width=200, height=580)
canvas1.grid(row = 0, column= 0)
canvas2.grid(row = 0, column= 0)

wbar1 = tk.Scrollbar(frame1, orient='vertical',command=canvas1.yview)
wbar1.grid(row = 0, column = 1 , sticky='ns')
canvas1.config(yscrollcommand=wbar1.set)

wbar2 = tk.Scrollbar(frame2, orient='vertical',command=canvas2.yview)
wbar2.grid(row = 0, column = 1 , sticky='ns')
canvas2.config(yscrollcommand=wbar2.set)

frame4.pack(side='top')
frame1.pack(side='left',fill='y')
frame2.pack(side='left',fill='y')
frame3.pack(side='left',fill='y')

root.mainloop()
