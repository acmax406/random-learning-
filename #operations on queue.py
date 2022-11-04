#operations on queue
queue=[]
def enqueue():
    element=input("enter the elementt:")
    queue.append(element)
    print(element,"is added to queue!")
def dequeue():
    if queue==0:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("removed element:",e)
def display():
    if queue==0:
        print("queue is empty")
    else:
        print(queue)

while True:
    print("operations:")
    print("1.enqueue  2. dequeue  3.display")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice ==2:
        dequeue()
    elif choice==3:
        display()
    else:
        print("error!")