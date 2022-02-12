import sys

n = int(input())
distance = list(map(int, sys.stdin.readline().split()))  # 거리
price = list(map(int, sys.stdin.readline().split()))  # 가격

# 1번 풀이(58점) - 가격순으로 정렬, 작은 가격 뒤로는 전부 무시
# answer = 0
# if n == 2 or max(price) == min(price):
#     print(sum(distance)*price[0])
# else:
#     sorted_price = sorted(price)  # 싼 순서로 정렬
#     before = n - 1
#
#     for p in sorted_price:
#         index = price.index(p)
#         if index > min(before, n-2):  # 마지막 인덱스는 노포함
#             continue
#         answer += sum(distance[index:before])*p
#         before = index
#
#     print(answer)

# 2번 풀이(100점) - 앞에서부터 반복문 돌려서 현재 가격과 앞선 가격중 가장 작은 가격을 비교해서 더해줌
min_price = price[0]
answer = price[0]*distance[0]
for i in range(1, n-1):
    if min_price > price[i]:
        min_price = price[i]
    answer += distance[i]*min_price

print(answer)