import sys
import math

a, b, v = sys.stdin.readline().strip().split()
a = int(a)
b = int(b)
v = int(v)

# 마지막날 올라갈거 먼저 빼주고 나눈다음 마지막에 하루 더해주기
print(math.ceil((v-a)/(a-b)) + 1)