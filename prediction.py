from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import pandas as pd
from scipy import stats
from functools import partial  
import matplotlib.pyplot as plt
filename=''
def plot(x,y):
    
    xvar=x.get()
    yvar=y.get()
    data = pd.read_csv("data.csv")
    xv = data[xvar]
    yv = data[yvar]

    slope, intercept, r, p, std_err = stats.linregress(xv, yv)

    def myfunc(xv):
        return slope * xv + intercept

    mymodel = list(map(myfunc, xv))

    plt.scatter(xv, yv)
    plt.plot(xv, mymodel)
    plt.ylim(ymin=0, ymax=2000)
    plt.xlim(xmin=0, xmax=200)
    plt.xlabel(xvar)
    plt.ylabel (yvar)
    plt.show()

def import_csv_data():
        global v
        global lc
        filetypes = (('csv', '*.csv'),('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        print(filename)
        v.set(filename)
        data = pd.read_csv(filename) 
        lc.set(data.columns)
        

window = Tk()

window.geometry("643x658")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 658,
    width = 643,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
v=tk.StringVar()
xaxis = tk.StringVar()  
yaxis = tk.StringVar()

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    271.5, 52.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    textvariable=v,
    highlightthickness = 0)

entry0.place(
    x = 141.0, y = 32,
    width = 261.0,
    height = 38)
lc=tk.StringVar()
entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    321.5, 284.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    textvariable=lc,
    highlightthickness = 0)

entry1.place(
    x = 22.0, y = 99,
    width = 599.0,
    height = 368)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    149.0, 520.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    textvariable=xaxis,
    highlightthickness = 0)

entry2.place(
    x = 78.0, y = 505,
    width = 142.0,
    height = 28)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    488.0, 520.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#f0f0f0",
    textvariable=yaxis,
    highlightthickness = 0)

entry3.place(
    x = 417.0, y = 505,
    width = 142.0,
    height = 28)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    221.0, 516.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
plot=partial(plot, xaxis, yaxis)
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = plot,
    relief = "flat")

b0.place(
    x = 244, y = 586,
    width = 126,
    height = 41)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = import_csv_data,
    relief = "flat")

b1.place(
    x = 427, y = 33,
    width = 40,
    height = 39)

window.resizable(False, False)
window.mainloop()