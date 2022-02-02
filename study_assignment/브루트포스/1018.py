import sys

n, m = sys.stdin.readline().strip().split()
blocks = [[] for _ in range(int(n))]
for i in range(int(n)):
    blocks[i] = sys.stdin.readline().strip()
result = int(n)*int(m)

for i in range(int(n)-7):
    for j in range(int(m)-7):
        r1 = r2 = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if blocks[k][l] == 'W':
                        r2 += 1
                    else:
                        r1 += 1
                else:
                    if blocks[k][l] == 'B':
                        r2 += 1
                    else:
                        r1 += 1
        result = min(result, r1, r2)
        if result == 0:
            break
    if result == 0:
        break

print(result)