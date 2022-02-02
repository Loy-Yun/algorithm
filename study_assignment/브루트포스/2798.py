import sys

n, m = sys.stdin.readline().strip().split()
nl = sys.stdin.readline().strip().split()

result = 0

for i in range(len(nl)-2):
    for j in range(i+1, len(nl)-1):
        if int(nl[i]) + int(nl[j]) > int(m):
            continue
        for k in range(j+1, len(nl)):
            sum = int(nl[i]) + int(nl[j]) + int(nl[k])
            if sum > int(m):
                continue
            else:
                result = max(result, sum)

print(result)