# 조건문
# 조건에 따라 프로그램의 실행 순서를 조정하는 문장
# '만약에 ~ 한다면 ~ 하고 아니면 ~ 하라' 라는
# 문제 해결시 주로 사용
# 조건문 내부의 실행문은 반드시 들여쓰기를 사용해야 함!

# if 조건식:
#    참일때 실행할 문장
# else:
#    거짓일때 실행할 문장

# ex)1 입력한 어떤 수가 짝수인지 판단하는 조건문
num = int(input("임의의 정수를 입력하세요."))

if num % 2 == 0:
    print('입력한 수는 짝수 입니다.')
else:
    print('입력한 수는 홀수 입니다.')

# ex)2 점수 3개를 입력받아 평균이 60 이상이고,
# 각 점수가 40점 이상이면 합격
num1 = int(input("첫번쨰 점수를 입력하세요."))
num2 = int(input("두번쨰 점수를 입력하세요."))
num3 = int(input("세번쨰 점수를 입력하세요."))

avg = (num1 + num2 + num3) / 3

if avg >= 60 and num1 >= 40 and num2 >= 40 and num3 >= 40:
    print('합격입니다.')
else: print('불합격입니다.')

is60 = avg >= 60
is40 = (num1 >= 40 and num2 >= 40 and num3 >= 40)

if is60 and is40:
    print('합격입니다.')
else: print('불합격입니다.')

# ex3) 입력한 어떤 수가 짝/홀 인지 판단하는 조건문
num = int(input('정수 하나를 입력하세요'))

if num % 2 == 0:
    print('짝수 입니다.')
else: print('홀수 입니다.')

# ex4) 아이디, 비번을 입력받고
# 미리 설정해둔 아이디, 비번과 일치하면 '로그인 성공' 아니면 실패라고 출력
uid = 'adc123'
pw = '1q2w3e'

in_id = input('아이디를 입력하세요')
in_pw = input('비밀번호를 입력하세요')

sameId = uid == in_id
samePw = pw == in_pw

if sameId and samePw:
    print('로그인 성공')
else: print('로그인 실패')