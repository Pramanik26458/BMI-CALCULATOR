from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI CALCULATOR")
root.geometry("470x580+300+200")
root.configure(bg="#f0f1f5")


def BMI():
    h = float(Height.get())
    W = float(Weight.get())

    # CONVERT HEIGHT INTO METER
    m = h /100
    bmi = round(float(W / m**2), 1)
    label1.config(text=bmi)

    # We can change value, because different countries have different BMI index
    if bmi <= 18.5:
        label2.config(text="Underweight!")
        label3.config(text="You have lower weight\n than a normal body!")
    elif 18.5 < bmi <= 25:
        label2.config(text="Normal!")
        label3.config(text="  It indicates that \n  you are healthy!")
    elif 25 < bmi <= 30:
        label2.config(text="Overweight")
        label3.config(text="It indicates that \n a person is slightly overweight.\nA doctor may advise to lose \n some weight for health reasons!")
    else:
        label2.config(text="Obese!")
        label3.config(text="Health may be at risk \n if they do not lose weight.")



image_icon = PhotoImage(file="python project/icon.png")
root.iconphoto(False, image_icon)


top = PhotoImage(file="python project/top.png",width=500,height=530)
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)


bottom_frame = Frame(root, width=470, height=530, bg="lightblue")
bottom_frame.place(x=20, y=300)


box = PhotoImage(file="python project/box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)


Label(root, text="Height (cm)", font="arial 10 bold", bg="#f0f1f5").place(x=20, y=70)
Label(root, text="Weight (kg)", font="arial 10 bold", bg="#f0f1f5").place(x=240, y=70)


scale = PhotoImage(file="python project/scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=310)


current_value = tk.DoubleVar()

def get_current_value():
    return "{:.2f}".format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    size = int(float(get_current_value()))
    img = Image.open("python project/man.png")
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.configure(image=photo2)
    secondimage.place(x=70, y=550 - size)
    secondimage.image = photo2


style = ttk.Style()
style.configure("TScale", background="white")
slider = ttk.Scale(root, from_=10, to=220, orient="horizontal", style="TScale", command=slider_changed, variable=current_value)
slider.place(x=80, y=250)


current_value2 = tk.DoubleVar()

def get_current_value2():
    return "{:.2f}".format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())


style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient="horizontal", style="TScale", command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)




Height = StringVar()
Weight = StringVar()

height_entry = Entry(root, textvariable=Height, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
height_entry.place(x=35, y=160)

weight_entry = Entry(root, textvariable=Weight, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
weight_entry.place(x=255, y=160)


secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y=530)

Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=280, y=340)

label1 = Label(root, font="arial 60 bold", bg="lightblue", fg="#fff")
label1.place(x=125, y=305)

label2 = Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=280, y=430)

label3 = Label(root, font="arial 15 bold", bg="lightblue")
label3.place(x=200, y=500)

root.mainloop()
