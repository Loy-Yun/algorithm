# 소수 구하기 - 시간초과
import sys

start, end = sys.stdin.readline().strip().split()

for num in range(int(start), int(end) + 1):
    if num > 1:
        if num == 2:
            print(num)
        else:
            for i in range(2, int(num**0.5) + 1): # 제곱근 이하에 무조건 약수를 가진다
                if num % i == 0:
                    break
                elif i == int(num**0.5):
                    print(num)

# 참고코드
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)