n = int(input())
nl = []

if n > 1:
    if n == 2:
        print(2)
    else:
        for _ in range(n):
            if n == 1:
                break
            for i in range(2, n+1):
                if n % i == 0:
                    print(i)
                    n = int(n / i)
                    break