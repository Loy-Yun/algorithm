nNum = int(input())
a = input()

def sum(nNum, a):
    result = 0
    for i in range(nNum):
        result += int(a[i])
    return result

print(sum(nNum, a))
