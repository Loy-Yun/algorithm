import sys

num1, num2 = sys.stdin.readline().strip().split()

for i in range(3):
    if int(num1[2-i]) > int(num2[2-i]):
        print(num1[::-1])
        break
    elif int(num1[2-i]) < int(num2[2-i]):
        print(num2[::-1])
        break