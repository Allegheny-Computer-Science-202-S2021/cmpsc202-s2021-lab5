import random
def generate(data,size):
    '''
        Data is prepared by inserting random values 
        between 1 and 100. Data items may be assumed to 
        be repeated. 
        Please refer to lab spec for the problem definiton.
    '''
    maximum = 100 # maximum weight of 300
    for i in range(0,size):
        data.insert(i,random.randint(1,maximum))

def getChildren(data, node):
    res = []
    # Add logic here to get all the childrens for the given node ...
    return res
def getParent(data, node):
    res = -1
    # Add logic here to get the parent for the given node ...
    return res

def getAncestors(data, node):
    # Get Ancestors #
    # develop a new method called recursive parent to get 
    # all the parents recursively. 
    # alternatively, you can also develop a formula to get all the 
    # ancestors. little bit tricky but doable. 
    res = []
    # Figure out the algorithm. 
    # Add required logic here, can be done mathematically 
    # or iteratively (programmatic).*/   
    return res
def getDescendents(data, node):
    # Get Decendents #
    res = []
    # develop a new method called recursive children to get 
    # all the childrens recursively. 
    # alternatively, you can also develop a formula to get all the 
    # descendents. little bit tricky but doable. 
    
    # Figure out the algorithm. 
    # Add required logic here, can be done mathematically or iteratively (programmatic).*/   
    return res
def findDepth(data, node):
    # Find Depth #
    res = 0
    # add required logic here */   
    return res

def findHeight(data, node):
    # Find Depth #
    res = 0
    # add required logic here */   
    return res

    
def isBalanced(data):
    # Check if the tree is balanced or not. #
    res = False
    # add required logic here #
    return res
    
# Assume binary tree, either complete or atmost complete.
# But not in-complete.   
data = []
size = int(input("Enter the no of items:")) # number of days provided by the user
generate(data,size)
print(f"Array:\t{data}")
# The lines below will print the output. Do not uncomment this lines. 
        
print("Welcome to the trees structure:")
while(True):
    print("------------------------------------------------")
    print("1 to get Children\n2 to get Parent \n" + "3 to get Ancestors \n4 to get Descendents \n" + "5 to get Depth \n6 to get Height \n7 to check balance")
    choice = int(input("Please make the following choice to get started:"))
    if (choice == 1):
        # Get children nodes 
        # node is the position no in the array
        node = int(input("Tell me the node no(pos - start from 0):"))
        children = getChildren(data, node)
        print(f"children:{children}")
            
    elif (choice == 2):
        # Get parent node 
        # node is the position no in the array
        node = int(input("Tell me the node no(pos - start from 0):"))
        parent = getChildren(data, node)
        print(f"parents:{parent}")
    elif (choice == 3):
        # Get ancestors
        # node is the position no in the array
        node = int(input("Tell me the node no(pos - start from 0):"))
        ancestors = getAncestors(data, node)
        print(f"Ancestors:{ancestors}")
    elif (choice == 4):
        # Get descendents
        # node is the position no in the array
        node = int(input("Tell me the node no(pos - start from 0):"))
        descendents = getDescendents(data, node)
        print(f"Descendents:{descendents}")
    elif (choice == 5):
        # Get depth
        # node is the position no in the array
        node = int(input("Tell me the node no(pos - start from 0):"))
        depth = findDepth(data, node)
        print(f"Depth:{depth}")
    elif (choice == 6):
        # Get height
        # node is the position no in the array
        node = int(input("Tell me the node no(pos - start from 0):"))
        height = findHeight(data, node)
        print(f"Height:{height}")
    elif (choice == 7):
        # Get balance status
        # node is the position no in the array
        node = int(input("Tell me the node no(pos - start from 0):"))
        status = isBalanced(data)
        print(f"Balance Status:{status}")
    else:
        print("Invalid choice. Please try again.")      
    print("------------------------------------------------")
    repeat = input("Do you want to try again? (y/n):")
    if (repeat == 'y'):
        continue
    else:
        break
data = []