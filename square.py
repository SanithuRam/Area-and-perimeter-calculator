import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def display_calc_area_perimeter(area):
    tbox_age.config(state='normal')
    #age calculated is inserted into the text box after clearing the previous info in the textbox.
    tbox_age.delete('1.0', tk.END)
    tbox_age.insert(tk.END, age)
    tbox_age.config(state='disabled')

def square():
  def validation():
    choice_2=None
    answer=['a','p']
    
    while choice_2 not in answer :#while loop for area and perimeter chooser in square
      choice_2=str(input("enter <a> if you want to calculate area.Enter <p> if you want to calculate perimeter. : "))
      if choice_2 not in answer:
        print("Select a-for area and , p- for perimeter")
        
      if choice_2 == 'a' :
        while True:
          try:
            lenght = float(input("Side of the Square :"))
          except:
            print('Please use numeric digits.')
            continue
          if lenght <= 0:
            print('Please enter a positive number.')
          else:  
            area = lenght * lenght
            print("Area of the Square : ", area)
            break
          
      elif choice_2 == 'p':
        while True:
          try:
            lenght = float(input("Side of the Square :"))
          except:
            print('Please use numeric digits.')
            continue
        
          if lenght <= 0:
            print('Please enter a positive number.')
          else:  
            perimeter = lenght*4
            print("Perimeter of the Square : ", perimeter)
            break

window = tk.Tk()
window.geometry("500x230")
window.config(bg="#F7DC6F")
window.resizable(width=False, height=False)
window.title('area and perimeter calculator---Square')
lb_heading = tk.Label(window,
                      text="The Area and perimeter calculator for Square!",
                      font=("Arial", 20),
                      fg="black",
                      bg="#F7DC6F")
lb_subheading = tk.Label(
    window,
    font=("Arial", 12),
    text="welcome tp the the Area and perimeter calculator --- Section Square!",
    fg="black",
    bg="#F7DC6F")
lb_side_lenght = tk.Label(window,
                   text="Side lenght of the square ",
                   font=('Arial', 12, "bold"),
                   fg="darkgreen",
                   bg="#F7DC6F")
e_side_lenght = tk.Entry(window, width=5)
n = tk.StringVar()
area_perimeter_choser = ttk.Combobox(window, textvariable=n, width=14)
area_perimeter_choser = ttk.Combobox(window, textvariable=n, width=14, state="readonly")

# Adding combobox drop down list
area_perimeter_choser['values'] = ('Select area or perimeter',)
# Shows Select a month as a default value
area_perimeter_choser.current(0)
#e_month = tk.Entry(window,width=5)
btn_calculate_area_perimeter = tk.Button(window,
                              text="Calculate Age!",
                              font=("Arial", 13),
                              command=validation)
tbox_age = tk.Text(window,
                   width=3,
                   height=0,
                   state="disabled",
                   bg="lightgreen",
                   font=('Arial', 24, "bold"))
btn_exit = tk.Button(window,text="Exit Application!",font=("Arial", 13),command=exit)
lb_heading.place(x=70, y=5)
lb_subheading.place(x=10, y=40)
area_perimeter_choser.place(x=120, y=105)
btn_calculate_area_perimeter.place(x=30, y=170)


