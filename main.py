# used to create a custom window for  calculator import tkinter as tk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from circle import *
from square import *
from triangle import *
from rectangle import *
from parallelogram import *


def clear():
    print("\033[H\033[J", end="")


#for shape chooser
def int_check(question, err, low, high):
    error = f"{err} between {low} and {high}"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
        except:
            print(error)


#code for user inputs
def open_square_window():
    square()
def open_rectangle_window():
    rectangle()
def open_triangle_window():
    triangle()
def open_circle_window():
    circle()
def open_parallelogram_window():
    parallelogram()

# Creating a custom window
window = tk.Tk()
window.geometry("750x500")
window.config(bg="#F7DC6F")
window.resizable(width=False, height=False)
window.title('Area and Perimeter  Calculator!')
# Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,
                      text="The Area and Perimeter Calculator!",
                      font=("Arial", 20),
                      fg="black",
                      bg="#F0F8FF")
lb_subheading = tk.Label(window,
                         font=("Arial", 12),
                         text="Welcome to the Area and Perimeter Calculator.",
                         fg="black",
                         bg="#F7DC6F")

# Labels for date, month and year
btn_square = tk.Button(window, text="square", font=("Arial", 13),command=open_square_window)
btn_rectangle = tk.Button(window, text="rectangle", font=("Arial", 13),command=open_rectangle_window)

btn_circle = tk.Button(window, text="circle", font=("Arial", 13),command=open_circle_window)
btn_triangle = tk.Button(window, text="triangle", font=("Arial", 13),command=open_triangle_window)

btn_parallelogram = tk.Button(window, text="parallelogram", font=("Arial", 13),command=open_parallelogram_window)
btn_exit = tk.Button(window,text="Exit Application!",font=("Arial", 13),command=exit)
# Placing the elements on the screen
lb_heading.place(x=70, y=5)
lb_subheading.place(relx=10, rely=40)
btn_square.place(x=20, y=80)
btn_rectangle.place(x=100, y=150)
btn_circle.place(x=400, y=80)
btn_triangle.place(x=200, y=80)
btn_parallelogram.place(x=300, y=150)
btn_exit.place(x=500, y=350)

