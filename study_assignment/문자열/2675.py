import sys

def repeat(test):
    result = ''
    for t in test[1]:
        result += t*int(test[0])
    return result

nTest = int(input())
rTest = [[] for i in range(nTest)]

for i in range(nTest):
    rTest[i] = sys.stdin.readline().split()

for test in rTest:
    print(repeat(test))