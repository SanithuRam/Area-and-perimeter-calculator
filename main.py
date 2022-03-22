               #---------------------MAIN------------------#

print("choose the shape you want to calculate area and perimeter")
#https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def clear():
  print("\033[H\033[J", end="")
#___________code to get area and perimeter of a rectangle_________________#
#https://www.code4example.cm/python/python-program-to-calculate-area-and-perimeter-of-rectangle/
rectangle=(input("Enter 'yes' if it is a rectangle or square  :"))
if rectangle== 'yes' : 
 clear()
 print("Calculating Area and Perimeter of a Rectangle-------------PLEASE ENTER LENGHT AND WIDTH OF THE RECTANGLE")
 l=int(input("Length : "))
 w=int(input("Width : "))
 area=l*w
 perimeter=2*(l+w)
 print("Area of Rectangle : ",area)
 print("Perimeter of Rectangle : ",perimeter)
else:

#----Code to find the area of a Triangle-------
#https://www.code4example.com/python/python-program-to-calculate-area-and-perimeter-of-triangle/
  triangle=(input("Enter 'yes' if it is a triangle :")) 
  if triangle== 'yes' :
     clear()
     print("Calculating Area and Perimeter of a Triangle-------------PLEASE ENTER HEIGHT AND BASE OF THE TRIANGLE")
  
     s1 = float(input("Enter the first side of the triangle : "))
     s2 = float(input("Enter the second side of the triangle : "))
     s3 = float(input("Enter the third side of the triangle : "))     
  
     b= float(input("Enter the base of the triangle:"))
     h= float(input("Enter the height of the triangle:"))
     perimeter= (s1 + s2 + s3)
     area = 0.5 * b * h
     print("The perimeter of the triangle is : {0:.2f}".format(perimeter))
     print("The area of the triangle is : {0:.2f}".format(area))
  else:

#____________code to fing area of the Circle______________

   circle=(input("Enter 'yes' if it is a circle: "))
   if circle == 'yes':
    clear()
    print("Calculating area and perimeter of a circle ------------PLEASE ENTER THE RADIUS OF THE CIRCLE")
    radius= float(input("Enter the radius of the circle:"))
    area=3.14*radius*radius
    perimeter=2*3.14*radius
    print("Area of Circle: ",(area))
    print("Perimeter of Circle: ",(perimeter))
   else:
  
  #-----Code to find area of a Parallelogram------
        
        paralgram=(input("Enter 'yes' if it is a parallelogram:"))
        if paralgram == 'yes':
          clear()
          print("Calculating area and perimeter of a parallelogram ------------PLEASE ENTER THE HEIGHT AND BASE OF THE PARALLELOGRAM")
          height=float(input("Enter the Height of the parallelogram:"))
          base=float(input("Enter the Base of thr parallelogram:"))
          s1=float(input("Enter the lenght of one identical sides of the  Parallelogram:"))
          s2=float(input("Enter the lenght of one identical sides of the  Parallelogram:"))
          area=height*base
          perimeter= 2*(s1+s2)
          print("Area of the Parallelogram is:",(area))
          print("Perimeter of the Parallelogram is :",(perimeter)) 
       
