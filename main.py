import math

def clear():
    print("\033[H\033[J", end="")

#code to find area and perimter of square
def square():
  choice_2=None
  answer=['a','p']
  while choice_2 not in answer :
        choice_2=str(input("Enter 'a' if you want to calculate area.   Enter 'p' if you want to calculate perimeter. : "))
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
        area = lenght * lenght
        print("Area of the Square : ", area)
        break
     
  
      
         

#code to find area and perimeter of rectangle
def rectangle():
  choice_2=None
  answer=['a','p']
  while choice_2 not in answer :
        choice_2=str(input("Enter 'a' if you want to calculate area.   Enter 'p' if you want to calculate perimeter. : "))
  if choice_2 == 'a' :
      while True:
        try:
          lenght = float(input("Input the length of the Rectangle:  "))
          breath = float(input("Input the breadth of the Rectangle: "))
        except:
          print('Please use numeric digits.')
          continue
        if lenght <= 0 or breath<=0 :
          print('Please enter a positive number.')
        else:  
           area_rectangle = lenght * breath
           print("Area of the Rectangle : ", area_rectangle)
           break



              
  elif choice_2 == 'p':
      while True:
        try:
          lenght = float(input("Input the length of the Rectangle:  "))
          breath = float(input("Input the breadth of the Rectangle: "))
        except:
          print('Please use numeric digits.')
          continue
        if lenght <= 0 or breath<=0 :
          print('Please enter a positive number.')
        else:  
            perimeter = 2 * (lenght + breath)
            print("Perimeter of the Rectangle : ", perimeter)
            break

#code to find area and perimter of triangle
def triangle():
  choice_2=None
  answer=['a','p']
  while choice_2 not in answer :
        choice_2=str(input("Enter 'a' if you want to calculate area.   Enter 'p' if you want to calculate perimeter. : "))
  if choice_2 == 'a' :
    while True:
        try:
          height = float(input("Input the Value of the Height:"))
          base = float(input("Input the base of the triangle :"))
        except:
          print('Please use numeric digits.')
          continue
        if height <= 0 or base<=0 :
          print('Please enter a positive number.')
        else:  
            area_triangle = 0.5 * height * base
        print("Area of the Triangle : ", area_triangle)
        break
            
  elif choice_2 == 'p':
        while True:
          try:
            s1 = float(input("Input the lenght of the side 1 of a triangle:"))
            s2 = float(input("Input the lenght of the side 2 of a triangle:"))
            s3 = float(input("Input the lenght of the side 3 of a triangle:"))
            triangle_validation = s1+s2>= s3 and  s2+s3>=s1 and  s3+s1>=s2
          except:
            print('Please use numeric digits.')
            continue
          if s1 <= 0 or s2<=0 or s3<=0 :
            print('Please enter a positive number.')
          elif triangle_validation==False:
              print("Sum of entered sides of the triangle show that its not a triangle" )
          else: 
              perimeter_triangle == (s1 + s2 + s3)
              print("perimeter of the triangle : ", perimeter_triangle)
   
              
              
  
#code to find area and circumference of a circle
def circle():
  choice_2=None
  answer=['a','c']
  while choice_2 not in answer :
        choice_2=str(input("Enter 'a' if you want to calculate area.   Enter 'c' if you want to calculate circumference. : "))
  if choice_2 == 'a' :
     while choice_2 not in answer :
        choice_2=str(input("Enter 'a' if you want to calculate area.   Enter 'p' if you want to calculate perimeter. : "))
  if choice_2 == 'a' :
    while True:
        try:
           radius = float(input("Input the Radius of The Circle :"))
        except:
          print('Please use numeric digits.')
          continue
        if  radius<=0 :
          print('Please enter a positive number.')
        else:  
          areacircle = math.pi * radius * radius
          print("Area of the Circle : ", areacircle)
        break
        
      
  elif choice_2 == 'c':
    while True:
      try:
           radius = float(input("Input the Radius of The Circle :"))
      except:
          print('Please use numeric digits.')
          continue
      if  radius<=0 :
          print('Please enter a positive number.')
    
      else:
        circumference = 2 * math.pi * radius
        print("circumference of the Circle : ", circumference)
      break
   

#code to find area and perimter of a paralleolgram
def parallelgram():
  choice_2=None
  answer=['a','p']
  while choice_2 not in answer :
        choice_2=str(input("Enter 'a' if you want to calculate area.   Enter 'p' if you want to calculate Perimeter. : "))
  if choice_2 == 'a' :
      while True:
       try:
          height = float(input("Input the height of the parallelogram:"))
          base = float(input("Input the base of the parallelogram:"))   
       except:
           print('Please use numeric digits.')
           continue
       if  height<=0 or base<=0  :
           print('Please enter a positive number.')
       else:
          area = height * base
          print("Area of the Parallelogram is:", (area))
       break
      
            
  elif choice_2 == 'p':
    while True:
       try:
         s1 = float(input("Enter the lenght of one identical sides of the  Parallelogram:"))
         s2 = float(input("Enter the lenght of one identical sides of the  Parallelogram:"))
          
       except:
           print('Please use numeric digits.')
           continue
       if  s1<=0 or s2<=0  :
           print('Please enter a positive number.')
       else:
           perimeter = 2 * (s1 + s2)
           print("Perimeter of the Parallelogram is :", (perimeter))
       break
        
     

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

    
    
      