import random as rd
# 1. 가위바위보 룰을 정하기
# 1 = 가위 2 = 바위 3 보
# 사용자에게 숫자를 입력 받기 (1~3 까지)
# rd.randint 사용해서 1~3 까지 램던한 숫자 얻기
# 조건 비교 1. 비긴조건 2. 이기는 조건 3.지는 조건
user_num = int(input("1.가위 2.바위 3.보 :"))
computer_num = rd.randint(1, 3)
print("computer_num:", computer_num)
if user_num == computer_num:
    print("비겼습니다!")
if user_num == 1:
    if computer_num == 3:
        print("이겼습니다.")
    elif computer_num == 2:
        print("지셨습니다.")
if user_num == 2:
    if computer_num == 1:
        print("이겼습니다.")
    elif computer_num == 3:
        print("지셨습니다.")
if user_num == 3:
    if computer_num == 2:
        print("이겼습니다.")
    elif computer_num == 1:
        print("지셨습니다.")

