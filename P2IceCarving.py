#My name: Akshay Gupta
#Partner name: Sofia Noejovich

import math
side = input("Enter side (in meters): ")
height = input("Enter pyramid height (in meters): ")

def cube_vol(side):
  side**3
print "volume of ice cube:", (side**3.0), "cubic meters"
  
def pyramid_vol(side, height):
  (side**2)*height*(1.0/3.0)
print "volume of pyramid:", (side**2)*height*(1.0/3.0), "cubic meters"

def ice_to_water(side, height):
  ((side**2)*height*(1.0/3.0) + side**3)*.92
print "A sculpture with side", side, "meters and total height", height, "meters requires:"
print ((side**2)*height*(1.0/3.0) + side**3)*.92 , "cubic meters of water"