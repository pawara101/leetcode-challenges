## 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
## 0  1  2  3  4  5  6   7   8   9

def fib(n):
    num1 = 0
    num2 = 1
    if n<=1:
        if n == 0:
            ##print(num1)
            num2 = 0
        else:
            ##print(num2)
            num2 = 1
    else:
        for k in range(n-1):
            numNew = num1+num2
            ##print('Num New :',numNew)
            num1 = num2
            ##print('Num 1 :',num1)
            num2 = numNew
            ##print('Num 2 :',num2)

    return num2

print(fib(0))