import sys

l = []
n = int(input())

for i in range(n):
    x = sys.stdin.readline().split()
    if x[0] == 'push':
        l.append(x[1])
    elif x[0] == 'pop':
        try:
            print(l.pop(0))
        except:
            print(-1)
    elif x[0] == 'size':
        print(len(l))
    elif x[0] == 'empty':
        print(1) if len(l) == 0 else print(0)
    elif x[0] == 'front':
        try:
            print(l[0])
        except:
            print(-1)
    elif x[0] == 'back':
        try:
            print(l[len(l)-1])
        except:
            print(-1)
