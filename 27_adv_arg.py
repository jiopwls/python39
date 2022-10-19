# 함수 고급 기능 - 키워드 함수
# 함수 호출시 전달되는 값이 어떤 매개변수에 지정되는 지 결정 : 순서대로 할당
# 인수의 순서를 바꿔 함수를 호출할 수 있음

def addV1(a,b):
    print(f'{a} + {b} = {a+b}')

addV1(3,5)
addV1(a=3, b=5) # 인수가 전달될 매개변수명 지정
addV1(b=3, a=5) # 매개변수 순서 바꿔 호출


# 함수 고급 기능 - 디폴트 인수
# 함수 호출시 전달하는 값이 없을 경우
# 미리 설정해둔 값이 매개변수로 전달되도록 설정

def addV2(a = 4,b = 6):
    print(f'{a} + {b} = {a+b}')

addV2(10, 10)
addV2(10) # b매개변수에 미리 정해둔 6이 전달
addV2() # a,b 매개변수에 미리 정해둔 4,6 전달
addV2(b = 10) #a 매개변수에 미리 정해둔 4가 전달

# 함수 고급 기능 - 가변 인수
# 함수 정의시 매개변수의 갯수를 고정이 아닌 가변으로 설정
# 가변인수 선언시 args에 *라는 기호 사용

def addV3(a = 7, b = 4, *args):
    print(f'{a} + {b} + {args} = {a+b+sum(args)}')

addV3(3,5)
addV3(3,5,100)
addV3(3,5,100,1,2,4)