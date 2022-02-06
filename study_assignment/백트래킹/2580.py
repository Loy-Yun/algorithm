# python 시간초과, pypy3 성공 -> find 3개를 한번에 해야 시간초과 안난다?
import sys
nums = []
for _ in range(9):
    nums.append(list(map(int, sys.stdin.readline().strip().split())))
blanks = []

for x in range(9):
    for y in range(9):
        if nums[x][y] == 0:
            blanks.append([x, y])
# nums 랑 blanks 방법 2
# sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
# zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
def findRow(x, i):
    if i not in nums[x]:
        return True
    else:
        return False

def findCol(y, i):
    if i not in map(lambda x: x[y], nums):
        return True
    else:
        return False

def findSq(x, y, i):
    x_range = x - x % 3
    y_range = y - y % 3
    for j in nums[x_range:x_range+3]:
        for k in j[y_range:y_range + 3]:
            if i == k:
                return False
    return True

def s(index):
    if index > len(blanks)-1:
        for num in nums:
            print(' '.join(map(str, num)))
        exit(0)
    x, y = blanks[index]
    for i in range(1, 10):
        if findRow(x, i) and findCol(y, i) and findSq(x, y, i):
            nums[x][y] = i
            s(index+1)
            nums[x][y] = 0  # 왜하지? - 초기화, 정답없을경우
s(0)