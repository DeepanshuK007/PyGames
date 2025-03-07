#In the last prog we used set mode to set the width and height.
"""But in here we will use diff variables for width and the height.
"""

import pygame
#We also need food for the snake, which will be at random places in the screen, this we can do using random pack
import random

pygame.init()

#bg Color Vars:
#We will use here rgb values in tuple which range from 0 -> 255
white = (255, 255, 255) #(==VIBGYOR)
red = (255, 0, 0)
black = (0, 0, 0)

#Creating a window
screen_width= 900
screen_height = 600
gameWindow= pygame.display.set_mode((screen_width, screen_height))

#Game Title
pygame.display.set_caption("Snakess")
pygame.display.update() #this func is uused when to update teh whole window

#Game specific variables
exit_game = False
game_over = False
gameWindow.fill(white)
snake_x = 45
snake_y = 55

score = 0

#We also need to give some velocity to our snake as we cant use the snakes pos to move the snake everytime.
velocity_x = 0
velocity_y = 0 #initially

#food at random coordinates
food_x = random.randint(20, screen_width-20)
food_y = random.randint(20, screen_height-20)

snake_size = 30 #snake shold look bigger than the food
fps = 20 #controls thhe speed of the snake
                                      

clock = pygame.time.Clock() #counts the time that has passed from the prev call

'''
Now we also neet ot move our sname for that we will use Clock class which is in time.py which has a tick func
time.py -> clock class -> tick()

tick() takes frame rate as an arg. It updates the frames acc to the frames we want per sec. 
When we press a key we want our snake to move with a cont speed, clock does that.
clock = pygame.time.Clock() 

'''


#Now we also want to showcase the score of the player on the gameWindow no tin the terminal
#So for that we will fiirst set the font
font = pygame.font.SysFont(None, 55)
#the SysFont methods first param is the font name which over here is default and the font size

#Now we need to display the text
def text_screen(text, color, x, y):
	screen_text = font.render(text, True, color)
	gameWindow.blit(screen_text, [x, y])

#now in this func to put the text we are taking text, color, and co-ordinates as args and then using render func which takes text, color, and antialias(bool) as argument.

#Then we are using "blit" means a logical operation in which a block of data is rapidly moved or copied in memory.


'''
Increasing snake length
#For this we will make 2 vars

'''
snk_list= [] #this is a list of lists and will ahve coordinates of the snakes rectangle
snk_length = 1 #this will have an int value and increment its value everytime our snake eats food

#Now we will make a func named plot snake. We will give it a list of coordinates(snk_list) and it will simply plot a rectangle on all those co-ordinates which will become our snake.

#With every loop we will add new coordinates to the snk_list var and it will pass those to the plot snake func to plot the squares.
def plot_snake(gameWindow, color, snk_list, snake_size):
	for x, y in snk_list:
		pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
#Just iterating the list and plotting its values

#Now as the snake moves its size will go on increasing as we are not deletionteh old rect and this will not make it look as if the snake is moving



#Game Loop
while not exit_game:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit_game = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				# snake_x = snake_x + 10 # moves the sq 10 pixs to the right
				velocity_x = 10
				velocity_y = 0 #also make sure that the snake doesnt move diagonally

			if event.key == pygame.K_LEFT:
				velocity_x = -10
				velocity_y = 0

			if event.key == pygame.K_UP:
				velocity_y = -10
				velocity_x = 0

			if event.key == pygame.K_DOWN:
				velocity_x = 0
				velocity_y = 10

	snake_x = snake_x + velocity_x #this increases the length
	snake_y = snake_y + velocity_y 

	#Now 2 things i) change food pos when eaten and ii)update score
	if abs(snake_x- food_x)<6 and abs(snake_x - food_x)<6:
		score += 1
		print ("Score: ", score * 10)
		food_x = random.randint(20, screen_width-20)
		food_y = random.randint(20, screen_height-20)


	#Now this func draws the box that is snake for each arrow press
	pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])		
	#The above func rect takes in arg such as platform, color, pos annd dimentions of a rec in a set
    
    text_screen("Score: " + str(score*10), red, 5, 5)

	#Draws random boxes
	pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size-10, snake_size-10])


	head = []
	head.append(snake_x)
	head.append(snake_y)
	snk_list.append(head)
 #append() method is used to add a new value in a dt 

 	if len(snk_length)>snk_list:
 		del snk_list[0]

	pygame.display.update()
	clock.tick(fps)

pygame.quit()
quit()