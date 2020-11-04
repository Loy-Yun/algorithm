n = int(input("입력할 숫자의 개수는?: "))
nlist = []

for i in range(n):
    nlist.append(int(input()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if nlist[j] < nlist[j-1]:
            nlist[j], nlist[j-1] = nlist[j-1], nlist[j]
        else: break

for i in nlist:
    print(i)
