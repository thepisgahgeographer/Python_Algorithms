
# importing all files  from tkinter 
from tkinter import * 
from tkinter import ttk 
from tkinter.filedialog import asksaveasfile 
  
root = Tk() 
root.geometry('700x250') 

def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
  
def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files) 
  
btn1 = ttk.Button(root, text = 'Save File', command = lambda : save()) 
btn1.pack(side = BOTTOM, pady = 20) 

btn2 = ttk.Button(root, text ='Input LAS File', command = lambda:open_file())
btn2.pack(side = TOP, pady = 30)
mainloop() 


  
