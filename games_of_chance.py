import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet):
	side = random.randint(1, 2)
	
	if side == 1 and guess == "heads":
		print("It's heads you win")
	elif side == 2 and guess == "tails":
		print("It's tails you win")
	else:
		print("You lose")
	return side

#at the moment the function only takes in the guess of the player
# need to set up the bet system.


#Call your game of chance functions here
coin_flip("heads",10)
coin_flip("heads",10)
coin_flip("heads",10)
coin_flip("heads",10)
coin_flip("heads",10)
coin_flip("heads",10)
coin_flip("heads",10)
coin_flip("heads",10)
coin_flip("heads",10)
coin_flip("heads",10)

