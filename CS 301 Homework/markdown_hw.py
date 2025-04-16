# My name: Akshay Gupta
# Partner: Sofia Noejovich

def paragraph(line):
  """This function takes a line and puts a <p> at the front and </p> at the back."""
  return "<p>"+line+"</p>" #takes the stringes and adds them to the beginning and end of the line
  
def header(line):
  """This function if there are two #'s will put the combinations for H2 at the beginning and end of the line. If it one hastag, it will do this with h1."""
  if line[0]=="#" and line[1]=="#": #creates a boolean expression where the first element of the string is a # and the second is as well
    return "<h2>"+line.lstrip("# ")+"</h2>" #removes the hashtag and places <h2> in the front and </h2> at the end of the string
  if line[0]=="#": # if the first element of a line is a #
    return "<h1>"+line.lstrip("# ")+"</h1>" #removes the # and places </h1>

def em(line):
  """Converts emphasized text with a '*' and replaces it with '</em>' at the end of a line."""
  counter=0 #initializes a counter
  line_list=[] #creates empty list, line_list
  for elements in line: #initializes for loop for characters in line
    line_list.append(elements) #appends characters in line into line_list
    #print line_list
  for iterator in range(len(line_list)): #initializes for loop for line_list
    if line_list[iterator]=="*": #if line_list contains '*'
      counter=counter+1 #increase counter by 1
      if counter%2!=0: #if counter is not divisible by 2
        line_list[iterator]="<em>" #replaces "*" with "<em>"
      if counter%2==0: #if counter is divisible by 2
        line_list[iterator]="</em>" #replaces "*" with "</em>"
  return "".join(line_list) #returns the the elements of line_list as a string

def link(line):
  """This function is able to determine where the index is for the parantheses and bracket. Then,
      it is able to remove the link or words in the square brackets to create a new line with the necessary components."""
  count=0 #initialize counter
  counta=0 #initialize counter a
  countb=0 #initialize counter b
  countc=0 #initialize counter c
  countd=0 #initialize counter d
  for char in line: #initialize for loop for a character in the desired line
    count=count+1 # allow counter to continue so it iterates through each letter in a line
    if char=="(": # the character the loop is on is equal to "("
      counta=count-1 #gives the index of this character
    if char==")": # the character the loop is on is equal to ")"
      countb=count-1#gives the index of this character
    if char=="[":# the character the loop is on is equal to "["
      countc=count-1 #gives the index of this character
    if char=="]":# the character the loop is on is equal to "]"
      countd=count-1#gives the index of this character
  new_line= line[:countc-1]+" <a href=\""+line[counta+1:countb]+"\">"+line[countc+1:countd]+"</a>"+line[countb+1:] #Rewrites new_line as the HTML format of line.
  return new_line #returns new_line 
      

def convert(input_file, output_file):
  """This function takes a .md file and formats it into HTML format using the first four functions and creates a new file in the new HTML format."""
  in_file=open(input_file) #opens input_file for reading and defines it as in_file
  out_file=open(output_file,"w") #opens output_file and allows it to be edited and defines it as out_file
  for line in in_file.readlines(): #initializes for loop for lines in the in_file
    line=line.strip() #removes white spaces from line
    if line.find("*")!=-1: #if line contains "*"
      line=em(line) #runs the funciton em(line)
    if line.find("#")!=-1: #if line contains "#"
      line=header(line) #runs the function header(line)
    else: #if the if statements are false
      line=link(line) #runs the function link(line)
      line=paragraph(line) #runs the function paragraph(line)
    out_file.write(line+'\n') #writes new line into out_file
  in_file.close() #closes in_file
  out_file.close() #closes out_file
