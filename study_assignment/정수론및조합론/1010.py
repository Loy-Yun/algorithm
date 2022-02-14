import sys

import math

n = int(input())

for _ in range(n):
    n, m = map(int, sys.stdin.readline().split())
    if n == m:
        print(1)
        continue
    else:
        print(int(math.factorial(m) // (math.factorial(n) * math.factorial(m - n))))