'''
날짜를 입력받아 요일을 구하시오
(단, 1일은 무조건 월요일이다. 7일은 일요일, 8일은 월요일
어떤 값을 입력을 받던 요일이 정확히 출력되야 함
'''

'''
day =(int)(input("날짜 입력 : "))

if day % 7 == 0: print("월요일")
if day % 7 == 1: print("화요일")
if day % 7 == 2: print("수요일")
if day % 7 == 3: print("목요일")
if day % 7 == 4: print("금요일")
if day % 7 == 5: print("토요일")
if day % 7 == 6: print("일요일")

'''



# 2. 입력한 데이터가 3의 배수인 경우에만 출력
'''
num = (int)(input("정수를 입력해주세요.:::"))

if(num % 3 == 0):
    print("출력완료.")
'''


#수를 입력받아 짝,홀수를 구분하여 출력하시오
'''
num = (int)(input("수를 입력하세요.:::"))

if(num % 2 == 0):
    print("짝수입니다.")
if(num % 2 != 0):
    print("홀수입니다.")
'''

#수를 입력받아 절대값을 출력하는 코드
'''
num = (int)(input("수를 입력하세요.:::"))

if(num > 0):
    print(num)
if(num < 0):
    num = num * -1
    print(num)
''' 

#두 수를 입력받아 큰 수만 출력
'''
n1 = (int)(input("첫 번째 수를 입력:::"))
n2 = (int)(input("두 번째 수를 입력:::"))

if(n1<n2):
    print(n2)
if(n1>n2):
    print(n1)
'''
#세 수를 입력받아 가장 큰수만 출력
'''
n1 = (int)(input("첫 번째 수를 입력:::"))
n2 = (int)(input("두 번째 수를 입력:::"))
n3 = (int)(input("세 번째 수를 입력:::"))

#if n1 >n2 and n1 > n3 :
if(n1<n2):
    if(n3<n2):
        print(n2)
if(n1>n2):
    if(n1>n3):
        print(n1)
if(n3>n1):
    if(n3>n2):
        print(n3)
'''
'''
n1 = (int)(input("첫 번째 수를 입력:::"))
n2 = (int)(input("두 번째 수를 입력:::"))

if n1<n2 and n1 % 2 ==0:
    print(n1)
    
if n1>n2 and n2 % 2 ==0:
    print(n2)
'''

'''
num1 = int(input("enter the num1 "))
num2 = int(int(input("enter the num2")))

if num1 > num2 :
    if num1 % 2 ==0:
        print(num1,"큰 수이면서 짝수")
else:
    if num2 % 2 == 0 and num2 != 0:ㅣ"))
'''



'''
num = int(input('enter the num:::'))
if num % 3 ==0:
    if num % 2 == 0:
        print(num, '3의 배수이면서 짝수 ')

'''



