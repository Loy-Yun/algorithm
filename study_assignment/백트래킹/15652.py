import sys

n, m = sys.stdin.readline().strip().split()
n = int(n)
m = int(m)

s = []

def findSequenceList(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        s.append(i)
        findSequenceList(i)
        s.pop()

findSequenceList(1)