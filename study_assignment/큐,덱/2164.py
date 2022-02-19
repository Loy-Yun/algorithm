import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([i for i in range(1, n+1)])

for i in range(n):
    if len(q) == 1:
        print(q[0])
        break
    q.popleft()
    if len(q) == 1:
        print(q[0])
        break
    q.append(q.popleft())
