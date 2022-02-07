result = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0]*91

n = int(input())
tests = [int(input()) for _ in range(n)]

max_test = max(tests)

if max_test > 10:
    for i in range(10, max_test):
        result[i] = result[i-3] + result[i-2]

for test in tests:
    print(result[test - 1])