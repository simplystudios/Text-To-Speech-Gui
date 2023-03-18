import text_to_speech
import os
from tkinter import *
from text_to_speech import *

directory = "Text-to-speech-files"
parent_dir = "./text-to-speech/"
path = os.path.join(parent_dir, directory)
isExist = os.path.exists(path)
if not isExist :
    os.mkdir(path)
    
splash_root = Tk()
splash_root.configure(bg='#18122B')
splash_root.title('Text To Speech Converter')
splash_root.geometry("420x320")

maintxt = Label(splash_root, text="Text To Speech Converter",
                font='Poppins 20 bold', fg='#FFFBEB', bg='#18122B')
maintxt.pack(pady=90)

subtxt = Label(splash_root, text="Loading...",
               font='Poppins 12 bold', fg='green',bg='#18122B')
subtxt.pack(pady=20)

subtxt = Label(splash_root, text="Made By Ansh Wadhwa & Open Source On Github",
               font='Poppins 12 ', fg='#FFFBEB', bg='#18122B')
subtxt.pack()


def mainwindow() :
    splash_root.destroy()
    root = Tk()
    root.geometry("420x320")
    root.configure(bg='#18122B')
    root.title("text-to-speech")
    #root.resizable(False,False)


    def textspeak() :
        text = input1.get()
        filename = input2.get()
        filenamefind = filename + ".mp3"
        save(text,"en",file = path + "/" + filename +".mp3")
        input1.delete(0, END)
        input2.delete(0, END)
        print(filenamefind)
    def click(event) :
        input1.configure(state=NORMAL)
        input1.delete(0, END)
        input1.unbind('<Button-1>', clicked)
        input2.configure(state=NORMAL)
        input2.delete(0, END)
        input2.unbind('<Button-2>', clicked2)

    title = Label(root, text="Text To Speech Converter",
                  fg="#FFFBEB", bg="#18122B", font='Poppins 20 bold')
    title.grid(padx=10,pady=10)

    inlab = Label(root, text="Enter Something To Say",
                fg="white", bg="#18122B", font='Poppins, 13 bold')
    inlab.grid(padx=0,pady=4)

    input1 = Entry(root,width=44,font=('Poppins',12))
    input1.insert(0, 'Enter Something To Convert')
    input1.grid(padx=0,pady=4)

    inlab2 = Label(root, text="Enter The File Name", fg="#ffffff",bg="#18122B", font='Poppins, 13 bold')
    inlab2.grid(padx=10,pady=4)

    input2 = Entry(root, width=44, font=('Poppins', 12))
    input2.insert(0, "Enter file name")
    input2.grid(padx=10,pady=8)

    savebtn = Button(root, text="Save", fg="#ffffff", bg="#251749", width=50)
    savebtn.configure(command=textspeak)
    savebtn.grid(padx=10,pady=10)

    closebtn = Button(root, text="Close", fg="#ffffff", bg="#251749", width=50)
    closebtn.configure(command=root.destroy,fg="#ffffff")
    closebtn.grid(padx=10,pady=10)

    about = Label(root, text="Made By Ansh Wadhwa & Open Source On Github",
                fg="white", bg="#18122B", font=('Poppins', 10))
    about.grid(padx=10, pady=10)

    clicked = input1.bind('<Button-1>', click)
    clicked2 = input2.bind('<Button-2>', click)
    root.mainloop()
    

splash_root.after(2000, mainwindow)
splash_root.mainloop()
