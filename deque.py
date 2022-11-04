#implemention of queue using differen calsses and modules
#deque->collection module
#   appendleft-> =========== <- append
#   popleft ->   =========== <- pop
import collections
q=collections.deque()#syntax deque
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)
print(q)
q.append(50)
print(q)
q.append(100)
print(q)
print(q.popleft())
print(q.pop())