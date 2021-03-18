import random
def generate(childrens,size):
	'''
        Data is prepared by inserting random values 
        between 1 - number of childrens.
        Please refer to lab spec for the problem definiton.
    '''
	for i in range(0,size):
		childrens.insert(i,i+1)
	random.shuffle(childrens)

def start_game(childrens):
	# Add your logic below to start the game 
    # and return the ID of the child who won. 
	winner = 0
	# your logic goes here ...
	return winner

children = []
size = int(input("Enter the no of children:")) # number of children provided by the user
steps = int(input("Enter the no of steps:")) # number of steps provided by the user
generate(children,size)
print(f"children:\t{children}")
print(f"no of steps:\t{steps}")
winner = start_game(children)
print(f"winner:\t{winner}")

children = []