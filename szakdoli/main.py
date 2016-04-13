import tkinter as tk
import pygame
import cx_Freeze

root = tk.Tk()
root.geometry("1000x600")

frame1 = tk.Frame(None, height=600, width=200, bg='red')
frame2 = tk.Frame(None, height=600, width=200, bg='green')
frame3 = tk.Frame(None, height=600, width=600, bg='blue')


label1 = tk.Label(frame1,text="parancsok",width=200)
label1.pack()
frame1.pack(side='left')

label2 = tk.Label(frame2,text='stroyboard',width=200)
label2.pack()


frame2.pack(side='left')
frame3.pack(side='left')


root.mainloop()