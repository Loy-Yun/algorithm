n = int(input())

count = 0
# 틀림ㅡ,,ㅡ
for _ in range(n):
    if n == 1:
        print(count)
        break
    if sum(map(int, str(n))) % 3 == 0:
        n = n // 3
    elif int(str(n)[-1]) % 2 == 0:
        n = n // 2
    else:
        n -= 1
    count += 1