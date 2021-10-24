import tkinter as tk
from tkinter import Entry, Tk, ttk
import subprocess


def python_open():
    subprocess.call([r'C:\Users\mizun\OneDrive\MyPythonProject\practice\ex5.py', 'htmlfilename.htm'], shell=True)#file name

def printer():
    print(entry.get())

root=tk.Tk()#making the interface
root.geometry('300x150+50+100')

frame1=ttk.LabelFrame(text='INPUT')
frame1.pack()

#frame1 START
entry=tk.StringVar()
entry=ttk.Entry(frame1,text=entry)
entry.pack()

button0=ttk.Button(frame1,text='ENTER',command=printer)
button0.pack()
#frame1 END

button1=ttk.Button(text='MECHANICS',command=python_open)
button1.pack()

root.mainloop()
