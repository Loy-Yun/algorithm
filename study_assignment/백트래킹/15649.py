import sys

n, m = sys.stdin.readline().strip().split()
n = int(n)
m = int(m)

def findSequenceList(sl):
    if len(sl) == m:
        print(' '.join(map(str, sl)))  # join 은 str 만 가능 -> map 으로 str 로 변경
    for i in range(1, n+1):
        if i not in sl:
            findSequenceList(sl + [i])

findSequenceList([])

# 두번째 방법 - 더 빠른듯?
s = []
def dfs():
    print(s)
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()