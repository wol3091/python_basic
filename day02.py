'''
print("크게 정수하고 실수하고 문자열")
print(10,",",10.2,",""hello")

print("123 + 123= ",123+123,"입니다")
print("542 - 242= ",542-242,"입니다")
print("2 * 123= ", 2*123,"입니다")
print("120 / 3= ",120/3,"입니다")
'''
#주석 (comment)
#
'''
여러 줄 주석은 요론고
'''

#변수(Variable)
'''
(n1 = 10)
 =는 = n1 기준으로 10연산자의 값을 n1에 대입하는 뜻으로 사용된다.
'''
#변수명의 첫 문자는 반드시 밑줄(_)이나 영문자로 시작해야한다.
#변수명은 대문자나 소문자일 수 있으며,대소문자 구분
#python에서 이미 사용하고 있는 단어(예약어)는 변수명으로 사용 불가
#글자,숫자,밑줄 이외에 문자는 사용 불
# import keyword , keyword.kwlist 로 예약어 살펴볼 수 있다.

# 대입 
'''
num1 =5
num2 =3

Num1 = num1 +num2
Num2 = num1 -num2
Num3 = num1 *num2
Num4 = num1 /num2

print (Num1)
print (Num2)
print (Num3)
print (Num4)
'''        
#round()는 소수점 자리를 제어(반올림)할 수 있다. round(3.151351,2) = 3.15
#math()함수 .. ceil()은 무조건 올려 같거나 큰수 floor()은 무조건 내려 같거나 작은수 trunc()도 이하동문
'''
while True:
    print("***과목 합계,평균 계산기***")
    Python = (int)(input("파이썬 점수:"))
    C = (int)(input("C언어 점수:"))
    Java = (int)(input("java 점수:"))

    Sum = Python+C+Java
    avg = (int)(Sum/3)

    print("당신의 총 합계 점수는",Sum,"입니다")
    print("당신의 평균은",avg,"입니다.")

    if input("재검색 할래요?? yes or no :") == "no":
        break


while True:
    
    station = (int)(input("정류장 수:"))
    time = (int)(input("소요 시간:"))

    so= (int)(time/station)
    print(station,"역을",time,"분 걸렸음으로","한 역당 약",so,"분 걸렸습니다.")

    if input("도움이 됐나요?") == "yes":
        break;
'''

'''
#내 코
hotelfloor = 260
hotel1F = 500.23
Sum= (hotelfloor * 13) + hotel1F
meter =(int)(Sum/10)
print("호텔의 높이는",Sum,"cm이며",meter,"미터이다.")
'''
'''
#강사 코드
one =500.23
avg =260
cntfloor= 14

bh=avg*(cntfloor-1)+one
print("건물높이",round(bh/100,3),'m')
'''


'''
second= 60*60
result=second/11.27
meter = result*100
kilometer = meter/1000
print("총:",round(kilometer,2),"m")

'''

 




'''
import turtle as t
t.shape("turtle")
t.speed(10)

def multicircle(r, d):
    
    for x in range(0,4):
        
        if d > 1:

            t.right(180)
            multicircle(r/2, d-1)
            t.right(180)
        
        t.circle(r, 90)
 


while True:

    r=eval(input("radius?(0, 1, 2, 3, ...)"))
    d=eval(input("depth?(0, 1, 2, 3, ...)"))
    t.reset()

    if d != 0:
        multicircle(r, d)
    else:
        break   

t.mainloop()
'''



#문자열 두 개 입력 받는 함수 split() (공백 기준으로 받는다)
'''
a,b = input(" 두개 입력: ").split()

a= int(a)
b= int(b)

print(a + b)
'''
#map 함수는 자동 int,float 변환
'''
a, b = map(int, input('숫자 두 개를 입력:').split(','))

print(a+b)
'''

#입력값 받기 
'''

play = True
while play:

    x = (int)(input("Enter a number: "))
    y = (int)(input("Enter a number: "))

    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x % y)

    if input("Play again?(yes or no) :") == "no":
        play = False
        print("종료")
# play =false 로 break거는거 별로임


while True:
    x = (int)(input("Enter a number:"))
    y = (int)(input("Enter a number:"))
    z = (int)(input("Enter a number:"))

    print (x+y+z)
    print (x-y-z)
    print (x*y*z)
    print (x/y/z)

    if input("play again?") == "no":
        break
    
'''       
    

    
