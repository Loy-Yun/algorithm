import sys

n = int(sys.stdin.readline())
res = []
for _ in range(n):
    res.append(int(sys.stdin.readline()))

for i in sorted(res):
    print(i)