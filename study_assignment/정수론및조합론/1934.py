import sys

n = int(input())

for _ in range(n):
    n1, n2 = list(map(int, sys.stdin.readline().split()))

    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            print(n1*n2//i)
            break