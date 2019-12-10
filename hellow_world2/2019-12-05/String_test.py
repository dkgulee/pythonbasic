name ="김한결"
if name.startswith("김"):
    print("성은 김씨입니다")
if name.startswith("한"):
    print("성은 한씨 입니다")
# 파일을 처내고 싶을떄
file = "girl.jpg"
if file.endswith(".jpg"):
    print("그림 파일입니다.")

# height = input("키를 입력하세요:")
# if height.isdecimal():
#     print("키 :", height)
# else:
#     print("숫자만 입력하세요.")

s = "good morning, my love KIM"
print(s.lower())
print(s.upper())
print(s)

print(s.swapcase())   # 소문자 -> 대문자 전환
print(s.capitalize())  # 첫글자만 대문자
print(s.title())  # 단어마다 첫글 마다 대문자로 만듬 영어 문서 title 형식

# python = input("파이썬의 영문 철자를 입력하시오 :")
# if python.lower() == "python":
#     print("맞췄습니다.")
# else:
#     print("틀렸습니다~")

s = "짜장 짬뽕 탕슉"
print(s.split()) # list로 반환이 된다.
for s in s.split():
    print(s, end=" ")
print()
s2 ="서울->대전->대구->부산"
print(s2.split("->"))
for city in s2.split("->"):
    print(city, "찍고", end=" ")
print()
s3 ="30.5:30.5:30.5:32.5"
print(s3.split(":"))

s = "독도는 일본땅이다. 대마도도 일본땅이다."
print(s.replace("일본", "한국"))  # 문자열은 한번 정의되면 바뀌지 않는다.
print(s) # 변환이 되지 않는다 따라서 재할당 해줘야 한다.
# 문자열 삽입
print(",".join("abcd"))
print(",".join(["a", "b", "c", "d"]))
# 문자열 포맷팅
price = 500.12121
print("궁금하면", price, "원!")
print("궁금하면 %0.3f 원" % round(price, 3))
month = 8
day = 15
anni = "광복절"
s = "%d월%d일은 %s이다." # 업무에서 포맷팅할떄 주로 편하게 이렇게 자주쓴다.
# print(month + "월" + day + "일" + anni + "이다.")  # unsupported operand type(s) for +: 'int' and 'str'
print(str(month) + "월 " + str(day) + "일은 " + anni + "이다.")
print(s % (month, day, anni)) # 가독성 + 편리함
value = 123
print("###%d###" % value)
print("###%5d###" % value)
print("###%10d###" % value)
print("###%1d###" % value)  # 값을 짜르진 않는다

price = [30, 13500, 2000]
for p in price:
    print("가격:%d원" % p)
for p in price:
    print("가격:%7d원" % p) # 오른쪽 정렬
for p in price:
    print("가격:%-7d원" % p) # 왼쪽 정렬

pie = 3.14159265 #반올림 해버림
#   %자릿수.소수점f
print("%10f" % pie)
print("%10.8f" % pie) # 소수점 8번쨰 자리수 까지
print("%10.5f" % pie) # 소수점 5번쨰 자리수 까지
print("%10.2f" % pie) # 두번쨰 까지


# 신형 포맷팅 파이썬 2.6 이후부터 새로운 문자열 포맷팅 방법을 지원
name = "한결"
age = 16
h = 162.6

print("이름 :{}, 나이 :{}, 키 :{}".format(name, age, h))
#번호를 매겨 사용 할 수 있다.
print("이름: {2}, 나이 :{0}, 키 :{1}".format(age, h, name))
# 변수를 지정 하여 사용 할 수 있다.
print("이름 :{name}, 나이 :{age}, 키 :{height}".format(age=age, height=h, name=name))

