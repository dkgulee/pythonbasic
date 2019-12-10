#score 리스트에 성적값 8개 저장하고 총점과 평균을 구해 출혁하라
import random as rd

score = [rd.randint(10, 100) for i in range(8)]

def sum_and_mean(score):
    sum = 0
    print(score)
    for i in score:
        sum += i
    return sum, sum/len(score)

print(sum_and_mean(score))

# 서울 우유는 1리터에 2500 매일우유 1.8 4200
# 용량 대비 어떤 우유가 더 싼지 계싼 및 판단하여 결과를 출력하라

soul = 2500/1000
meil = 4200/1800

def comparsion(a, b):
    if a > b:
        print("서울 우유값이 더 큽니다".format(a))
    else:
        print("매일 우유값이 더 큽니다".format(b))

comparsion(soul, meil)

# 임의 개수의 인수를 전달 받아 가장 큰 숫자를 찾아 리턴하는 함수를 작성하라

def return_max(*n):
    max = 0
    for i in n:
        max < i
        max = i
    return max
print(return_max(10, 20 ,30 ,40))

# 로또 번호 생성기를 만들어 봅시다.


def lotto():
    lot_num = [i for i in range(1, 46)]
    rd.shuffle(lot_num)
    print(lot_num[:6])

lotto()



# 남여 파트너 정해주기

male = {"슈퍼맨", "심봉사", "로미오", "이몽룡", "마루치"}
female = {"원터우먼", "뺑덕", "줄리엣", "성충향", "아라치"}

for i in zip(male, female):
    print(i)

