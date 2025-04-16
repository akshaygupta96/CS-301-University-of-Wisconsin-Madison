#My name: Akshay Gupta
#Partner name: Sofia Noejovich

def cube_vol(side):
  return side**3.0
  
def pyramid_vol(side, height):
  return (side**2.0)*height*(1.0/3.0)

def ice_to_water(volume):
  return volume*.92
  
print "a sculpture with side 1.6m  and a total of 2m height requires:" 
print ice_to_water(cube_vol(1.6)+pyramid_vol(1.6,.4))
print "cubic meters of water"