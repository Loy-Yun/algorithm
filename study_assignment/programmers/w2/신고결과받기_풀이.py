def solution(id_list, report, k):
    # 신고 몇번 당했는지 기록하는 딕셔너리
    reported = {user: 0 for user in id_list}
    # 메일 몇 통 받는지, 기본값 0
    answer = [0 for _ in id_list]

    # 힌반에 한명만 신고 -> 중복 제거 필요
    for r in set(report):
        # 신고자, 신고 당한 사람
        req, res = r.split()
        # 당한 사람은 reported +1
        reported[res] += 1

    # k보다 신고 많이 받은 사람 필터
    blocked = dict(filter(lambda x: x[1] >= k, reported.items()))

    for r in set(report):
        req, res = r.split()
        # 신고 당한 사람이 정지 당한 경우
        if res in blocked:
            # 신고자 인덱스에 +1
            answer[id_list.index(req)] += 1

    return answer
