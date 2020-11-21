import random

# normal values
shape = (512, 512)	#The dimensions of the map

# The seed the program use to create maps
# If you wont to save a map, just save it's seed
seed = int(input("Insert de seed or 0 to create a random one: "))

if seed == 0:
	seed = random.randint(0, 99999999)
