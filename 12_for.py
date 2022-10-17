# 반복문
# 정해진 횟수 만큼 특정코드를 실행하도록 만든 문장
# 파이썬에서는 for문과 while문이 지원

print('Hello, World!!') # 한번 출력

print('Hello, World!!') # 3번 출력
print('Hello, World!!')
print('Hello, World!!')

# 만일, 100번 출력해야 한다면 복붙을 계속할 것인가?
# 또한, 반복시 출력하는 문구가 변경된다면? - 다시 수정
# 효율적인 반복실행을 위해서 반복문을 사용함

# for 반복변수 in range(시작값, 종료값-1, 증감값):

# range함수 사용하기
# range(숫자) - 0 부터 -1까지의 범위
list(range(10))

# range(시작, 끝+1) - 시작값부터 끝값 +1 까지의 범위
list(range(1, 10+1))

# range(시작, 끝-1, 증감값) - 시작값부터 증감값을 처리
list(range(0, 11, 2))

for i in range(1,10+1):
    print(i, end=', ')

# 100 ~ 1 사이 정수 출력
list(range(100, 0, -1))

# 1 ~ 100 사이 정수 중 짝수만 출력
list(range(2, 101, 2))

for i in range(2,100+1,2):
    print(i,end=', ')

for i in range(1, 100+1):
    if i % 2 == 0: print(i, end= ' ')

# 1 ~ 100사이 정수들의 합을 계산 후 출력
sum = 0
for i in range(1, 100+1):
    sum = sum + i
    print(sum)

# 가우스 덧셈 공식을 이용해 1 ~ 100 사이 모든 정수들의 합 계산 후 출력
((1 + 100) * (100 - 1 + 1)) / 2


# 문자열 반복 -> 문자 하나씩 출력
for i in '안녕 파이썬':
    print(i, end='')

# 단을 입력받아 해당 단의 구구단을 출력
dan = int(input('구구단 정수를 입력하세요: '))
for i in range(1, 10):
    print(f'{dan} X {i} = {dan * i}')

# 79쪽 문제3
sum = 0
result = ' '
for i in range(1,100+1):
    if i % 3 == 0 and i % 2 !=0:
        result += str(i) + ' '
        sum += i

print(result)
print(sum)