# # your code 를 지우고 그 부분에 본인의 코드를 작성해주세요.
# 4주차 과제에는 출력이나 입력을 요구하는 문제가 없습니다. print(), input() 사용하지 마세요.
# 코드 실행 시 컴파일 에러, 런타임 에러가 발생하면 해당 문제 0점 처리하겠습니다.
# 함수 이름 변경하지 마세요. 변경 시 해당 문제 0점 처리 하겠습니다.
# 제출 기한 : 2023년 4월 10일 23시 59분
# 지각 제출 기한 : 2023년 4월 11일 23시 59분

# 1번
def double(lst):
    lst2=set(lst)
    for i in range(len(lst)):
        lst2.add(lst[i]*2)
    return len(lst)*2-len(lst2)

# 2번
def pascal(n):
    list1=[]
    for i in range(n):
      if i==0 or i==n-1:
           list1.append(1)
      else:
          N=1
          q=n-1
          b=i+1
          while b>1:
            N*=q
            q-=1
            b-=1
          M=1
          while i>0:
              M*=i
              i-=1
          list1.append(N//M)
    return list1

# 3번
def beerRefrigerator(n):
    x=float('inf')
    y=None

    for a in range(1, n+1):
        for b in range(a, n//a+1):
            if n%(a*b)==0:
                c=n//(a*b)
                z=2*(a*b+b*c+c*a)
                
                if z<x:
                    x=z
                    y=(f"{a} X {b} X {c}")
    
    return y

# 4번
def matrixMul(mat1, mat2):
    k= len(mat1[0])
    j= len(mat2[0])
    i= len(mat1)
    mat3=[]
    mat=[]
    o=0
    for m in range(i):
        for p in range(j):
            for n in range(k):
                o+=mat1[m][n]*mat2[n][p]
            mat.append(o)
            o=0
        mat3.append(mat) 
        mat=[]            
    return mat3

a= [[1,2], [3,4], [5,6]]
b=[[-1,-2,0], [0,0,3]]
print(matrixMul(a,b))
