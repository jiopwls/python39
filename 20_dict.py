# dict
# 비순차 자료구조
# 키를 통해 값을 찾는 연관배열 객체
# 선언방법은 {키:값} 형태로 정의하고 사용
# 다양한 자료형으로 구성된 데이터를
# 하나의 변수로 접근할 수 있음

# dict 선언
member = {'userid':'abc123' , 'password':'1q2w3e'}

# dict 값 조회 : 객체명['키명']
print(member['userid'])
print(member['password'])

# dict 모든 키 조회 : 객체명.keys()
# for ~ in 반복문으로 조회 가능
print(member.keys())

for key in member.keys():
    print(key, end=' ')

# dict 모든 값 조회 : 객체명.values()
print(member.values())

for key in member.values():
    print(key, end=' ')

# dict 모든 키와 값을 조회 1 : 객체명.items()
print(member.items())

for k, v in member.items():
    print(f'({k}, {v})', end=' ')


# dict 모든 키와 값을 조회 2 : 키 이용 (추천)
for k in member.keys():
    print(member[k], end=' ')
    # 값이 없을 경우 오류 발생


# dict 모든 키와 값을 조회 3 : 객체명.get(키) 이용 (추천!)
for k in member.keys():
    print(member.get(k), end=' ')
    # 값이 없을 경우 None 값 반환 (None = null)

# dict 동적 생성
user = {} # 사용자 - 이름, 나이, 이메일로 구성

# 객체명[새로운키] = 새로운 값
user['name'] = '홍길동'
user['age'] = 35
user['email'] = 'test@naver.com'

print(user)

# dict 동적 생성 2
user2 = dict(name='홍길순', age=30, email='test2@navercom')

print(user2)

# dict 동적 생성 3 : list 이용
user3 = [['name','홍길철'], ['age',33], ['email','test3@naver.com']]

print(dict(user3))

# dict 수정하기 : 객체명[기존키] = 새로운 값
user['age'] = 20
user['email'] = 'asdf@naver.com'

# dict 삭제 : del 객체명[기존키] - 키와 값 모두 삭제
del user['age']

print(user)

# 객체명.get(키) vs 객체명[키]
user['regdate'] # 존재하지 않는 키 호출 시 - 오류표시, 오류발생시 예외처리 코드로 적절히 대처

user.get('regdate') # 존재하지 않는 키 호출 시 - 오류표시x, 반환값이 None인지 여부에 따라 오류처리 대처

# ex1 dict 자료구조를 이용해서 학생 1명분의 데이터를 입력받아 처리
# 저장형식 : {'name':??, 'kor':??, 'eng':??, 'mat':??, 'tot':??, 'avg':??, 'grd':??}
name = int(input('이름?'))
kor = int(input('국어?'))
eng = int(input('영어?'))
mat = int(input('수학?'))
tot = kor + eng + mat
avg = int(tot) / 3
grd = '가'
if avg >= 90:
    grd = '수'
elif avg >= 80:
    grd = '우'
elif avg >= 70:
    grd = '미'
elif avg >= 60:
    grd = '양'

sj = {}
sj['name'] = name
sj['kor'] = kor
sj['eng'] = eng
sj['mat'] = mat
sj['tot'] = tot
sj['avg'] = avg
sj['grd'] = grd

print(sj)

# ex2 dict 자료구조를 이용해서 학생 3명분의 데이터를 입력받아 처리
# 저장형식 : {'name':??, 'kor':??, 'eng':??, 'mat':??, 'tot':??, 'avg':??, 'grd':??}

sjs = []

for _ in range(3):

    name = int(input('이름?'))
    kor = int(input('국어?'))
    eng = int(input('영어?'))
    mat = int(input('수학?'))

    tot = kor + eng + mat
    avg = int(tot) / 3
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'

    #데이터 저장
    sj = {'name':name, 'kor':kor, 'eng':eng, 'mat':mat, 'tot':tot, 'avg':avg, 'grd':grd}

    sjs.append(sj)

# 결과 출력
for sj in sjs:
    print(sj)

# dict 형식 데이터 출력시 예쁘게 표시 : pretty print
from pprint import pprint as pp

for sj in sjs:
    pp(sj)