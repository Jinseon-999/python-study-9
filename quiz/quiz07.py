# FizzBuzz 문제
# 1 ~ 100 까지 출력하면서
# 3의 배수는 Fizz, 5의 배수는 Buzz, 3과 5의 공배수는 FizzBuzz 출력

'''
# num%3 == 0   num%5 == 0       
# num%3 == 0  and  num%5 == 0       
# num%15 == 0


for i in range(1, 101):

    #if i%3==0 and i%5 ==0 :
    if i%15 == 0 :
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)
'''



# 내 답안)
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# 1 ~ 100 사이 랜덤 숫자를 하나 정하고
# 사용자가 숫자를 입력하면 'UP' / 'DOWN' 힌트를 주세요.
# 맞추면 몇 번 만에 맞췄는지 출력하고 종료합니다.
# +옵션1) 기회는 7번. 7번 안에 못 맞추면 정답을 알려주고 종료
# +옵션2) 1 ~ 100 범위를 벗어난 입력은 기회를 차감하지 않고 다시 입력 받기

'''

import random

answer = random.randint(1, 100)   #1~100사이 랜덤값

print(answer)

count = 0


#while count < 7:
#    시도 count += 1

while True:

    #사용자 숫자 입력
    num = int(input("숫자 입력 (1~100): "))

    # 정상범위를 벗어나면 필터링
    #if num < 1 or num > 100:
    if not (1 <= num <= 100) :
        print('잘못입력하셨습니다 1~100 중에...')
        continue

    #시도횟수 증가
    count += 1

    #정답에 맞는지, UP, DOWN 조건
    if num == answer:
        print(answer, " 정답입니다!!!")
        print(count, '회 만에 맞췄습니다!!!')
        break  #정답이므로 종료
    elif num > answer:
        print("DOWN")
    elif num < answer:
        print("UP")


    if count == 7:
        print("기회 7번 모두 소진. 정답은 ", answer)
        break

    #출력

    #정답 -> 종료
    #틀리면 -> 돌아가서 입력부터 재시도


#print("기회 7번 모두 소진. 정답은 ", answer)

'''

# 내 답안)
import random

answer = random.randint(1, 100)

count = 0
chance = 7

while True:
    num = int(input("숫자입력(1~100) : "))

    if 1 > num or num > 100:
        print("1~100 범위가 아닙니다. 다시입력해주세요.")
        print("남은기회", chance)
        continue

    count += 1
    chance -= 1

    if num > answer:
        print("DOWN")
    elif num < answer:
        print("UP")
    else:
        print("정답입니다.", count, "번 만에 맞췄습니다.")
        break
    
    if chance == 0:
        print("7번안에 맞추지 못하셨습니다.")
        print("정답은 ", answer," 입니다.")
        break

