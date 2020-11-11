import sys
word = list(sys.stdin.readline().split()[0])
word2 = []
n = int(input())
c = len(word)

for i in range(n):
    x = sys.stdin.readline().split()   
    if x[0] == 'L':
        try:
            word2.append(word.pop())
        except: pass
    elif x[0] == 'D':
        try:
            word.append(word2.pop())
        except: pass
    elif x[0] == 'B' and c > 0:
        try:
            word.pop()
        except: pass
    elif x[0] == 'P':
        word.append(x[1])
        

print("".join(word+word2[::-1]))
