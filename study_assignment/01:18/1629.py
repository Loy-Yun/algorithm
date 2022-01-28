import sys
a, b, c = map(int, sys.stdin.readline().split())
def mul(a, b):
    if b == 0: return 1
    elif b == 1: return a
    if b%2 == 0:
        return mul(a, b//2)*mul(a, b//2)%c
    else: return mul(a, b//2)*mul(a, b//2)*a%c
    
print(mul(a, b)%c)
