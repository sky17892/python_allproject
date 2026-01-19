''' .get() - key를 이용하여 value 호출 '''
# a = {'one':'하나', 'two':'두울', 'three':'세엣'}
# #print(a['one'])
# #print(a['four']) # error code
# print(a.get['one'])
# print(a.get['four'])
# b = 'default'
# print(a.get['two',b])
# print(a.get['four',b])
# c = True
# print(a.get['nine',c])

''' in 연산자 - 데이터 범위 자료형에 특정 데이터가 존재하는지 확인 '''
# a = 'tester'
# b = [1, 2, 3, 4]
# c = ['a', 'b', 'c', 'd']
# d = {'one':'하나', 'two':'둘', 'three':'셋'}
# print('e' in a)
# print('e' in a)
# print(1 in b)
# print(2 in b)
# print('b' in c)
# print('e' in c)
# print('one' in d)
# print('하나' in d)

''' set 집합 자료형 '''
# s1 = set([1, 2, 3])
# print(s1)
# print(type(s1))
# s2 = {1, 2, 3}
# print(s2)
# print(type(s2))

''' 형변환 예시 '''
# a = '123'
# b = 123
# #print(a + b) # error code123
# print(int(a) + b)
# print(a + str(b))

''' 집합은 중복되는 데이터를 허용하지 않는다 '''
# st = 'Hello'
# s3 = set(st)
# print(s3)

''' 순서 개념이 없기 때문에 index를 이용한 참조 x '''
# ls = [1, 2, 3]
# s1 = set(ls)
# print(s1[0])           

# s1 = set([1,2,3])
# ls = list(s1)
# print(ls[0])

''' set 자료형은 집합 자료형 '''
# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1 & s2)
# print(s1.intersection(s2))
# print(s2.intersection(s1))

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1 | s2)
# print(s1.union(s2))
# print(s2.union(s1))

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1 - s2)
# print(s1.difference(s2))
# print('-' * 10)
# print(s2 - s1)
# print(s2.difference(s1))

''' .add() - 집합에 데이터 추가 '''
# s1 = set([1, 2, 3])
# print(s1)
# s1.add(4)
# print(s1)
# s1.add(2)
# print(s1)

''' .update() - 집합에 데이터 여러개 추가 '''
# s1 = set([1, 2, 3])
# print(s1)
# s1.update([4, 5, 6])
# print(s1)
# s1.update([6, 7, 8])
# print(s1)

''' .remove() - 집합에서 데이터 제거 '''
# s1 = set([1, 2, 3])
# print(s1)
# s1.remove(2)
# print(s1)

''' bool '''
# a = True
# b = False
# print(a)
# print(type(a))
# print(b)
# print(type(b))

''' 여러 자료형에서 값이 없으면 False로 취급 '''
# i1 = 1
# i2 = 0
# print(bool(i1))
# print(bool(i2))

# ls1 = [1, 2, 3]
# ls2 = []
# print(bool(ls1))
# print(bool(ls2))

''' 여러 자료형들의 False로 구분 '''
# a = 0
# b = []
# c = ()
# d = ''
# e = {}
# f = set()

# a = [1, 2, 3, 4]
# while a:
#     print(a.pop())
# print('---')
# print(a)

''' 변수 '''
# a = 10
# a = {1, 2, 3}
# a = 'test'

# b = 10
# c = '10'

''' id() 함수를 데이터가 메모리 어느 위치에 저장되었는지 확인 '''
# a = 10
# print(id(a))
# b = 10
# print(id(b))

''' list 등의 여러 데이터를 다루는 자료형에서는
    의도하지 않은 데이터 변경이 일어날 수 있다 '''

''' 정수 등의 단일 데이터 '''
# a = 10
# b = 18
# print(id(a))
# print(id(b))
# print('-' * 20)
# a = 20
# print(id(a))
# print(id(b))
# print('-' * 20)
# b = a
# print(id(a))
# print(id(b))

# a = [1, 2, 3]
# b = a[:]
# print(id(a))
# print(id(b))
# print('-' * 20)
# b[1] = 100
# print(a)
# print(b)

''' index 번호 개념이 없으면 copy() 함수를 사용 '''
# from copy import copy      # copy() 함수를 사용하기 위한 코드
# a = [1, 2, 3]
# b = copy(a)
# print(id(a))
# print(id(b))
# print('-' * 20)
# b[1] = 100
# print(a)
# print(b)

# from copy import deepcopy      # deepcopy() 함수를 사용하기 위한 코드
# a = [1, 2, 3]
# b = deepcopy(a)
# print(id(a))
# print(id(b))
# print('-' * 20)
# b[1] = 100
# print(a)
# print(b)

# from copy import copy, deepcopy 
# a = [1, 2, [3, 4]]
# b = copy(a)
# print(a)
# print(b)
# b[2][1] = 100
# print(a)
# print(b)
# print('-' * 20)
# a = [1, 2, [3, 4]]
# b = deepcopy(a)
# print(a)
# print(b)
# b[2][1] = 100
# print(a)
# print(b)

# a, b = 'python', 'test'
# print(a)
# print(b)

# [a,b] = [10,20]
# print(a)
# print(b)

# a = b = 5
# print(a)
# print(b)

''' 데이터 교환 '''
# a = 10
# b = 20
# print(a)
# print(b)
# print('-'*5)
# # tmp = a
# # a = b
# # b = tmp
# a, b = b, a
# print(a)
# print(b)

''' 제어문 '''
# a = 1
# b = 2
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)

''' if문에서의 사용 '''
# money = 3500
# print('집에 걸어가기 귀찮은데')
# if money >= 5000:
#     print('택시 타자')
# print('집까지 얼른 가야지')

''' 들여쓰기 코드 작성시 주의사항 '''

''' 1. ㅁ;ㅣ호943-222222 '''
# money = 1000
# if money > 10:
# print('10원 이상')
# print('테스트 코드')

''' 2. 들여쓰기 된 코드가 여러줄인 경우 간격을 맞춰줘야 한다 '''
# money = 1000
# if money > 10:
#     print('10원 이상')
#     print('아니 10원 초과')
# print('테스트 코드')

''' 3. 들여쓰기 된 코드 사이에 일반 코드가 들어갈수 없다 '''
# money = 1000
# if money > 10:
#     print('10원 이상')
# print('테스트 코드')
#     print('아니 10원 초과')
# print('테스ㅡㅌ 코드')

''' 4.위의 사항들을 주의하여 들여쓰기를 하면 몇칸이어도 상관없다 '''
# money = 1000
# if money > 10:
#     print('10원 이상')
#     print('아니 10원 초과')

# print('테스트 코드')

''' 비교연산자 아닌 다른 방식의 True/False 활용 '''
# su1 = 10
# if su1:
#     print('숫자가 있다')

# su2 = 0
# if su2:
#     print('숫자가 없다')

# ls = [1, 2, 3, 4]
# if 1 in ls:
#     print('1은 있다')
# if 10 in ls:
#     print('10은 없다')

# st = 'test'
# if 't' not in st:
#     print('t는 있다')
# if 'a' not in st:
#     print('a는 없다')

''' 논리 연산자 '''
# moneyyy = 1000
# carddd = True
# if moneyyy >= 1700 or carddd:
#     print('대중교통을 이용하자')
# print('집에 가야지')

# su = 130000000000000000
# if su % 3 == 0 and su % 4 == 0:
#     print('3과 4의 공배수')

# su = 16
# if not su % 3 == 0:
#     print('3의 배수가 아니다')

''' if ~ else문 '''
# su = 1
# if su % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# money = 3000
# if money >= 5000:
#     pass
# else:
#     print('걸어가자')
# print('집에 가야지')

# su = 19
# if su % 2 == 0:
#     print('짝수')
# elif su % 5 == 0:
#     print('5의 배수')
# elif su % 3 == 0:
#     print('3의 배수')
# else:
#     print('모든 조건이 거짓이다')
# print('다음 코드')

# while True:
#     cho = int(input('1. 커피\n2. 코코아 \n3. 종료 \n>>> '))
#     print('하나만 꼭 하나만~~~')
#     if cho == 1:
#         print('커피 한 잔 나옵니다')
#     elif cho == 2:
#         print('코코아 한잔 나옵니다')
#     elif cho == 3:
#         print('프로그램을 종료합니다')
#         break
#     else:
#         print('잘못된 선택입니다')

# Day = 5
# if Day in (5, 12, 19, 25):
#     print('월요일')
# elif Day in (6, 13, 20, 27):
#     print('화요일')
# elif Day in (7, 14, 21, 28):
#     print('수요일')

''' 조건문 표현식 
if ~ else 동작을~
'''

# score = 77
# if score >= 60:
#     res = '합격'
# else:
#     res = '불합격'
# res = '합격' if score >= 60 else '불합격'
# print(res)

# # sc1, sc2, sc3 = 88, 39, 97
# # avg = (sc1 + sc2 + sc3) / 3
# if sc1 >= 40 and sc2 >= 40 and sc3 >= 40 and avg >= 60:
#      print('합격')
# else :
#      print('불합격')

#avg = int(input('1. 40\n2. 코코아 \n3. 종료 \n>>> '))
# sc1, sc2, sc3 = 88, 39, 97
# avg = (sc1 + sc2 + sc3) / 3
# if sc1 < 40:  print('과목1 과학')
# elif sc2 < 40:  print('과목2 과학')
# elif sc3 < 40:  print('과목3 과학')
# elif avg < 60:  print('평균 미달')
# else: print('합격')

# sc1, sc2, sc3 = 88, 39, 97
# avg = (sc1 + sc2 + sc3) / 3
# if sc1 >= 40 and sc2 >= 40 and sc3 >= 40:
#     if avg >= 60:
#         print('합격')
#     else:
#         print('평균 미달')
# else:
#     print('과학 과목이 있습니다')

# su = 0
# if su == 0:   
#    print('0은 3의 배수도 4의 배수도 아니다')
# elif su % 3 == 0:
#    print('3의 배수')
# elif su % 4 == 0:
#    print('4의 배수')
# elif su % 3 == 0 and su % 4 == 0:
#    print('3의 배수이면서 4의 배수')
# else:
#    print('0은 3의 배수도 4의 배수도 아니다')

# su = 12
# if su != 0:
#     if su % 3 == 0 and su % 4 == 0:
#        print('3의 배수이면서 4의 배수')
#     elif su % 3 == 0:
#        print('3의 배수')
#     elif su % 4 == 0:
#        print('4의 배수') 
#     else:
#        print('3의 배수도 4의 배수도 아니다')
# else:
#     print('0은 3의 배수도 4의 배수도 아니다')

''' 실습3 '''
#money = 5000 
# Time = int(input('비행기 탑승 시간(분): '))

# if Time <= 30:
#     res = 30000
# else:
#     #Time = Time - 30
#     Time -= 30
#     if Time % 10 == 0:
#         res = 30000 + Time // 10 * 5000
#     else:
#         res = 30000 + (Time // 10 + 1) * 5000
# print(f'요금의 {res:,}원 입니다')

# hitCnt = 0
# while hitCnt < 10:
#     hitCnt += 1
#     print('나무를 %d번 찍었습니다'%hitCnt)
# print('나무가 쓰러졌네요')

# hitCnt = 10
# while hitCnt < 10:
#     hitCnt += 1
#     print('나무를 %d번 찍었습니다'%hitCnt)
#     if hitCnt == 10:
#         print('나무가 쓰러졌네요')

# prompt = '''
#     1. add
#     2. del
#     3. List
#     4. Quit

#     Enter number (1 ~ 4) : '''
# number = 0
# while number != 4:
#     print(prompt,end='')
#     number = int(input())
    
''' while문을 중간에 빠져나가는 방법 '''
# coffee = 10
# money = 300
# while money:
#     print('돈을 받았으나 커피를 줍니다')
#     coffee -= 1
#     print('남은 커피는 {}잔 입니다'.format(coffee))
#     if coffee == 0:
#         print('커피가 다 떨어져서 판매를 중단합니다')
#         break

''' while문을 조건식으로 바로 이동해버림! '''
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue     # 만나는 즉시 while의 조건식으로 이동
        print('패스!')
    print(a)


