import collections
stack=collections.deque()#deque=double ended que we can add the element
#at both the sides, it is use for to create the stack
#here we use the stack so use only one end to add or remove the element

print(stack)
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
print(stack.pop())
print(not stack)

import queue
stack = queue.LifoQueue()
stack.put(10)#here using put instead of push
stack.put(20)
stack.put(30)
stack.put(40)
print(stack)
