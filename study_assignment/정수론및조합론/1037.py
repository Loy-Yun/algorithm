import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

if n % 2 == 0:
    print(nums[n//2]*nums[n//2-1])
else:
    print(nums[n//2]**2)