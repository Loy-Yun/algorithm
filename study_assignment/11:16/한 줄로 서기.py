import sys

n = int(sys.stdin.readline().rstrip())

inl = sys.stdin.readline().split()
inl = list(map(int, inl))
outl = [n]

for i in reversed(range(n-1)):
    outl.insert(inl[i], i+1)

print(" ".join(map(str, outl)))
