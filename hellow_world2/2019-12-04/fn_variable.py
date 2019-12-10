def kim_fn():
    temp = "김과장의 함수"    # 지역변수 함수 내부에 선언하는 변수를 지역변수라고 한다.
    print(temp)
kim_fn()
# print(temp) # name 'temp' is not defined

# 함수 밖에서 선언된 변수를 전역 변수라고 한다.  프로그램 어디서나 사용가능

salerate = 0.9
def kim():
    print("오늘의 할인율 :", salerate)

def lee():
    price = 1000
    print("가격:", price * salerate)

kim()
lee()  # 900.0
salerate = 1.1
lee() # 1100.0 호출할떄 시점에 따라서 값이 달라진다.

#전엳 변수

def sale():
    global price  # 한번은 호출을 해야 사용이 가능하다
    price = 1000

sale()
print(price)

# docString
# 함수의 사용법이나 인수의 의미, 주의 사항 등을 남길 수 있다.
# 함수 선언문과 본체 사이에 작성한다.
def calcsum(n):
    """
    0부터 n까지 더하는 함수 입니다.
    1~n까지의 합계를 구해 리턴한다.

    """
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum
help(calcsum)
print(calcsum(10))

# 함수의 장점
# 반복을 제거 할 수 있다.
# 코드 수정이 쉽다.
# 재사용하기 쉽다.
# 실수의 가능성을 줄여 준다

# 파이썬 내부에 미리 정의 해높은 함수
# 별도의 import 문을 사용하지 않아도 언제든지 사용할 수 있다.


a = slice(4, 6)
print(type(a))
b = [i for i in range(1, 10)]
print(b[a])