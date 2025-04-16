# My name: Akshay Gupta
# Partner: Sofia Noejovich

import random #imports random module

def generate_pokemon(names,powers):
  """This function takes the list of names and powers and picks a random name and power and in the dictionary pokemon assigns the random name and power to the keys 'name' and 'power'"""
  randname=random.choice(names) # picks a random name from the given list of names
  randpowers=random.choice(powers) #picks a random power from the given list of powers
  pokemon={'name': randname, 'power': randpowers, 'level': random.randint(1, 10)} #creates the dictionary pokemon assinging the key 'name' to the randname and the key 'power' to randpowers
  return pokemon #returns the dictionary pokemon


class Ditto:
	"""Defines the class, Ditto"""
	def __init__(self):
    """This function defines initial information about Ditto"""
    self.power=['absorb'] #defines self.power as a list
    self.count=0 #defines self.count as 0
    self.level=[1] #defines self.level as a list
    
	def get_level(self):
    """ This function computes the average of all the pokemon ditto (self) has absorbed so far"""
    average=(float(sum(self.level)))/(float(len(self.level))) #This takes the sum of all the values in self.level and turns it into a float so that python does not compute integer divison. It then divides it by the number of elements in the list to compute the average
    return average #returns average
  
	def should_absorb(self,pokemon):
     """This function checks if ditto's (self) level increases when ditto absorbs the new pokemon. If it does, True is returned. If not, False is returned."""
    average=self.get_level() #get current average from get_level(self)
    new_average= (float((sum(self.level))+pokemon['level']))/(float((1+len(self.level)))) #calculates new average by adding the new pokemon's level to the the total and increasing the number of values by 1
    if new_average>average: #if new_average is greater than average
      return True #function returns True
    else: #else
      return False #function returns False
      
	def absorb(self,pokemon):
    """This function adds on the self.level, self.power and number of pokemon absorbed (self.count) to ditto whenever called by appending self.level and self.power to the lists in ditto (self) and increasing the pokemon absorbed self.count by 1."""
    self.level.append(pokemon['level']) #adds new level to the list self.level in Ditto
    self.power.append(pokemon['power']) #adds new power to the list self.power in Ditto
    self.count=self.count+1 #adds 1 to self.count in Ditto
    
def take_walk(poke_list):
  """This function uses a while loop, to use the should absorb function to determine whether ditto should absorb the pokemon. It uses boolean expressions for if the ditto does not contain that power, it will absorb the pokemon despite the conditions of the should_absorb function. Then it returns the dictionary for ditto."""
  ditto=Ditto() #defines ditto as the the class Ditto
  counter1=0 #initialize counter
  while counter1<len(poke_list): #creates while loop for when counter1 is less than the length of the poke_list
    pokemon=poke_list[counter1] #pokemon is equal to each element in poke_list which is a list of dictionaries
    counter1=counter1+1 #increases the counter by 1 continues and the loop proceeds and ends
    if ditto.should_absorb(pokemon)==True: #if should_absorb(ditto,pokemon) return True
      ditto.absorb(pokemon) #runs absorb(ditto,pokemon)
    elif pokemon['power']not in ditto.power:# if one of the powers in the pokmeon's dictionary is not in ditto, it will run the absorb function
      ditto.absorb(pokemon) #runs function so that ditto absorbs the pokemon
  return ditto #returns dictionary for ditto
  
if __name__ == "__main__": #when program runs
  random.seed(100) #set random seed to 100
