def solution(numbers, hand):
    current = [3, 11]
    position = [1, 4, 7, '*', 2, 5, 8, 0, 3, 6, 9, '#']
    answer = []
    for n in numbers:
        index = position.index(n)
        if index // 4 == 0:
            answer.append('L')
            current[0] = index
        elif index // 4 == 1:
            l_dis = abs((current[0] % 4) - (index % 4))
            r_dis = abs((current[1] % 4) - (index % 4))
            if current[0] // 4 == 1:
                l_dis -= 1
            if current[1] // 4 == 1:
                r_dis -= 1
            if l_dis < r_dis:
                answer.append('L')
                current[0] = index
            elif l_dis > r_dis:
                answer.append('R')
                current[1] = index
            else:
                if hand == 'left':
                    answer.append('L')
                    current[0] = index
                else:
                    answer.append('R')
                    current[1] = index
        else:
            answer.append('R')
            current[1] = index
    return ''.join(answer)