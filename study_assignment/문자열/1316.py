import sys

nTerms = input()
terms = ['' for i in range(nTerms)]
for i in range(nTerms):
    terms[i] = sys.stdin.readline().strip()
count = 0

for t in terms:
    if t == 'Z':
        count += 10
    elif ord(t) > 82:
        count += (ord(t)-66) // 3 + 3
    else:
        count += (ord(t)-65) // 3 + 3

print(count)