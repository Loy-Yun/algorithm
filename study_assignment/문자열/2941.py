import sys

# 런타임에러
terms = sys.stdin.readline().strip()
words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

def find(terms, count):
    if len(terms) == 1:
        return count + 1
    elif len(terms) == 2:
        return count + 1 if terms[0:2] in words else count + 2
    elif terms[0:2] in words:
        return find(terms[2:], count + 1)
    elif terms[0:3] in words:
        return find(terms[3:], count + 1)
    else:
        return find(terms[1:], count + 1)

print(find(terms, count))

# 참고
x = input()
y = len(x)
cro_al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in range(0, len(x)):
    if len(x) < 2:
        y = len(x)
    elif len(x) == 2:
        if (x[i-2] + x[i-1]) in cro_al:
            y = 1
    elif (x[i-3]+x[i-2]+x[i-1]) in cro_al:
        y -= 2
    elif (x[i-2] + x[i-1]) in cro_al:
        y -= 1
print(y)