import csv

# 성적 데이터 저장할 변수 선언
sjs = []

# sungjuk_v6C.dat 파일을 읽어서 sjs 변수에 초기화
def loadSungJuk():
    global sjs
    # 파일에 저장된 성적데이터들을 모두 읽어 리스트에 저장
    try:
        with open('data/sungjuk_v6C.dat', encoding='utf-8') as f:
            data = csv.reader(f)
            sjs = list(data)
    except:
        pass
# 성적데이터들을 sungjuk_v6C.dat 파일에 저장
# [ [ㄱ, 1, 1, 1]
# [ㄴ, 2, 2, 2]
# [ㄷ, 3, 3, 3] ]
def saveSungJuk(sjs):
    # newline : 줄바꿈이 2번 추가되는 것을 제어
    with open('data/sungjuk_v6C.dat', 'w', encoding='utf-8', newline='') as f:
        # 방금 입력한 성적데이터와 기존에 입력한 성적데이터를 csv 형식으로 파일에 함께 저장
            wf = csv.writer(f) # csv 작업 초기화
            for sj in sjs:
                wf.writerow(sj) # sjs 리스트의 요소를 csv 행으로 저장


def displayMenu():
    main_menu = f"""
    성적처리 프로그램v6
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

    sjs.append(sj)

    # sjs에 저장된 성적데이터를 파일에 저장
    saveSungJuk(sjs)

def readSungJuk():
    hdr = ('-=-=-=-=-=-=-=-=-\n'
           '이름|국어|영어|수학'
           )
    print(hdr)

    for sj in sjs:
        # print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]}')
        print(f'{sj[0]} {sj[1]} {sj[2]} {sj[3]}')
def readOneSungJuk():
    name = input('조회할 학생의 이름은?')

    sj = None
    for item in sjs:
        if item['name'] == name: sj = item

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
    print(hdr)
    # for k in sj.keys():
    #     print(sj.get(k), end=' ')
    print(f'{sj[0]} {sj[1]} {sj[2]} {sj[3]} {sj[4]} {sj[5]:.1f} {sj[6]}')

def modifySungJuk():
    name = input('수정할 학생 이름은?')

    idx = None
    for i in range(len(sjs)):  # 입력한 이름과 일치하는 항목을 sjs에서 찾음

        if sjs[i][0] == name:
            idx = i
            break

    # 새로운(기존) 값을 입력
    kor = int(input(f'수정할 국어 점수는? (이전 점수:{sjs[idx][1]})'))
    eng = int(input(f'수정할 영어 점수는? (이전 점수:{sjs[idx][2]})'))
    mat = int(input(f'수정할 수학 점수는? (이전 점수:{sjs[idx][3]})'))

    # 다시 성적 처리
    # sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    sj = [name, kor, eng, mat]
    tot, avg, grd = computeSunkJuk(sj)

    # sj['tot'] = tot
    # sj['avg'] = avg
    # sj['grd'] = grd
    sj = sj + [tot, avg, grd]

    # 기존 위치에 다시 저장
    sjs[idx] = sj

    # 수정된 성적데이터를 파일에 저장
    saveSungJuk(sjs)

def removeSungJuk():
    name = input('삭제할 데이터의 학생 이름은?')

    idx = None
    for sj in sjs: # 삭제할 데이터가 sjs에 있는지 조사
        if sj[0] == name: # 존재한다면 삭제
            sjs.remove(sj)
            # 삭제된 성적데이터를 파일에 반영
            saveSungJuk(sjs)

    # for i in range(len(sjs)):  # 삭제할 데이터의 인데스 조사
    #     item = sjs[i]
    #     if item[0] == name: idx = i
    #
    # sjs.pop(idx)

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