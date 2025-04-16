# My name: Akshay Gupta
# Partner: Shreya Gaur

import turtle #imports turtle module
import os #imports os
import math #imports math module
import random #imports random
wn=turtle.Screen() #sets up window
wn.bgcolor("black") #sets window color to black
wn.title("Space Invaders") #sets window title

if os.path.exists("space.gif"): #if file exists
    wn.bgpic("space.gif") #sets window background image as file

#sets up window size and borders and colors
border_pen=turtle.Turtle() #creates new turtle
border_pen.speed(0) #speed at which information is written
border_pen.color("white") #border color
border_pen.penup() #stops giving information about turtle
border_pen.setposition(-300,-300)
border_pen.pendown() #stops drawing
border_pen.pensize(3) #size of border
for side in range (4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle() #hides turtle

#adds score to the turtle window on the left
score=0 #sets score to 0
score_pen=turtle.Turtle() #creates new turtle
score_pen.speed(0) #speed at which information is written
score_pen.color("white") #sets font color to white
score_pen.penup() #stops drawing
score_pen.setposition(-290,280) #position of text in the windo
scorestring="Score: %s" %score #score string to be shown in window
score_pen.write(scorestring, False, align="left", font=("Arial",14, "normal")) #formats text
score_pen.hideturtle() #hides turtle

#adds remaining lives to the turtle window on the right
lives=3 #sets lives to 0
lives_pen=turtle.Turtle() #creates new turtle
lives_pen.speed(0) #speed at which information is written
lives_pen.color("white") #sets font color to white
lives_pen.penup() #stops drawing
lives_pen.setposition(290,280) #position of text in the window
livesstring="Lives Remaining: %s" %lives # lives string to be shown in window
lives_pen.write(livesstring, False, align="right", font=("Arial",14, "normal")) #formats text
lives_pen.hideturtle() #hides turtle


player=turtle.Turtle() #defines player as a turtle
player.color("blue") #player color
player.shape("triangle") #player shape
player.penup() #stops giving information about turtle
player.speed(0) #speed at which turtle is drawn
player.setposition(0, -250) #sets player position
player.setheading(90)

playerspeed=15 #number of pixels that the player moves at a time

number_of_enemies=5 #no. of enemies
enemies=[] #defines enemies as an empty list

for i in range(number_of_enemies): #for loop for the number of enemies
    enemies.append(turtle.Turtle()) #creates a new turtle for each enemy
    
for enemy in enemies: #for loop for each enemy in enemies
    enemy.color("red") #enemy color
    enemy.shape("circle") #enemy shape
    enemy.penup() #stops giving information about turtle
    enemy.speed(0) #speed at which turtle is drawn
    x=random.randint(-200,200) #sets random x coordinate
    y=random.randint(100,250) #sets random y coordinate
    enemy.setposition(x, y) #sets enemy position

enemyspeed=2 #number of pixels that the enemy moves at a time

bullet=turtle.Turtle() #defines bullet as a turtle
bullet.color("green") #bullet color
bullet.shape("square") #bullet shape
bullet.penup() #stops giving information about turtle
bullet.speed(0) #speed at which turtle is drawn
bullet.setheading(90)
bullet.shapesize(0.25, 0.25) #bullet size
bullet.hideturtle() #hides turtle

bulletspeed=20 #number of pixels that the bullet moves at a time
bulletstate="ready" #defines bulletstate as "ready"



def move_left():
    """defines a function when the player moves left and prevents the player from leaving the left border"""
    x=player.xcor() #defines x as the player's current x coordinate
    x-=playerspeed #subtracts x by the playerspeed
    if x<-280: #if x is less than -280
        x= -280 #define x as -280
    player.setx(x) #moves player to new x position
    
def move_right():
    """defines a function when the player moves right and prevents the player from leaving the right border"""
    x=player.xcor() #defines x as the player's current x coordinate
    x+=playerspeed #adds x by the playerspeed
    if x>280: #if x is more than 280
        x=280 #define x as 280
    player.setx(x) #moves player to new x position

def fire_bullet():
    """defines a function when the player fires a bullet"""
    global bulletstate #retrieves bulletstate variable from outside the function
    if bulletstate=="ready": #if bulletstate is "ready"
        bulletstate="fire" #define bulletstate as "fire"
        x=player.xcor() #defines x as the player's current x coordinate
        y=player.ycor()+10 ##defines y as the player's current y coordinate + 10
        bullet.setposition(x,y) #defines bullet position
        bullet.showturtle() #shows the bullet turtle
        if bullet.ycor()>275: #if bullet y coordinate in more than 275
            bullet.hideturtle() #hides turtle
            bulletstate="ready" #defines bulletstate as "ready"
        
def isCollision(t1,t2):
    """defines a funciton to check if t1 and t2 collide"""
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+(math.pow(t1.ycor()-t2.ycor(),2))) #calculates distance between t1 and t2
    if distance<15: #if distance is less than 15
        return True
    else:
        return False
    



turtle.listen() #allows keyboard keys to be assigned
turtle.onkey(move_left, "Left") #assigns the left arrow key to the move_left() function
turtle.onkey(move_right, "Right") #assigns the right arrow key to the move_right() function
turtle.onkey(fire_bullet, "space") #assigns the space bar to the fire_bullet() function

while True: #while program runs
    
    for enemy in enemies: #for each enemy in enemies list
        x=enemy.xcor() #defines x as the enemy's current x coordinate
        x+=enemyspeed #adds x by the playerspeed
        enemy.setx(x) #moves enemy to new x position
        
        if enemy.xcor()>280: #if enemy x coordinate is more than 280
            for enemy in enemies: #for each enemy in enemies list
                y=enemy.ycor() #defines y as the enemy's current y coordinate
                y-=30 #subtracts 30 from y
                enemy.sety(y) #moves enemy to new y position
            enemyspeed*=-1 #changes enemy direction
                
            
        if enemy.xcor()<-280: #if enemy x coordinate is less than -280
            for enemy in enemies: #for each enemy in enemies list
                y=enemy.ycor() #defines y as the enemy's current y coordinate
                y-=30 #subtracts 30 from y
                enemy.sety(y) #moves enemy to new y position
            enemyspeed*=-1 #changes enemy direction

        if enemy.ycor()<-300: #if enemy y coordinate is less than -300
            x=random.randint(-200,200) #sets random x coordinate
            y=random.randint(100,250) #sets random y coordinate
            enemy.setposition(x,y) #sets enemy position
            player.hideturtle() #hides turtle
            enemy.hideturtle() #hides turtle
            print("Game Over! The Aliens Have Invaded Earth") #prints "Game Over" message
            break #ends program

        if isCollision(bullet, enemy): #if isCollision(bullet, enemy) returns True
            bullet.hideturtle() #hides turtle
            bulletstate="ready" #defines bulletstate as "ready"
            bullet.setposition(0, -400) #sets bullet position
            x=random.randint(-200,200) #sets random x coordinate
            y=random.randint(100,250) #sets random y coordinate
            enemy.setposition(x,y) #sets enemy position
            score+=10 #adds 10 to score
            scorestring="Score: %s"%score #score string to be shown in window
            score_pen.clear() #removes old string
            score_pen.write(scorestring, False, align="left", font=("Arial",14, "normal")) #formats text
                        
        if isCollision(player, enemy): #if isCollision(player, enemy) returns True
            x=random.randint(-200,200) #sets random x coordinate
            y=random.randint(100,250) #sets random y coordinate
            enemy.setposition(x,y) #sets enemy position
            lives-=1 #decrases lives by 1
            livesstring="Lives Remaining: %s" %lives #lives string to be shown in window
            lives_pen.clear() #removes old string
            lives_pen.write(livesstring, False, align="right", font=("Arial",14, "normal")) #formats text
            if lives==0: #when there are no lives left
                player.hideturtle() #hides turtle
                enemy.hideturtle() #hides turtle
                print("Game Over! No More Lives.") #prints "Game Over" message
                break #ends program
    
    if bulletstate=="fire": #if bulletstate is "fire"
        y=bullet.ycor() #defines y as the bullets's current y coordinate
        y+=bulletspeed #adds bulletspeed to y
        bullet.sety(y) #moves bullet to new y position
                    
    if bullet.ycor()>275: #if bullet y posistion is more than 275
        bullet.hideturtle() #hides turtle
        bulletstate="ready" #defines bulletstate as "ready"


delay=raw_input("Press enter to finish") #defines delay so that game runs until user 
