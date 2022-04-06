import math
def circle():
  choice_2=None
  answer=['a','c']
  while choice_2 not in answer :#while loop for area and perimeter chooser in circle
        choice_2=str(input("Enter 'a' if you want to calculate area.   Enter 'c' if you want to calculate circumference. : "))
        if choice_2 not in answer:
          print("Select a-for area and , p- for perimeter")
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