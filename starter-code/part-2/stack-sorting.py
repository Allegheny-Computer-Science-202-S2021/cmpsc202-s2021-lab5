import random
def display(self,stack):
		# This method is used to display the stack contents. 
		# PS this method usage in stack-example folder.
        # If stack is empty then return  
        if (len(self.s) == 0): 
            return  
        x = self.s[len(self.s)-1]  
        # Pop the top element of the stack  
        self.s.pop()
        # Print the stack element starting  
        # from the bottom  
        print(f"{x} ",end="")
        # Recursively call the function PrintStack  
        self.display(stack)  
        # Push the same element onto the stack  
        # to preserve the order  
        self.s.append(x)
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