from tkinter import *
from tkinter import filedialog 
import os

root = Tk()
#open files funtion
def browseFiles(): 
    filenamee = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Bilder", "*.jpg*;*.png"), ("all files", "*.*"))) #
    path_label.configure(text="File Opened: "+filenamee) #writes the file path in the label

    #main file.read/write
    f = open(f"{filenamee}", encoding="ISO-8859-1", mode="r")
    try:
        byte = f.read(1) #byte gets read
        str = ""
        while byte != "":
            str = str + byte
            byte = f.read(1)
        text_label.insert(1.0, f"{str}")
    finally:
        f.close()

#show output in txt file
def browseFiles_txt(): 
    filenamee = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Bilder", "*.jpg*;*.png"), ("all files", "*.*"))) #
    path_label.configure(text="File Opened: "+filenamee) #writes the file path in the label
    text_label.insert(1.0, "A output.txt file should appeared on you Desktop which containts the picture code. If there is a hidden message look at the bottom of the code in the file.")
    #main file.read/write
    f = open(f"{filenamee}", encoding="ISO-8859-1", mode="r")
    try:
        byte = f.read(1) #byte gets read
        str = ""
        while byte != "":
            str = str + byte
            byte = f.read(1)
        with open(os.path.join(os.path.expanduser('~'), 'Desktop', 'output.txt'), mode='w', encoding="utf8") as fh:
                    fh.write(f"{str}")
    finally:
        f.close()

#window configs 
root.title('Gemimnachricht') 
root.geometry("450x250") 
root.config(background = "white") 
#buttons
b_open = Button(root, text="open file", command=browseFiles)
b_open.pack()
read_file = Button(root, text="open in txt", command=browseFiles_txt)
read_file.pack()
#labels
path_label = Label(root, text="file path will me shown here")
path_label.pack()        #grid(row=1, column=1)
text_label = Text(root)
text_label.pack()      #grid(row=2, column=1000)

root.mainloop()
