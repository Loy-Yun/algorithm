import sys

n = int(input())
stairs = [int(sys.stdin.readline().strip()) for _ in range(n)]

# 틀림....
if n > 2:
    n -= 1
    while True:
        if n == 0:
            break
        if n == 1:
            stairs[0] += stairs[1]
            break
        if n >= 2:
            stairs[n - 2] = stairs[n] + max(stairs[n-1], stairs[n-2])
            n -= 2
            continue
    print(stairs[0])
else:
    print(sum(stairs))