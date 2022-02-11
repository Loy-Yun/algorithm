import re

expression = input()

operator = re.sub(r'[0-9]+', '', expression)  # 연산자
operand = list(map(int, re.split(r'[+,-]', expression)))  # 숫자

if operator.count('-') > 0:
    next = operator.index('-')+1
    answer = [sum(operand[:next])]  # 첫번쨰 - 전까지
    for i in range(operator.index('-')+1, len(operator)):
        if operator[i] == '-':
            answer.append(-sum(operand[next:i+1]))
            next = i+1
    answer.append(-sum(operand[next:]))
    print(sum(answer))
else:
    print(sum(operand))