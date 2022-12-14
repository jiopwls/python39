# 함수 결과 반환하기 : return
# 호출한 함수 내부에서 어떤 처리를 한 후,
# 함수를 호출한 대상에게
# 그 결과를 반환하기 위해 사용하는 명령문

# return [변수 또는 식, ...]

# 간단한 인삿말 함수
def sayHi(msg):
    print(f'안녕,{msg}')

sayHi('하이')
sayHi('hi')

# 위 함수는 결과를 print 하고 종료하기 때문에 다른 함수가 이것을 활용할 여지가 없음 - 확정성x
# 함수의 결과를 외부로 넘겨서 다른 코드가 처리하도록 개선

def sayHi2(msg):
    return f'안녕,{msg}'

print(sayHi2('asdf'))
print(sayHi2('asdf') + 'ㄱㄴㄷㄹ')

# 다중값 반환
# 다른 프로그래밍 언어와는 달리 파이썬의 함수는
# 여러 개의 결과를 그대로 반환할 수 있음
# 단, 반환값들은 튜플형태로 전달됨
def addsubmildiv(a, b):
    r1 = a + b
    r2 = a - b
    r3 = a * b
    r4 = a / b
    return r1, r2, r3, r4 # 4개의 결과를 튜플로 리턴

addsubmildiv(10,5)

result = addsubmildiv(10, 5)
print(result[3], result[2], result[1], result[0])

# 함수의 반환값이 여러 개인 경우 unpack기능을 이용해서
# 미리 선언된 여러 개의 변수에 나눠 초기화 할수 있음
# 언팩시 변수 갯수와 반환될 값의 개수는 반드시 일치해야 함!

plus, minus, multi, div = addsubmildiv(10, 5)
print(plus, minus, multi, div)


