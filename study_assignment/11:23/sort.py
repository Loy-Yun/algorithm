import sys

n = int(sys.stdin.readline().rstrip())
l = []

for i in range(n):
    l.append(int(sys.stdin.readline().rstrip()))

for i in range(n):
    for j in range(n-i-1):
        if(l[j]>l[j+1]):
            l[j], l[j+1] = l[j+1], l[j]

###l.sort()
print("\n".join(map(str,l)))
