# 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은 sungjuk_v5lib.py에 작성, 모듈명은 sjv5로 줄여서 사용함

import sungjuk_v6lib as sjv6

# 파일에 저장된 성적데이터 불러오기
sjv6.loadSungJuk()
while True:

    # 메뉴 표시 및 값 입력
    menu = sjv6.displayMenu()

    if menu == '1': sjv6.addSungJuk()

    elif menu == '2': sjv6.readSungJuk()

    elif menu == '3': sjv6.readOneSungJuk()

    elif menu == '4': sjv6.modifySungJuk()

    elif menu == '5': sjv6.removeSungJuk()

    elif menu == '0':
        # 메모리에 존재하는 성적데이터를 파일에 저장
        # sjv6.saveSungJuk()
        break

    else: print('잘못된 번호를 입력했습니다.')
