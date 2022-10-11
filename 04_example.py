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

#10