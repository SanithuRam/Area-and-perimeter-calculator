import math

def clear():
    print("\033[H\033[J", end="")

#code to find area and perimter of square
def square():
    choice_2 = str(input("If you wanna calculate area enter 'a' if perimeter enter 'p' : "))
    if choice_2 == 'a' :
        lenght = float(input("Side of the Square :"))
        if lenght <=0:
          print("enter a valid input for the lenght")
        else:
           area = lenght * lenght
           print("Area of the Square : ", area)
    elif choice_2 == 'p':
        lenght_1 = float(input("Side of the Square :"))
        if lenght_1 <=0:
          print("enter a valid input for the lenght")
        else:
          
          perimeter = lenght_1 * 4
          print("Perimeter of the square:", perimeter)
    else: 
        print("entered input for area and perimeter choser is wrong:(" )
      
         

#code to find area and perimeter of rectangle
def rectangle():
    choice_2 = str(input("If you wanna calculate area enter 'a' if perimeter enter 'p': "))
    if choice_2 =="a":
        lenght = float(input("Input the length of the Rectangle:  "))
        breath = float(input("Input the breadth of the Rectangle: "))
        if lenght <=0 or breath<=0 :
          print("enter a valid input for the lenght")
        else:
          area_rectangle = lenght * breath
          print("Area of the Rectangle : ", area_rectangle)
    elif choice_2 =="p":
        lenght = float(input("Input the length of the Rectangle:  "))
        breath = float(input("Input the breadth of the Rectangle: "))
        if lenght <=0 or breath<=0 :
          print("enter a valid input for the lenght")
        else:
          perimeter = 2 * (lenght + breath)
          print("Perimeter of the Rectangle : ", perimeter)
    else: 
        print("entered input for area and perimeter choser is wrong:(" )

#code to find area and perimter of triangle
def triangle():
    choice_2 = str(input("If you wanna calculate area enter 'a' if perimeter enter 'p': "))
    if choice_2 == 'a':
        height = float(input("Input the Value of the Height:"))
        base = float(input("Input the base of the triangle :"))
        if height <=0 or base<=0 :
          print("enter a valid input for the lenght")
        else:
          area_triangle = 0.5 * height * base
          print("Area of the Triangle : ", area_triangle)
    elif choice_2 == 'p':
        s1 = float(input("Input the lenght of the side 1 of a triangle:"))
        s2 = float(input("Input the lenght of the side 2 of a triangle:"))
        s3 = float(input("Input the lenght of the side 3 of a triangle:"))
        if s1 <=0 or s2<=0 or s3<=0 :
          print("enter a valid input for the lenght")
        else:
          perimeter_triangle = (s1 + s2 + s3)
          print("Area of the Rectangle : ", perimeter_triangle)
    else:
        print("entered input for area and perimeter choser is wrong:)")
        

#code to find area and circumference of a circle
def circle():
    choice_2 = str(input("If you wanna calculate area enter 'a' if circumference enter 'c': "))
    if choice_2 == 'a':
        radius = float(input("Input the Radius of The Circle :"))
        if radius<=0 :
          print("enter a valid input for the lenght")
        else:
          areacircle = math.pi * radius * radius
          print("Area of the Circle : ", areacircle)
    elif choice_2 == 'c':
        radius = float(input("Input the Radius of The Circle :"))
        if radius<=0 :
            print("enter a valid input for the lenght")
        else:
          circumference = 2 * math.pi * radius
          print("circumference of the Circle : ", circumference)
    else :
        print("entered input for area and perimeter choser is wrong:)")


#code to find area and perimter of a paralleolgram
def parallelgram():
    choice_2 = str(input("If you wanna calculate area enter 'a' if perimeter enter 'p': "))
    if choice_2 == 'a':
        height = float(input("Input the height of the parallelogram:"))
        base = float(input("Input the base of the parallelogram:"))
        if height<=0 or base<=0 :
            print("enter a valid input for the lenght")
        else:
          area = height * base
          print("Area of the Parallelogram is:", (area))
    elif choice_2 == 'p':
        s1 = float(input("Enter the lenght of one identical sides of the  Parallelogram:"))
        s2 = float(input("Enter the lenght of one identical sides of the  Parallelogram:"))
        if s1<=0 or s2<=0 :
            print("enter a valid input for the lenght")
        else:
          perimeter = 2 * (s1 + s2)
          print("Perimeter of the Parallelogram is :", (perimeter))
    else:
       print("entered input for area and perimeter choser is wrong:)")

  
#code for user inputs
shapes = ['square', 'circle', 'triangle', 'rectangle','parallelogram']

i=0
for shape in shapes:
  print(i, shape)
  i += 1
  
choice = int(input("What you want to Find? enter the name of the shape as above:  "))

#loop for shape chooser (are a and perimeter)
if choice == 0:
    clear()
    square()
elif choice == 1:
   clear()
   rectangle()
elif choice == 2:
   clear()
   triangle()
elif choice == 3:
   clear()
   circle()
elif choice == 4:
   clear()
   parallelgram()
try:
    shapes= None  
    while shapes is None:
         print(choice, "is not a number, please enter a valid number only".format(input=shapes))
         shapes = ['square', 'circle', 'triangle', 'rectangle','parallelogram']
         choice = int(input("What you want to Find? enter the name of the shape as above :  "))
except ValueError:
            print("{input} is not a number, please enter a number only".format(input=shapes))
    
      