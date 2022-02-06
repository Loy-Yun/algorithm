n = int(input())
tests = [int(input()) for _ in range(n)]

zero = [1, 0, 1]
one = [0, 1, 1]

def f(i):
    if i >= len(zero):
        for j in range(len(zero), i+1):
            zero.append(zero[j-1]+zero[j-2])
            one.append(one[j - 1] + one[j - 2])
    print(zero[i], one[i])

for test in tests:
    f(test)