import sys

n = int(input())
pyramid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for i in range(n-1, 0, -1):
    for j in range(i):
        pyramid[i-1][j] += max(pyramid[i][j], pyramid[i][j+1])

print(pyramid[0][0])