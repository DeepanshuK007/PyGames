import pygame

x = pygame.init() 

#Creating Window
gameWindow = pygame.display.set_mode((1200, 500)) 
pygame.display.set_caption("My First Game")


#Game specific vars
exit_game = False 
game_over = False 

#Creating a game loop
while not exit_game: 
	for event in pygame.event.get(): #inside pygame.evnt.get() fetches all the event that are possible while the game runs
		print(event) #this will log all the events executed with I/O devices
		if event.type == pygame.QUIT:
			exit_game = True

		#if we want to detect which key is pressed 
		if event.type == pygame.KEYDOWN: #if key is pressed
			if event.key == pygame.K_RIGHT: #this line of code will only run if u have declared the type of event that is KEYDOWN
				print("You have pressed right arrow key")


		#now if the player presses the close button that event will also be handled in here

pygame.quit() #decativates the pygame lib
quit() #closes python