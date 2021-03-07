from collections import deque

deq = deque('andré')
print(deq)

deq.append('w')
print(deq)
deq.appendleft('w')
print(deq)
print(deq.popleft())
print(deq)
