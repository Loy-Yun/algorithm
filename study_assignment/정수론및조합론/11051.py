import sys
from math import factorial

n, k = map(int, sys.stdin.readline().split())

answer = factorial(n) // (factorial(k) * factorial(n - k))

if answer < 10007:
    print(answer)
else:
    print(answer % 10007)