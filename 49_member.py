# 회원가입을 처리하는 클래스 생성
# MemberVO :
#     userid, passwd, name, email, mileage, grade
# MemberService :
#  registerMember  : 회원 정보 입력
#  processMemberGrade : 마일리지에 따라 회원 등급 결정
#      vip : 마일리지 - 10000이상
#      gold : 마일리지 - 7000이상
#      silver : 마일리지 - 4000이상
#      bronze : 마일리지 - 1000이상
#      member : 그외

class MemberVO:
    def __init__(self, userid, passwd, name, email, mileage):
        self.__userid = userid
        self.__passwd = passwd
        self.__name = name
        self.__email = email
        self.__mileage = mileage
        self.__grade = 'member'

    def __str__(self):
        result = f'아이디 : {self.__userid} 비밀번호 : {self.__passwd} 이름 : {self.__name} 이메일 : {self.__email} 마일리지 : {self.__mileage} 등급 : {self.__grade}'
        return result

    @property
    def userid(self):
        return self.__userid

    @property
    def passwd(self):
        return self.__passwd

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def mileage(self):
        return self.__mileage

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade


class MemberService:
    @staticmethod
    def register_member():
        userid = input('아이디는?')
        passwd = input('비번은?')
        name = input('이름은?')
        email = input('이메일은?')
        mileage = int(input('마일리지는?'))

        return MemberVO(userid, passwd, name, email, mileage)

    # __ 언더바 두개는 private 라는 뜻
    @staticmethod
    def process_membergrade(mb):

        if mb.mileage >= 10000: mb.grade = 'vip'
        elif mb.mileage >= 7000: mb.grade = 'gold'
        elif mb.mileage >= 4000: mb.grade = 'silver'
        elif mb.mileage >= 1000: mb.grade = 'bronze'

# 실행
mb = MemberService.register_member() # 회원정보 입력
MemberService.process_membergrade(mb) # 회원등급 처리
print(mb) # 결과출력

