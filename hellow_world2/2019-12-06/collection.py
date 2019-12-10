from test_file import print_ as pt
import copy
# enumerate --> 순서값과 요소값 둘을 한꺼번에 구해 주는 내장 함수 #열거 하다
# 리스트의 순서값과 요소값을 튜플로 묶은 컬렉션을 리턴한다.
# enumerate(iterable, start=0)
# 기본적으로 0번 부터 시작을 한다.
# (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
score = [88, 95, 70, 100, 99]
no = 1
for s in score:
    print(no, "번 학생의 성적 :", s)
    no += 1
pt.under_line(10)
for no in range(len(score)):             # 다이렉트로 접근하는 방번 추천 하지 않는다.
    print(no + 1, "번 학생의 성적:", score[no])
pt.under_line(10)
for no, s in enumerate(score, 1):
    print(no, "번 학생의 성적:", s)

# zip 여러 개의 컬렉션을 합쳐 하나로 만든다.
# 리스트의 대응되는 요소끼리 짝을 지어 튜플의 리스트를 생성한다
# 리스트의 길이가 달라도 상관 없다
# 짧은 리스트 기준으로 맟추어진다.
pt.under_line(10)
yoil = ["월", "화", "수", "목", "금", "토", "일"]
food = ["갈비탕", "순대국", "칼국수", "삼겹살"]   # 짧은 리스트 기중으로 맟추어 진다

for y, f in zip(yoil, food):   # zip(iter1 [,iter2 [...]]) --> zip object 튜플의 언팩킹
    print("{}요일 메뉴는 {} 입니다.".format(y, f))

pt.under_line(10)
# collection in lambda function
# 이름이 없고 입력과 출력만으로 함수를 정의하는 축약된 방법이다. (익명 함수)
# lambda 라는 키워드로 시작하고 인수와 리턴한 값을 밝힌다.
# 인수는 콤마로 구분하여 여러 개 값을 가질 수 있다.
# (lambda 매개변수들: 식)(인수들)
# lambda - filter
print("람다를 쓰기 전")


def flunck(s):
    return s < 60


score = [45, 89, 72, 53, 94, 10]
for s in filter(flunck, score):
    print(s, end=" ")
print()
print("람다를 쓴 후")  # 인수 리턴값
for s in filter(lambda x: x < 60, score):
    print(s, end=" ")
print()
# lambda - map
print("람다를 쓰기 전")


def half(n):
    return n/2


print([s for s in map(half, score)])
print("람다를 쓴 후")
print([s for s in map(lambda x: x/2, score)])

# collection's 사본

list1 = [1, 2, 3]
list2 = list1   # 복사

print(list1, list2)

list2[1] = 100  # 주소값이 copy 되었기 때문에 값이 같이 바뀜
list1[0] = 50   # 주소값이 copy 되었기 때문에 값이 같이 바뀜
print(list1, list2)

# 해결책
list1 = [1, 2, 3]        # 주소값이 copy되는게 아니라 값이 copy가 됨
list2 = list1.copy()

list2[1] = 100
print(list1, list2)

pt.under_line(10)
# 이중리스트를 사용하게 되면 전부다 카피가 되지 않는다.
list1 = [1, 2, 3]
list2 = [list1, 4, 5] # list1 은 list1 만 가르킨다.
list3 = list2.copy() # 4, 5는 카피가 된게 맞지만 list1은 그대로 가져온다(point)
print(list1, list2, list3)
list3[0][1] = 99
print(list1, list2, list3)

pt.under_line(10)
print("deepcopy")
list1 = [1, 2, 3]
list2 = [list1, 4, 5] # list1 은 list1 만 가르킨다.
list3 = copy.deepcopy(list2) # 탐색하면서 가져온다
print(list1, list2, list3)
list3[0][1] = 99
print(list1, list2, list3)
# is 연산자를 사용해서 같은 객체인지 확인 해보기
pt.under_line(10)
list1 = [1, 2, 3]     # 1724136407880
list2 = list1   # 리스트를 대입해서 복사하면 같은 주소 값이 되고  #1724136407880
list3 = list1.copy()  # copy를 하면 다른 주소값에 대입이 된다 list3 = 1724137427016

print("list1 == list2 :", list1 is list2)
print("list1 == list3 :", list1 is list3)  # copy를 했기 때문에 다르다
print("list2 == list3 :", list2 is list3)  # copy를 했기 때문에 다르다
print("list1 의 주소값: {} list2 의 주소값: {} list3 의 주소값: {}".format(id(list1), id(list2), id(list3)))