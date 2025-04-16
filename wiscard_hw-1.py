# My name: Akshay Gupta
# Partner: Sofia Noejovich

def calculate_total():
  student_faculty = raw_input ("(S)tudent or (F)aculty?")
  if student_faculty != 'S' and student_faculty != 'F':
    print "Invaild input. S or F only"
  elif student_faculty == 'S':
    dorm_resident = raw_input ("Dorm resident? (Y/N)")
    if dorm_resident == "Y":
      name1=calculate_food('S', True)
      name2= calculate_other()
      print "Total cost $" , name1 + name2
    if dorm_resident == "N":
      name1=calculate_food('S', False)
      name2= calculate_other()
      print "Total cost $" , name1 + name2
    if dorm_resident != "Y" and dorm_resident != "N":
      print "Invaild input. Y or N only"
  elif student_faculty == 'F':
    meal_plan = raw_input ("Meal plan? (Y/N)")
    if meal_plan == "Y":
      name1=calculate_food('F', True)
      name2= calculate_other()
      print "Total cost $" , name1 + name2
    if meal_plan == "N":
      name1=calculate_food('F', False)
      name2= calculate_other()
      print "Total cost $" , name1 + name2
    if meal_plan != "Y" and meal_plan != "N":
      print "Invaild input. Y or N only"
      
  

  

def calculate_food(user_type, gets_discount):
  price = raw_input ("Food cost? $")
  price = float(price)
  if user_type == 'S': 
    (price*.95)
    if gets_discount == True:
      return (price*.90)
    elif gets_discount == False: 
      return (price*.95)
  elif user_type == 'F':
    price*.95
    if gets_discount == True: 
      return (price*.80)
    elif gets_discount == False: 
      return (price*.95)
      
      
def calculate_other():
  cost = raw_input ("Non-food cost? $")
  cost = float(cost)
  return cost*1.055
  
calculate_total()