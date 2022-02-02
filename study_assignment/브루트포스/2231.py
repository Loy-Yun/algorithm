import sys

n = int(sys.stdin.readline().strip())
result = 0

for i in range(1, n):
    sum = i
    for j in str(i):
        sum += int(j)
        if sum > n:
            break
    if sum == n:
        result = i
        break

print(result)