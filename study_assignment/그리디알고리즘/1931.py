import sys

n = int(input())

meeting_time = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
meeting_time.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간이 빠른 순으로 정렬

count = 1
min_start = meeting_time[0][1]

for i in range(1, n):
    if min_start <= meeting_time[i][0]:  # 이전 값 끝나는 시간보다 시작시간이 큰 경우
        count += 1
        min_start = meeting_time[i][1]  # 최소 시작시간 업데이트

print(count)