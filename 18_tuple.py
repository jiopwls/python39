# 튜플tuple
# 파이썬의 리스트와 유사한 자료구조 - 순서기억, 중복저장
# 선언방법은 ()안에 값들을 정의하고 사용
# 단, 튜플의 요소는 수정이나 삭제 불가 (생성은 가능)
# 주로, 읽기전용 데이터를 다룰때 사용 - 상수값 저장(변하지 않는)

# 튜플 선언
nums = (1,5,10,15,20)
print(nums)

# 튜플의 요소 읽기 - 객체명[인덱스]
print(nums[0], nums[3])

# 튜플의 요소 수정 - 객체명[인덱스] = 수정값
nums[0] = 999

# 튜플의 요소 삭제 - del 객체명[인덱스]
del nums[1]

# 만일, 튜플의 요소를 수정/삭제하려면
# 튜플을 리스트로 변환 - 값을 수정/삭제하고 다시 리스트를 튜플로 변환
# 변환함수 : list(객체명), tuple(객체명)
nums = list(nums) # 튜플 -> 리스트

nums[0] = 999
print(nums)

nums = tuple(nums) # 리스트 -> 튜플

BASE = 1444
ten = ('갑', '을', '병', '정', '무', '기', '경', '신', '임', '계')
twelve = tuple('자축인묘진사오미신유술해'[:])
# twelve = ('자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해')
animal = tuple('쥐 소 호랑이 토끼 용 뱀 말 양 원숭이 닭 개 돼지'.split(' '))
# animal = ('쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지')

year = int(input("연도 입력 : "))
i1 = (year - BASE) % 10
i2 = (year - BASE) % 12
print(f'{year}년은 {ten[i1]+twelve[i2]}년({animal[i2]}의 해)입니다.')