# My name: Sofia Noejovich
# Partner: Akshay Gupta

def has_unique_letters(pw_1):
  length = len(pw_1)
  counter1=0
  counter2=0
  while counter1 < length:
    a=pw_1[counter1]
    counter1= counter1 +1
    counter2 = counter1
    while counter2 < length:
      b=pw_1[counter2]
      counter2= counter2 +1
      if a==b:
        return False
  return True


def has_even_vowels(pw_2):
  length1 = len(pw_2)
  password_iterator=0
  vowels = "aeiouAEIOU"
  length2 = len(vowels)
  vowel_iterator=0
  counter3=0
  while password_iterator<length1:
    a=pw_2[password_iterator]
    password_iterator = password_iterator+1
    #print "inside outer loop"
    #print a
    vowel_iterator = 0
    while vowel_iterator < length2:
      b=vowels[vowel_iterator]
      vowel_iterator= vowel_iterator +1
      #print vowel_iterator
      #print "inside inner while"
      #print a
      #print b
      if a==b:
        #print "inside if loop"
        counter3=counter3+1

  #print counter3
  if counter3%2>0:
    return False
  elif counter3%2==0:
    return True

def has_special_character(pw_3):
  length1 = len(pw_3)
  password_iterator=0
  special = "@#*$"
  length2 = len(special)
  special_iterator=0
  while password_iterator<length1:
    a=pw_3[password_iterator]
    password_iterator = password_iterator+1
    #print "inside outer loop"
    #print a
    special_iterator = 0
    while special_iterator < length2:
      b=special[special_iterator]
      special_iterator= special_iterator +1
      #print special_iterator
      #print "inside inner while"
      #print a
      #print b
      if a==b:
        #print "inside if loop"
        return True
  return False

def has_divisible_numbers(pw_4):
  length = len(pw_4)
  counter1=0
  while counter1 < length:
    a=pw_4[counter1]
    counter1= counter1 +1
    #print a
    if str.isdigit(a) is True:
      if int(a)%2!=0 and int(a)%3!=0:
        return False
  return True

def check_password(pw_5):
  if has_unique_letters(pw_5) is False:
    print "Warning! Please ensure letters are not repeated."
  if has_even_vowels(pw_5) is False:
    print "Warning! Please ensure password contains an even number of vowels."
  if has_special_character(pw_5) is False:
    print "Warning! Please ensure password contains at least one of {@, #, *, $}"
  if has_divisible_numbers(pw_5) is False:
    print "Warning! Please ensure all numbers are divisible by 2 or 3."
  if has_unique_letters(pw_5) is True:
    if has_even_vowels(pw_5) is True:
      if has_special_character(pw_5) is True:
        if has_divisible_numbers(pw_5) is True:
          print "Congratulations, your password meets our criteria."
  else:
    print "Sorry, your password does not meet our criteria."
  return

if __name__=="__main__":
  pw_5= raw_input ("Welcome to the Iron Bank of Braavos. Please set your password:")
  check_password(pw_5)