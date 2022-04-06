def triangle():
  choice_2=None
  answer=['a','p']
  while choice_2 not in answer :#while loop for area and perimeter chooser in triangle
        choice_2=str(input("Enter 'a' if you want to calculate area.   Enter 'p' if you want to calculate perimeter. : "))
        if choice_2 not in answer:
          print("Select a-for area and , p- for perimeter")
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
              perimeter_triangle = (s1 + s2 + s3)
              print("perimeter of the triangle : ", perimeter_triangle)
              break 