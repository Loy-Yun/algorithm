import math
import sys

a, b, c = sys.stdin.readline().strip().split()
a = int(a)
b = int(b)
c = int(c)

if b == c or b > c:
    print(-1)
else:
    print(math.trunc(a / (c - b)) + 1)
