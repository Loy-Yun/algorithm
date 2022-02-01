n = int(input())

def f(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return f(n-1)+f(n-2)

print(f(n+1))