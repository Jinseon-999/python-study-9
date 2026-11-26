# 높이를 입력 받아서 아래 모양을 각각 출력하세요. (높이 5 예시)


# 문제1) 역삼각형
# *****
# ****
# ***
# **
# *

# i : 5번 반복
# j : 5 4 3 2 1 

height = int(input("높이 입력 : "))

# i : 0 1 2 3 4     i:0  j:0 1 2 3 4    i:1  j:0 1 2 3   i:2  j:0 1 2

# i: 5 4 3 2 1
# i:5  j: 1 2 3 4 5   i:4  j: 1 2 3 4
for i in range(5):  # i: 0 1 2 3 4
    for j in range(5):
        if j < (5-i):   # 5 4 3 2 1 
            print("*", end="")
    print()

for i in range(5):  # i: 0 1 2 3 4
    for j in range(5-i):    # range(5) range(4) range(3) 
        print("*", end="")
    print()

for i in range(5, 0, -1):  # i: 5 4 3 2 1 
    for j in range(i):     
        print("*", end="")
    print()

for i in range(5, 0, -1):  # i: 5 4 3 2 1 
    print("*", i)

# 내 답안)
for i in range(height):  # i: 0 1 2 3 4
    for j in range(height):
        if i <= j:   # 5 4 3 2 1 
            print("*", end="")
    print()

# 문제2) 피라미드
#     *
#    ***
#   *****
#  *******
# *********

for i in range(height):
    for j in range(height):         # 0 1 2 3 4     0 1 2 3 4    0 1 2 3 4      0 1 2 3 4
        if j < height - 1 - i:      # j < 4 - 0     j < 3        j< 4 - 2
            print(" ", end="")
        else:
            print("*", end="")

    for k in range(i):              # * 출력횟수 : 0 1 2 3 4
        print("*", end="")
    print()

# 띄어쓰기 4 3 2 1 0    *출력 1 3 5 7 9 
for i in range(5):    # i: 0 1 2 3 4
    # 띄어쓰기
    for j in range(4-i):    # 4-0 4-1 4-2 4-3 4-4
        print(" ", end="")
    # *출력
    for k in range(2*i +1):
        print("*", end="")
    print()
print()

# i : 4 3 2 1 0     k : 9 - 2*i
#                       9 - 2*4 =1
#                       9 - 2*3 =3
#                       9 - 2*2 =5
for i in range(4, -1, -1):    # i: 0 1 2 3 4
    # 띄어쓰기
    for j in range(i):    # 4-0 4-1 4-2 4-3 4-4
        print(" ", end="")
    # *출력
    for k in range(9 - 2*i):
        print("*", end="")
    print()
print()

#' '*4 '*' * 5      띄어쓰기    4   3   2   1   0
#                   뱔표출력    1   3   5   7   9
for i in range(5):
    print(' '*(4-i) + '*'*(2*i+1))


# 문제3) 역피라미드 (문제2 를 뒤집은 모양)

for i in range(height):
    for j in range(i):              # 공백 0 1 2 3 4
            print(" ", end="")

    for k in range(2*(height-i)-1):              # * 출력횟수 : 4 3 2 1 0
        print("*", end="")
    print()
    
# 문제4) 다이아몬드 (문제2 + 문제3, 가운데 줄은 한 번만)

# 위쪽 피라미드
for i in range(height):
    for j in range(height - 1 - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

# 아래쪽 역 피라미드
for i in range(height - 1):
    for j in range(i + 1):
        print(" ", end="")
    for k in range(2 * (height - 1 - i) - 1):
        print("*", end="")
    print()


for i in range(n):
    print(' ' * (n - 1 - i) + '*' * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(' ' * (n - 1 - i) + '*' * (2 * i + 1))