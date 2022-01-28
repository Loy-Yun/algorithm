text = input()

for alp in range(97, 123):
    if alp == 122:
        print(text.find(chr(alp)))
    else:
        print(text.find(chr(alp)), end=' ')