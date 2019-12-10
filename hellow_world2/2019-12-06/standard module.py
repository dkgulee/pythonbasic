import math
from test_file import print_ as pt
import statistics as st
import time
import datetime
import calendar
import random as rd
import sys
# math
print(math.sin(math.radians(45)))
print(math.sqrt(4))
print(math.factorial(5))

pt.under_line(10)
# statistics

score = [10, 30, 40, 60, 70, 90]
print(st.mean(score))  # 평균
print(st.harmonic_mean(score)) #조화평균
print(st.median(score))  # 중앙값
print(st.median_low(score))  # 중앙값 - > 집합 내의 낮은 값을 선택
print(st.median_high(score))   #중앙값 - > 집합 내의 높은 값을 구함

pt.under_line(10)
# time
print(time.time())
print(time.ctime()) # ctime 함수를 사용하면 문자열 형태로 시간을 알려준다.

print(time.localtime()) # localtime 현재시간

now = time.localtime()  # 컴퓨터의 로컬 시간을 가져온다
print("{}년{}월{}일".format(now.tm_year, now.tm_mon, now.tm_mday), end=" ")
print("{}:{}:{}".format(now.tm_hour, now.tm_min, now.tm_sec))
print("----------------datetime-----------------------")
now = datetime.datetime.now()
print("{}년{}월{}일".format(now.year, now.month, now.day), end=" ")
print("{}:{}:{}".format(now.hour, now.minute, now.second))


# practice time  measurement

start = time.time()
for a in range(1000):
    print(a, end=" ")
end = time.time()
print()
print(end - start)

# calendar -> 모듈은 달력 기능을 제공한다.
print(calendar.calendar(2019))
print(calendar.month(2019, 10))
# 파이썬 시작 날짜 -- > 1970 그날 날짜
yoil = ['월', '화', '수', '목', '금', '토', '일']
day = calendar.weekday(2019, 8, 15)
print(day)
print("광복절은 "+yoil[day] + "요일이다.")

print(60 * 60 * 24) # 하루의 시간

print([int(rd.random() * 10) + 1 for i in range(5)])
print([rd.randint(1, 10) for i in range(5)])

a, b = [rd.randint(1, 9) for i in range(2)]
# question = "{} + {} = ?".format(a, b)
# c = int(input(question))
#
# if c == a + b:
#     print("정답입니다.")
# else:
#     print("틀렸습니다.")
# while True:
#     a, b = [rd.randint(1, 9) for i in range(2)]
#     question = "{} + {} = ?".format(a, b)
#     c = int(input(question))
#
#     if c == a + b:
#         print("정답입니다.")
#         break
#     else:
#         print("틀렸습니다.")
#         0
# 난수를 이용해서 점심 메뉴를 정해보자
food = {1: "피자", 2: "햄버거", 3: "탕수육", 4: "단백질", 5: "굷는다"}
num = rd.randint(1, len(food))
print(food[num])
# 중복을 방지하기 위해서 는 set 자료형을 써도될거 같다.
# 입력을 받은 상테에서 값을 저장하고 다시 입력을 했을 떄 중복이 된다면 값을 저장하지 않는다

food = ["갈비탕", "피자", "파스타", "고기"]
rd.shuffle(food)
print(food.pop())

# 로또 번호 생성기 -> 1 ~ 45 까지의 난수를 6개 만들어보기
print({rd.randint(1, 45) for i in range(6)})
lotto = [i for i in range(1, 46)]
rd.shuffle(lotto)
for i in range(6):
    print(lotto.pop(), end=" ")
print()

pt.under_line(10)
print("버전 :", sys.version)
print("플랫폼 :", sys.platform)
print("바이트 순서 :", sys.byteorder)
print("모듈 경로 :", sys.path)
sys.exit(0)