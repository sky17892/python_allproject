# print(1 + 2)
# print('1 + 2')
# print(3 - 2)
# print(3 + 4)
# print(4 / 2)

# a = 1
# b = 2
# print(a + b)

# a = 'python'
# print(a)

# a = 2
# if a > 1:
#     print('a는 1보다 크다')

# for a in [1, 2, 3]:
#     print(a)

# i = 0
# while i < 3:
#     i = i + 1
#     print(i)

# def add(a, b):
#     return a + b

# print(add(3, 4))

"""
    주석
    인터프리터가 특정 코드를 읽지 않도록 만드는 기호

    # 기호를 사용하여 주석을 설정
    # 기호 뒷쪽의 내용은 인터프리터가 읽지 않는다

    작성한 코드에 주석을 설정할 때
    코드 영역을 드래그하여 지정을 할 때 마어라머람ㄴ얾ㄴㅇㄹ+c
    해당 영역에 일괄적으로 주석 설정이 가틍한다
    (해제는 드래그로 영역 지정 후 ㅁㄴ아림넒낭+u를 눌러준다)
"""

# print('테스트 코드 1')
# print('테스트 코드 2##')
# print('테스트 코드 3')

'''
    자료형
      프로그램에서 다루는 데이터의 형태(분류)

      python에서 사용하는 자료형
      1. 단일 데이터
            점수         ; <class 'int'>
            실수         ; <class 'float'>
            논리값       ; <class 'bool'>
            (참/거짓 => True/False)

      2. 여러 데이터
            리스트       ; <class 'list'>
            튜플         ; <class 'tuple'>
            집합         ; <class 'set'>
            딕셔너리     ; <class 'dict'>
            문자열       ; <class 'str'>
'''

'''
     숫자열 데이터
        - 정수(int)
        - 실수(float)
        - 십진수가 아닌 수(이진수, 팔진수, 십육진수)

     숫자열 데이터들은 각종 연산자들 이용한
     일반적인 형태의 숫자 계산 작업이 가능한 데이터
'''

# a = 123
# b = -456
# c = 0
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))

# a = 1.2
# b = -3.45
# print(a)
# print(type(a))
# print(b)
# print(type(b))

'''
   실수 자료형에서 사용하는
   컴퓨터용 지수 표현 방식(자리수 압축용 사용)
'''

# a = 4.24E10
# b = 4.24e10
# c = 4.24E-10
# d = 4.24e-10
# print(a)
# print(b)
# print(c)
# print(d)

'''
    it에서의 숫자 체계
    이진수 : 0과 1, 총 2개의 숫자로 모든 수를 표현
    팔진수 : 0 ~ 7, 총 8개의 숫자로 모든 수를 표현
    십진수 : 0 ~ 9, 총 10개의 숫자로 모든 수를 표현
    십육진수 : 0 ~ 9 + A ~ F, 총 16개의 숫자의 문자로 모든 수를 표현
              (10 = A, 11 = 8, 12 = C, 13 = D, 14 = E, 15 = F)

    일반적으로 IT 분야에서 팔진수와 십육진수는
    이진수를 압축하여 표현하는 용도로 사용

    python 프로그래밍에서 특정 숫자를 십진수가 아닌
    다른 진수로 인식시키기 위해 표혀현식으로 사용
     이진수 : 0b            (binary)
     팔진수 : 0o            (actal)
     십육진수 : 0x          (hexadecimal)
'''

# print(11001010)
# print(0b11001010)
# print(0o11001010)
# print(0x11001010)

'''
    bin(data)     : 이진수로 변환
    oct(data)     : 팔진수로 변환
    hex(data)     : 십육진수로 변환
'''

# print(101)
# print(bin(101))
# print(oct(101))
# print(hex(101))

# print(hex(255))
# print(hex(0b11111111))
# print(hex(0o377))
# print(hex(0xff))

'''
   숫자형 데이터는 각종 연산 기호(연산자)를 이용하여
   데이터 감의 계산이 가능하다
'''

''' 기본 사칙연산(+, -, *, /) '''
# a = 3
# b = 4
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

''' 제곱 계산은 ** 기호를 사용 '''
# a = 3
# b = 4
# print(a ** b)

'''
    나눗셈 연산 시 정수까지만 연산 후
    몫과 나머지를 반환하는 연산자가 각각 존재
'''

# a = 7
# b = 4
# print(a / b)
# print(a // b)
# print(a % b)

'''
   실습 ㄱㄱㄱ
'''
# print(18 ** 2 * 10 + 2 * 11)
# print(10 * 18 ** 2 + 2 * 11)
# print(14 // 3)
# print(14 % 3)

''' 연산 우선 순위를 모르면 생기는 문제 '''
# print(-3 ** 2)
# print((-3) ** 2)

'''
    문자열 자료형
      string
      작은 따음표나 란 따음표로 묶어준 데이터
      python에서는 단일 문자의 문자열의 따로 구분하지 않는다
      (= 단일 문자도 문자열도 작은 따음표와 큰 따음표 전부 사용 가능)
'''

# a = 'test'
# b = "test"
# c = 'A'
# b = "A"
# print(a)
# print(b)
# print(c)
# print(d)

'''
   작은 따음표 내부에서 작은 따음표 출력이나
   큰 따음표 내부에는 큰 따음표 출력은
   일반적인 문자 작성으로는 불가능
'''

#print('I'm Ironman')
# print("I'm Ironman")
# print('I\'m Ironman')

# a = "I'm Ironman"
# b = 'I\'m Ironman'
# #c = 'I'm Ironman'
# print(a)
# print(b)

#print(""Python is very easy", he says")
# print('"Python is very easy", he says')
# print("\"Python is very easy\", he says")

# #c = ""Python is very easy", he says"
# a = '"Python is very easy", he says'
# b = "\"Python is very easy\", he says"
# print(a)
# print('"Python is very easy", he says')
# print("\"Python is very easy\", he says")

#c = ""Python is very easy", he says"
# a = '"Python is very easy", he says'
# b = "\"Python is very easy\", he says"
# print(a)
# print(b)

# a = 'Good day\nHave a nice day'
# b = '''Good day
# Have a nice day'''

# print(a)
# print('-' * 10)
# print(b)

'''
    이스케이프 문자
     역슬래시 기호 뒤에 특정 문자를 붙여서
     특별한 특수 문자를 사용하는 문자

          \'       : 작은 따음표 안에서 작은 따음표 사용
          \"       : 큰 따음표 안에서 큰 따음표 사용
          \\       : 역슬래시 기호를 출력하기 위해 사용
          \n       : 개형 문자(줄 바꿈 문자 => enter)
          \t       : 탭 문자(탭 변경 문자 => 8칸 단위의 가상 공간 탭 이동)
          \b       : 벽 스페이스 문자(커서를 왼쪽으로 한 칸 이동)
          \r       : 캐리지 문자(커서를 그 줄의 첫 칸으로 이동)
          \f       : 폼 이동 문자(프린터 출력 시 다음 페이지로 이동)
          \a       : 경고음 문자(컴퓨터에서 경고등 1회 출력)
          \000     : NULL문자
'''

# print('\20,001')
# print('\\20,000')
# print('d:\\')

# print('이름 : 김용주')
# print('나이 : 47세')
# print('사는 곳 : 서울')
# print('전화번호 : 010-8888-7777')

# print('123456788')
# print('1234567\r8890898')
# print('123456788124\r12421')

'''
   문자열 연산
    문자열과 문자열의 + 연산과
    문자열과 숫자의 * 연산이 가능하다    
'''

''' 문자열과 문자열의 * 연산 => 문자열 확장(= 이어붙이기) '''
# head = 'Python is'
# tail = ' very easy'
# print(head + tail)

# ''' 문자열 * 숫자 => 문자열 반복 '''
# a = 'one'
# print(a * 3)

''' 문자열 길이 구하기 '''
# a = 'have a nice day'
# print(len(a))

''' 
   문자열 인덱싱 
   {}를 사용하여 데이터를 묶어주는 dict, set를 제외한
   나머지(list, tuple, str) 자료형들은
   내부 요소에 접근 시 index 번호를 사용하여 접근
   (데이터의 인덱싱이 되어있다)
'''

# a = 'Good Luck!'
# print(a[3])
# print(a[9])
# print(a[-1])

'''
   문자열 슬라이싱
    index 번호를 사용하여 연속된 내부 데이터 일부를
    복제하는 방법

    [] 내부에 : 기호로 구분지에서 시작과 끝을 작성
    시작점부터 끝점 전까지를 복제
'''

# a = 'have a nice day'
# print(a[0:4])
# print('!' + a[0:4] + '!')
# print(a[7:11])
# print(a[-3:15])

'''
    슬라이싱에서 시작 index와 끝 index를 생략할 수 있다
    시작점에서 생략하면 0번 index 부터를 의미
    끝점을 생략하면 마지막 index 까지를 의미
'''

# a = 'Happy new year'
# print(a[0:5])
# print(a[:5])
# print('-' * 8)
# print(a[10:14])
# print(a[10:])
# print(a[-4:])

# data = '20251231python'
# birth = data[:8]
# name = data[8:]
# print('이름 : ' + name)
# print('생일 : ' + birth)

'''
     문자열은 index 번호와 = 기호를 사용하여
     데이터를 변경하는 것은 불가능하다
'''
# a = 'have a nice day'
# # a[0] = 'H'
# a = 'H' + a[1:]
# print(a)
# b = a[:7] + 'NICE' + a[-4:]
# print(b)

'''
    문자열 포매팅
     문자열 내부에 다른 데이터를 삽입하기 위한 방법

     내부에 다른 데이터가 위치할 곳에 서식 문자라는
     특수한 문자를 작성하고, 문자열 뒤에 해당 서식 문자에
     대치될 데이터를 작성

     서식 문자는 python에서는 두 가지가 사용
     1. %  서식 문자
     2. {} 서식 문자
'''

'''
    % 서식 문자
     '%알파벳' 형식으로 데이터의 위치와
     출력된 형식까지도 지정하는 서식 문자

        %d    : 정수형 데이터(dicimal)
        %f    : 실수형 데이터(float)
        %c    : 단일 문자 데이터(character)
        %s    : 문자열 데이터(string)
        %o    : 팔진수 데이터(octal)
        %x    : 십육진수 데이터(hexadecimal)
        %%    : % 서식 문자 사용 시 % 문자를 출력
'''

# a = 3
# print('숫자 1 : %d' % a)

# a = 5
# print('숫자 1 : %d' % a)

# a = 1111
# print('숫자 1 : %d' % a)

# b = 3.14
# print('원주율 : %f' % b)

# ch = 'a'
# print('문자 : %c' % ch)

# st = 'tester001'
# print('아이디 : %s' % st)

# ch = 'a'
# st = 'tester001'
# #print('%%c에 문자열 : %c' % st)
# print('%%s에 문자 : %s' % ch)

'''
    % 서식 문자가 여러개 작성되어야 여러 데이터를 전달해야 하거나
    % 서식 문자에 연산식에 결과를 전달할 때는
    데이터를 ()로 묶어준다
'''

#a = '%s님의 나이는 %d세 d입니다' % '김기태', 35
# a = '%s님의 나이는 %d세 d입니다' % ('김기태', 35)
# print(a)

#print('10 + 20 = %d' % (10 + 20))

'''
    % 서식 문자를 사용하는 따옴표 안에서
    % 서식 문자를 출력할 떄에는 %% 사용
'''

# a = 7
# b = 5
# print('%d % %d = %d' % (a, b, a % b))

''' %s는 특이하게도 모든 데이터를 문자로 변환하여 대체가 가능 '''
# print('%s님의 나이는 %s세 입니다' % ('김기태', 35))
# print('원주율 : %s' % 3.14)

'''
   서식 문자 위치에 데이터를 출력하면서
   적용시킬 형식을 지정할 수 있다
   1. 소수점 아래 자리수 제어(%f에서만 사용)
   2. 출력 영역 지정
               + 영역 내부에서의 정렬
'''

# a = 3.141592
# b = 3.14
# print('원주율 : %f %f' % (a, b))
# print('원주율 : %.2f %.2f' % (a, b))
# print('원주율 : %.3f %.3f' % (a, b))

''' 영역 지점 - 데이터를 몇 칸 영역 내부에 출력할 것인지 지정 '''
# a = 123
# b = 45
# print('!%d!\n!%d!' % (a, b))
# print('!%5d!\n!%5d!' % (a, b))
# c = 123456789
# print('!%5d!' % c)

# a = 'tester1'
# b = 'tester001'
# print('<%10s님 반갑습니다>' % a)
# print('<%10s님 반갑습니다>' % b)

''' 실수 데이터는 %d와 f 사이에 영역.자리수 형식의 작성이 가능 '''
# a = 3.141592
# print('!%10.2f!' % 0)

''' % 서식 문자에서 영역을 지정하고 출력하면
    기본적으로는 오른쪽 정렬이 되어 출력

    필요에 따라 영역 크기를 음수를 입력하면
    왼쪽 정렬하여 출력이 가능   
'''

# print('!%5d!%-5d!' % (123, 123))

'''
   {} 서식 문자
   python 3.6 버전에서 추가된 python 전용의 서식 문자
   {} 하나로 모든 종류의 데이터를 대체할 수 있다

   따옴표 뒤에 .format() 함수를 붙여서
   함수의 () 내부에 서식 문자를 대체할 데이터를 작성
'''

# a = 10
# b = 3.14
# c = 'a'
# d = 'test'
# print('{} {} {} {}'.format(a, b, c, d))
# print('{0} {1} {2} {3}'.format(a, b, c, d))
# print('{3} {2} {1} {0}'.format(a, b, c, d))
# print('{0} {2} {3} {1}'.format(a, b, c, d))

'''
    {} 서식 문자에서 형식 지정은 {} 내부에 작성
    1. 자리수 제어 - {;.숫자} or {:.숫자f}
    2. 영역 지정   - {:숫자}
         + 영역 내 정럴 - {:기호숫자}
'''

''' 소수점 아래 자리수 제어 '''
# a = 3 / 5
# b = 5 / 3
# print('{}'.format(a))
# print('{}'.format(b))
# print('-' * 20)
# print('{:.3}'.format(b))
# print('{:.3f}'.format(b))

''' 영역 지정 '''
# a = 10
# b = 'test'
# print('!{:5}!'.format(a))
# print('!{:10}!'.format(b))

''' 실수의 경우 출력 영역 지점과 자리수 제어를 동시에 할 수 있다 '''
# a = 5 / 3
# print('!{:8.3f}!'.format(a))

''' 영역 내부 정렬 '''
# a = 'test'
# b = 123
# print('!{:<10}!{:^10}!{:>10}!'.format(a, a, a))
# print('!{:>5}!{:<5}!{:^5}!'.format(b, b, b))

''' 숫자 외에도 이름을 지정해서 데이터 위치 지정이 가능 '''
#print('{name}님의 나이는 {0}세 입니다'.format(40, name='tester'))

''' 영역 지정시 공백 채우기 '''
# print('!{:^10}!'.format('ID'))
# print('!{:=^10}!'.format('ID'))

'''
   {} 서식 문자에서 인덱싱 응용이나 데이터에 이름 붙여서
   위치를 지정하는 작업이 가능한데,
   python 3.6버전에서 해당 기능을 정식으로 만들어서 넣어주었다

   따옴표 앞에 f라는 알파벳을 붙여서 f-string이 적용된다 알려주고,
   따옴표 내부에는 {데이터} or {변수명} 등의 방식으로
   해당 중괄호에 어느 데이터가 출력되는지 지정
'''

# name = 'tester'
# age = 22
# print('{}님의 나이가 {}세 입니다'.format(name, age))
# print('내일이나 {}세가 되시겠네요'.format(age + 1))
# print('-'*50)
# print(f'{name}님의 나이는 {age}세 입니다')
# print(f'내일이나 {age + 1}세가 되시겠네요')

# money = 10000
# print(f'지불하실 요금은 <{money:10,}>원 입니다')

''' .count() - 문자열 '''
# a = 'Have a nice day'
# print(a.count('v'))
# print(a.count('e'))
# print(a.count('day'))


'''  .index() .find() - 문자열 내부의 특정 데이터 위치(index 번호) '''
# a = 'Have a nice day'
# print(a.index('v'))
# print(a.find('v'))
# print(a.index('a'))
# print(a.find('a'))
# print(a.index('day'))
# print(a.find('day'))
# #print(a.index('t'))
# print(a.find('t'))

''' join() - 문자열 삽입 '''
# a = '1234'
# print(', '.join(a))
# b = ['a', 'b', 'c', 'd']
# print('-'.join(b))

''' .upper() - 소문자를 대문자로 변경 '''
# a = 'hi!'
# print(a)
# print(a.upper(a))

# a = 'HELLO'
# print(a)
# print(a.lower())

''' .lstrip() - 문자열 왼쪽의 공백 문자를 제거 '''
# a = ' hi '
# print(f'!{a}!')
# print(f'!{a.lstrip()}!')
# print(f'!{a.rstrip()}!')
# print(f'!{a.strip()}!')

# b = '-test-'
# b = '- -test- -'
# print(f'{b}')
# print(f'{b.lstrip('- -')}')
# print(f'{b.rstrip('- -')}')
# print(f'{b.strip('- -')}')

# a = 'have a nice day'
# print(a)
# print(a.replace('h', 'H'))
# print(a.replace('nice', 'good'))
# print(a.replace(a[:5] + 'A' + a[6:]))

# a = 'have a nice day'
# b = '2025/12/31'
# print(a)
# print(a.split())
# print('-'*20)
# print(b)
# print(b.split('/'))

# su = [1, 2, 3, 4]
# print(su)
# print(type(su))

# a = [1, 2, 3]
# b = [1.1, 2.2, 3.3]
# c = ['a', 'b', 'c']
# d = [1, 2.22, 'test']
# print(a)
# print(b)
# print(c)
# print(d)

# a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# b = [1, 2.3, ['a', 'b', 'c']]
# print(a)
# print(b)

# a = [1, 2, 3, 4]
# print(a[1])
# print(a[-2])
# print(a[1:3])

# a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(a)
# print(a[1])
# print(a[1][2])
# print(a[-1][:2])

# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)
# print(a * 2)

''' 요소의 개수도 문자열과 마찬가지로 len() 함수로 확인 '''
# a = [1, 2, 3, 4]
# print(a)
# print(len(a))

# b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(len(b))

# a = [1, 2, 3, 4]
# print(a)
# a[2] = 20
# print(a)

''' del()함수 ㄱㄱㄱ '''
# a = [1, 2, 3, 4]
# print(a)
# del(a[1])
# print(a)
# del a[1]
# print(a)
# a = [1, 2, 3]
# print(a)
# a.append(100)
# print(a)
# a.append(12.345)
# a.append('test')
# a.append([10, 11])
# print(a)

# a = [1, 2, 3]
# print(a)
# a.insert(1, 100)
# print(a)

# a = [1, 2, 3, 4]
# print(a)
# a.remove(2)
# print(a)

# b = [1, 2, 3, 2, 4, 3]
# print(b)
# b.remove(2)
# print(b)

# a = [1, 2, 3, 4]
# print(a)
# a.pop()
# print(a)
# su = a.pop()
# print(a)
# print(su)

''' .count() '''
# a = [1, 2, 3, 2, 4]
# print(a)
# print(a.count(3))
# print(a.count(2))
# print(a.count(5))

# b = ['a', 'b', 'c', 'd']
# print(b)
# print(b.index('b'))
# print(b.index('c'))
# print(b.index(b[1]))
#print(b.index('z'))

# a = [1, 3, 2, 4, 6, 8, 7]
# print(a)
# a.reverse()
# print(a)

# a = [1, 3, 2, 4, 6, 8, 7]
# b = [1, 3, 2, 4, 6, 8, 7]
# print(a)
# a.sort()
# print(a)
# print('-'*30)
# print(b)
# b.sort(reverse=True)
# print(b)

''' .extend() - list 뒤에 list를 이어붙이는 함수(list 확장) '''
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a)
# a.extend(b)
# print(a)
# a.extend([7, 8, 9])
# print(a)

''' tuple rrr
    () 묶어낸다 tuple은~
    이 때, 필요에 따라 ()는 생략이 가능

    tuple은 내부 요소의 변경이 불가능하다
'''

# a = (1, 2, 3)
# b = 1, 2, 3
# c = (1, 2.22, 'test', ['a', 'b', 'c'])
# print(a)
# print(b)
# print(c)

# a = [10]
# print(a)
# print(type(a))

# a = (10)
# print(a)
# print(type(a))

# a = (10,)
# b = 10,
# print(a)
# print(type(a))
# print(b)
# print(type(b))

#a = (1, 2, 3)
#del a[1]
#a[1] = 100

'''''''''''''''''''''''''''''''''
    인덱싱과 슬라이싱은 동일하게 가능
'''''''''''''''''''''''''''''''''

# a = (1, 2, 3, 4)
# print(a)
# print(a[2])
# print(a[2:])

# a = (1, 2, 3)
# b = ('a', 'b', 'c')
# c = a + b
# d = b * 2
# print(c)
# print(d)

# a = (1, 'c', 2, 'z', 3, 4, 'test')
# print(a)
# print(len(a))

''' .index() 함수와 .count() 함수를 동일하게 사용 가능 '''
# a = 'test', 1.2323, 1, 'a', 1
# print(a.count('a'))
# print(a.index('a'))
# print(a.count(1))
# print(a.index(1))
# print(a.count(3))
# print(a.index(3))

'''
    dict
     딕셔너리(dictionary)
     {} 를 이용하여 여러 데이터들을 묶어주는데,
     딕셔너리의 요소는 key:value 형식으로 두 개의 데이터가
     하나의 요소로 저장된다

     key를 이용하여 value 데이터를 사용하는 형식의 자료형

     기존의 index 번호를 사용하는 자료형들은 각 요소에 접근 시
     index 번호로 접근하고, 메모리에서 연속된 메모리 구조를 갖는다

     딕셔너리는 key를 이용하여 value에 접근하고,
     메모리에서 해시 테이블(hash table) 구조를 갖는다
'''

# people = {'이름':'김앵주', '나이':36, '사는 곳':'서울시'}
# print(people)
# print(people['이름'])

# people = {'이름':'김앵주', '나이':37, '사는 곳':'서울시', '이름':'김용주'}
# print(people)

# dic = {1: 'one', 'two':2, 'list':[1,2,3,4]}
# print(dic)

# # test = {[1,2,3,4]:'list'}
# # print(test)

# a = 'have a nice day'
# a.upper()
# print(a)

# a = 123
# b = 456

# test = {(1,2,3,4):'list'}
# print(test)

''' 딕셔너리 요소 추가 및 제거 '''

# dic = {'1':'one'}
# print(dic)
# dic['2'] = 'two'
# del dic['1']
# print(dic)

'''
    .keys()

    .values()

    .items()
'''

# dic = {1:'one', 2:'two', 3:'three', 4:'four'}
# print(dic.keys())
# print(list(dic.keys()))
# print('-'*50)
# print(dic.values())
# print(list(dic.values()))
# print('-'*50)
# print(dic.items())
# print(list(dic.items()))

''' clear() '''
# dic = {1:'one', 2:'two', 3:'three', 4:'four'}
# print(dic)
# dic.clear()
# print(dic)
