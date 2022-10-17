# 다중 if문
# if~else만으로 다양한 조건을 판단하기 어려움
# => 물론 여러개의 if문을 사용해서 처리 하기도 함
# 다양한 조건에 따라 판단하기 위해서는
# if ~ elif ~ else 구문을 사용해야 함

# if 조건식1:
#    조건식1이 참일때 실행할 문장
# elif 조건식2:
#    조건식2이 참일때 실행할 문장
# ...
# else:
#    거짓일때 실행할 문장

# 결과 조건 : 점수 0 ~ 50 괜찮아요 /  51 ~ 80 잘했어요 /  81 ~ 100 최고예요
score = int(input('점수를 입력하세요.'))

# 들여쓰기를 조건에 따라 작성해야 함
if score <= 50: print('괜찮아요')
else:
    if score <= 80: print('잘했어요')
    else:
        if score <= 100: print('최고예요')

# 조건문장 작성시 들여쓰기를 일정하게 사용 -가독성 좋음
if score <= 50: print('괜찮아요')
elif score <= 80: print('잘했어요')
elif score <= 100: print('최고예요')

# 성적처리 프로그램v3
# 이름, 국어, 영어, 수학을 입력받아 총점, 평균 학점을 계산하고 출력함
# 학점처리 조건은 수우미양가
name = input('이름을 입력하세요')
kor = int(input('국어 점수를 입력하세요'))
eng = int(input('영어 점수를 입력하세요'))
mat = int(input('수학 점수를 입력하세요'))

sum = kor + eng + mat
score = sum / 3
grade = ''
if score <= 30: grade='가'
elif score <= 50: grade='양'
elif score <= 70: grade='미'
elif score <= 90: grade='우'
elif score <= 100: grade='수'

print(f'이름 :{name} 국어 :{kor} 수학 :{mat} 영어 :{eng}')
print(f'총점 :{sum} 평균 :{score} 등급 :{grade}')

# 연도를 입력받아 나이 계산후 나이에 따른 학생 분류 후 결과 출력
# ~ 7 유아 ~13 초등학생 ~16 중학생 ~ 19 고등학생 ~20 성인
import datetime

nowYear = datetime.datetime.now().year

years = int(input('태어난 연도 4자리를 입력해주세요.'))
age = nowYears - years
stu = '성인'
if age < 8: stu = '유아'
elif age <= 13: stu = '초등학생'
elif age <= 16: stu = '중학생'
elif age <= 19: stu = '고등학생'
print(f'{years}년도에 태어나셔서 현재 {age}살 {stu}이시네요.')

# 책 77쪽 항공사 짐 무게 측정
cargo = int(input('짐의 무게는 얼마입니까? (단위kg)'))
result = '수수료가 없습니다.'

if cargo >= 10: result = '1만원의 수수료가 발생합니다.'
print(f'짐의 무게는 {cargo}이고 {result}  ')

# 77쪽 항공사 짐 무게에 따른 수수료 계산
cargo = int(input('짐의 무게는 얼마입니까? (단위kg)'))
result = '수수료가 없습니다.'
pay = 0

if cargo >= 10:
    pay = (cargo //10) * 10000
    result = f'수수료는 {pay} 입니다.'