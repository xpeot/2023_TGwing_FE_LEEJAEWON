# 1번
def grade(score):
    if 100>=score>=90:
        grade="A"
    elif 90>score>=80:
        grade="B"
    elif 80>score>=70:
        grade="C"
    elif 70>score>=60:
        grade="D"
    else:
        grade="f"
    return grade

# 2번
def quadrant(x, y):
    if x>0 and y>0:
        quadrant="제 1사분면"
    elif x<0 and y>0:
        quadrant="제 2사분면"
    elif x<0 and y<0:
        quadrant="제 3사분면"
    elif x>0 and y<0:
        quadrant="제 4사분면"
    else:
        quadrant="어느 사분면에도 속하지 않습니다."
    return quadrant

# 3번
def leapYear(year):
    if year % 4 == 0 or year % 400 == 0:
        if year % 100 == 0:
            LY="윤년이 아닙니다."
        else:
            LY="윤년입니다."
    else:
        LY="윤년이 아닙니다."
    return LY

# 4번
def dice(a, b, c):
    if a==b==c:
        prize=(a*1000)+10000
    elif a==b: 
        prize=(a*100)+1000
    elif b==c:
        prize=(b*100)+1000
    elif c==a:   
        prize=(c*100)+1000
    else:
        prize=int(max(a,b,c))*100
    return prize

# 5번
def alarm(time):
    if 60>time>=0:
        t=time-45
        if t<0:
            t="23"+"시"+" "+str(60+t)+"분"
        else:
            "0시"+" "+str(t)+"분"
    elif 1000>time>=100:
        t=time-((time//100)*100)-45
        if t<0:
            t=str((time//100)-1)+"시"+" "+str(60+t)+"분"
        else:
            t=str(time//100)+"시"+" "+str(t)+"분"
    elif time>=1000:
        t=time-((time//100)*100)-45
        if t<0:
            t=str((time//100)-1)+"시"+" "+str(60+t)+"분"
        else:
            t=str(time//100)+"시"+" "+str(t)+"분"
    return t