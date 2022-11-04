#proyarity queue
#value of the element itself as the priority  of the
#element OR
#take the element and it priority values as tuple
#if low value-> high priority then lowesst value will
#pop up first

#binary heap data structuree

import queue
q=queue.PriorityQueue()
q.put(10)
q.put(40)
q.put(70)
q.put(30)

print(q.get())