a = int(input()) - 1
count = 1

for i in range(2, a + 2):
    a = a - (6 * i) + 6
    count += 1
    if a <= 0:
        break

print(count)