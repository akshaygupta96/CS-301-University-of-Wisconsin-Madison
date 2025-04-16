#My name: Akshay Gupta
#Partner name: Sofia Noejovich

import random

def run_simulation():
  """Function takes the raw_input from the user for num_drinks and the distance Hobbes is from her home. It then randomly selects the hole position between Hobbes and her home. It calls the functions, get_level() and get_walk() and  updates Hobbes' position in a list until she reaches home or falles into the hole."""
  #pass
  value= int(raw_input("Enter random seed value:"))
  random.seed(value)
  num_drinks=int(raw_input('How many shots did Hobbes take?'))
  distance=int(raw_input('How Far is it to Hobbes home?'))
  hole_position=random.randint(1,distance-1)
  print ""
  print ""
  print "Hole position is", hole_position
  drunk_level=get_level(num_drinks)
  step_list=get_walk(drunk_level)
  print "Level is", drunk_level
  print "Step length is",step_list[0]
  print "Step pattern is", step_list[1], " forward and", step_list[2], "backward"

  current_position=0
  step_length= step_list[0]
  final_list=[0]
  while current_position!= hole_position and current_position!= distance and current_position<distance:
    forward_counter=0
    backward_counter=0
    while forward_counter< step_list[1]:
      step_direction=1
      current_position=update(current_position, step_direction, step_length)
      forward_counter=forward_counter+1
      final_list.append(current_position)
    while backward_counter<step_list[2]:
      step_direction=-1
      current_position=update(current_position, step_direction, step_length)
      backward_counter=backward_counter+1
      final_list.append(current_position)
  if final_list[-1]==hole_position:
    print ""
    print ""
    print "Oh no! Hobbes fell near the bar!"
  else:
    print ""
    print ""
    print "Hurray! Hobbes makes it through the day!"
  return final_list






def get_level(num_drinks):
  """Function takes number of the number of shots Hobbes took and returns the inebriation level based on alcohol_list."""
  alcohol_list=[2,5,8,11]
  counter=0
  while counter<len(alcohol_list):
    if num_drinks<=alcohol_list[counter]:
      return counter
    counter=counter+1
  return 4


def get_walk(drunk_level):
  """Function returns step_length, a random number from 1 to 5 based on the drunk_level; the forward steps (a random number from 1-4); the backward steps (a random number from 1 to 3) in a list, pattern."""
  step_length=random.randint(1,5-drunk_level)
  forward=random.randint(4,6)
  backward=forward - random.randint(1,3)
  pattern=[step_length, forward, backward]
  return pattern

def update(current_position, step_direction, step_length):
  """Function updates current_position by adding it to the step_direction*step_length"""
  return current_position + step_direction*step_length
  
if __name__ == "__main__":
  run_simulation()