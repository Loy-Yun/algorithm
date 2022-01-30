a = int(input())

for i in range(1, a + 1):
    if a <= i:
        b = i + 1 - a
        print("%d/%d" % (a, b)) if i % 2 == 0 else print(b, "/", a, sep='')
        break
    else:
        a = a - i