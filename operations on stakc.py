stack=[] #defining the empty list
def push():
    element =  input("enter the element:")#entering element
    stack.append(element)
    print(stack)
def pop():
    if stack==0:
        print("there is nothing to pop")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)

while True:
    print("select the operation: ")
    print("1.push  2.pop  3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter the correct operation!")
        