import math

num = str(math.factorial(int(input())))
count = 0

for i in range(len(num)-1, -1, -1):
    if num[i] != '0':
        print(count)
        break
    else:
        count += 1
        continue