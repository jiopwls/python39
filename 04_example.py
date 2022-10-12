#1
# 프로그래밍 언어 실습시 글꼴은 고정폭 글꼴을 사용할 것을 추천
print('*' + '\t' + '*'  + '\t' +' ** ' + '\t' + '****' + '\t' + '****' + '\t' + '*' + '\t' + '*' + '\t' + '\t' + '/////')
print('*' + '\t' + '*' + '\t' + '*  ' + '*' + '\t' + '*'+ '\t' + '*' + '\t' + '*' + '\t' + '* ' +'  *' + '\t' + '*' + '\t' + '   | o o |')
print('*****' + '  *' + '\t' + '*' + '\t' + '**** ' + '\t' + '****'  + '\t' + ' * *' + '\t' + '  (|  ㅅ |)' )
print('*' + '\t' + '*' + '  ******' + '\t' + '*  ' + ' *' + '\t' + '*  ' + ' *' + '\t' + '  *' + '\t'+ '\t' + '   | ___ |')
print('*' + '\t' + '*' + '  *' + '\t' + '*' + '\t' + '*' + '\t' + ' *' + '\t'+ '*' + '\t' + ' *' + '\t'+'  *' + '\t' + '\t' + '\t' +'-----')

#3
print('rate1', 'TImeLimit', 'long', 'numberOfWindows')

#4
x, y, z = 1, 2, 3
s0, v0, t, g = 4, 5, 6, 9.8
print(3 * x, 3 * x + y, (x + y) / 7)
print(s0 + v0 * t + (1/2)*g*t**2)

#5

#6
x, y, m, n = 2.5, 1.5, 18, 4
print( x + n * y - (x + n) * y)
print(m/n + m % n)
print(5 * x - n / 5)
print(1 - ( 1 - ( 1 - ( 1 -( 1 - n)))))

#7
print(3 + 4.5 * 2 + 27 / 8)

# || = or, && = and 논리연산시 경우에 따라 단축식 평가가 적용되기도 함
print(True or False and 3 < 4 or not(5 == 7))
print(True or (3 < 5 and 6 >= 2))
# print(not True > 'A')
print(not True > bool('A')) #not (True > True)
# print(7 % 4 + 3 - 2 / 6 * 'Z')
print(7 % 4 + 3 - 2 / 6 * bool('Z'))
# print('D' + 1 + 'M' % 2 / 3)
print( bool('D') + 1 + bool('M') % 2 / 3)

print( (4 < 6) or True and False or False and (2 > 3))



#9
print(True and False and True or True)
print(True or True and True and False)
print((True and False) or (True and (not False)) or (False and (not False)))
print((2 < 3) or (5 > 2) and (not 4 == 4) or 9 != 4)
print(6 == 9 or 5 < 6 and 8 < 4 or 4 > 3)

#10
# 논리식과 산술식(값)이 결합된 수식에서는
# 논리식의 결과가 True 면 값이 출력
# 논리식의 결과가 False 면 False가 출력

#11
name = '원진'
weight = 67
age = 29
print('이름은',name,'이고,','몸무게는', weight,'나이는', age,'살')

#12
# K나이 - 세는나이(출생시 1살, 해가 바뀌면 + 1)
#        만나이(출생시 0살, 생일이 지나면 + 1)
#        연나이(현재연도 - 출생연도)

birthYear = 1993
nowYear = 2022
isPassBirth = True
age = nowYear - birthYear

print('연나이',age)
print('세는나이',age+1)
# 파이썬 if 단축식 : 참일때 값 if 조건식 else 거짓일때 값
print('만나이',(age + 1) if isPassBirth else age)

#13
print('7 x 1 =', (7*1))
print('7 x 2 =', (7*2))
print('7 x 3 =', (7*3))
print('7 x 4 =', (7*4))
print('7 x 5 =', (7*5))
print('7 x 6 =', (7*6))
print('7 x 7 =', (7*7))
print('7 x 8 =', (7*8))
print('7 x 9 =', (7*9))