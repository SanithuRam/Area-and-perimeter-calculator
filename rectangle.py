def rectangle():
  choice_2=None
  answer=['a','p']
  while choice_2 not in answer :#while loop for area and perimeter chooser in rectangle
        choice_2=str(input("Enter 'a' if you want to calculate area.   Enter 'p' if you want to calculate perimeter. : "))
        if choice_2 not in answer:
          print("Select a-for area and , p- for perimeter")
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