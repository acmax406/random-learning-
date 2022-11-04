#linked list
#linear data structure
#it is chain of nodes
#elements of the list is called as the nodes
#dynamic data structure: as there is no need to metion
#the size of the list
#advantage:no mentions of size, insertion and deltion
#we can implement stack queue etc
#disadvantage: accessing randomly elements is not 
#possible, use extra memory
#===================================================
#single  linked list limplimentation
#===================================================
  
class Node:
    def __init__(self,data):#this mtd used to initialise the field of hte nodes
        self.data=data
        self.ref=None

node1=Node(10) #nodes is created and ref would be none as  |10|none|

print(node1)