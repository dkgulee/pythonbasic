# 함수명(인수 목록):
# body 파이썬과 다른언어 코드 위치를 조심해라 --> 인터프리터 순차적
#print(calcsum(10))  # name 'calcsum' is not defined ->  함수를 찾지 못한다
def calcsum(n):
    sum = 0
    for num in range(11):
        sum += num
    return sum

print(calcsum(10))
# 여러 인수가 있는 예제
def calcsumrange(begin, end):
    sum = 0
    for num in range(begin, end + 1):
        sum += num
    return sum

print(calcsumrange(3, 7))

# 함수는 리턴값이 있거나 없는경우
# 리턴값이 없는 경우

def printsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    print("~", n, "=", sum)

printsum(10)
print(printsum(10)) # None
print(print())  # None 함수에 return 값이 없으면 None type을 도출

# pass : 로직을 나중에 넣고 돌아가게끔 만들어놈 -> 에러 발생을 방지하기 위함!
def calctotal():
    pass
print(calctotal())

# 가변 인수
# def intsum(s, *int)  # 가변 인수는 인수 목록의 마지막에 와야 한다.
# def intsum(*int,s )  # TypeError -->  어떤게 필수적인거인지 모름
# def intsum(*int, *nums)  # SyntaxError --->

def calcsum(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(calcsum(1, 2, 3))
print(calcsum(1, 2, 3, 5, 5, 45, 45))

# 인수의 기본값 (값이 잘변하지 않는 값이 호출이 될떄 사용한다.
# def calcstepPlus(begin, end, step = 1 , plus = 0):   자바에서 기능을 추가 하고 싶을떄 이렇게 한다
#    return calcstep(begin, step, end) + 1
def calcstep(begin, end, step = 1, plus = 0):
    sum = 0
    for num in range(begin, end + 1, step):
        sum += num
    return sum + plus
print("1 ~ 10 짝수의 합 =", calcstep(0, 10, 2))
print("1 ~ 10 sum =", calcstep(1, 10))
print("1 ~ 10 sum+1", calcstep(1, 10, 1, 1))

def calcsum(start, end, step):
    sum = 0
    for num in range(start, end+1, step):
        sum += num
    return sum
print("-" * 30)
print("~ 10까지 합은", calcsum(0, 10, 1))
print("~ 10까지 합은", calcsum(start=0, end=10, step=1))
print("~ 10까지 합은", calcsum(0, step=1, end=10))

#print("~ 10R까지 합은", calcsum(stat=0, 10, 1))

# 키워드 가변인수 함수를 정의 할 떄 인수 목록에 ** 기호를 붙여 사용한다 호출시 적용을 해놔야 한다.
def calcstep(**args):
    begin = args['begin']
    end = args['end']
    step = args['step']
    sum = 0
    print(begin, end, step)
    for num in range(begin, end + 1, step):
        sum += num
    return sum
print("3 ~ 5 = ", calcstep(begin=3, end=5, step=1))
print("3 ~ 5 = ", calcstep(step=1, end=5, begin=3))

def calcscore(name, *ints, **op):
    print(name)
    sum = 0
    for i in ints:
        sum += i
    print("총점:", sum)
    if op['avg']:
        print("평균:", round(sum/len(ints), 2))
calcscore("김상현", 88, 99, 100, avg=True)
calcscore("김한슬", 88, 99, 100, 99, avg=False)