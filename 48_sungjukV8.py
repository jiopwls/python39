# OOP를 이용한 성적처리 프로그램
# 성적처리 프로그램의 함수들은 sungjukV8dao, sungjukv8lib에 작성하고 모듈명은 sjv8 로 사용

from SungJuk_v8Lib import SungJuk_v8Lib as sjv8

# 파일에 저장된 성적데이터 불러오기
# 프로그램 시작전 데이터 초기화
while True:

    # 메뉴 표시 및 값 입력
    menu = sjv8.display_menu()

    if menu == '1': sjv8.add_sungjuk()

    elif menu == '2': sjv8.read_sungjuk()

    elif menu == '3': sjv8.readone_sungjuk()

    elif menu == '4': sjv8.modify_sungjuk()

    elif menu == '5': sjv8.remove_sungjuk()

    elif menu == '0':break

    else: print('잘못된 번호를 입력했습니다.')
