# My name: Akshay Gupta
# Partner: Sofia Noejovich

def menu(my_schedule):
  """This function displays a menu to the user. The user then selects one of the options in the menu by inputting the option number. Option 1 runs add_massage(my_schedule); option 2 runs view_schedule(my_schedule); option 3 runs cancel_massage(my_schedule); option 4 runs calculate_total(my_schedule); options 5 quits the program. If the input is not equal to 1-5, the function will prompt the user to select options 1-5 and run the menu function again."""
  print "Make a selection: \n 1. Add a massage to my schedule \n 2. View my current schedule \n 3. Cancel a massage from my schedule \n 4. Calculate fundraising total \n 5. Quit" #prints menu list
  x=raw_input("Your selection:") #asks for user input and equates it to x
  x=int(x) #defines x as an integer
  if x==1: #compares x to 1
    add_massage(my_schedule) #runs add_massage(my_schedule)
  if x==2: #compares x to 2
    view_schedule(my_schedule) #runs view_schedule(my_schedule)
  if x==3: #compares x to 3
    cancel_massage(my_schedule) #runs cancel_massage(my_schedule)
  if x==4: #compares x to 4
    calculate_total(my_schedule) #runs calculate_total(my_schedule)
  if x==5: #compares x to 5
    print "Goodbye!" #prints "Goodbye!"
    quit() #quits the program
  else: #if x is not equal to 1-5
    print "Menu options are 1-5." #prints "Menu options are 1-5."
    print "\n" #creates an empty line
    return menu(my_schedule) #returns to the main function


def add_massage(my_schedule):
  """This function prompts the user to input a number that corresponds to one of the massages. The function translates the string into an integer and based on the value of the integer, the boolean expressions will determine what should be appended to the string that represents the users schedule. If the user does not input a a number that corresponds to one of the prompts, the function will tell the user to choose an option provided (1-3) and then return to the menu option"""
  time=int(raw_input ("Add a (1) 15 minute, (2) 30 minute, or (3) 60 minute massage? ")) #the user inputs a string that  converted to an integer
  if time == 1: #compares the time to 1
    my_schedule.append("15 minute") #adds the string "15 minute" to the list my_schedule
  elif time == 2: #compares the time to 2
    my_schedule.append("30 minute") #adds the string "30 minute" to the list my_schedule
  elif time==3:#compares the time to 3
    my_schedule.append("60 minute") #adds the string "60 minute" to the list my_schedule
  else: #if time does not equal 1,2 or 3, the function goes to this boolean expression
    print "Add options are 1-3." #function prints the statement "Add options are 1-3."
  #print my_schedule
  print "\n" #creates an empty line
  return menu(my_schedule) #returns to the main function

def view_schedule(my_schedule):
  """This function displays the list, my_schedule, in the form of "'counter' : 'elements in the my_schedule'" to the user"""
  print "Your day contains:" #prints "Your day contains:"
  counter=0 #starts a counter at 0
  while counter<len(my_schedule): #begins while loop for the length of my_schedule
    print counter, ":" , my_schedule[counter] #prints 'counter' : 'element in the my_schedule'
    counter=counter+1 #increases value of counter by 1 so that the while loop works
  print "\n" #creates an empty line
  return menu(my_schedule) #returns to the main function

def cancel_massage(my_schedule):
  """ This function displays the schedule based on the users input using a while loop.If the length of the schedule is zero meaning the list is empty, it will display an error message and return to the menu. Otherwise, the function will proceed to obtain an input from the user and convert it to an intger. Using that integer, it passes through a boolean expression and if the integer is within the range of the length of the schedule, the integer will be the index that the user wants to remove from their schedule. The function will pop that value from the list and revise the schedule and return to the menu. """
  print "Your day contains:" #prints the expression "Your day contains:"
  counter=0 #starts a counter at 0
  if len(my_schedule)==0: # if the length of the counter is equal to zero meaning it is empty
    print "Unable to cancel a massage, no massages scheduled.\n" #prints the statement "Unable to cancel a massage, no massages scheduled." and creates a space
    return menu(my_schedule)# returns to the main function
  while counter<len(my_schedule): # begins the while loop for when counter is less than the length of the schedule
    print counter, ":" , my_schedule[counter] # prints the counter, ":" and corresponds the counter to the corresponding index in the list my_schedule
    counter=counter+1 #increases value of counter by 1 so that the while loop works
  removed_massage=int(raw_input("Which massage do you want to cancel?")) #asks the user which massage the user wants to remove and converts the string to an integer
  if removed_massage>=0 and removed_massage<=len(my_schedule)-1: # if the integer chosen is in the range of the index of the list, then the expression will proceed.
    my_schedule.pop(removed_massage) #the integer corresponds to an index and will remove that string from the list
  else: #if the user inputs a number outside the length of the string
    print "Unable to cancel a massage, no massages scheduled." #function prints the statement  "Unable to cancel a massage, no massages scheduled."
  print "\n" #creates an empty line
  return menu(my_schedule) #returns to the main function

def calculate_total(my_schedule):
  """This function calculates the total amount that the massages cost. $20 for a 15-minute massage, $30 for a 30-minute massage, $60 for a 60-minute massage. It takes the each element of the list, my_schedule to get the fundraising total."""
  cost=0 #defines cost as 0
  for element in my_schedule: #begins for loop for all the elements in my_schedule
    if my_schedule==[]: #if my_schedule is empty
      print "Your current total is $0" #prints "Your current total is $0"
    if element=='15 minute': #if an element in my_schedule is '15 minute'
      cost=cost+20 #adds 20 to the cost
    if element=='30 minute': #if an element in my_schedule is '30 minute'
      cost=cost+30 #adds 30 to the cost
    if element=='60 minute': #if an element in my_schedule is '60 minute'
      cost=cost+60 #adds 60 to the cost
  print "Your current total is $" + str(cost) #prints "Your current total is $" and cost
  print "\n" #creates an empty line
  return menu(my_schedule) #returns to the main function

if __name__ == "__main__": #when the program is running
  print "UW-Madison DPT Massage Fundraiser Scheduler\n" #prints "UW-Madison DPT Massage Fundraiser Scheduler" with an empty line
  my_schedule=[] #defines my_schedule as an empty list
  menu(my_schedule) #runs menu(my_schedule)