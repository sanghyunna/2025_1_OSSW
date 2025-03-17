def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

if __name__ == '__main__':
    print('enter first num')
    input1 = input("enter : ")

    print('enter action')
    act = input("enter : ")

    print('enter second num')
    input2 = input("enter : ")


    if act == '+':
        result = plus(input1,input2)
    elif act == '-':
        result = minus(input1,input2)
    elif act == '*':
        result = mul(input1,input2)
    elif act == '/':
        result = div(input1,input2)

    print(f'result is {result}')


# 문제 1 : else 문이 없음
# 문제 2 : 0으로 나누는 경우를 처리하지 않음
# 문제 3 : 입력을 int화 하지 않음