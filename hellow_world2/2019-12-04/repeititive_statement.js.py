# 반복문
student = 1
while student <= 5:
    print(student, "번 학생의 성적을 처리한다.")
    student += 1  #복합 대입연산자

num = 1
sum = 0
while num <= 10:
    sum += num
    num += 1
print("sum =", sum)
# 구구단을 만들어 보기
dan = 1
while dan <= 9:
    print("2 x", dan, "=", 2*dan)
    dan += 1

# while문을 사용하려면 초기값을 정해 줘야한다

for student in list(range(1, 6)):
    print(student, "번 학생의 성적을 처리한다.")

sum = 0
for num in list(range(1, 11)):
    sum += num
print("sum =", sum)
# range -->> range([시작], 끝, [증가값])  -- > [] 는 필수가 아님
sum = 0
for i in range(1, 101):
    sum += i
print("sum =", sum)

print(list(range(0, 10, 1)))
# for문 으로 만드는 구구단
for i in range(1, 10):
    print("2 x", i, "=", 2*i)

#반복문 내부에서 제어 변수 활용
for x in range(51):
    if x % 10 == 0:
        print('+', end="")
    else:
        print('-', end="")

# 1 ~ 10 홀수와 짝수를 구분해보자
print()
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "짝수 입니다.")
    else:
        print(i, "홀수 입니다.")
print("-"*30)
n = 1
while n <= 10:
    if n % 2 == 0:
        print(n, "짝수 입니다.")
    else:
        print(n, "홀수 입니다.")
    n += 1

# break statement
score = [92, 86, 68, 120, 56]
for s in score:
    if s < 0 or s > 100:   # 이조건을 만족할떄 안의 루프문을 종료 한다.
        break
    print(s)
print("성적 처리 끝")
# continu statemnet
score = [92, 86, 68, -1, 56]  #
for s in score:
    if s == -1:   # 이조건이 만족이 되면 다시 루프문으로 돌아간다
        continue
    print(s)
print("성적 처리 끝")

# loop
dan = 2
while dan <= 9:
    hang = 1
    print(dan, "단")
    while hang <= 9:
        print(dan, "*", hang, "=", dan * hang)
        hang += 1
    dan += 1
    print()

for dan in range(2, 10):
    print(dan, "단")
    for hang in range(1, 10):
        print(dan, "*", hang, "=", dan * hang)
    print()
# 무한 루프  while문으로 작성이 가능하고 for 문으로는 불가능하다.

print("3 + 4 = ?")
while True:
    a = int(input("정답을 입력하시오 :"))
    if a == 7:
        break
    else:
        print("틀렸어요!")
print("참 잘했어요!")
# 이중루프 사용 x
for i in range(1, 7):
    print("*" * i)

# 이중루프 사용
for i in range(1, 7):
    for j in range(i):
        print("*", end="")
    print()