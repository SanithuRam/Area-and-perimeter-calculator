import math

def clear():
    print("\033[H\033[J", end="")

#code to find area and perimter of square
def square():
    valid = False
    while not valid:
      try: 
        choice_2=str(input("enter 'a' if you wanna calculate area and enter 'p' if you wanna calculate perimeter:  "))
        if choice_2 == 'a' :
          lenght = float(input("Side of the Square :"))
          if lenght <=0:
              print("enter a valid input for the lenght")
          else:
                 area = lenght * lenght
                 print("Area of the Square : ", area)
          break
        elif choice_2 == 'p':
              lenght_1 = float(input("Side of the Square :"))
              if lenght_1 <=0:
                  print("enter a valid input for the lenght")
              else:
                  perimeter = lenght_1 * 4
                  print("Perimeter of the square:", perimeter)
                  break
      except:
        print('Entered input invalid')
    
  
      
         

#code to find area and perimeter of rectangle
def rectangle():
    valid = False
    while not valid:
      try: 
        choice_2=str(input("enter 'a' if you wanna calculate area and enter 'p' if you wanna calculate perimeter:  "))
        if choice_2 =="a":
            lenght = float(input("Input the length of the Rectangle:  "))
            breath = float(input("Input the breadth of the Rectangle: "))
            if lenght <=0 or breath<=0 :
              print("enter a valid input for the lenght")
            else:
              area_rectangle = lenght * breath
              print("Area of the Rectangle : ", area_rectangle)
            break
        elif choice_2 =="p":
            lenght = float(input("Input the length of the Rectangle:  "))
            breath = float(input("Input the breadth of the Rectangle: "))
            if lenght <=0 or breath<=0 :
              print("enter a valid input for the lenght")
            else:
              perimeter = 2 * (lenght + breath)
              print("Perimeter of the Rectangle : ", perimeter)
              break
      except:
        print('Entered input invalid')

#code to find area and perimter of triangle
def triangle():
  valid = False
  while not valid:
      try: 
        choice_2=str(input("enter 'a' if you wanna calculate area and enter 'p' if you wanna calculate perimeter:  "))
    
        if choice_2 == 'a':
            height = float(input("Input the Value of the Height:"))
            base = float(input("Input the base of the triangle :"))
            if height <=0 or base<=0 :
              print("enter a valid input for the lenght")
            else:
              area_triangle = 0.5 * height * base
              print("Area of the Triangle : ", area_triangle)
            break
        elif choice_2 == 'p':
            s1 = float(input("Input the lenght of the side 1 of a triangle:"))
            s2 = float(input("Input the lenght of the side 2 of a triangle:"))
            s3 = float(input("Input the lenght of the side 3 of a triangle:"))
            if s1+s2>=s3 and s2+s3>=s1 and s3+s1>=s2 :
               continue
            else:
              print("Entered sides of the triangle show that its not a triangle,try again" )
            if s1 <=0 or s2<=0 or s3<=0 :
              print("enter a valid input for the lenght")
            else:
              perimeter_triangle = (s1 + s2 + s3)
              print("Area of the Rectangle : ", perimeter_triangle)
            break
      except:
        print('Entered input invalid')

#code to find area and circumference of a circle
def circle():
   valid = False
   while not valid:
      try: 
        choice_2=str(input("enter 'a' if you wanna calculate area and enter 'c' if you wanna calculate perimeter:  "))
    
        if choice_2 == 'a':
            radius = float(input("Input the Radius of The Circle :"))
            if radius<=0 :
              print("enter a valid input for the lenght")
            else:
              areacircle = math.pi * radius * radius
              print("Area of the Circle : ", areacircle)
            break
        elif choice_2 == 'c':
            radius = float(input("Input the Radius of The Circle :"))
            if radius<=0 :
                print("enter a valid input for the lenght")
            else:
              circumference = 2 * math.pi * radius
              print("circumference of the Circle : ", circumference)
            break
      except:
        print('Entered input invalid')


#code to find area and perimter of a paralleolgram
def parallelgram():
    valid = False
    while not valid:
      try: 
        choice_2=str(input("enter 'a' if you wanna calculate area and enter 'p' if you wanna calculate perimeter:  "))
    
        if choice_2 == 'a':
            height = float(input("Input the height of the parallelogram:"))
            base = float(input("Input the base of the parallelogram:"))
            if height<=0 or base<=0 :
                print("enter a valid input for the lenght")
            else:
              area = height * base
              print("Area of the Parallelogram is:", (area))
            break
        elif choice_2 == 'p':
            s1 = float(input("Enter the lenght of one identical sides of the  Parallelogram:"))
            s2 = float(input("Enter the lenght of one identical sides of the  Parallelogram:"))
            if s1<=0 or s2<=0 :
                print("enter a valid input for the lenght")
            else:
              perimeter = 2 * (s1 + s2)
              print("Perimeter of the Parallelogram is :", (perimeter))
            break
      except:
          print('Entered input invalid')

def int_check(question, err,low, high):
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
shapes = ['square', 'rectangle', 'triangle', 'circle','parallelogram']

i=0
for shape in shapes:
  print(i, shape)
  i += 1

choice = int_check("What you want to Find? enter the number of the shape as above :  ","please enter an interger ",0,4)
                 


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
else:
  print("brokmn")
    
    
      