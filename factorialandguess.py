def fact(n):
  if n == 1:
    return 1
  else:
    #n! = n*(n-1)* ... * 1
    #n! = n * (n-1)!
    return n * fact(n-1)
  
print fact(3)

#Guessing game
def game():
  print "guess"
  guess = raw_input()
  guess = int(guess)
  if 3 == guess: #Trick to make debugging easier
    print "Yay!"
  else:
    print "Boo"
    
print game()