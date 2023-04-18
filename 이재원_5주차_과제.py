# your code 를 지우고 코드를 작성하세요.
# 5주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# result, answer 변수를 사용하여 문제를 풀이하세요. 반환값은 result나 answer 변수입니다.
# 제출 기한: 2023년 4월 17일 23시 59분
# 지각 제출 기한: 2023년 4월 18일 23시 59분
import math

def calcCircleArea(r):
    result = float()
    result = (r**2)*math.pi
    return round(result, 2)

def calcLog(a, b):
    result = float()
    if a == "e":
        result = math.log(int(b))
    else:
        result = math.log(int(b), int(a))
    return round(result, 2)

def calcSin(x):
    result = float()
    result = math.sin(x)
    return round(result ,2)

def calcFactorial(x):
    result = int()
    result = 1
    for i in range(2, x+1):
        result *= i
    return result

def calcCombination(n, r):
    result = int()
    result = 1
    for i in range(r):
        result *= (n-i) / (i+1)
    return result

def calculator(order):
    answer = 0
    f = order.split(" ")
    
    if f[0] == "원넓이:":
        r = int(f[1])
        answer = calcCircleArea(r)

    elif f[0] == "로그:":
        a = f[1] 
        b = f[2]
        answer = calcLog(a, b)
    
    elif f[0] == "사인:":
        x = int(f[1])
        answer = calcSin(x)
    
    elif f[0] == "팩토리얼:":
        x = int(f[1])
        answer = calcFactorial(x)
    
    elif f[0] == "조합:":
        n = int(f[1])
        r = int(f[2])
        answer = calcCombination(n, r)
    
    return answer