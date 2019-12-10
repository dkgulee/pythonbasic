# # a = 10
# # b = 20
# # c = 30
# # print(a, b)
# # print(a, b, c, sep=",")
# # print(a, b, c, end="")
# # print(a, b, c)
# # print(a, b, c, end="------>")
# # print(a, b, c)
# #
# # a = '서울'
# # b = '대전'
# # c = '대구'
# # d = '부산'
# #
# # print(a, b, c, d)
# # print(a, b, c, d, sep="-->" ) # 기호를 넣어 의미있는 출력을 할 수 있다
# # print(a, b, c, d, end=" 띄어쓴다 ")
# # print(a, b, c, d)
#
# # age = input("몇살이세요? :")
# # print(age, "살 입니다")
#
# # price = input("가격을 입력하세요 :")
# # count = input("갯수를 입력하세요 :")
# # print(type(price))
# # result = int(price) * int(count)
# # print("총 금액은 :", result, "입니다")
#
# a = "hello world"
# print(a)
#
# b = 'hello world'
# print(b)
#
# print('I say "help" to You')
#
# # 문자열(확장열) \n, \t, \', \", \\
#
print("first\nsecond")  # first
                        # second
print("old\nnew")       # old
                        # new
print("c:\temp\new.text") # c:	emp
                          #  ew.text
print("c:\\temp\\new.text")
print(r"c:\temp\new.text")  # r을 추가하게 되면 문자열(확장열) 을 적용하지 않는다
# # 개행하기 이 자동적으로 이루어짐
# s = """강나루 건너서 밀받 길을 구름에 달 가듯이 가는
# 나그네
# 길은 외줄기 남도 삼백리 술 익는 마을마다 타는 저녁놀
# 구름에 달 가듯이 가는 나그네"""
# print(s);
# # 개행하기 이 선택적으로 이루어짐 --> \ 사용
# s = """강나루 건너서 밀받 길을 구름에 달 가듯이 가는
# 나그네 \
# 길은 외줄기 남도 삼백리 술 익는 마을마다 타는 저녁놀 \
# 구름에 달 가듯이 가는 나그네"""
# print(s)
# # 이런것도 된다!
# a = "korea" "japen" "c"
# print(a)
# a = (
#     "a"
#     "b"
#     "c"
# )
# print(a)
# bool 타입
a = True
print(a)

b = 5
c = b == 5
print(c)

c = b == 7
print(c)
# collection

member = ["손오공", "저팔계", "사오정", "삼정법사"]
print(member)

member[0] = "우마왕"
print(member)

member = ("손오공", "저팔계", "사오정", "삼정법사")
print(member)
# member[0] = "우마왕" # 'tuple' object does not support item assignment'
print(member)

a = 5
a = a + 1
print(a)

a = 5

a += 1
print(a)

s1 = "대한민국"
s2 = "만세"
print(s1 + s2)
print(s1 * 5)
print("*" * 20, end="")
print("Spring Boot Start", end=" ")
print("*" * 20)

print("대한민국" + 2002) #can only concatenate str (not "int") to str
print("대한민국" + str(2002))
print(22 + "10") # can only concatenate str (not "int") to str
print(22 + int("10"))
# 의외로 전처리하는데 사용이 된다
print(22 + float("22.3"))
print(11 + int(11.1))
print(10 + int(float("222.2")))

# 반올림 round indexing  파이썬은 뒤에서부터도 지원을 한다.
print(int(2.54))
print(round(2.54))
print(round(2.54, 1))  # 소수점 첫쨰 자리수 까지
print(round(123456, -1))  # 맨뒤자리 를 반올림 해서 값을 도출
print(round(123456, -2))  # 맨뒤에서 두번쨰까지를 반올림 해서 값을 도출
# 연산자 우선순위와 결합순서
a = 3 + 8 * 2
print(a)
a = (3 + 8) * 2 # ()를 처서 우선순위를 정해 준다
print(a)