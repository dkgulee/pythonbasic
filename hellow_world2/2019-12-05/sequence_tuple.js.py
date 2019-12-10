# tuple - 불변 자료 집합. --> 초기화한 후 편집할 수 없다, 상수리스트, 정의시 () 사용
import sys
score = (i for i in range(88, 101, 4))  # <generator object <genexpr> at 0x000001CD0C2880C8>
# generator 는 간단하게 설명하면 iterator 를 생성해 주는 function 이다. iterator 는 next()
# 메소드를 이용해 데이터에 순차적으로 접근이 가능한 object 이다. iterator 에 대한 자세한 설명은 링크에서 확인. ( iterable 과 iterator 의 의미 )
print(score)
score = (88, 95, 70, 100, 99)
sum = 0
for s in score:
    sum += s
print("총점 :", sum)
print("평균:", sum/len(score))

# 튜플 -> 괄호 없이 튜플을 정의 할 수 있다.
print("----" * 8)
score = 88, 95, 70, 100, 99
sum = 0
for s in score:
 sum += s
print("총점 :", sum)
print("평균 :", sum / len(score))

# 변수 정의 조심할 점
tuple_value = 2,  # (2,)
value = 2     #  2
print(type(tuple_value))
print(type(value))

# 튜플로 가능한 일
# - 요소를 읽어 오기
# - 범위로 요소 읽어 오기
# - 일부를 잘라 내기
# - +, * 연산자로 튜플 연결 하기
# - 튜플의 요소 변경 및 삭제 불가능

tuple_value = 1, 2, 3, 4, 5
print(tuple_value[3])
print(tuple_value[1:4])
print(tuple_value[:4])
print(tuple_value + (6, 7))
print(tuple_value * 2)  # 값이 2개가 나온다
print(tuple_value)  # (1, 2, 3, 4, 5) 초기화 하면 값이 절대 변경되지 않는다
# tuple_value[1] = 100 # 'tuple' object does not support item assignment
# del tuple_value[1] # 'tuple' object doesn't support item deletion
# tuple unpecking
member = ("이순신", "김유신", "감강찬")
lee, kim, kang = member
print(lee, kim, kang)
def aaa():
    return 12, 213, 12313, 124141  # 리턴값이 여러개 있다 단-- > 튜플로 반환이 됨
print(type(aaa()))
# 튜플과 리스트를 변경하는 예제
score = [88, 95, 70, 100, 99]
tu = tuple(score)
print(tu)
li = list(tu)
li[0] = 100
print(li)
print("---" * 10)
print(sys.getsizeof([i for i in range(100) if i % 2]))
print(sys.getsizeof([i for i in range(1000) if i % 2]))
a = (i for i in range(1000) if i % 2)
print(sys.getsizeof((i for i in range(100) if i % 2)))
print(sys.getsizeof((i for i in range(1000) if i % 2)))
print(sys.getsizeof(list(a)))

# 사용자에게 5개의 성적을 입력받아 리스트에 저장한후 오름차순으로 정렬하여 출력하라

# a, b, c, d, e = input("성적을 입력하세요 :").split(',')
# print(a, b, c, d, e)
# for i in range(5):
#     score = int(input("성적을 입력하세요 :"))
# score.sort()
# print(score)

# for문으로 1부터 10까지 출력하되 3의 배수는 건너 뛰는 예제

print([i for i in range(1, 11) if i % 3 != 0])

# 임의 개수의 인수를 전달 받아 가장 큰 숫자를 찾아 리턴하는 함수

def score_max(s):
    max = s[0]
    for num in s:
        if max < num:
            max = num
    return max
print(score_max(score))

def score_max(*s):
    max = s[0]
    for num in s:
        if max < num:
            max = num
    return max
print(score_max(10, 9 ,12,31))

#세 개의 정수를 전달받아 평균값을 구해 리턴하는 함수를 작성해라

def mean_value(a, b, c):
    return int((a + b + c)/3)
print(mean_value(10, 20, 30))

def mean(*n):
    mean_sum = 0
    count = 0
    for i in n:
        mean_sum += i
        count += 1
    return round(float((mean_sum)/count), 2)

print(mean(10, 10, 11))


