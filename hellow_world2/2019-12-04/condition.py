#if 조건 : 명령
age = int(input("몇살이니???"))
if age < 19:
    print("자 애들은가~")
else:
    print("이라세이 마세이!!")

a = 5
if a == 5:
    print("a는 5이다")
if a < 5:
    print("a는 5보다 작다")
if a > 5:
    print("a는 5보다 크다")
if a <= 5:
    print("a는 5보다 작거나 같다")
if a >= 5:
    print("a는 5보다 크거나 같다")
if a != 6:
    print("a는 6이 아니다.")
# 숫자의 경우
if 0:
    print("거짓")
if -9:
    print("참")
# 문자의 경우
if "":
    print("거짓")
if "sd":
    print("참")

korea = "korea"
if korea == "korea":
    print("대한민국")
if korea == "Korea":
    print("한국")
# 사전순
if "korea" > "japen":
    print("한국이 일본 보다 크다")
if "korea" < "japen":
    print("일본이 한국 보다 크다")

if "9" > "1":
    print("9가 더 크다")
else:
    print("아니다")
if "9" > "10":    # 문자열 비교는 앞자리부터 비교를 한다.
    print("9가 더 크다")
# 숫자를 문자여롤 비교를 할떄 같은 자리수 이면 상관이 x
if "2019-01-13" > "2019-01-12":
    print("2019-01-13 가 더 크다")


# logic operater
a = 3
b = 5
if a == 3 and b == 5:
    print("a=3, b=5 and")
if a == 3 and not b == 7: #출력이 되지 않음
    print("a = 3, not  b = 7 and")
if a == 3 or b == 5:
    print("a = 3 , b = 5 or")
if not a == 3 or b == 7:
    print("a = 3, b = 7 or")
if not a == 5 or b == 7:
    print("not a == 5 , b == 7 or")
if a == 5 or b == 5:
    print("a = 5 b = 5 or")

age = 14
if age < 19:
    print("애들은가")
    print("공부 열심히해라")

if age < 19:
    print("애들은가")
print("공부 열심히 해라")

age = 22
if age < 19:
    print("애들은가")
    print("공부 열심히 해야지")
else:
    print("어서오에")
    print("have a good time")

if age < 19:
    print("애들은가")
elif age < 25:
    print("대학생 입니다")
else:
    print("어서 오세요")

money = 6500
if money >= 20000:
    print("탕수육을 먹는다.")
elif money >= 10000:
    print("쟁반 짜장을 먹는다.")
elif money >= 7000:
    print("짬뽕을 먹는다.")
elif money >= 6000:
    print("짜장면을 먹는다.")
else:
    print("단무지를 먹는다.")

money = 9000   # 순차적 언어기 떄문에 순서를 잘 맞추어 주어야 한다
if money >= 20000:
    print("탕수육을 먹는다.")
elif money >= 6000:
    print("짜장면을 먹는다.")
elif money >= 10000:
    print("쟁반 짜장을 먹는다.")
elif money >= 7000:
    print("짬뽕을 먹는다.")
else:
    print("단무지를 먹는다.")

# 다중 if 문 --  if 문을 최대 3개까지만 쓰는것 을 권고함 너무 많으면 해독 해야하기때문 -> 더 많아 질거 같으면 함수로 뻄
men = True
age = 10
if men:
    if age > 19:
        print("성인 남자입니다")
    else:
        print("소년 입니다.")
# else 뒤에도 if 문을 중첩해서 사용 가능 하다.
age = 27
if age < 19:
    print("애들은 가")
else:
    if age < 25:
        print("대학생 입니다")
    else:
        print("성인입니다.")

money = 7500
if money >= 20000:
    print("탕수육을 먹을 수 있습니다.")
else:
    if money >= 10000:
        print("쟁반짜장을 먹을 수 있습니다.")
    else:
        if money >= 7000:
            print("짬뽕을 먹을 수 있습니다.")
        else:
            if money >= 6000:
                print("짜장면을 먹을 수 있습니다.")
            else:
                print("단무지 먹을 수 있습니다.")

