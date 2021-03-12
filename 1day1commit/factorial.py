def fac(n):
    if n == 1:
        return 1
    else: return n*fac(n-1)
    
num = eval(input("0보다 크거나 같은 숫자를 입력하세요: "));

if(num == 0): print(1);
else: print(fac(num));
