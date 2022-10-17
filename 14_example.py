# 48번 복리계산
money = 25000 # 통장잔액
inter = 1.06 #이율
inter2 = 0.06
limit = money * 2

while True:
        if money > limit:break
        money = money * inter

print(money)

for i in range(999):
        if money > limit:break
        money = money * inter

print(i + 1, money )


bank1 = bank
i = 0
print(bank * 1.06)
print(i)
while bank1 <= (bank * 2):
        bank1 += bank * 1.06
        i += 1

        print(i)


# 53번 입력한 연도의 1월 달력 출력
year = int(input('년도는?'))

exYear31 = ((year - 1)*365 + (year - 1)/4 - (year - 1)/100 + (year - 1)/400) % 7

# 0 : 일 ~~~ 6 : 토
print(int(exYear31)) # 2021년 12월 31일의 요일
print(int(exYear31) + 1) # 2022년 1월 1일의 요일
