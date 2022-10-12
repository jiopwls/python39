# input 함수
# 변수명 = input(입력메시지)

# 성적처리 프로그램 v2
# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균을 계산, 출력

name = input('이름 입력')
kor = int(input('국어 점수 입력'))
eng = int(input('영어 점수 입력'))
mat = int(input('수학 점수 입력'))

sum = kor + eng + mat
avg = sum / 3
print(sum , avg)

# 책 57쪽 문제3


tan = float(input('탄수화물의 그램을 입력하세요'))
dan = float(input('단백질의 그램을 입력하세요'))
gi = float(input('지방의 그램을 입력하세요'))

Kcal = tan * 4 + dan * 4 + gi * 9
print(f'총 칼로리는 {Kcal}Kcal 입니다')

# 성적처리 프로그램의 메뉴화면 작성
main_menu = '성적처리 프로그램 \n'
main_menu += '-=-=-=-=-=-=-=-=-=-=-='
print(main_menu)

main_menu = f"""
성적처리 프로그램
-=-=-=-=-=-=-=-=-=
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
-=-=-=-=-=-=-=-=-="""
print(main_menu)
input('=> 작업을 선택하세요')

