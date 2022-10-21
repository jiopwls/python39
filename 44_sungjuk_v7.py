# maria DB을 이용한 성적처리 프로그램
# 모듈을 이용한 성적처리 프로그램
# 성적 처리 프로그램의 모든 함수들은 sungjuk_v5lib.py에 작성, 모듈명은 sjv5로 줄여서 사용함

import sungjuk_v7lib as sjv7

# 파일에 저장된 성적데이터 불러오기
# 프로그램 시작전 데이터 초기화
while True:

    # 메뉴 표시 및 값 입력
    menu = sjv7.displayMenu()

    if menu == '1': sjv7.addSungJuk()

    elif menu == '2': sjv7.readSungJuk()

    elif menu == '3': sjv7.readOneSungJuk()

    elif menu == '4': sjv7.modifySungJuk()

    elif menu == '5': sjv7.removeSungJuk()

    elif menu == '0':break

    else: print('잘못된 번호를 입력했습니다.')
