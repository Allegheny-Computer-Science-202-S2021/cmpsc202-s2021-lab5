import random
def generate(athletes,size):
	'''
        Data is prepared by inserting random values 
        between 150 and 300. Data items may be assumed to 
        be repeated. 
        Please refer to lab spec for the problem definiton.
    '''
	maximum = 300; # maximum weight of 300
	for i in range(0,size):
		athletes.insert(i,random.randint(150,maximum))
	
def start_sort(athletes):
	# Add your logic below to sort the list 
	# and store the final output in athletes.*/
	pass


athletes = []
size = int(input("Enter the no of athletes:")) # number of days provided by the user
generate(athletes,size)
print(f"unsorted:\t{athletes}")
start_sort(athletes)
print(f"sorted:\t\t{athletes}")

athletes = []