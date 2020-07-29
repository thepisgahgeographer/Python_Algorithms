
# importing all files  from tkinter 
from tkinter import * 
from tkinter import ttk 
from tkinter.filedialog import asksaveasfile 
from tkinter.filedialog import askopenfile 
import laspy
import numpy
  
root = Tk() 
root.geometry('700x250') 

def open_file(): 
    global infile
    infile = askopenfile(mode ='r', filetypes =[('Raw LAS Files', '.las')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
  
def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files) 

def processLAS():
    lasFile =  File(infile, mode = "r")
    headerformat = lasFile.header.header_format
    for spec in headerformat:
        print(spec.name)


  
btn1 = ttk.Button(root, text = 'Save File', command = lambda : save()) 
btn1.pack(side = BOTTOM, pady = 20) 

btn2 = ttk.Button(root, text ='Input LAS File', command = lambda:open_file())
btn2.pack(side = TOP, pady = 30)
mainloop() 


  
