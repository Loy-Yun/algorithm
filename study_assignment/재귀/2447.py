# 다시 풀기
n = int(input())
start = ['***', '* *', '***']

def s(n: int) -> list:
    r = []
    if n == 1:
        return ['*']
    sl = s(n//3)

    for i in sl:
        r.append(i * 3)
    for i in sl:
        r.append(i + ' ' * (n//3) + i)
    for i in sl:
        r.append(i * 3)
    return r

print('\n'.join(s(n)))