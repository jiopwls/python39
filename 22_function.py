# 함수function
# 주어진 입력값으로 무언가를 수행하고 결과물을 내놓는 객체
# 한번 작성해두면 언제든 재사용 가능
# 논리적인 단위 분할 가능 -> 개발의 분업화
# 코드의 구현을 외부로 부터 숨길수 있음 -> 캡슐화

# 함수 정의
# def 함수이름(매개변수):
#     함수몸체

# 함수 호출
# 함수이름(인수)

# 인사말 출력하는 코드1
print('안녕!')

# 인사말 출력하는 코드2 - 3번 반복
# print('안녕!')
# print('안녕!')
# print('안녕!')
for _ in range(3):
    print('안녕!!')

# 인사말 출력하는 코드3 - 3번 반복하는 코드를 3번 반복
# 복붙으로 해결 가능. 하지만 수정사항 발생시 유지보수 어려움
for _ in range(3):
    print('안녕!!')
for _ in range(3):
    print('안녕!!')
for _ in range(3):
    print('안녕!!')

# 인사말 출력하는 코드4 - 함수
def sayHello():
    for _ in range(3):
        print('안녕~')

sayHello()
sayHello()
sayHello()

# 매개변수parameter vs 인수argument
# 매개변수 : 함수 정의시 입력으로 전달된 값을 받는 변수
# 인수 : 함수 호출시 실제 입력으로 전달하는 값
def sayHello(msg):
    for _ in range(3):
        print(f'안녕~ {msg}')

sayHello('파이썬')
# 함수호출시 함수내부로 전달하는 실제값

sayHello('퇴근')

# ex 두 수를 입력받아 add라는 함수로 호출해서 결과 출력
# 단 add 라는 함수는 두 입력값을 더한 후 결과 출력함
def add():
    a1 = int(input('숫자를 입력하세요'))
    a2 = int(input('숫자를 입력하세요'))
    print(a1 + a2)

add()

def addNums(a,b):
    print(f'{a} + {b} = {a + b}')

a = int(input('숫자를 입력하세요'))
b = int(input('숫자를 입력하세요'))

addNums(a,b)

# 함수 다중정의 - overloading
# 동일한 이름의 함수를 매개변수에 따라 다른 기능으로 동작하도록 작성하는 것을 의미
# 파이썬에서는 공식적으로 지원하는 기능은 아님 - 구현가능
# 다중정의를 너무 남발하면 코드가 복잡해짐

# ex) 잔돈계산하는 프로그램을 함수로 작성
# 함수명: computeCharge(비용, 지불)
def computeCharge(cost, money):
    change = money - cost

    print(f'비용은 {cost:,d}원이고, 받은 금액은 {money:,d}원이며,\n잔액은 {change:,d}원입니다.')

    cash50000 = change // 50000
    change = change % 50000

    cash10000 = change // 10000
    change = change % 10000

    cash5000 = change // 5000
    change = change % 5000

    cash1000 = change // 1000
    change = change % 1000

    cash500 = change // 500
    change = change % 500

    cash100 = change // 100
    change = change % 100

    cash50 = change // 50
    change = change % 50

    cash10 = change // 10
    change = change % 10

    # 파이썬에서 제공

    ment = f'''
50,000원권은 {cash50000:d}장, 10,000원권은 {cash10000:d}장,
5,000원권은 {cash5000:d}장, 1,000원권은 {cash1000:d}장,
500원은 {cash500:d}개, 100원은 {cash100:d}개,
50원은 {cash50:d}개, 10원은 {cash10:d}개입니다.
    '''

    print(ment)

cost = int(input('비용: '))
money = int(input('지불금액: '))

computeCharge(cost, money)


# ex) 신용카드 판별하는 프로그램을 함수로 작성
# 함수명 : checkCredit(코드)
# dict 자료구조를 이용해서 작성

def checkCredit(code):
    cards = {'356317':'NH농협JCB카드', '356901':'신한JCB카드',
             '356912':'KB국민JCB카드', '404825':'비씨비자카드',
             '438676':'신한비자카드', '457973': '국민비자카드',
             '515594': '신한Master카드', '524353': '외환Master카드',
             '540926': '국민Master카드'}

    cardname = cards.get(code)

    if cardname == None: print('카드번호를 잘못 입력하셨습니다.')
    else: print(cardname)

code = input('조회할 카드번호는?')
checkCredit(code)


# 60갑자를 출력해주는 프로그램을 함수로 작성 / checkChinaZodiac(년도)

def checkChinaZodiac(year):
    baseYear = 1444
    ten = ('갑','을','병','정','무','기','경','신','임','계')
    twelve = ('자','축','인','묘','진','사','오','미','신','유','술','해')
    animal = ('쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지')

    t10idx = (year - baseYear) % 10
    t12idx = (year - baseYear) % 12

    print(f'{year}년은 {ten[t10idx]},{twelve[t12idx]}년{animal[t12idx]}의 해 입니다.')

year = int(input('년도는?'))
checkChinaZodiac(year)



