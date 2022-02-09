def solution(id_list, report, k):
    reported = {user: 0 for user in id_list}
    answer = [0 for _ in id_list]

    for r in set(report):
        req, res = r.split()
        reported[res] += 1

    blocked = dict(filter(lambda x: x[1] >= k, reported.items()))

    for r in set(report):
        req, res = r.split()
        if res in blocked:
            answer[id_list.index(req)] += 1

    return answer