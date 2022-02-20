import sys
from collections import deque

n = int(input())

for _ in range(n):
    count = 0
    ndoc, index = map(int, sys.stdin.readline().split())
    docs = deque(sys.stdin.readline().split())
    while docs:
        top = max(docs)
        index -= 1
        pop = docs.popleft()
        if top != pop:
            docs.append(pop)
            if index < 0:
                index = len(docs) - 1
        else:
            count += 1
            if index == -1:
                print(count)
                break