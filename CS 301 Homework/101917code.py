a = [ 'a', 'b', 'c' , 'd']
for i in a :
  print i 

print"\n\n"

j = 0
for i in a: 
  print j, i 
  j = j + 1 


for j,i in enumerate(a):
  print j, i 

print"\n\n"

i = 0
while i < len(a): 
  print i, a[i]
  i = i+1
  
print"\n\n"

import random
a=[1,2,3,4]
a.reverse()
print a

a.pop(2)
a.insert(2,88)
print a

def reverse(my_list):
  my_list.reverse()
  print my_list.pop(1)
  my_list.insert(4,"hello")
  print my_list.pop() #last element in the list is popped
  return my_list
  
for i in range(10):
  print i #prints 1-9
  
  
print"\n\n\n\n"  
  
  
import random
a=[1,2,3,4,5,6,7,8,9,10]
my_list=[element**2 for element in a]
#print my_list

#my_list[0]=9
print a
print my_list


my_list=[random.randint(0,100) for i in range(1000)]
print my_list