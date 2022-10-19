# 내장함수
# don`t reinvent the wheel
# 파이썬에서 활용빈도 높은 기능을 함수로 미리 작성해둠
# 이러한 함수를 사용할때는 특별한 지시문 필요 x

# 숫자관련
abs(-10) #절대값
abs(10)

sum([10,20,30])   #요소 총합 계산

max([10,20,30]) #최대값 출력
min([10,20,30]) #최소값 출력

round(34.56)    #반올림
round(34.46)    #반올림

# 자료형 관련
type(10)
type(10.6)
type(True)

# 변환 함수
ord('A') # 유니코드 문자를 입력하면 코드값 출력
chr(65) # 코드값 입력하면 유니코드 문자 출력

# 정렬 함수
nums = [10, 7, 15, 4]
sorted(nums)    #오름차순 정렬
sorted(nums, reversed=True)    #내림차순 정렬
list(reversed(nums))    #순서 반전

# 묶음 함수 : zip
names = ['ㄱㄱ','ㄴㄴ','ㄷㄷ']
ages = [1,2,3]

man = list(zip(names,ages))
man

# 함수를 조건식에 적용 - filter, map
# ex) 1 ~ 100 사이 정수 중 짝수만 골라 리스트에 저장 : 소비
evens = []
for num in range(1, 100+1):
    if num % 2 == 0:
        evens.append(num)

print(evens)

# 짝수를 선별하는 코드를 함수로 캡슐화하고 다시 실행
def chk_evens(num):
    isEven = False
    if num % 2 == 0: isEven = True

    return isEven

evens = []
for num in range(1, 100 + 1):
    if chk_evens(num):
        evens.append(num)

# 짝수를 판별하는 함수를 filter 함수로 재적용
# filter(적용할 함수, 함수를 적용할 대상)
# 리턴값 : 조건을 만족하는 값
evens1 = list(filter(chk_evens, range(1, 100+1)))
print(evens1)

# 짝수를 판별하는 함수를 람다식으로 재적용
# 첫x 는 range의 첫번째 객체 1, 두번째x는 100+1
evens2 = list(filter(lambda x:x % 2 == 0, range(1, 100+1)))
print(evens2)

# ex2) 1~10사이 정수를 제곱해서 리스트에 저장
squares = []
for num in range(1, 10 + 1):
    val = num ** 2
    squares.append(val)

print(squares)

# 정수를 제곱하는 함수를 만들어 재적용
def squareNum(num):
    return num ** 2

squares = []
for num in range(1, 10 + 1):
    squares.append(squareNum(num))

# 정수를 제곱하는 함수를 map 함수로 재적용
# map(적용할 함수, 함수를 적용할 대상)
# 리턴값 : 함수를 적용한 값
sqr1 = list(map(squareNum, range(1, 10+1)))
print(sqr1)

# 정수를 제곱하는 함수를 람다식으로 재적용
sqr2 = list(map(lambda x:x ** 2, range(1, 10+1)))
print(sqr2)

# 열거형 데이터 다루기 : enumerate
# 순서있는 객체들을 다룰때 인덱스를 포함시켜 객체를 리턴해 줌
print(names) # 값만 출력

for n in names: # 값만 출력
    print(n)

for n in enumerate(names): # 값과 순서 출력
    print(n)

for idx, name in enumerate(names): # 값과 순서 출력
    print(idx, name)

# 사용자로부터 소문자를 입력받아 대문자로 변환
# 단, 숫자나 대문자 입력시 경고 출력
# 대문자 A : 65, 소문자 a : 97
while True:
    word = ord(input('영어 소문자 입력'))
    if word >= 97 and word <= 122:
        print(chr(word - 32))
    else:print('영어 소문자를 입력해주세요')

# 강사님 코드
# 변환 알고리즘 파악
ord('x')
chr(ord('x') - 32)

while True:
    ch = input('변환할 소문자 입력 / 종료를 원하면 느낌표를 입력')

    # 입력한 문자가 소문자인지 확인
    if 97 <= ord(ch) <= 122:
        nch = chr(ord(ch) - 32)
        print(f'입력한 {ch}의 대문자는 {nch}입니다')
    elif ch == '!' : break
    else: print('입력한 문자는 소문자가 아닙니다.')