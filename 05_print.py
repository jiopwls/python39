# print 함수

# 성적처리 프로그램 v1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산, 출력
name = 'jinn'
kor = 98
eng = 90
mat = 80

sum = kor + eng + mat
ave = (kor + eng + mat) / 3

print('총점 :',sum)
print('평균 :',ave)

# 출력 서식 사용 : % 문자 사용
# print(출력서식 % 변수들)
# 출력서식 문자 : %d 정수, %f 실수, %s 문자
print('이름 : %s' % name)
print('국어 : %d 영어 : %d 수학 : %d' % (kor, eng, mat))
print('국어 : %3d 영어 : %3d 수학 : %3d' % (kor, eng, mat))
print('국어 : %03d 영어 : %03d 수학 : %03d' % (kor, eng, mat))

print('총점 : %d, 평균 : %.1f' %(sum, ave))

# 인덱스, 출력서식 사용 : .format함수 사용
# print({인덱스:출력서식}.format(변수들))
print('이름 : {0:s}'.format(name))
print('국어 : {0:03d} 영어 : {1:03d} 수학 : {2:03d}'.format(kor, eng, mat))
print('국어 : {:03d} 영어 : {:03d} 수학 : {:03d}'.format(kor, eng, mat)) #인덱스 생략 가능
print('총점 : {:d}, 평균 : {:.1f}' .format(sum, ave))
print('총점 : {0:d}, 평균 : {1:.1f} ({1:f})' .format(sum, ave))

# 문자열 템플릿(f-string) : .format함수 사용 : 파이썬 3.6이후 지원
# print(f'{변수명:출력서식}')
print(f'이름 : {name:s}')
print(f'국어 : {kor:d} 영어 : {eng:d} 수학 : {mat:d}')

# % 서식
print('7 x 1 = %d' %(7*1))
print('7 x 2 = %d' %(7*2))
print('7 x 3 =%d' %(7*3))
print('7 x 4 =%d' %(7*4))
print('7 x 5 =%d' %(7*5))
print('7 x 6 =%d' %(7*6))
print('7 x 7 =%d' %(7*7))
print('7 x 8 =%d' %(7*8))
print('7 x 9 =%d' %(7*9))

# .format
print('7 x 1 = {:d}'.format(7*1))
print('7 x 2 = {:d}'.format(7*2))
print('7 x 3 = {:d}'.format(7*3))
print('7 x 4 = {:d}'.format(7*4))
print('7 x 5 = {:d}'.format(7*5))
print('7 x 6 = {:d}'.format(7*6))
print('7 x 7 = {:d}'.format(7*7))
print('7 x 8 = {:d}'.format(7*8))
print('7 x 9 = {:d}'.format(7*9))

# f-string
print(f'7 x 1 = {7*1:2d}')
print(f'7 x 2 = {7*2:2d}')
print(f'7 x 3 = {7*3:2d}')
print(f'7 x 4 = {7*4:2d}')
print(f'7 x 5 = {7*5:2d}')
print(f'7 x 6 = {7*6:2d}')
print(f'7 x 7 = {7*7:2d}')
print(f'7 x 8 = {7*8:2d}')
print(f'7 x 9 = {7*9:2d}')
print(
f"""
7 x 1 = {7*1}
7 x 1 = {7*1}
7 x 1 = {7*1}
7 x 1 = {7*1}
7 x 1 = {7*1}
"""
)