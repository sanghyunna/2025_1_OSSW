def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

if __name__ == '__main__':
    while True:
        try:
            print('enter first num')
            input1 = int(input("enter : "))
            break
        except ValueError:
            print('wrong input')
            continue

    while True:
        print('enter action')
        act = input("enter : ")
        if act in ['+','-','*','/']:
            break
        else:
            print('wrong action')
            continue

    while True:
        try:
            print('enter second num')
            input2 = int(input("enter : "))
            
            if act == '/' and input2 == 0:
                print('cannot divide by 0')
                continue
            else:
                break

            
        except ValueError:
            print('wrong input')
            continue

    if act == '+':
        result = plus(input1,input2)
    elif act == '-':
        result = minus(input1,input2)
    elif act == '*':
        result = mul(input1,input2)
    elif act == '/':
        result = div(input1,input2)
    else:
        print('wrong action')
        result = None

    print(f'result is {result}')


# 문제 1 : else 문이 없음
# 문제 2 : 0으로 나누는 경우를 처리하지 않음
# 문제 3 : 입력을 int화 하지 않음