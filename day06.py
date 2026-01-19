# su = 0
# while su <= 20:
#      su += 1
#      if su % 3 == 0:
#           continue
#      print(su)     
# if 1 <= hug <= 20 and hug % 3 != 0:
#     print('1부터 20까지 숫자 중 3의 배수이다.')
# else:
#     while True:
#           print('1부터 20까지 숫자 중 3의 배수가 아니다.')

# su = 0
# while su < 20:
#     su += 1
#     if su % 3 == 0:
#         pass
#     else:
#         print(su)

''' 
    무한 반복
    while문은 조건식이 거짓이 될 때 까지 동작하는 반복문
    그댈서 조건식이 거짓이 될 수 없다는 무한 반복이 발생
    (조건식을 사용하는 while문 작성 시 주의 사항)

    단, 필요에 따라서는 무한 반복 일부러 발생시키는
    코드를 작성해야 할 떄도 있다
    (ex. 프로글매 전체 틀 구성)  

    이 때는 while문 뒤에 조건식을 따로 작성하지 않고
    True라는 논리값을 직접 작성하여 쉽게 무한 반복을 만들 수 있다
     + 이 경우에는 무조건 break로 while문을 종료할 수 있도록
     코드를 작성해야 한다
'''

# a = 0
# while True:
#     print(a)
#     a += 1
    
# ''' 일반적으로 종료 조건을 제시하여 무한 반복을 빠져나온다 '''
# a = 0
# while True:
#     print(a)   
#     a += 1 
#     if a == 10:
#         break

# while True:
#     print('1. 커피\n2. 코코아\n3. 종료')
#     cho = int(input())
#     if cho == 1:
#         print('커피 한 잔 나옵니다')
#     elif cho == 2:
#         print('코코아 한 잔 나옵니다')
#     elif cho == 3:
#         print('프로그램 종료됩니다')
#         break
    
''' 무한 반복을 이용한 특정 데이터 입력 '''
# print('계속 하시겠습니까?(y/n)')
# while True:    
#     cho = input()
#     if cho in ('y', 'n', 'Y', 'N'):
#         break
#     else:
#         print('y와 n 중 하나만 입력하세요')
# print('--- 입력 결과 ---')
# print(cho)

# rice = 100000
# mouse = 2
#a = rice - mouse * 20


#print('창고의 쌀이 다 떨어지는데 걸리는 기간이 얼마일까??')
# day = 0
# while True: 
#     day = day + 1
#     a = rice - mouse * 20
#     if a <= 0:
#         break
#     if day % 10 == 0:
#         mouse = mouse * 2
# print(f'{day}일, {mouse}마리')

''' for문 '''
# ls = ['one', 'two', 'three']
# for i in ls:
#     print(i)
# print('다음 코드 진행')

# st = 'Have a nice day'
# for i in st:
#     print(i)

# a = {1, 2, 3}
# print(dir(a))

# a = [(1, 2), (3, 4), (5, 6)]
# for i, j in a:
#     print(i + j)

# dic = {1:'one', 2:'two', 3:'three'}
# for i in dic.keys():
#     print(f'{i} : {dic[i]}')
# print('-' * 20)
# for i, j in dic.items():
#     print(f'{i} : {j}')

# score = [90, 26, 67, 45, 88]
# number = 0

# for sc in score:
#     number += 1
#     if sc >= 60:
#         print(f'{number}번 학생은 합격입니다.')
#     else:
#         print(f'{number}번 학생은 불합격입니다.')

''' break문과 continue문도 for문 안에서 사용이 가능 '''
# a = [1, 2, 3, 4, 5]
# for su in a:
#     print(su)
#     if su == 3:
#         break

# score = [90, 26, 67, 45, 88]
# number = 0
# for sc in score:
#     number += 1
#     if sc < 60:
#         continue
#     print(f'{number}번 학생은 합격입니다.')

''' python의 for문은 범위로 range() 클래스의 객체를 자주 사용한다 '''
# print(range(1, 10, 1))
# print(list(range(1, 10, 1)))    
# for i in range(10, -1, -1):
#     print(i)

# for i in range(0, 11, 2):
#     print(i)

# score = [90, 26, 67, 45, 88]
# #number = 0
# for number in range(len(score)):
#     if score[number] < 60:
#         continue
#     print(f'{number + 1}번 학생은 합격입니다.')

''' 실습3* '''
#print(list(range(1, 100)))
# number = 0
# #add = 0
# for su in range(1, 101):
#     number += su
# print(number)

''' 다중 반복문(중첩 반복문) 
    반복 횟수에 따라 변수 데이터의 변경이 많이 달라진다

    기본적으로 전체 반복 횟수는 
        외부 반복 횟수 * 내부 반복 횟수
    가 되며, 결과적으로 내부 반복문의 코드가 많이 반복된다    
'''

# cnt = 0
# for line in range(1, 4):
#     print(f'{line}번째 줄')
#     for no in range(1, 6):
#         cnt += 1
#         print(f'{no} - 총 {cnt}회 동작')
#     print('xxxxxx')

# while True:
#     print('1. 실행\n2. 종료')
#     while True:
#         cho = int(input())
#         if cho in (1, 2):
#             break
#         else:
#             print('1, 2 중 하나 입력하세요!')
#         print()

#     if cho == 1:
#         print('프로그램이 이어서 ㄱㄱㄱ')
#     elif cho == 2:
#         print('프로그램이 종료됩니다!')
#         break

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i * j, end=' ')
#     print()

''' 실습4 '''

''' 1!! '''
# for i in range(5):
#     for j in range(1, 6):
#         print(f'{i * 5 + j}',end='\t')
#     print()

''' 2!! '''

# for i in range(1, 22, 5):
#     for j in range(5):
#         print(f'{i + j}',end='\t')
#     print()

''' 3!! '''

# for i in range(1, 22, 5):
#     for j in range(i, i+5):
#         print(f'{j}',end='\t')
#     print()

''' 실습5 '''
#a = 1
# #b = 10
# for a in range(1, 10):
#     print(f'--- {a}단 ---')
#     for b in range(1, 10):
#         print(f'{a} x {b} = {a * b}',end='\n')
#     print()

# a = 1
# while a < 10:
#     print(f'--- {a}단 ---')
#     b = 1
#     while b < 10:
#         print(f'{a} x {b} = {a * b}')
#         b += 1
#     a += 1
#     print()

# a = 1
# #b = 1
# while a < 10:
#     b = 1
#     while b < 10:
#         print(f'{b} x {a} = {a * b}',end='\t')
#         b += 1
#     a += 1
#     print()

# for c in range(1, 10):
#     for d in range(1, 10):
#         print(f'{d} x {c} = {c * d:<2}',end='    ')
#     print()

''' 1단 2단 3단
    4단 5단 6단
    7단 8단 9단  '''

''' 실습6 '''
# for a in range(5):
#     for b in range(a+1):
#         print('*',end=' ')
#     print()

# for a in range(1, 6):
#     print('* ' * a)

# for a in range(5, 0, -1):
#     print('* ' * a)

# for i in range(1, 6):
#     print(' ' * (5 - i) + '* ' * i)

# for a in range(1, 1001):
#     sum = 0
#     for b in range(1, a):
#         if a % b == 0:
#             sum = sum + b
#         if sum == a:
#             print(f'{a} - 완전수')

''' 리스트 컴프리펜션 '''
# a = [1, 2, 3, 4]
# b = []
# for i in a:
#     b.append(i * 3)
# print(b)

# a = [1, 2, 3, 4]
# res = [num * 3 for num in a]
# print(res)

#ls = [a for a in range(1, 101)]
#print(ls)

# st = 'have a nice day'
# ls = [ch for ch in st]
# print(ls)

# ls = [1, 2, 3, 4]
# tmp = [su for su in range(5, 11)]
# ls += tmp
# print(ls)

''' 중첩 for문의 컴프리펜션 
    객체명 = [추가할요소 외부for문 내부for문] 
     * 추가할 요소가 내부 for문에서 .append()로 추가되는 형식 '''
# ls = [i * j for i in range(1, 10) for j in range(1, 10)]
# print(ls)

# ls = [(i, j) for i in range(1, 6) for j in range(1, 6)]
# print(ls)

# ls = [num for num in range(1, 51) if num % 5 == 0]
# print(ls)

# ls = [f'{su} - 짝수' if su % 2 == 0 else f'{su} - 홀수' for su in range(1, 11)]
# print(ls)

# numbers = [1, 2, 3, 4, 5]
# result = [n * 2 for n in numbers if n % 2 == 1]
# #for n in numbers:
# #    if n % 2 == 1:
# #        result.append(n * 2)
# print(result)

''' 함수(function) 
    코드를 작게 분할하여 생성, 유지/관리, 수정 등을
    편하게 하기 위해 사용하는 개념

    함수이름, 매개변수, return
    필요에 따라서는 반환값 없이 return만 작성하기도 한다
'''

# def add(a, b): # add
#     return a + b  # 반환시키겠당!

# #print(add(4, 5))    

# a = 3
# b = 4
# c = add(a, b) # add를 호출하면서 a, b 변수 두 개의 데이터를 전달(인수)
# print(c) # 반한값을 c라는 이름으로 받아서 출력

''' 매개변수 : 함수 정의하면서 작성, 데이터를 넘겨받을 변수
    인수 : 함수를 호출하면서 넘겨주는 데이터
     '''

''' 여러가지 형태로 함수를 정의(생성)하게 된다
    1. 매개변수 0, return 0    ; 일반적인 함수(위에꺼!)
    2. 매개변수 x, return 0 
    3. 매개변수 0, return x
    4. 매개변수 x, return x 
''' 

# def add(a, b): # add
#     return a + b  # 반환시키겠당!

# a = 3
# b = 4
# c = add(a, b) # add를 호출하면서 a, b 변수 두 개의 데이터를 전달(인수)
# print(c) 

''' 매개변수 x, return 0 '''
# def say():
#     return 'Hi'

# a = say()    # 매개변수가 없는 함수는 호출 시 인수를 작성하지 않는다!
# print(a)

# def say():
#     return 'Hi'

# a = say('철수')    # 매개변수가 없는 함수는 호출 시 인수를 작성하지 않는다!
# print(a)

''' 매개변수 0, return x '''

# def add(a, b):
#     print(f'{a} + {b} = {a + b}') # return x ==> 마지막 코드 동작 후 함수 종료

# add(3, 4)    # return이 없는 함수는 호출 시 반환값의 이름을 지정 x
# s1 = 5
# s2 = 10
# res = add(s1, s2) # 반환값의 이름을 작성하여도 None 데이터의 사용
# print(res)

''' 매개변수 x, return x '''
# def say():
#     print('Hi')

# say()   # 매개변수 X => 인수 작성 X // return x ==> 반환값의 이름 작성 x


