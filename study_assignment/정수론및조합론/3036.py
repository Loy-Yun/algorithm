import sys

n = int(input())
rings = list(map(int, sys.stdin.readline().split()))

for ring in rings[1:]:
    for i in range(ring, 0, -1):
        if ring % i == 0 and rings[0] % i == 0:
            print(rings[0]//i,"/",ring//i, sep='')
            break