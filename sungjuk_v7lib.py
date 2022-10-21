import pymysql

def displayMenu():
    main_menu = f"""
    성적처리 프로그램v7
    -=-=-=-=-=-=-=-=-=
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    -=-=-=-=-=-=-=-=-="""
    print(main_menu)
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu

def inputSungjuk():
    name = input('이름은?')
    kor = int(input('국어 성적은?'))
    eng = int(input('영어 성적은?'))
    mat = int(input('수학 성적은?'))
    # sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    sj = [name, kor, eng, mat]

    return sj

def addSungJuk():
    # 성적 데이터 입력받기
    sj = inputSungjuk()

    # 입력받은 성적데이터 초기화
    tot, avg, grd = computeSunkJuk(sj)

    # sj['tot'] = tot
    # sj['avg'] = avg
    # sj['grd'] = grd
    # + : 2개의 리스트를 하나의 리스트로 만듦
    sj = sj + [tot, avg, grd]

    # 처리된 성적데이터를 sungjuk 테이블에 저장
    # pass

def readSungJuk():
    hdr = ('-=-=-=-=-=-=-=-=-\n'
           '이름|국어|영어|수학'
           )
    print(hdr)

    # 성적테이블에서 이름/국어/영어/수학 만 select해서 출력

def readOneSungJuk():
    name = input('조회할 학생의 이름은?')

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
    print(hdr)

    # 입력한 학생이름으로 성적테이블을 조회해서 조회된 결과를 출력

def modifySungJuk():
    name = input('수정할 학생 이름은?')

    # 수정할 학생이름으로 기존데이터 조회

    # 새로운(기존) 값을 입력
    kor = int(input(f'수정할 국어 점수는? (이전 점수:)'))
    eng = int(input(f'수정할 영어 점수는? (이전 점수:)'))
    mat = int(input(f'수정할 수학 점수는? (이전 점수:)'))

    # 다시 성적 처리
    # sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    sj = [name, kor, eng, mat]
    tot, avg, grd = computeSunkJuk(sj)

    # sj['tot'] = tot
    # sj['avg'] = avg
    # sj['grd'] = grd
    sj = sj + [tot, avg, grd]

    # 새롭게 입력된 성적데이터를 기존 성적데이터에 반영

def removeSungJuk():
    name = input('삭제할 데이터의 학생 이름은?')

    # 삭제할 학생이름 입력받아 성적테이블에서 해당 학생 데이터 삭제

def computeSunkJuk(sj):
    tot = sj[1] + sj[2] + sj[3]
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

    return tot, avg, grd