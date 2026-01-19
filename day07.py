''' 매개변수를 지정하여 함수 호출 '''

# def sub(a, b):
#     return a - b

# result1 = sub(7, 3)            # 매개변수 이름 사용 x
# print(result1)

# result2 = sub(a=7, b=3)        # 매개변수 이름 사용
# print(result2)

# result3 = sub(b=3, a=7)        # 매개변수를 지정하면 순서에 상관 x
# print(result3)

# a = [1, 3, 2, 4, 6, 8, 7]
# b = [1, 3, 2, 4, 6, 8, 7]
# print(a)
# a.sort()
# print(a)
# print('-'*30)
# print(b)
# b.sort(reverse=True)
# print(b)

''' 여러개의 입력값을 받는 함수 '''
# def add(a, b):
#     return a + b

# ''' 7+3+4 '''
# tmp = add(7, 3)
# res = add(tmp, 4)
# print('7 * 3 + 4 = %d' % res)

# # 1 + 2 + 3 + 5
# tmp1 = add(1, 2)
# tmp2 = add(3, 5)
# res = add(tmp1 + tmp2)

# def add_many(*args):     # *매개변수 => 배달 이름의 tuple
#     sum = 0              
#     for i in args:
#         sum = sum + 1
#     return sum

# res1 = add_many()   # args = (1, 2, 3)
# print(res1)

# res2 = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)   
# print(res2)

# res1 = add_many(1, 2, 3)   # args = (1, 2, 3)
# print(res1)

# res2 = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)   
# print(res2)

''' 일반 매갭ㄴ수와 *매개변수 함께 사용 '''
# def add_mul(choice, *detas):    
#     if choice == 'add' :
#         result = 0
#         for i in detas:
#             result = result + i
#     elif choice == 'mul' :
#         result = 1
#         for i in detas:
#             result = result * i
#     return result

# res1 = add_mul('add', 1, 2, 3, 4, 5)
# print(res1)

# res2 = add_mul('mul', 1, 2, 3, 4, 5)
# print(res2)

''' 키워드 매개변수 - 매개변수 앞에 ** 붙여서 작성 '''
# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1)
# age = 11
# print_kwargs(name='tester', age=33)

''' 여러 데이터를 변환해도 하나의 tuple로 묶어서 반환단다
    (= 여러 데이터를 반환이 아닌 tuple의 반환) '''

# def addAndMul(a, b):
#     return a+b, a*b

# result = addAndMul(3, 4)
# print(result)
# print(type(result))
    
# addRes, nulRes = addAndMul(3, 4)
# print(addRes)
# print(nulRes)

# def addAndMul(a, b):
#     return a+b
#     return a*b

# result = addAndMul(3, 4)
# print(result)
# print(type(result))

''' return을 여러개 사용하는 예시 '''
# def add_mul(choice, *detas):    
#     if choice == 'add' :
#         result = 0
#         for i in detas:
#             result = result + i
#         return result
#     elif choice == 'mul' :
#         result = 1
#         for i in detas:
#             result = result * i
#         return result

# res1 = add_mul('add', 1, 2, 3, 4, 5)
# print(res1)

# res2 = add_mul('mul', 1, 2, 3, 4, 5)
# print(res2)

''' return을 함수 종료 용도로만 사용하는 예시 '''
# def say_nick(nick):
#     filter = '바보', '멍청이', '똥개'
#     if nick in filter:
#         print('부적절한 별명입니다')
#         return
#     print(f'나의 별명은 {nick} 입니다')

# say_nick('뚱땡이')   # return 노만남 print() 동작
# say_nick('바보')     # return 만남 print() 동작 x
# say_nick('멍청이') 
# say_nick('잠탱이') 

''' return으로 함수 종료 시 다른 동작에 관계없이 무조건 종료 '''
# def print_num(start):
#     while True:
#         print(start)
#         if start == 10:
#             print('10까지만 보여드림니돠!')
#             return
#         start = start + 1
    
# print_num(1)

''' 매개변수에 초깃값 미리 설정하기
    함수 작성 시 매개변수에 특정 데이터를 붙여줄 수 잇다
    이렇게 작성된 매개변수는 데이터 전달이 되지 않으면 작성된 데이터를 사용

    단, 무조건 마지막 매개변수부터 차례대로 초기값을 설정해야 한다
'''

# def say_myself(name='테스트', age=35, man=True):
#     print('나만 이름은 %s 입니다'%name)
#     print('나이는 {}살 입니다'.format(age))
#     if man:
#         print('남자입니다')
#     else:
#         print('여자입니다')

# say_myself('tester', 00)    # man 매개변수에 데이터 전달 x ==> 기본값 사용
# say_myself('user', 1, False)

''' 함수 안에서 선언한 변수의 효력 범위 
    기본적으로 함수 밖에서 선언한 변수는 함수 안에서도 사용 가능 
    (전체 영역에서 사용 가능한 변수 = 전역 변수)
    (해당 함수 지역에서만 사용 가능한 변수 = 지역 변수)  '''

# def vartest(a):
#     a = a + 1
#     print(a)

# a = 1
# vartest(a)
# print(a)

# def vartest():
#     print(a)

# a = 1
# vartest()
# print(a)

# def func1():
#     a = 100
#     print(f'func1() 에서 a 출력: {a}')

# def func2():
#     print(f'func2() 에서 a 출력: {a}')

# a = 10
# func1()
# func2()
# print(f'함수 밖에서 a 출력 : {a}') # 전역 변수 a 출력

''' 지역변수, 전역변수 밖에서 함수 싶다면 어떻해?? '''
# def vartest(a):
#     a = a + 1
#     return a

# a = 1
# print(f'변경 전 a : {a}')
# a = vartest(a)
# print(f'변경 후 a : {a}')

# def vartest():
#     global a
#     a = a + 1

# a = 1
# print(f'변경 전 a : {a}')
# vartest()
# print(f'변경 후 a : {a}')

# def func1():
#     global b
#     b = 200
#     print(f'func1() 에서 a: {a}, b: {b}')

# a = 100
# func1()
# print(f'func1() 에서 a: {a}, b: {b}')

''' lambda 예약어 '''
# add = lambda a, b : a + b

# res = add(3, 4)
# print(res)

''' 매개변수 x, return x '''
# say = lambda : print('Hi')

# say()

''' 실습1*
    몇 개의 정수가 입력되어도 평균 점수를 구할 수 있는
    avg_score() 함수를 완선해보세요  '''

# def avg_score(*args):   
#     number = 0
#     for i in args:
#         number = number + i
#     avg = number / len(args)
#     print(f'평균 점수 : {avg:.2f}점')

#     # global a
#     # a = (95, 8, 15, 68) / 4
#     # global b
#     # b = (88, 45, 79, 94, 39, 64, 78) / 6
#     pass

# avg_score(95, 8, 15, 68)
# avg_score(88, 45, 79, 94, 39, 64, 78)
#print(avg_score(a))
#print(avg_score(b))

''' 사용자 입출력 
    print() -- 출력함수, () 안에 있는 내용을 터미널에 출력
    input() -- 입력함수, 함수가 동작되면 터미널에서 데이터를 입력받을 준비를 하고
    사용자가 직접 터미널에 데이터를 작성하고 enter를 눌러서
    함수 위치에 데이터를 전달
'''

''' print() '''
# print('test')
# print(123)
# a = 12345
# print(a)
# print('숫자 : {}'.format(a))

# b = '숫자 : {}'.format(a)
# print(b)

''' print() 함수는 마지막에 자동으로 enter가 들어간다
    필요 시 출력할 데이터 뒤에 ,end='문자' 형식으로
    enter 대신 다른 문자를 출력
     
    이 경우에 enter가 없으므로 다음 출력 내용이
    해당 문자 뒸쪽으로 출력
'''

# for i in range(1, 6):
#     print(i)

# for i in range(1, 6):
#     print(i,end=' ')
# print('출력 내용이 옆으로 이어진다')

# print(end=' ',123)    # error code   : 출력할 데이터 --> end

# for i in range(1, 11):
#     print(i, end=', ')
# print('\b\b ')
# print('다음 내용')

# gugu = 2
# for i in range(1, 10):
#     print(f'{gugu} x {i} = {gugu * i}', end='\t')
# print()
# print('다음 내용')

'''
    print() 함수의 매개변수ㄹ르 보면
    end 매개변수 앞쪽으로 *values 매개변수가 존재

    매개변수 이름 앞에 * 기호가 붙으면 여러 데이터 전달이 가능
    그래서 print() 함수의 괄호 안에 여러 데이터를 작성하는 것이 가능
'''

# print(123, 456)

# a = 123
# b = 345
# print(a, b)

# print(123, 456, 789)

# a = 123
# b = 345
# print(a, b)

# pi = 3.141556
# ls = [1, 2, 3, 4]
# print(123, 'test', 456.789, pi, ls[0])

# print('원주를 : %.4f'%pi)
# print('원주를 : {}'.format(pi))
# print(f'원주율 : {pi}')
# print('원두율 :',pi)

# a = 10
# b = 4
# print('%d + %d = %d'%(a, b, a + b))
# print('{} + {} = {}'.format(a, b, a + b))
# print(f'{a} + {b} = {a + b}')
# print(a, '+', b, '=', a + b)

''' 일반적인 데이터들은 전부 , 기호로 구분하여 하지만
    문자열만 예외적으로 , 기호 없이 여러개를 작성할 수 있다
    (문자열 간의 + 연산과 동일한 결과) '''

# print('have' 'a' 'nice' 'day')
# print('have'+'a'+'nice'+'day')
# print('have','a','nice','day')

''' input() '''
# print('숫자1 입력')
# a = input()
# print('숫자2 입력')
# b = input()
# print(f'{a} + {b} = {a + b}')
# print('숫자1 자료형 :',type(a))
# print('숫자2 자료형 :',type(b))

''' 필요에 따라 input() 함수로 입력받은 데이터의 자료형을 변환 '''
# print('숫자1 입력')
# a = input()
# a = int(a)
# print('숫자2 입력')
# b = int(input())
# print(f'{a} + {b} = {a + b}')

''' 입력 위치 왼쪽에 특정 문자열 출력 '''
# print('숫자1 입력 : ',end='')
# a = int(input())
# b = int(input('숫자2 입력 : '))
# print(f'\n{a} + {b} = {a + b}')

# score = []
# for i in range(1, 6):
#     sc = int(input(f'{i}1번 학생 점수 : '))
#     score.append(sc)
# print('\n전체 점수 :',score)

# score = [int(input(f'{i}번 학생 점수 : ')) for i in range(1, 6)]
# print('\n전체 점수 :',score)

# score = input('5개 점수 입력 : ').split()
# print('\n전체 점수 :',score)
# #score = map(int, score)
# score = [int(x) for x in input('5개 입력 : ').split()]
# print('\n전체 점수 :',score)

''' 실습 2 '''


# def add(a, b, sc):
#     a = int(input('첫번째 수를 입력하세요!'))
#     b = int(input('두번째 수를 입력하세요!'))
#     sc = input('연산자를 입력해주세요!')    
#     print(f'{add(a)} + {add(b)}')

#def add():
# a = int(input('첫번째 수를 입력하세요 : '))
# #print('\n첫번째 수 :',a)
# b = int(input('두번째 수를 입력하세요 : '))
# #print('\n첫번째 수 :',b)
# while True:
#     sc = input('사칙연산 연산자(+, -, *, /) : ')
#     if sc in ('+', '-', '*', '/'):
#         break

# if sc == '+':
#     print(f'{a} {sc} {b} = {a + b}')
# elif sc == '-':
#     print(f'{a} {sc} {b} = {a - b}')
# elif sc == '*':
#     print(f'{a} {sc} {b} = {a * b}')
# elif sc == '/':
#     print(f'{a} {sc} {b} = {a / b:.3}')

#print('\n연산자 :',sc)
#print(f'\n{a} {sc} {b} = {a * b}')

# def sdfwefwef(a, b, sc):
#     a = int(input('첫번째 수를 입력하세요 : '))
#     #print('\n첫번째 수 :',a)
#     b = int(input('두번째 수를 입력하세요 : '))
#     #print('\n첫번째 수 :',b)
# while True:
#     sc = input('사칙연산 연산자(+, -, *, /) : ')
#     if sc in ('+', '-', '*', '/'):
#         break

# sum = lambda a, b: a + b
# sub = lambda a, b: a - b
# mul = lambda a, b: a * b
# div = lambda a, b: a / b

''' 풀이더더더 '''

# def printRes(a, b, sc):
#     if sc == '+':     res = sum(a, b)
#     elif sc == '-':     res = sub(a, b)
#     elif sc == '*':     res = mul(a, b)
#     elif sc == '/':     res = div(a, b)

# sum = lambda a, b: a + b
# sub = lambda a, b: a - b
# mul = lambda a, b: a * b
# div = lambda a, b: a / b

# def Check(ls):
#     if ls[0].isdigit() and ls[2].isdigit() and ls[1] in ('+', '-', '*', '/'):
#         return True
#     elif ls[1] not in ('+', '-', '*', '/'):
#         print('시칙연산만 가능합니다')
#         return False
#     elif not(ls[0].isdigit() and ls[2].isdigit()):
#         print('숫자건의 연산만 가능합니다')
#     else:
#         print('알 수 없는 오류입니다')
#     print()
#     return False

# info = '''
# 수식어 ㄱㄱㄱ
# '''

# print(info)
# while True:
#     tmp = input('수식 입력 : ').split()
#     if Check(tmp):
#         break
# printRes(tmp[0], tmp[2], tmp[1])

# info = """1. 한 단 출력
# 2. 전체 출력
# 3. 프로그래 종료"""

# def printSingle():
#     gugu = asdasdasd

# def printAll():


#while True:
    # x1 = int(input('구구단 출력 단: '))
    # for x1 in range(1, 10):    
    #     print(f'--- {x1}단 ---')            
    #     for x2 in range(1, 4):
    #         if x2 == 1:               
    #             print(f'{x2} * {x1} = {x2 * x1}', end='\t\n')
    #             break
    #             print(f'{x2} * {x1} = {x2 * x1}', end='\t\n')
    #     for x2 in range(4, 7):
    #         print(f'{x2} * {x1} = {x2 * x1}', end='\t\n')
    #     for x2 in range(7, 10):
    #         print(f'{x2} * {x1} = {x2 * x1}', end='\t\n')
    #     print('\b ')
    # aaa = input('프로그램을 종료하겠습니까??')
    # print(aaa)
    # print(info)
    # cho = input('>>> ')
    # if cho == '1':
    #     print('1번 메뉴 동작')
    #     x1 = int(input('구구단 출력 단: '))           
    #     print(f'--- {x1}단 ---')            
    #     for x2 in range(1, 10): 
    #         print(f'{x1} x {x2} = {x1 * x2}')
    #     break

    # elif cho == '2':
    #     print('2번 메뉴 동작')
    #     x4 = int(input('구구단 출력 단: '))
    #     for x4 in range(1, 10):    
    #         print(f'--- {x4}단 ---')            
    #     for x5 in range(1, 4):
    #         print(f'{x5} * {x1} = {x5 * x1}', end='\t\n')
    #     for x5 in range(4, 7):
    #         print(f'{x5} * {x1} = {x5 * x1}', end='\t\n')
    #     for x5 in range(7, 10):
    #         print(f'{x5} * {x1} = {x5 * x1}', end='\t\n')
    #     print('\b ')
    #     break
    # elif cho == '3':
    #     print('프로그램을 종료합니다')
    #     break
    # print()    

# info = """0. 점수 입력
# 1. 각 반의 평균 점수 확인
# 2. 선택한 반의 최고 점수, 최저 점수 확인
# 3. 프로그래 종료"""

# def inputScore():
#     ls = []
#     cnt = int(input('몇 개 반인가요? >>> '))
#     for a in range(1, cnt+1):
#         score = [int(b) for b in input(f'{a}반 성적 입력 : ').split()]        
#         ls.append(score)
#     return ls

# #allScore = inputScore()
# #print(allScore)

# def classAvg(ls):
#     for classScore in range(len(ls)):
#         sum = 0
#         for i in ls[classScore]:
#             sum = sum + 1
#         avg = sum / len(ls(classScore))
#         print(f'{classScore + 1}반 평균 : {avg:3}점')

# ''' 실습4 '''
# while True:
#     print('0. 점수 입력\n1. 반 별 평균\n2. n반 최고/최저\n3. 종료')
#     cho = input('>>> ')
#     print()
#     if cho == '0':
#        if not(allScore):
#            allScore = inputScore()
#        else:
#            print('이미 입력된 점수가 있습니다')
#     elif cho == '1':
#         classAvg(allScore)
#     elif cho == '2':
#         classAvg(allScore)
#     else:
#         print('\n\n\n\n\n\n\n')
#         break
#     print()

''' 참고
min(), max()  '''
# ls = [78, 55, 62, 14, 95]
# MIN = ls[0]
# MAX = ls[0]
# for score in ls:
#     if score < MIN:
#         MIN = score
# print('최저점 :',MIN)
# for score in ls:
#     if score > MAX:
#         MAX = score
# print('최고점 :',MAX)


