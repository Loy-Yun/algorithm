import sys

n = int(sys.stdin.readline().strip())
l = []
r = [0 for _ in range(n)]

for _ in range(n):
    l.append(sys.stdin.readline().strip().split())

for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        if int(l[i][0]) > int(l[j][0]) and int(l[i][1]) > int(l[j][1]):
            r[j] += 1
        elif int(l[i][0]) < int(l[j][0]) and int(l[i][1]) < int(l[j][1]):
            r[i] += 1

# 자기보다 큰 사람수 + 1 == 등수
for i in r:
    print(i+1, end=" ")
