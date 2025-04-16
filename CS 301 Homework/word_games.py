# My name: Akshay Gupta
# Partner: Sofia Noejovich

import random

#######################################################
#
# HI 301 STUDENTS! YOUR FUNCTIONS WILL GO UP HERE. :)
def most_repeated_letters(word_1):
  """This function takes the individual letters in a string and counts the number of times it is repeated in the string.
The function returns the number of times the most frequent letter repeats.
"""
  length = len(word_1)
  counter1=0
  current_max=-999
  while counter1 < length:
    a=word_1[counter1]
    b= word_1.count(a, 0, length)
    counter1=counter1+1
    if current_max<b:
      current_max=b
  return current_max

def has_equal_letters(word_2):
  """In this function, we took the individual letters of each stirng and converted it to lowercase to
simplify the function. We then compared each letter to each vowel and 
created a counter for vowels and if it wasn't a vowel we counted it as a constant. Then, if the counters were
 equal we said  it was True. If not we said it was False.
 """
  word_2 = str.lower(word_2)
  length1= len(word_2)
  word_counter=0
  constants=0
  vowels=0
  for word_counter in range (length1):
    a=word_2[word_counter]
    if a=="a":
      vowels=vowels+1
      word_counter=word_counter+1
    elif a=="e":
      vowels=vowels+1
      word_counter=word_counter+1
    elif a=="i":
      vowels=vowels+1
      word_counter=word_counter+1
    elif a=="o":
      vowels=vowels+1
      word_counter=word_counter+1
    elif a=="u":
      vowels=vowels+1
      word_counter=word_counter+1
    else:
      constants=constants+1
      word_counter=word_counter+1
  if vowels==constants:
    return True
  else:
    return False

def is_palindrome(word_3):
  """In this function, we created a loop that compared the first letter of a word to the last letter of a word and continued 
until the word reached the middle. If the words at any point were not equal, it would turn the statement False."""
  length= len(word_3)
  counter1=0
  while counter1<length:
    if word_3[counter1]== word_3[-1-counter1]:
      counter1=counter1+1
    elif word_3[counter1]!= word_3[-1-counter1]:
      return False
  return True

def total_points(word):
  """Here we combined the functions by turning out functions into variables with the provided input. Based on the answers of each 
functions, we created if statements that would amount to certain amounts of points."""
  starting_points=len(word)
  repeated_letter_points= most_repeated_letters(word)
  equal_letter_points=has_equal_letters(word)
  palindrome=is_palindrome(word)
  if repeated_letter_points >= 3:
    e=starting_points*(1.0/3.0)
  elif repeated_letter_points==2:
    e=starting_points*(2)
    #print e
  elif repeated_letter_points==1:
    e= starting_points*(1)
  if equal_letter_points is True:
    f=2*e
  elif equal_letter_points is False:
    f=e
    #print f
  if palindrome == True:
    g=f*5
  elif palindrome == False:
    g=f
  return int(g)

def is_trick_round(p1_word,p2_word):
  """In this function we created two loops that counted the number of y's in each function. Then we combined the counts 
and created conditions to make the even number of y's false and the odd number of y's even"""

  p1_word_length=len(p1_word)
  p2_word_length=len(p2_word)
  word_counter1=0
  word_counter2=0
  number_of_y1=0
  number_of_y2=0
  for word_counter1 in range (p1_word_length):
    x=p1_word[word_counter1]
    if x=='y':
      number_of_y1=number_of_y1+1
      word_counter1=word_counter1+1
  for word_counter2 in range (p2_word_length):
    x=p2_word[word_counter2]
    if x=='y':
      number_of_y2=number_of_y2+1
      word_counter2=word_counter2+1
  total_y=number_of_y1 + number_of_y2
  if total_y%2==0:
    return False
  else:
    return True
#	
#######################################################



#######################################################
#
# EVERYTHING BELOW THIS IS HOBBES' CODE; MODIFY AT YOUR OWN RISK.
#
#######################################################

def get_computer_play():
    """
    Chooses a random word from this list of ridiculous English words and returns it
    """
    return random.choice(['Ailurophile', 'Assemblage', 'Becoming', 'Beleaguer', 
                          'Brood', 'Bucolic', 'Bungalow', 'Chatoyant', 'Comely', 
                          'Conflate', 'Cynosure', 'Dalliance', 'Demesne', 'Demure', 
                          'Denouement', 'Desuetude', 'Desultory', 'Diaphanous', 
                          'Dissemble', 'Dulcet', 'Ebullience', 'Effervescent', 
                          'Efflorescence', 'Elision', 'Elixir', 'Eloquence', 
                          'Embrocation', 'Emollient', 'Ephemeral', 'Epiphany', 
                          'Erstwhile', 'Ethereal', 'Evanescent', 'Evocative', 
                          'Fetching', 'Felicity', 'Forbearance', 'Fugacious', 
                          'Furtive', 'Gambol', 'Glamour', 'Gossamer', 'Halcyon', 
                          'Harbinger', 'Imbrication', 'Imbroglio', 'Imbue', 
                          'Incipient', 'Ineffable', 'Ingenue', 'Inglenook', 
                          'Insouciance', 'Inure', 'Kayak', 'Labyrinthine', 
                          'Lagniappe', 'Lagoon', 'Languor', 'Lassitude', 'Leisure', 
                          'Lilt', 'Lissome', 'Lithe', 'Love', 'Mellifluous', 
                          'Moiety', 'Mondegreen', 'Murmurous', 'Nemesis', 'Numbered',
                          'Offing', 'Onomatopoeia', 'Opulent', 'Palimpsest', 
                          'Panacea', 'Panoply', 'Pastiche', 'Penumbra', 'Petrichor', 
                          'Plethora', 'Propinquity', 'Pyrrhic', 'Python', 
                          'Quintessential', 'Ratatouille', 'Ravel', 'Redolent', 
                          'Riparian', 'Ripple', 'Scintilla', 'Sempiternal', 'Seraglio', 
                          'Serendipity', 'Summery', 'Sumptuous', 'Surreptitious', 
                          'Susquehanna', 'Susurrous', 'Talisman', 'Tintinnabulation', 
                          'Umbrella', 'Untoward', 'Vestigial', 'Wafture', 
                          'Wherewithal', 'Woebegone'])

def play_game():
    """
    Runs the word game, user vs computer, using your functions.
    Will not work until you have them implemented correctly!
    """
    cutoff = 30       # CHANGE THIS IF YOU WANT A LONGER GAME!
    user_total = 0
    comp_total = 0

    print "First to", cutoff, "points wins!"
    print

    while user_total < cutoff and comp_total < cutoff:

        # get the user and computer words, convert to lower case
        user_word = raw_input("Your play:").lower()
        comp_word = get_computer_play().lower()
        print "Computer played", comp_word

        # calculate user and computer scores
        user_score = total_points(user_word)
        print "User score:", user_score
        comp_score = total_points(comp_word)
        print "Computer score:", comp_score

        # check whether this was a trick round, and score appropriately
        # round winner's score is added, round loser's score is subtracted
        is_trick = is_trick_round(user_word, comp_word)
        if is_trick:
            print "TRICK ROUND!"
        if (is_trick and user_score < comp_score) or (not is_trick and user_score > comp_score):
            print "You win!"
            user_total += user_score
            comp_total -= comp_score
        elif (is_trick and user_score > comp_score) or (not is_trick and user_score < comp_score):
            print "You lose!"
            user_total -= user_score
            comp_total += comp_score
        else:
            print "You tie!"
        
        # display current score totals
        print "Current scores:"
        print "\tYou:", user_total
        print "\tComputer:", comp_total
        print

    # display overall winner
    print "Game over:",
    if comp_total > user_total:
        print "Computer wins!"
    else:
        print "You win!"

if __name__ == "__main__":
    play_game()
