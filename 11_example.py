# 33. 임의의 숫자 6자리를 입력하면 신용카드의 종류와 은행정보를
# 출력하는 프로그램을 작성해보세요.  (CardCheck)
# 35(JCB카드)
# 356317 - NH농협카드, 356901 - 신한카드, 356912 - KB국민카드
# 4(비자카드)
# 404825 – 비씨카드, 438676 – 신한카드, 457973 – 국민은행
# 5(마스타카드, Maestro)
# 515594 – 신한카드, 524353 - 외환카드, 540926 – 국민은행
card = input('신용카드 번호는?')
result = ''

if card[:2] == '35':
    nums = card[2:] # 나머지 카드 번호 추출
    if nums == '6317': result = 'NH농협카드'
    elif nums == '6901': result = '신한카드'
    elif nums == '6912': result = 'KB국민카드'
    else: result = '잘못된 카드번호 입니다.'
elif card[:1] == '4':
    nums = card[1:]  # 나머지 카드 번호 추출
    if nums == '6317':
        result = 'NH농협카드'
    elif nums == '6901':
        result = '신한카드'
    elif nums == '6912':
        result = 'KB국민카드'
    else:
        result = '잘못된 카드번호 입니다.'
elif card[:1] == '5':
    pass
else:
    result = '잘못된 카드번호입니다.'

# 시간때
daytime = input('시간때를 의미하는 영단어 입력')
result = '잘못입력'

if daytime == 'morning hours'         : result = '아침시간(7~12)'
elif daytime in ('midday', 'noon')    : result = '점심시간 (12-1)'
elif daytime == 'afternoon hours'     : result = '오후 (1-6)'
elif daytime == 'evening hours'       : result = '저녁시간 (6-9)'
elif daytime == 'night hours'         : result = '밤시간 (9-12)'
elif daytime == 'midnight'            : result = '자정시간 (12)'
elif daytime == 'early morning hours' : result = '새벽시간 (12-5)'
elif daytime == 'small hours'         : result = '새벽 (1-3)'
elif daytime in ('dawn', 'daybreak')  : result = '해뜰력 (5-7)'
print(f'{daytime}는 {result}')
# switch ~ case 와 비슷하게 작성해보기
# 파이썬은 v3.9까지 switch ~ case 구문 지원x
# 만약 switch ~ case 구문을 구현하려면 dict를 사용
# 한편 v3.10 이상부터는 match case라는 구문으로 구현 가능

# dict 자료구조
# 키와 값 형태로 자료를 저장하는 형식
# 연관(키-값) 배열 자료형의 한 종류
# 객체명 = {키 : 값} => 객체 명.get(키), 객체명[키]

cards = {'356317':'NH농협카드',
         '404825':'비씨카드',
         '515594':'신한카드'
         }
cards.get('404825')

print('''\
성적 처리프로그램 v3b
-------------------''')
name = input('이름 : ')
kor = int(input('국어 : '))
eng = int(input('영어 : '))
mat = int(input('수학 : '))

tot = kor + eng + mat
avg = tot/3
grd = '가'
grds = {
    10 : '수',
     9 : '수',
     8 : '우',
     7 : '미',
     6 : '양'
}
grd = grds.get(avg//10)
print(f'''\
이름:{name:s}\n국어:{kor:3d}점, 영어:{eng:3d}점, 수학:{mat:3d}점
총점:{tot:3d}점, 평균:{avg:.1f}점, 학점은 {grd:s}입니다.''')

# 3항 연산자 - if 단축문
# 참일때값 if 조건식 else 거짓일때 값
print('참' if True else '거짓')
print('참' if False else '거짓')

# ex) 윤년여부를 출력하는 프로그램, 3항 연산자로.
year = int(input('연도는'))

isLeapYear = (year % 4 == 0 and year % 100 !=0) or year % 400 == 0
result = '는 윤년입니다.' if isLeapYear else '윤년이 아닙니다.'

print(year, result)

# 년도와 월을 입력받아 윤년여부와 입력한 달의 마지막 날을 출력하는 프로그램
# 30 : 4, 6, 9, 11
# 31 : 1, 3, 5, 8, 10, 12
# 28, 29 : 2 (윤년여부에 따라 다름)




