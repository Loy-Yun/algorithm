import sys

n = int(sys.stdin.readline())
res = [0]*10001

for _ in range(n):
    res[int(sys.stdin.readline())] += 1

for i in range(10001):
    if res[i] > 0:
        for j in range(res[i]):
            print(i)