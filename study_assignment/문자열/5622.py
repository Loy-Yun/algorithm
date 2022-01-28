import sys

terms = sys.stdin.readline().strip()
result = 0

for t in terms:
    if t == 'Z':
        result += 10
    elif ord(t) > 82:
        result += (ord(t)-66) // 3 + 3
    else:
        result += (ord(t)-65) // 3 + 3

print(result)