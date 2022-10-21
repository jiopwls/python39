# 성적 데이터 저장할 변수 선언
sjs = []

# sungjuk.dat 파일을 읽어서 sjs 변수에 초기화
def loadSungJuk():
    global sjs
    # 파일에 저장된 성적데이터들을 행 단위로 읽어 리스트에 저장
    with open('data/sungjuk.dat', encoding='utf-8') as f:
        data = f.readlines()

    outs = [] # 성적 데이터를 저장하기 위해 리스트 선언
    for d in data: # 리스트에 저장된 성적데이터에서 한 행씩 읽어옴
        items = d.strip().split(',') # 읽어온 데이터를 콤마로 분리 , strip은 쓸데없는 방해문자들은 다 지우고 불러옴
        # dict형식으로 성적데이터를 재작성함
        item = {'name': items[0], 'kor': items[1], 'eng': items[2], 'mat': items[3],
                'tot': items[4], 'avg' : items[5], 'grd' : items[6]}
        # dict로 작성된 데이터를 리스트에 저장
        outs.append(item)

    sjs = outs

# 성적데이터들을 sungjuk.dat 파일에 저장
# [ {'name': ㄱ, 'kor': 1, 'eng': 1, 'mat': 1}
# {'name': ㄴ, 'kor': 2, 'eng': 2, 'mat': 2}
# {'name': ㄷ, 'kor': 3, 'eng': 3, 'mat': 3}
# ]
def saveSungJuk(sjs):
    with open('data/sungjuk.dat', 'w', encoding='utf-8') as f:
        # 방금 입력한 성적데이터와 기존에 입력한 성적데이터를 파일에 함께 저장
        for sj in sjs:
            dat = f"{sj['name']}, {sj['kor']}, {sj['eng']}, {sj['mat']}, {sj['tot']}, {sj['avg']}, {sj['grd']}"
            f.write(dat+'\n')

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
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    return sj

def addSungJuk():
    # 성적 데이터 입력받기
    sj = inputSungjuk()

    # 입력받은 성적데이터 초기화
    tot, avg, grd = computeSunkJuk(sj)

    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd'] = grd

    sjs.append(sj)

    # sjs에 저장된 성적데이터를 파일에 저장
    saveSungJuk(sjs)

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

    # 다시 성적 처리
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
    tot, avg, grd = computeSunkJuk(sj)

    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd'] = grd

    # 기존 위치에 다시 저장
    sjs[idx] = sj

    # 수정된 성적데이터를 파일에 저장
    saveSungJuk(sjs)

def removeSungJuk():
    name = input('삭제할 데이터의 학생 이름은?')

    idx = None
    for i in range(len(sjs)):  # 삭제할 데이터의 인데스 조사
        item = sjs[i]
        if item['name'] == name: idx = i

    sjs.pop(idx)

    # 삭제된 성적데이터를 파일에 반영
    saveSungJuk(sjs)

def computeSunkJuk(sj):
    tot = sj['kor'] + sj['eng'] + sj['mat']
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