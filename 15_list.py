# 파이썬 자료구조
# 자료구조는 대량의 데이터를
# 효율적으로 저장,조회,수정,삭제하기 위해
# 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리

# 성적프로그램 v2
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 단, 3명의 학생에 대해 성적처리를 진행함
# 변수 초기화
name1, name2, name3 = '소희', '예지', '지현'
kor1, kor2, kor3 = 90, 80, 70
# .... 처리할 데이터 갯수에 따라 변수를 일일이 선언해야 함 - 불편, 성적처리시에도 동일한 코드 반복 작성 - 번거로움
# tot1 = kor1 + eng1 + mat1
# tot2 = kor2 + eng2 + mat2
# tot3 = kor3 + eng3 + mat3

#이러한 문제를 해결하기 위해 자료구조와 관련된 기술을 사용

# 리스트list
# 다른 프로그래밍 언어에서는 배열array과 유사
# 동일한(동일하지 않은) 형식의 데이터를
# 1차원 형태로 순차적으로 저장하는 자료구조 (중복 허용)
# 선언방법은 값들을 []안에 정의하고 사용
# 리스트의 각 요소에 접근(참조)하려면 변수[인덱스] 형식을 사용

#점심메뉴를 리스트로 정의
menus = ['라면','돈까스','짜장면','냉면','정식']
print(menus)

# 리스트에서 일부만 출력
print(menus[0], menus[3])

# 리스트의 모든 요소 출력
print(menus[0], menus[1], menus[2], menus[3], menus[4], menus[5])

# 리스트의 모든 요소를 반복문으로1
#for i in range(5):
for i in range(len(menus)): #len(대상) : 요소 갯수 출력
    print(menus[i], end=' ')

# 리스트의 모든 요소를 반복문으로2
# for 변수 in 객체
# 리스트의 요소를 하나씩 훑어가며 출력
for menu in menus:
    print(menu, end=' ')

# 동적으로 리스트 생성하기
menus = [] # 빈 리스트 선언

# list에 요소를 추가하려면 append 함수
# append한 요소는 list의 맨 뒤에 부착
menus.append('닭가슴살')
menus.append('고구마')
menus.append('밥')
menus.append('오트밀')
menus.append('물')

# 지정한 위치에 새로운 요소 추가 insert(인덱스, 값)
menus.insert(1,'아몬드')
print(menus)

# list 요소 값 수정 : 객체명[인덱스] = 새로운값
menus[4] = '고기'
print(menus)

# list 요소 값 삭제 : remove(값), pop(인덱스)
menus.remove('고기')
menus.pop(4)
print(menus)

# list 요소 값 삭제 : pop() - 맨 뒤부터 삭제
menus.pop()
print(menus)

# list 다양한 데이터 다루기
datas = []

datas.append(1)
datas.append(2.5)
datas.append(True)
datas.append('안녕')
datas.append([1,4,5])

print(datas)

# 성적프로그램 v2
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 단, list를 이용해서 학생 3명에 대한 성적처리
names = ['소희','지현','수지']
kors = [100,90,80]
engs = [100,90,80]
mats = [100,90,80]
tots = [0,0,0]
avgs = [0,0,0]
grds = ['가','가','가']

# 성적처리1
tots[0] = kors[0] + engs[0] + mats[0]
tots[1] = kors[1] + engs[1] + mats[1]
tots[2] = kors[2] + engs[2] + mats[2]

avgs[0] = tots[0] / 3
avgs[1] = tots[1] / 3
avgs[2] = tots[2] / 3

if avgs[0] >= 90: grds[0] = '수'
elif avgs[0] >= 80: grds[0] = '우'
elif avgs[0] >= 70: grds[0] = '미'
elif avgs[0] >= 60: grds[0] = '양'

if avgs[1] >= 90: grds[1] = '수'
elif avgs[1] >= 80: grds[1] = '우'
elif avgs[1] >= 70: grds[1] = '미'
elif avgs[1] >= 60: grds[1] = '양'

if avgs[2] >= 90: grds[2] = '수'
elif avgs[2] >= 80: grds[2] = '우'
elif avgs[2] >= 70: grds[2] = '미'
elif avgs[2] >= 60: grds[2] = '양'

# 결과출력
print(names[0], kors[0], engs[0], mats[0], tots[0], avgs[0], grds[0])
print(names[1], kors[1], engs[1], mats[1], tots[1], avgs[1], grds[1])
print(names[2], kors[2], engs[2], mats[2], tots[2], avgs[2], grds[2])

# 성적처리 2
for i in range(len(names)):
    tots[i] = kors[i] + engs[i] + mats[i]
    avgs[i] = tots[i] / 3
    if avgs[i] >= 90: grds[i] = '수'
    elif avgs[i] >= 80: grds[i] = '우'
    elif avgs[i] >= 70: grds[i] = '미'
    elif avgs[i] >= 60: grds[i] = '양'

# 결과출력 2
for i in range(len(names)):
    print(names[i], kors[i], engs[i], mats[i], tots[i], avgs[i], grds[i])


# p110 1,2
lst = [10, 1, 5, 2]

# lst 를 2배 생성 후 result에 저장
result = lst * 2
print(result)

# 방법2
result = []
for _ in range(2):
    result += lst
print(result)

# lst 첫번쨰 요소에 *2 한 후 result 에 저장
result.append(lst[0] * 2)
print(result)

# result의 홀수요소만 추출 -> result2에 저장 / 첫번째 요소, 세번째 요소 ...
result2 = []
result2.append(result[1])
result2.append(result[3])
result2.append(result[5])
result2.append(result[7])
print(result2)

# result의 홀수요소만 추출2 -> result2에 저장
result2 = []
#for i in range(1, 8, 2):
for i in range(1, len(result), 2):
    result2.append(result[i])
print(result2)

# result의 홀수 요소만 추출 3 - 리스트 슬라이스
result2 = result[1::2]
print(result2)


# p110 ex2) A
import random as rnd

lst = []
size = int(input('리스트의 크기는?'))

for i in range(size):
    val = rnd.randint(1, 10)
    print(val)
    lst.append(val)

print(f'리스트의 크기는 {len(lst)}')
# p110 ex2) B
lst = []
size = int(input('리스트의 크기는?'))

for i in range(size):
    val = rnd.randint(1, 10)
    print(val)
    lst.append(val)

key = int(input('리스트에서 찾을 값은?'))

# 검색기능 1
isFind = 'No'
for i in range(size):
    if lst[i] == key: isFind = 'YES'
print(isFind)

# 검색기능 2
isFind = 'No'
for val in lst:
    if val == key: isFind = "Yes"
print(isFind)

# 검색기능 3
isFind = 'No'
if key in lst: isFind = "Yes"
print(isFind)


# employees.csv를 이용해서 사원정보를 입력하면
# list에 각각 저장하는 코드를 작성하세요
# 사번empno, 이름fname, 성lname, 이메일email,
# 입사일hdate, 직책jobid, 급여sal, 부서번호deptid
empnos = []
fnames = []
lnames = []
emails = []
hdates = []
jobids = []
sals = []
deptids = []

empno = input('사원번호는?')
fname = input('이름은?')
lname = input('성은?')
email = input('이메일?')
hdate = input('입사일?')
jobid = input('직책은?')
sal = input('급여?')
deptid = input('부서번호?')

empnos.append(empno)
fnames.append(fname)
lnames.append(lname)
emails.append(email)
hdates.append(hdate)
jobids.append(jobid)
sals.append(sal)
deptids.append(deptid)

# 저장된 모든 사원정보 출력
for i in range(len(empnos)):
    print(f'{empnos[i]} ,{fnames[i]} ,{lnames[i]} ,{emails[i]}'
          f'{hdates[i]} ,{jobids[i]} ,{sals[i]} ,{deptids[i]}')

# 다루어야 할 데이터의 항목수가 많을수록 일일이 리스트로 선언해서 저장하는 것은 불편
# -> 딕셔너리, 클래스를 이용하면 편리하게 다룰수 있음

# 2차원 리스트
# 리스트 선언시 요소의 자료형에는 제약이 없음
# 따라서 리스트의 요소로 리스트 자체를 구성할 수 있음

# a,b,c 반 학생의 성적 데이터를 리스트로 구현
# 리스트의 요소로 사용하는 리스트의 길이는 일정하지 않아도 됨
score = [[12,45,23,78],
         [37,63,44,25,80],
         [36,12,37]]

print(score)

# 2차원 리스트 출력하기 1
for i in range(len(score)):
    print(score[i])

# 2차원 리스트 출력하기 2
for sc in score:
    print(sc)

# 2차원 리스트 출력하기 3
for sc in score:
    for s in sc:
        print(s, end=' ')
    print() # 요소 리스트 모든 값 출력 후 줄바꿈

# 2차원 리스트 동적 생성
# 전체 리스트 크기를 사용자로부터 입력
# 요소로 사용하는 리스트의 크기는 난수로 생성
# 요소 리스트를 구성하는 값 역시 난수로 생성
import random as rnd

lsts = []
size1 = int(input('리스트의 크기는?'))

for i in range(size1):
    lst = []
    size2 = rnd.randint(1,10)
    for j in range(size2): # 리스트안 리스트에 값 생성
        val = rnd.randint(50,100)
        lst.append(val)
    lsts.append(lst)