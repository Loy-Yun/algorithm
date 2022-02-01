start = int(input())
end = int(input())
nl = []

for num in range(start, end + 1):
    if num > 1:
        if num == 2:
            nl.append(num)
        else:
            for i in range(2, num):
                if num % i == 0:
                    break
                elif i == num - 1:
                    nl.append(num)

if len(nl) > 0:
    print(sum(nl))
    print(min(nl))
else:
    print(-1)