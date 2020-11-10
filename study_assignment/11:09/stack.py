import sys

def push(x) :
    l.append(x)

def size() :
    return len(l)

def empty() :
    return 1 if size() == 0 else 0

def pop() :
    try:
        print(l.pop())
    except: print(-1)

def top() :
    try:
        print(l[size()-1])
    except:
        print(-1)

l = []
n = int(input())

for i in range(n):
    act = sys.stdin.readline().split()
    if act[0] == 'push':
        push(int(act[1]))
    elif act[0] == 'pop':
        pop()
    elif act[0] == 'size':
        print(size())
    elif act[0] == 'empty':
        print(empty())
    elif act[0] == 'top':
        top()
