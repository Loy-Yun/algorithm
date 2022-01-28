import sys
a = int(sys.stdin.readline().split()[0])
n = [[0]*a for _ in range(a)]
for i in range(a):
    n[i] = sys.stdin.readline().split()
c = int(n[0][0])
sum = 0
index = 0

def sum_left():
    
for i in range(1, a):
    for x, j in n[i]:
        index += 1
    


print(c)
