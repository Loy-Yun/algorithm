def solution(lottos, win_nums):
    # 빵개 맞추면 6등
    rank = [6, 6, 5, 4, 3, 2, 1]
    # 확실한 값
    correct = len(set(lottos) & set(win_nums))
    # 최고등수: 확실한 값 + 0의 개수 / 최저등수: 확실한 값
    return rank[correct + lottos.count(0)], rank[correct]