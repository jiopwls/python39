# 함수를 이용한 성적처리 프로그램

# 성적 데이터 저장할 변수 선언
sjs = []

# 함수 정의
def displayMenu():
    main_menu = f"""
    성적처리 프로그램v4
    -=-=-=-=-=-=-=-=-=
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    -=-=-=-=-=-=-=-=-="""
    print(main_menu)

def addSungJuk():
    name = input('이름은?')
    kor = int(input('국어 성적은?'))
    eng = int(input('영어 성적은?'))
    mat = int(input('수학 성적은?'))

    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'

    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}

    sjs.append(sj)
    hdr = ('-=-=-=-=-=-=-=-=-\n'
           '이름|국어|영어|수학'
           )
    print(hdr)

    for sj in sjs:
        print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]}')

def readSungJuk():
    hdr = ('-=-=-=-=-=-=-=-=-\n'
           '이름|국어|영어|수학'
           )
    print(hdr)

    for sj in sjs:
        print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]}')


def readOneSungJuk():
    name = input('조회할 학생의 이름은?')

    sj = None
    for item in sjs:
        if item['name'] == name: sj = item

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
    print(hdr)
    for k in sj.keys():
        print(sj.get(k), end=' ')


def modifySungJuk():
    name = input('수정할 학생 이름은?')

    idx = None
    for i in range(len(sjs)):  # 입력한 이름과 일치하는 항목을 sjs에서 찾음

        if sjs[i]['name'] == name:
            idx = i
            break

    # 새로운(기존) 값을 입력
    kor = int(input(f'수정할 국어 점수는? (이전 점수:{sjs[idx]["kor"]})'))
    eng = int(input(f'수정할 영어 점수는? (이전 점수:{sjs[idx]["eng"]})'))
    mat = int(input(f'수정할 수학 점수는? (이전 점수:{sjs[idx]["mat"]})'))

    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'

    # 값 다시 저장
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}

    # 기존 위치에 다시 저장
    sjs[idx] = sj


def removeSungJuk():
    name = input('삭제할 데이터의 학생 이름은?')

    idx = None
    for i in range(len(sjs)):  # 삭제할 데이터의 인데스 조사
        item = sjs[i]
        if item['name'] == name: idx = i

    sjs.pop(idx)

# 프로그램 주 실행

while True:
    # 메뉴 표시 및 값 입력
    displayMenu()
    menu = input('=> 메뉴를 선택하세요 : ')

    if menu == '1': addSungJuk()

    elif menu == '2': readSungJuk()

    elif menu == '3': readOneSungJuk()

    elif menu == '4': modifySungJuk()

    elif menu == '5': removeSungJuk()

    elif menu == '0': break

    else: print('잘못된 번호를 입력했습니다.')
