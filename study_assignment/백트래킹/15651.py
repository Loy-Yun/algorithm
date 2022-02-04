import sys

n, m = sys.stdin.readline().strip().split()
n = int(n)
m = int(m)

s = []

def findSequenceList():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        s.append(i)
        findSequenceList()
        s.pop()

findSequenceList()