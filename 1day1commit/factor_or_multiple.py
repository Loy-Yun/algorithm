result=[]

while(True):
    n, m = input().split()
    n = int(n)
    m = int(m)
    if n==0 & m==0:
        break
    if n > m and n % m == 0:
        result.append('multiple')
    elif n < m and m % n == 0:
        result.append('factor')
    else:
        result.append('neither')

for i in result:
    print(i)
