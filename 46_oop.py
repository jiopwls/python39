# 개선된 성적 클래스 - 생성자를 통해 변수 초기화
class sungjukVO:
    # 생성자
    def __init__(self, name, kor, eng, mat):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        self.__tot = 0
        self.__avg = 0.0
        self.__grd = ''

    # __str__ : 멤버변수들의 값을 문자열화해서 객체 정보를 외부에 표현할떄 사용
    def __str__(self):
        self.computeSungjuk()
        result = f'{self.__name} {self.__kor} {self.__eng} {self.__mat} {self.__tot} {self.__avg} {self.__grd}'
        return result

    # 성적 처리
    def computeSungjuk(self):
            self.__tot = self.__kor + self.__eng + self.__mat
            self.__avg = self.__tot / 3

            if self.__avg >= 90: self.__grd = '수'
            elif self.__avg >= 80: self.__grd = '우'
            elif self.__avg >= 70: self.__grd = '미'
            elif self.__avg >= 60: self.__grd = '양'

# 성적 개체 생성
sj = sungjukVO('소희', 100, 100, 100)
print(sj)

# 클래스에 대한 객체 생성
# 변수명 = 클래스명()
sj = sungjukVO()

