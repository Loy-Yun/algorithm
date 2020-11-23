import sys
d = []

def push_front(x):
    [x].extend(d)

def push_back(x):
    d.append(x)

def pop_front():
    try:
        return d.poplift()
    except:
        return -1

def pop_back():
    try:
        return d.pop()
    except:
        return -1

def size():
    return(len(d))

def empty():
    return 1 if len(d) == 0 else 0

def front():
    try:
        return d[0]
    except:
        return -1

def back():
    try:
        return d[size()-1]
    except:
        return -1

n = int(sys.sydin.readline())
for i in range(n):
    a = sys.sydin.readline().split()
    if a[0] == 'push_front':
        push_front(a[1])
    elif a[0]


    
