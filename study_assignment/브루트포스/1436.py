n = int(input())

if n == 1:
    print(666)
elif n == 2:
    print(1666)
else:
    num = 2665
    count = 2
    while True:
        if str(num).find('666') >= 0:
            count += 1
            if count == n:
                print(num)
                break
        num += 1