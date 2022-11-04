#implementation of queue with Queue class/modules
#queue.Queue(maxsize=__)we can define the maximum size
#queue.size, queue.empty,queue.full,queue.put
#put(item,block=True,timeout)
#put-nowait(item)
#get(block=true, timeout=None)------get-nowait()
import queue
q=queue.Queue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)
print(q)
print(q.get())
