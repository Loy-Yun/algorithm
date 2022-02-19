import sys
from collections import deque

n = int(input())
q = deque([])

for _ in range(n):
    action = sys.stdin.readline().split()
    if action[0] == 'push':
        q.append(int(action[1]))
    elif action[0] == 'front':
        print(q[0] if q else -1)
    elif action[0] == 'back':
        print(q[-1] if q else -1)
    elif action[0] == 'pop':
        print(q.popleft() if q else -1)
    elif action[0] == 'size':
        print(len(q))
    elif action[0] == 'empty':
        print(0 if q else 1)