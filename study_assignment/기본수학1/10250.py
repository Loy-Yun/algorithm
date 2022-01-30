import sys
import math

n = int(input())
tests = [[0, 0, 0] for i in range(n)]
for i in range(n):
    tests[i] = sys.stdin.readline().strip().split()

for test in tests:
    f = int(test[2]) % int(test[0]) if int(test[2]) % int(test[0]) > 0 else test[0]
    i = int(test[2]) // int(test[0]) + 1 if int(test[2]) % int(test[0]) > 0 else int(test[2]) // int(test[0])
    print(f, str(i).zfill(2), sep='')