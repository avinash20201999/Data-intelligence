from tkinter import *
from examin import examinewindow
from analysis import analysis
import os

def btn_clicked():
    a=analysis()
def btn_clicked2():
    os.system('python prediction.py')
def btn_clicked3():
    os.system('python visualize.py')
def btn_clicked4():
    
    a=examinewindow()


def homepagewindow():
    window = Tk()

    window.geometry("1080x720")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"Homebackground.png")
    background = canvas.create_image(
        540.0, 363.5,
        image=background_img)

    img0 = PhotoImage(file = f"homecontactus.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 951, y = 17,
        width = 118,
        height = 33)

    img1 = PhotoImage(file = f"home.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 695, y = 17,
        width = 111,
        height = 33)

    img2 = PhotoImage(file = f"homeAboutus.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b2.place (
        x = 823, y = 17,
        width = 111,
        height = 33)

    img3 = PhotoImage(file = f"uploadDownload.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command =btn_clicked4,
        relief = "flat")

    b3.place(
        x = 43, y = 123,
        width = 231,
        height = 127)

    img4 = PhotoImage(file = f"predictiveview.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked2,
        relief = "flat")

    b4.place(
        x = 42, y = 548,
        width = 232,
        height = 127)

    img5 = PhotoImage(file = f"visualize.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked3,
        relief = "flat")

    b5.place(
        x = 43, y = 405,
        width = 231,
        height = 127)

    img6 = PhotoImage(file = f"Examin.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b6.place(
        x = 43, y = 264,
        width = 231,
        height = 127)

    window.resizable(False, False)
    window.title("Data Intelligence-Home Page")
    window.mainloop()
