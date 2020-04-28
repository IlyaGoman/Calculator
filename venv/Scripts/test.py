from collections import deque

q = deque()
for i in range(10):
    q.appendleft(i)

q.popleft()
print(q)
