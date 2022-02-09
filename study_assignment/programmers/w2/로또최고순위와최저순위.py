def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    correct = len(set(lottos) & set(win_nums))

    return [rank[correct + lottos.count(0)], rank[correct]]