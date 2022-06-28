import tkinter as tk
from tkinter import filedialog as fd
import pandas as pd
from tkinter.messagebox import showinfo

class examinewindow():
    
    filename=''
    global v
    def __init__(self):
        
        root = tk.Tk()
        root.resizable(False,False)
        root.title("Upload Your Dataset")
        tk.Label(root, text='File Path').grid(row=0, column=0)
        self.v = tk.StringVar()
        entry1 = tk.Entry(root,textvariable=self.v).grid(row=0, column=1)
        tk.Button(root, text='Browse Data Set',command=self.import_csv_data).grid(row=1, column=0)
        tk.Button(root, text='Download prep data',command=self.prepare).grid(row=1, column=1)
        root.mainloop()
        
    
    def import_csv_data(self):
        
        
        filetypes = (('csv', '*.csv'),('All files', '*.*'))
        self.filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        print(self.filename)
        self.v.set(self.filename)
        
        
    
    def prepare(self):
    
        hd= pd.read_csv(self.filename, header=0, sep=",")
        hd.dropna(axis=0,inplace=True)
        #for x in hd:
            #hd[x] = hd[x].astype(float)
        data=pd.DataFrame(hd)
        data.to_csv("prepared.csv")
        showinfo(
            title='YOUR DATA IS PREPARED',
            message=self.filename
        )



 

    
