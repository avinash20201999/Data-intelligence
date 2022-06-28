import tkinter as tk 
import pandas as pd
from pandas.io.formats.format import TextAdjustment
class analysis:
    def __init__(self):
        
        root = tk.Tk()
        root.title("Your Examin DataSet")
        root.resizable(False,False)
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=50, width=125)
        l = tk.Label(root, text = "ANALYSIS REPORT OF PREPARED DATA SET")
        l.config(font =("Courier", 14))
        l.pack()
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack()
        T.config(font=("Airial", 14))
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        
        hd= pd.read_csv("prepared.csv", header=0, sep=",")
        quote=hd.describe()
        T.insert(tk.END, quote)
        tk.mainloop()
