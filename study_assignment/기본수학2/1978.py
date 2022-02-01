import sys

n = int(input())
nl = sys.stdin.readline().strip().split()
count = 0

for num in nl:
    num = int(num)
    if num > 1:
        if num == 2:
            count += 1
        else:
            for i in range(2, num):
                if num % i == 0:
                    break
                elif i == num - 1:
                    count += 1

print(count)