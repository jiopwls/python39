import awsdbinfo as db

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
    conn, cur = db.openConn()

    sql = 'insert into sungjuk (name, kor, eng, mat, tot, avg, grd) values (%s, %s, %s, %s, %s, %s, %s)'
    cur.execute(sql, sj)
    conn.commit()

    db.closeConn(cur,conn)
def readSungJuk():
    hdr = ('-=-=-=-=-=-=-=-=-\n'
           '이름|국어|영어|수학'
           )
    print(hdr)

    # 성적테이블에서 이름/국어/영어/수학 만 select해서 출력
    conn, cur = db.openConn()

    sql = 'select name, kor, eng, mat from sungjuk order by sjno'
    cur.execute(sql)
    rows = cur.fetchall()

    db.closeConn(conn, cur)

    result = ''
    for row in rows:
        result += f'{row[0]} {row[1]} {row[2]} {row[3]}\n'
    print(result)

def readOneSungJuk():
    name = input('조회할 학생의 이름은?')

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
    print(hdr)

    # 입력한 학생이름으로 성적테이블을 조회해서 조회된 결과를 출력
    conn, cur = db.openConn()

    sql = 'select * from sungjuk where name = %s'
    cur.execute(sql, [name])
    row = cur.fetchone()

    db.closeConn(conn, cur)

    result = f' {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]:.1f} {row[7]}\n'
    print(result)
def modifySungJuk():
    name = input('수정할 학생 이름은?')

    # 수정할 학생 이름으로 기존데이터 조회
    conn, cur = db.openConn()
    sql = 'select name, kor, eng, mat from sungjuk where name = %s'
    cur.execute(sql, [name])
    sj = cur.fetchone()
    db.closeConn(conn, cur)

    # 새로운 값을 입력
    kor = int(input(f'새로운 국어 점수는? ({sj[1]}'))
    eng = int(input(f'새로운 영어 점수는? ({sj[2]}'))
    mat = int(input(f'새로운 수학 점수는? ({sj[3]}'))

        # 다시 성적 처리
    sj = [name, kor, eng, mat]
    tot, avg, grd = computeSunkJuk(sj)
    sj = sj + [tot, avg, grd]


    # 새롭게 입력된 성적데이터를 기존 성적데이터에 반영
    conn, cur = db.openConn()

    sql = "update sungjuk set kor=%(kr)s, eng=%(en)s, mat=%(mt)s, tot=%(tt)s, avg=%(av)s, grd=%(gd)s, regdate=current_timestamp where name = %(nm)s"
    params = dict(nm=sj[0], kr=sj[1], en=sj[2], mt=sj[3], tt=sj[4], av=sj[5], gd=sj[6])

    cur.execute(sql, params)
    cnt = cur.rowcount
    conn.commit()

    row = cur.fetchone()

    db.closeConn(conn, cur)

    if cnt > 0 : print('성공적으로 수정되었습니다.')
    else: print('수정에 실패했습니다. 이름을 확인해주세요.')


def removeSungJuk():
    name = input('삭제할 데이터의 학생 이름은?')

    # 삭제할 학생이름 입력받아 성적테이블에서 해당 학생 데이터 삭제
    conn, cur = db.openConn()

    sql = 'delete from sungjuk where name = %s'
    cur.execute(sql, [name])
    cnt = cur.rowcount
    conn.commit()

    db.closeConn(conn, cur)

    if cnt > 0: print('성공적으로 삭제 되었습니다.')
    else: print('삭제에 실패했습니다. 이름을 확인해주세요.')
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