'''
#print("입력:",end='')
n1 = int(input("입력:"))
#print("입력:",end='')
n2 = int(int(input("입력:"))
#print(type(n1))
#print(type(n2))
print(n1 + n2)
'''




#산술연산자(Operator)
# +, -, *, /, //(나누기,몫), %(나머지), **(제곱)
'''
n1=10; n2=3

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1//n2)
print(n1%n2)
print(n1**n2)
'''





#관계연산자
# <, >, <=, >=, ==, !=
'''
a=3.1; b=3
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)
'''

# 대입 연산자
# +=, -=, *=, /=, //=, %=, **=
'''
a=3; b=1

a += b# a = a+b
#a랑 b랑 더해서 덧셈의 결과를 첫번째 피연산자(a)에 저장해라 
print(a)
'''


'''
su1 = su2 = 5

su1 += 1
print("su1 + 1 = ",su1)

su1 -= 1
print("su1 - 1 = ",su2)

su1 *= su2
print("su1 * su2 = ",su1)

su1 //= su2
print("su1 // su2 = ",su1)

su1 %= su2
print("su1 % su2 = ",su1)
'''



#논리연산자
#and, or, not
'''
print(False or False)
print(False or True)
print(True or False)
print(True or True)



print(False and False)
print(False and True)
print(True and False)
print(True and True)

print(not True )

'''

'''
a = 10; b = 3

if a>b and b>c:
    print("종속문장1")
    print("종속문장2")
    if 조건식:
        print()
print("다음문장")
'''

print("정수를 입력하세요ㅜ:")
num = int(input())
if num % 2 ==0:
    print("짝수")
if num % 2 !=0:
    print("홀수")








