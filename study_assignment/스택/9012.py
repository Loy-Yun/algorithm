import sys

n = int(input())

for _ in range(n):
    ps = sys.stdin.readline().strip()
    if ps[0] != '(' or ps[-1] != ')' or ps.count('(') != ps.count(')'):
        print('NO')
        continue
    while True:
        if len(ps) == 0:
            print('YES')
            break
        if ps.count('()') == 0:
            print('NO')
            break
        ps = ''.join(ps.split('()'))