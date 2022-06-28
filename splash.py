from tkinter import *
import homepage


def btn_clicked():

    window.destroy()
    homepage.homepagewindow()
    




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

background_img = PhotoImage(file = f"splashbackground.png")
background = canvas.create_image(
    540.0, 360.0,
    image=background_img)

img0 = PhotoImage(file = f"startbutton.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 885, y = 648,
    width = 170,
    height = 54)

window.resizable(False, False)
window.title("Data Intelligence")
window.mainloop()
