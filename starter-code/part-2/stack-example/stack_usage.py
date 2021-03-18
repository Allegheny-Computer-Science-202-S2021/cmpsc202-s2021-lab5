'''
Please refer to the link below for more examples:
https://www.geeksforgeeks.org/stack-in-python/
'''

class stack_usage:
    def __init__(self,s):
        self.s = s
    def display(self,stack):
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


# Initialize the stack
stack_size = int(input("Enter the size of the stack:"))
stack = []
for i in range(stack_size):
    stack.append(i+1) #enqueue
obj = stack_usage(stack)
obj.display(stack)
print()