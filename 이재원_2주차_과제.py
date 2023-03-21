# 1번
def sum(a, b):
    return a+b

# 2번
def sub(a, b):
    return a-b

# 3번
def mul(a, b):
    return a*b

# 4번
def div(a, b):
    return a/b

# 5번
def distance(x1, y1, x2, y2):
    a = (x1-x2)**2+(y1-y2)**2
    return a**(1/2)

# 6번
def title():
    lylics = "Switch sides and I'm beside you."
    return lylics[-11:-1]

# 7번
def reverseStr(string):
    return string[::-1]

# 8번
def introduce():
    name=input("이름을 입력하세요 :")
    hobby=input("취미를 입력하세요: ")
    school=input("재학 중인 학교를 입력하세요 :")
    birthday=input("생일을 입력하세요(ex.yymmdd) :")
    return "제 이름은 {0}입니다. 취미는 {1}입니다. 저는 {2}를 다니고 있습니다. 제 생일은 {3}월 {4}일 입니다.".format(name, hobby, school, birthday[2:4], birthday[4:])

# 9번
def calc():
    a=input("첫 번째 수를 입력하세요 :")
    b=input("두 번째 수를 입력하세요 :")
    a=int(a)
    b=int(b)
    return "두 수의 합 : {0}\n두 수의 차 : {1}\n두 수의 곱 : {2}\n두 수의 몫 : {3}".format(a+b, a-b, a*b, a//b)