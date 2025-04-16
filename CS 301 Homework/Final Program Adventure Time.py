# My name: Akshay Gupta
# Partner: Shreya Gaur

import numpy as np
import random

board=np.array([random.sample(range(1,26), 4), random.sample(range(1,26), 4), random.sample(range(1,26), 4), random.sample(range(1,26), 4)], int)
print board

board=board()
print board
x=0
y=0
def position(move,x,y):
  if move=="up":
    y-=1
  if move=="down":
    y+=1
  if move=="left":
    x-=1
  if move=="right":
	x+=1
  if move=="crunch":
	for a in range(1,board[x,y]):
		if board[x,y]%a!=0:
			board[x,y]=0
			print "Number CRUNCH!"
  
  player_postion=board[x,y]
  return player_postion