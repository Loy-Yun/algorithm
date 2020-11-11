import sys
word = sys.stdin.readline().split()
a = [0 for i in range(26)]

for i in word[0]:
    a[ord(i)-97] += 1

for i in a:
    print(i, end=" ")
