def solution(board, moves):
    stack = []
    count = 0
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                stack.append(b[m-1])
                b[m-1] = 0
                break
        if len(stack) > 1:
            if stack[-2] == stack[-1]:
                count += 1
                del stack[-2:]
    return count*2