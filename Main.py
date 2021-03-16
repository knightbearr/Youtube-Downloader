# ---IMPORT PACKAGE TKINTER AND PYTUBE---
from tkinter import *
from pytube import YouTube
from tkinter import messagebox

# ---SET TKINTER---
root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title("Youtube Downloader")

# ---BACKGROUND IMAGE---
bg = PhotoImage(file="1.png")
btn = Button(root, image=bg)
btn.place(x=0, y=0)

# ---LINK---
link = StringVar()
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 250)

# ---FUNCTION---
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    messagebox.askokcancel('info','Video anda telah berhasil didownload')  

# ---BUTTON---
button = Button(root,text = 'DOWNLOAD', font = 'Helevatica 15 bold' ,bg = 'white', bd=0, padx = 2, command = Downloader)
button.place(x=180 ,y = 280)

# ---MAINLOOP---
root.mainloop()