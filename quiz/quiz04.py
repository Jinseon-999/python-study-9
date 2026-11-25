# 문제1)
# 나이를 입력 받아서 요금을 출력하세요.
# - 8세 미만 : 무료
# - 8 ~ 13세 : 650원
# - 14 ~ 18세 : 1050원
# - 19 ~ 64세 : 1350원
# - 65세 이상 : 무료

age = int(input("나이를 입력하세요 : "))

if age < 8:
    print("무료")
elif age <= 13:
    print("650원")
elif age <= 18:
    print("1050원")
elif age <= 64:
    print("1350원")
else:
    print('무료')
    

# 문제2)
# 년도를 입력 받아서 윤년인지 출력하세요.
# - 4로 나누어 떨어지고 100으로 나누어 떨어지지 않으면 윤년
# - 또는 400으로 나누어 떨어지면 윤년

year = int(input("년도를 입력하세요 : "))

if year%4 == 0 and year%100 != 0:
    print("윤년")
elif year%400 == 0:
    print("윤년")
else:
    print("윤년아님")

# 문제3)
# 교통카드 잔액 9000원에서 나이에 따른 요금(문제1)을 차감하고
# 남은 잔액을 출력하세요.


#(문제1)
# age = int(input("나이를 입력하세요 : "))

# if age < 8:
#     print("무료")
# elif age <= 13:
#     print("650원")
# elif age <= 18:
#     print("1050원")
# elif age <= 64:
#     print("1350원")
# else:
#     print('무료')

money = 9000

if age < 8:
    money = money - 0
elif age <= 13:
    money = money - 650
elif age <= 18:
    money = money - 1050
elif age <= 64:
    money = money - 1350
else:
    money = money - 0

print("남은 잔액 : ", money, "원")


# 문제4)
# 세 정수를 공백으로 구분해 입력 받아서 가장 큰 수를 출력하세요. (max 함수 사용하지 않기)

x = int(input('아무숫자나 입력 : '))
y = int(input('아무숫자나 입력 : '))
z = int(input('아무숫자나 입력 : '))

if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
elif z > x and z> y:
    print(z)
elif x == y > z:
    print(x)
elif x < y == z:
    print(y)
elif x == z > y:
    print(x)
elif x == y ==z:
    print(x)
else:
    print("잘못된 입력입니다")

