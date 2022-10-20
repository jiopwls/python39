# 컨프리헨션comprehension - 축약표기
# 다양한 데이터 객체에 사용하는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원

# 파이썬에는 4가지 축약을 지원
# list(py2), set(py3), dict(py3), generator(py3)

# 리스트에 적용하는 축약
# 1 ~ 10까지의 정수를 생성해서 리스트에 저장
a = list(range(1, 10+1))
print(a)

b = []
for i in range(1,10+1):
    b.append(i)

print(b)

# list for 축약문
# [표현식 for 항목 in 반복가능개체]
c = [i for i in range(1,10+1)]
print(c)

# ex) 1 ~ 20 사이 정수 중 짝수를 리스트로 생성
d = []
for i in range(2,20+1, 2):
    d.append(i)

print(d)

e = [i for i in range(2, 20+1, 2)]
print(e)

# ex) 1 ~ 10 사이 정수를 제곱한 값을 리스트로 생성
f = []
for i in range(1, 10 + 1):
    f.append(i ** 2)

print(f)

g = [i ** 2 for i in range(1, 10 + 1)]
print(g)

# ex) 아래 각각의 리스트를 이용해서 제곱값을 계산하고
# 새로운 리스트에 생성하세요
val1 = [1, 2, 3, 4, 5]
val2 = [1, 2, 'A', False, 9, 100]

h = []
for v in val1:
    h.append(v ** 2)
print(h)

i = [v ** 2 for v in val1]
print(i)

j = [v ** 2 for v in val2] # 오류발생. 문자, bool은 제곱이 안되니깐
print(j)

# 변수 유형 확인 : type(대상)
print(type(1), type('a'), type(False))

# 조건식을 이용해서 재작성 - 정수일 경우 제곱 연산

k = []
for v in val2:
    if type(v) == int:
        k.append(v ** 2)
print(k)

# for if 축약문  [표현식 for 항목 in 반복가능개체 if조건]
l = [v ** 2 for v in val2 if type(v) == int]
print(l)

# 1 ~ 60 사이 정수 중 홀수만 골라 리스트에 저장
#mnopqrstuv
m = [i for i in range(1, 60+1, 2)]
print(m)

# 1 ~ 60 사이 정수 중 5의 배수만 골라 리스트에 저장
n = [i for i in range(1, 60+1) if i % 5 == 0]
print(n)

# 1 ~ 100 사이 정수중 임의의 정수가 짝수면 'even' 홀수면 'odd'라고 구분해서 리스트에 저장
o = []
for i in range(1, 100+1):
    if i % 2 == 0: val = 'even'
    else: val = 'odd'
    o.append(val)
print(o)

# for 다중 if 축약문 [표현식1(참일떄 적용) if 조건 else 표현식2(거짓일때 적용) for 항목 in 반복가능개체]

import random as rnd

p = ['even' if i % 2 == 0 else 'odd' for i in range(1, 100)]

print(p)

# 구구단 중 7, 8단의 결과값을 리스트에 저장

q = []
for i in range(7, 8+1):
    for j in range(1, 9+1):
        print(f'{i} x {j} = {j*j}')
        q.append(i * j)

print(q)

# 중첩 for 축약 [for 항목1 in 반복가능개체1 for 항목2 in 반복가능개체2]
gugu = [i * j for i in range(7, 8+1)
                for j in range(1, 9+1)
        ]
print(gugu)

# name, grd 리스트의 값들을 각각의 키와 값으로 딕셔너리에 저장
name = ['혜교','지현','수지']
grd = ['우','미','수']

# 단순하게 작성
# 새로운 dict요소 생성 : 객체명[키이름] = 값
s = {}
s[name[0]] = grd[0]
s[name[1]] = grd[1]
s[name[2]] = grd[2]

print(s)

# 반복문으로 재작성
s = {}
for i in range(len(name)):
    s[name[i]] = grd[i]
print(s)

# 딕셔너리 for 축약문 {키값표현식 for k,v in zip(반복가능객체1, 반복가능객체2)}
sj = {k:v for k, v in zip(name, grd)}
print(sj)

# 학생과 국어점수에 대한 리스트가 있을때
# 학생은 키로, 합격여부를 값으로 하는 딕셔너리 객체를 생성
# 단, 합격여부에는 국어점수가 85점이상인 경우 '합격'
# 그외는 '불합격'이라고 출력함
name = ['철수','영희','길동','꺽정']
kor = [50, 80, 90, 60]

t = {}
for i in range(len(name)):
    if kor[i] >= 85: val = '합격'
    else: val = '불합격'
    t[name[i]] = val
print(t)

# 딕셔너리 for if 축약문 {키:표현식1 if 조건식 else 표현식2 for k,v in zip(반복가능객체1, 반복가능객체2)}
t = {k:'합격' if v >= 85 else '불합격' for k, v in zip(name, kor)}
print(t)

# p111 문제3
message = ['spam', 'ham','spam', 'ham','spam']

#1
q = [1 if i == 'spam' else 0 for i in message]
print(q)

#2
def makeDummy(x):
    val = 0
    if x == 'spam': val = 1
    return val

dummy = list(map(makeDummy, message))
print(dummy)

# spam만 추출
#1
q = [i for i in message if i == 'spam']
print(q)
#2
spams = []
for m in message:
    if m == 'spam':
        spams.append(m)
print(spams)
#3
def makeSpams(x):
    isSpam = False
    if x == 'spam': isSpam = True
    return isSpam

list(filter(makeSpams,message))

list(filter(lambda x:x == 'spam', message))