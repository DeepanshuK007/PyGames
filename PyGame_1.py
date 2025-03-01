import pygame

x = pygame.init() #initializes the pygame module
# print(x)


#Creating Window
gameWindow = pygame.display.set_mode((1200, 500)) #this takes in a tuple as an input(width, height), display is a module in py
pygame.display.set_caption("My First Game")

#When u make a game the diff events associated with it. Such as start, end etc 

#Game specific vars
exit_game = False #this var will turn True idi anyone closes the game
game_over = False #this will turn True when the person has lost, and then give options such as iif they want to exit or continue or restart

#Creating a game loop
#What this does is that till the game is running it will take care of all the events that will run, such as when mouse pressed,
#when joystick is used
while not exit_game: 
	pass #this loop will go under an infinite while loop

pygame.quit() #decativates the pygame lib
quit() #closes python