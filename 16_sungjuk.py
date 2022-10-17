# 성적 데이터 저장할 변수
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []

# 프로그램 메뉴 출력을 위한 변수
main_menu = f"""
성적처리 프로그램v2
-=-=-=-=-=-=-=-=-=
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
-=-=-=-=-=-=-=-=-="""

# 프로그램 주 실행
while True:
    print(main_menu)
    menu = input('메뉴를 선택하세요 : ')
    if menu == '0':
        print('성적 프로그램을 종료합니다.')
        break
    elif menu == '1': # 성적 데이터 입력, 성적처리
        name = input('이름은?')
        kor = int(input('국어 성적은?'))
        eng = int(input('영어 성적은?'))
        mat = int(input('수학 성적은?'))

        tot = kor + eng + mat
        avg = tot / 3
        grd = '가'
        if avg >= 90: grd = '수'
        elif avg >= 80: grd = '우'
        elif avg >= 70: grd = '미'
        elif avg >= 60: grd = '양'

        names.append(name)
        kors.append(kor)
        engs.append(eng)
        mats.append(mat)
        tots.append(tot)
        avgs.append(avg)
        grds.append(grd)

        input('성적 추가 완료')
    elif menu == '2':
        hdr = ('-=-=-=-=-=-=-=-=-\n'
            '이름|국어|영어|수학'
               )
        print(hdr)

        for i in range(len(names)):
            print(f'{names[i]} {kors[i]} {engs[i]} {mats[i]}')

        print('성적 데이터 조회 완료')
    elif menu == '3':

        print('성적 데이터 상세조회')
    elif menu == '4':

        print('성적 데이터 수정')
    elif menu == '5':

        print('성적 데이터 삭제')
    else: print('잘못된 번호를 입력하셨습니다.')