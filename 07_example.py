# 주민번호에서 생년과 월, 일, 성별을 추출해서 각 변수에 적절히 저장하시오
jumin = '202205092123456'

year = jumin[:4]
print(year)
month = jumin[4:6]
print(month)
day = jumin[6:8]
print(day)
gender = jumin[8]
print(gender)
print(('남성') if gender == 1 else('여성'))

# 시간계산
time = 123456789
days = time // 86400 #정수만 추출
print(days)

time = 98765
hours = time / 3600
print(hours)

time = 12345
mins = time // 60
print(mins)

# 잔돈계산 - 가격과 지불금액을 입력받아 잔돈 계산
# 지불금액은 ??원이고 받은금액은 ??원 이고 잔액은 ??원 입니다.
cost = int(input('가격을 입력하세요'))
pay = int(input('지불금액을 입력하세요'))
change = pay - cost
print((f'잔돈은 {change:d}원 입니다.') if cost < pay else ('전액 다 받았습니다. 감사합니다.'))
# 5만원 권 ? 장, 1만원 권 ? 장, 5천원 권 ? 장, 1천원 권 ? 장
# 500원 ? 개, 100원 ? 개, 50원 ? 개, 10원 ? 개 입니다.

w50k = change // 50000
change = change % 50000

w10k = change // 10000
change = change % 10000

w5k = change // 5000
change = change % 5000

w1k = change // 1000
change = change % 1000

w500 = change // 500
change = change % 500

w100 = change // 100
change = change % 100

w50 = change // 50
change = change % 50

w10 = change // 10
change = change % 10

text = f'''
가격은 {cost:,d}원이고,
받은금액은 {pay:,d}원이고,
잔돈은 {change:,d}원입니다.\n
50,000원권은 {w50k}장, 10,000원권은 {w10k}장,
5,000원권은 {w5k}장, 1,000원권은 {w1k}장,
500원은 {w500}개, 100원은 {w100}개,
50원은 {w50}개, 10원은 {w10}개입니다.'''

print(text)