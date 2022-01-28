a = int(input())

def factorial(n):
    if n == 2 or n == 1:
        return n
    elif n < 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(a))