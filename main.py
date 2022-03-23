import math
def clear():
  print("\033[H\033[J", end="")

#code to find area and perimter of square
def square():
  l = float(input("Side of the Square :"))
  def area_1():
   area = l* l
   print("Area of the Square : ", area)

  def perimeter_1():
   perimeter=4*l
   print("Perimeter of the square:",perimeter)
  
  
#code to find area and perimeter of rectangle
def rectangle():
  length = float(input("Input the length of the Rectangle:  "))
  breath =float(input("Input the breadth of the Rectangle: "))
  def area_2():
    area_rectangle = length * breath
    print("Area of the Rectangle : ", area_rectangle)
  def perimeter_2():
    perimeter=2*( length + breath)
    print("Perimeter of the Rectangle : ", perimeter)

#code to find area and perimter of triangle
def triangle():
  def area_3():
   height = float(input("Input the Value of the Height:")) 
   base = float(input("Input the base of the triangle :"))
   area_triangle= 0.5 * height * base
   print("Area of the Triangle : ", area_triangle)
  def perimeter_3():
    s1= float(input("Input the lenght of the side 1 of a triangle:"))
    s2= float(input("Input the lenght of the side 2 of a triangle:"))
    s3= float(input("Input the lenght of the side 3 of a triangle:"))
    perimeter_triangle=s1+s2+s3
    print("Area of the Rectangle : ", perimeter_triangle)

#code to find area and circumference of a circle
def circle():
  radius = float(input("Input the Radius of The Circle :"))
  def area_4():
    areacircle =math.pi * radius * radius
    print("Area of the Circle : ", areacircle)
  def circumference_4():
    circumference =2*math.pi * radius
    print("circumference of the Circle : ", circumference)

  


#code to find area and perimter of a paralleolgram
def parallelgrom():
   def area_5():
     height = float (input("Input the height of the parallelogram:"))
     base=float (input("Input the base of the parallelogram:"))
     area=height*base
     print("Area of the Parallelogram is:",(area))
   def perimeter_5(): 
     s1=float(input("Enter the lenght of one identical sides of the  Parallelogram:"))
     s2=float(input("Enter the lenght of one identical sides of the  Parallelogram:"))
     perimeter= 2*(s1+s2)
     print("Perimeter of the Parallelogram is :",(perimeter))

#code for user inputs
print(" [ square, circle, triangle, rectangle,parallelogram ] ")
choice = str(input("What you want to Find?   "))

print(" [area or perimeter/circumference]")
choise_2 =str(input("????-"))
clear()
   
#loop for shape chooser and choice_2(are a and perimeter)
if choice == "square":
  square()
  if  choice_2 == "area":
      area_1()
  else:
    choice_2 == "perimeter":
    perimeter_1()

elif choice == "rectangle":
  rectangle()
  if choice_2 == " area":
    area_2()
  else:
    choice_2=="perimeter":
    perimeter_2()
  

elif choice == "triangle":
  triangle()
  if  choice_2 == " area":
    area_3()
  else:
    choice_2=="perimeter":
    perimeter_3()
  

elif choice == "circle" :
  circle()
  if  choice_2 == " area":
    area_4()
  else:
    choice_2=="perimeter":
    circumference_4()

elif choice == "parallelogram" :
  parallelgrom()
  if choice_2 == " area":
    area_5()
  else:
    choice_2=="perimeter":
    perimeter_5()


else:
   