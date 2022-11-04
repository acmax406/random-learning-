#limits
import queue
stack = queue.LifoQueue(3)#putting the limits
stack.put(10)
stack.put(20)
stack.put(30)

print(stack.get())