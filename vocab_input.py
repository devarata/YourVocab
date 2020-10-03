import tkinter as tk
from tkinter import StringVar
import os
import tkinter.messagebox as mb



def getWord(entry1,root):
    outF = open("D:\\Practice\\Python\\Vocabulary\\output.txt","w")
    outF.write(entry1.get())
    outF.close()
    root.destroy()


#011740
def word(root,final_word):
    try:
        os.remove("D:\\Practice\\Python\\Vocabulary\\output.txt")
    except OSError:
        pass
    canvas = tk.Canvas(root, width = 400, height = 300,  relief = 'raised',bg = "#011740")
    canvas.pack()
    label1 = tk.Label(root, text='Vocabulary')
    label1.config(font=('helvetica', 14))
    label1.config(bg="#011740")
    label1.config(fg='white')
    canvas.create_window(200, 25, window=label1)
    label2 = tk.Label(root, text='Adding to Vocabulary:')
    label2.config(font=('helvetica', 10))
    label2.config(bg = "#011740")
    label2.config(fg='white')
    canvas.create_window(200, 100, window=label2)
    entry1 = tk.Entry(root)
    entry1.focus()
    canvas.create_window(200, 140, window=entry1)
    button1 = tk.Button(text='Search', command=lambda:getWord(entry1,root), bg='#73AFF6', fg='#011740', font=('helvetica', 9, 'bold'))
    canvas.create_window(200, 180, window=button1)
    root.mainloop()



def word_func():
    root= tk.Tk()
    final_word = ""
    word(root,final_word)
    try:
        with open('D:\\Practice\\Python\\Vocabulary\\output.txt','r') as f:
            final_word = f.readline()
    except FileNotFoundError:
            mb.showerror('Output','closed the box without entering anything')
    return final_word
