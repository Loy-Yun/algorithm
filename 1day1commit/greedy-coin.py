n, m = input().split()
n = int(n)
m = int(m)

nlist = []
count = 0

for i in range(n):
    nlist.append(eval(input()))
    
nlist.sort(reverse=True)

for i in nlist:
    if m <= 0: break
    if i <= m:        
        x = m//i
        m = m - i*x       
        count+=x

print(count)
