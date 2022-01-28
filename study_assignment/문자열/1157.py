import sys

word = sys.stdin.readline().rstrip().upper()

if len(word) == 1:
    print(word)
else:
    result = dict.fromkeys(word)

    for w in result.keys():
        result[w] = word.count(w)

    result = [k for k,v in result.items() if max(result.values()) == v]
    print(result[0] if len(result) == 1 else "?")