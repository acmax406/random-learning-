#queue: open at both the end
#FIFO=first in first out
#LILo=last in last out
#same as standing in line to get the ticket
#enqueue: process of adding the element
#dequeue: process of deleting the element 
#isFUll, u=isEmpty
#queue can be impimeted using two way one with list and another with 
#different moduless
queue=[]#creation of empty list
queue.append(10)
queue.append(30)
queue.append(40)
print(queue)
print(queue.pop(0))#in queue pop(0) putting zero is impt as we are 
#removing the element fro the first elemnt of the list
#to insert any elemnt at initial
queue.insert(0,100)
#(0,100) 0 is location in list and 100 is the value assign to that loc
print(queue)
#to check the element at rear and front side
print(queue[-1])#at end
print(queue[0])#prints the initiial
