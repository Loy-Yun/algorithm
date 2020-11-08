n = int(input())
t = list(map(int, input().split()))

sum = 0
t.sort()

for i in range(n):
    for j in range(i + 1):
        sum += t[j]
print(sum)
