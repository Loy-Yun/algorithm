import sys

n = int(input())
price = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(3):
        prev = list(price[i-1])
        prev.pop(j)
        price[i][j] += min(prev)

print(min(price[n-1]))