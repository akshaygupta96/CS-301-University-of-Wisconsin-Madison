#if, if: both run!
#if, elif: If both conditions are true, still only first body runs; the second condition is not checked.
#NESTED if, if: If both conditions are true, both run! If the OUTER condition is FALSE, then neither runs.

x=3

if x>4:
	print "x is big!"
	if x<10:
		print "x is not too big!"
	print "outer if body ends here"
	
#-------------------------------------------------------------#
def checkage(age):
  if age >=21:
    print "They can drink"
    "They can vote"
    "They can drive"
  elif age>=18:
    print"They can vote"
    print "They can drive"
  elif age>=16:
    print "They can drive"
  else:
    print "They can't do anything!"
    
def checkage2(age):
  if age >=21:
    print "They can drink"
  if age >= 18:
    print "They can vote"
  if age  >=16:
    print "They can drive"
  if age <16:
    print "They can't do anything!"
    
def checkage3(age):
  if age >=16:
    if age>=18:
      if age >21:
        print "They can drink"
      print "They can vote"
    print "They can drive"
  else: print "They can't do anything!"

checkage(20)
checkage2(20)
checkage3(20)

#----------------------------------------------------#

def istriangle(a,b,c):
  if (a+b) > c:
    if (a+c) > b:
      if (b+c) > a:
        return "Valid"   
  return "Not valid"
        
print istriangle(3,5,7)