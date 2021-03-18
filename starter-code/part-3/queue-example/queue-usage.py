'''
Please refer to the link below for more examples:
https://www.geeksforgeeks.org/queue-in-python/
'''
class queue_usage: 
    def __init__(self,q):
        self.q = q
    def display(self,q):  
        # If queue is empty then return  
        if (len(self.q) == 0): 
            return;  
        x = self.q[0]   # front element
        # Dequeue the front element from the queue  
        self.q.pop(0)  # dequeue
        # Print the queue element starting  
        # from the front 
        print(f"{x} ",end="")
        # Recursively call the function printQueue  
        self.display(q)  
        
#Initialize the queue
queue_size = int(input("Enter the size of the queue:"))
queue = []
for i in range(queue_size):
    queue.append(i+1) #enqueue
obj = queue_usage(queue)
obj.display(queue)
print()