import sys
# 틀림
n = int(input())

nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()

if len(nums) > 2 and nums[1] > nums[0]*2:
    for num in nums[2:]:
        if (num - nums[0]) % (nums[1]-nums[0]) != 0:
            break
        if num == nums[-1]:
            print(num-nums[0])

for i in range(2, nums[0]+1):
    isAnswer = True
    rest = nums[0] % i
    for num in nums[1:]:
        if num % i == rest:
            continue
        else:
            isAnswer = False
            break
    if isAnswer:
        print(i, end=" ")