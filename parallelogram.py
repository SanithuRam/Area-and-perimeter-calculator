def parallelgram():
  choice_2=None
  answer=['a','p']
  while choice_2 not in answer :#while loop for area and perimeter chooser in parallelogram
        choice_2=str(input("Enter 'a' if you want to calculate area.   Enter 'p' if you want to calculate Perimeter. : "))
        if choice_2 not in answer:
          print("Select a-for area and , p- for perimeter")
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