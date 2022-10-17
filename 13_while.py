# while 반복문
# 횟수와는 상관없이 조건에 따라 반복실행하는 반복문
# 즉, 조건식의 결과가 참이면 실행하고, 거짓일 경우 실행을 중단함

# 변수초기화
# while 조건식:
#    반복실행할 문장
#    증감식

i = 1
while i <=30:
    print(i, end=' ')
    i += 1

# 1 ~ 100 사이 홀수 출력
i = 1
while i <= 100:
    if i % 2 != 0:
        print(i, end=' ')
        i += 1
# 1 ~ 100 사이 짝수 출력
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i, end=' ')
        i += 1

# 1 ~ 100 정수의 모든 합 계산 후 출력
i = 1
hap = 0
while i <= 100:
    hap += i
    i += 1

print(hap)

# ex) 단을 입력받아 해당 단의 구구단을 출력
dan = int(input('구구단 정수를 입력하세요: '))
i = 1
while i <= 9:
    print(f'{dan} X {i} = {dan * i}')
    i += 1

# p79 ex3) 3의 배수지만 2의 배수는 아닌 정수 출력하고 누적합도 계산해서 출력
hap = 0
result = ''
i = 1
while i <= 100:
    if i % 3 == 0 and i % 2 != 0:
        result += str(i) + ' '
        hap += i
    i += 1
print(result)
print(f'합: {hap}')

# 무한루프
# 반복문의 조건식이 언제나 참이면
# 반복을 중단하지 않고 계속 반복을 지속하는 상황
# 단, 무한루프에서 탈출하려면 break를 이용
# while True:
#    반복실행할 문장

# 반복실행 중지 : break
# 반복 실행을 중지하고 반복문에서 나올때 사용

# 1 ~ 100 사이 정수들의 모든 합 계산 후 출력
# 단 무한루프와 break를 이용

i = 1
hap = 0
while True:
    if i <= 100: hap += i
    else: break
    i += 1

print(hap)

# 1 ~ 1000 사이 모든 정수의 합을 출력
# 단 누적합이 15000을 넘으면 반복문 중지후 결과 출력
i = 1
hap = 0
while True:
    if hap >=15000: break
    elif i <=1000: hap += i
    i += 1

print(i,hap)

# 방법2
i = 1
hap = 0
while i <= 1000:
    if hap > 15000: break
    hap += i
    i += 1

print(i,hap)

# while문과 break 사용

main_menu = f"""
성적처리 프로그램
-=-=-=-=-=-=-=-=-=
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
-=-=-=-=-=-=-=-=-="""

while True:
    print(main_menu)
    menu = input('작업을 선택하세요 : ')
    if menu == '0':
        print('성적 프로그램을 종료합니다.')
        break
    elif menu == '1': print('성적 데이터 추가')
    elif menu == '2': print('성적 데이터 조회')
    elif menu == '3': print('성적 데이터 상세조회')
    elif menu == '4': print('성적 데이터 수정')
    elif menu == '5': print('성적 데이터 삭제')
    else: print('잘못된 번호를 입력하셨습니다.')


# 반복 실행시 특정 코드 회피 -> continue
# 반복 실행을 유지하면서 특정 코드블럭의 실행을 생략하고 싶을때

# ex) 1~100사이의 모든 정수의 합을 출력
# 단 7의 배수나 9의 배수는 제외하고 누적합
i = 0
hap = 0

while i<=100:
    i += 1
    if i % 7 ==0 or i % 9 ==0: continue
    hap += i # 상황에 따라 실행될수도 않될수도 있음

    print(hap)

# ex4) 아이디, 비번을 입력받고
# 미리 설정해둔 아이디, 비번과 일치하면 '로그인 성공' 아니면 실패라고 출력
uid = 'adc123'
pw = '1q2w3e'

while True:
    in_id = input('아이디를 입력하세요')
    in_pw = input('비밀번호를 입력하세요')

    if uid == in_id and pw == in_pw:
        print('로그인 성공')
        break
    else:
        print('로그인 실패')


# 난수 생성하기
# 파이썬에서 난수를 생성하려면 random 패키지 이용
# 생성방법 : 패키지명.random.randint(시작값, 끝값)
import random as rnd # 별칭으로 패키지명 줄여씀

rnd.seed(202210171044) #난수새성 초기값 지정
# 1 ~ 10 사이 임의의 정수 생성
print(rnd.randint(1,10))

# 1 ~ 45 사이 임의의 정수 6개 생성
for i in range(6):
    print(rnd.randint(1,45), end=' ')

# i(인덱스)값이 필요 없을땐 _ 언더바 이용
for _ in range(6):
    print(rnd.randint(1,45), end=' ')

# p78 숫자 맞추기 (1~10)
i = rnd.randint(1, 10)

while True:
    myNum = int(input('1 ~ 10 중 번호 입력'))
    if i == myNum:
        print('정답')
        break
    else: print('실패')

# 복권 프로그램 - 3자리수 난수 생성/ 사용자 입력
# 100~ 999 위치 상관x 문자열 슬라이싱을 위한 문자열 변환 str 함수 사용
lotto = str(rnd.randint(100, 999))
# lotto1 = str(rnd.randint(100, 999))
# lotto2 = str(rnd.randint(100, 999))
# lotto3 = str(rnd.randint(100, 999))
# lotto = lotto1 + lotto2 + lotto3
print(lotto[:0])
print(lotto[:1])
print(lotto[:2])
print(lotto[:3])

match = 0 # 일치여부 저장
myNum = str(input('3자리 수 입력 100 ~ 999'))
# 1 자리 비교
if myNum[0] == lotto[0] or myNum[1] == lotto[0] or myNum[2] == lotto[0]:
    match += 1

# 2 자리 비교
if myNum[0] == lotto[1] or myNum[1] == lotto[1] or myNum[2] == lotto[1]:
    match += 1

# 3 자리 비교
if myNum[0] == lotto[2] or myNum[1] == lotto[2] or myNum[2] == lotto[2]:
    match += 1

# 개선된 코드 1
for i in range(3):
    if myNum[0] == lotto[i] or myNum[1] == lotto[i] or myNum[2] == lotto[i]:
        match += 1

# 개선된 코드 2
for i in range(3):
    for o in range(3):
        if myNum[o] == lotto[i] :
            match += 1



# 당첨 여부 판단
if match == 3: print('3개 일치')
elif match == 2: print('2개 일치')
elif match == 1: print('1개 일치')
else: print('0개 일치')

print(myNum, lotto, match)



while True:
    myNum = str(input('100 ~ 999 중 번호 3자리 입력'))
    if myNum == i[:3]:
        print('3개 일치')
    elif myNum == i[:2] or myNum == i[1:3] or (myNum == i[1] and myNum ==i[3]):
        print('2개 일치')
    elif myNum == i[1] or myNum == i[2] or myNum == i[3]:
        print('1개 일치')
    else: print('0개 일치')
