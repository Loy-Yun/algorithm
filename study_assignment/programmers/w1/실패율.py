import sys

n = int(input())
s = sys.stdin.readline().strip().split()
for i in range(len(s)):
    s[i] = int(s[i])


def solution(N, stages):
    answer = {}
    count = len(stages)

    for i in range(1, N + 1):
        if count > 0:
            answer[i] = stages.count(i) / count
            count -= stages.count(i)
        else:
            answer[i] = 0

    return sorted(answer, key=lambda x: answer[x], reverse=True)

print(solution(n, s))