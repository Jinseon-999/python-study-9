# 문제1)
scores = [88, 92, 75, 64, 95, 81, 70]
# - 최고점, 최저점, 평균을 출력하세요.
# - 80점 이상인 점수만 모은 리스트를 만들어 출력하세요. (for 와 리스트 표현식 두 가지 방법)
# - 점수를 높은 순서로 정렬한 새 리스트를 출력하세요. (원본 유지)

# 최고점
largest = scores[0]
for v in scores:
    if v >= largest:
        largest = v
print("최고점: ", largest )

# 최저점
smallest = scores[0]
for v in scores:
    if v <= smallest:
        smallest = v
print("최저점: ", smallest )

# 평균
print("평균: ", round(sum(scores) / len(scores), 2))

# 80점 이상 점수만 모은 리스트
high_score = []
for i in scores:
    if i >= 80:
        high_score.append(i)
print(high_score)

#점수를 높은 순서로 정렬한 새 리스트
a = sorted(scores)
print(a)


#
# 문제2)
# 공백으로 구분된 단어들을 입력 받아서
# - 단어 개수
# - 가장 긴 단어
# - 길이가 5 이상인 단어만 대문자로 바꾼 리스트
# 를 출력하세요.

# 공백으로 구분된 단어 입력받기
x = list(map(str, input("단어를 입력하세요(공백구분) : ").split()))

# 단어 개수
y = list(map(len, x))
print(y)

z = [ len(v) for v in x ]
print(z)

# 가장 긴 단어
print(max(x, key=len))

# 길이가 5 이상인 단어만 대문자로 바꾼 리스트
words = [v.upper() for v in x if len(v) >= 5]
print(words)

# 문제3)
# 장바구니 프로그램
cart = []
# 'add 상품명' 을 입력하면 추가, 'del 상품명' 을 입력하면 삭제, 'q' 입력시 종료
# 종료할 때 장바구니 목록을 번호와 함께 출력하세요.
while True:
    command = input("add 상품명 을 입력하면 추가됩니다.").split()

    
# +옵션1) 이미 있는 상품을 add 하면 '이미 담긴 상품' 출력
# +옵션2) 없는 상품을 del 하면 '없는 상품' 출력