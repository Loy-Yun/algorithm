import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().strip().split()))

dp = [[0, 0] for _ in range(n)]

for i in range(1, n-1):
    if nums[i-1] < nums[i]:
        dp[i-1][1] += 1
        dp[i][0] += 1

