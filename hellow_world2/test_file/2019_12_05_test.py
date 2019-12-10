import random as rd
#사용자에게 5개의 성적을 입력받아 리스트에 저장한후 오름차순으로 정렬하여 출력하라
list = []
a, b, c, d, e = map(int, input("점수를 입력하세요").split(","))
list = [a, b, c, d, e]
print(list)
list.sort(reverse=False)
print(list)


# for문으로 1부터 10까지 출력하되 3의 배수는 건너 뛰는 예제
print([i for i in range(1, 11) if i % 3 != 0])


# 임의 개수의 인수를 전달 받아 가장 큰 숫자를 찾아 리턴하는 함수
def randomly_max(*s):
    max = 0
    for i in s:
        if i > max:
            max = i
    return max

print(randomly_max(10, 20, 30, 10, 50))

def randomly_min(*s):
    min = s[0]
    for i in s:
        if i < min:
            min = i
    return min
print(randomly_min(10, 2, 312, 1, -1))

#여러개의 정수를 전달받아 평균값을 구해 리턴하는 함수를 작성해라

def mean_value(*n):
    sum = 0
    count = 0
    for i in n:
        sum += i
        count += 1
    return round(float(sum/count), 2)

print(mean_value(10, 30, 40, 50))

# 랜덤으로 값을 6번 받아서 정렬하기

rand_tuple = []
for i in range(1, 7):
    a = rd.randint(1, 10)
    rand_tuple.append(a)
rand_tuple.sort(reverse=False)
print(rand_tuple)


song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
new how shall we sing the lord's song in a strange land
"""

alphabet = {}

for s in song:
    if s.isalpha() == False:
        continue
    if s in alphabet:
        alphabet[s] += 1
    else:
        alphabet[s] = 1
print(alphabet)
print("----" * 5)
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)
# 괄호 안에 표션식을 넣으면 튜플이 아니라 제너레이터 표현식이 된다.
print((i for i in range(10) if i % 2 == 0)) # <generator object <genexpr> at 0x000001E73937B2C8>
# 2의 거듭제곱 리스트 생성하기
print([2**n for n in range(11)])
#
a = [[10, 20], [30, 40], [50, 60]]

for i in range(len(a)):      # 세로 크기
    for j in range(len(a[i])):  # 가로 크기
        print(a[i][j], end=' ')
    print()
i = 0
print(len(a))
while i < len(a):
    x, y = a[i]  # unpacking
    print(x, y)
    i += 1

# 반복문으로 리스트 만들기
a = []
for i in range(10):
    a.append(i)
print(a)
# 반복문으로 이중 리스트 만들기
a = []
for i in range(1, 10):
    line = []
    for j in range(2):
        line.append(i)
    a.append(line)
print(a)

# 리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(10)]
print(a)
a = [[i] * 2 for i in range(11)]  # 이중 리스트 값 넣기
print(a)
print([0] * 2)

# 톱니형 리스트 만들기
a =[[i] * i for i in [1, 3, 4, 2, 5]]
print(a)
# 가로 3 세로 4 높이 3 인 다차원 배열 만드는 코드
a = [[[0] * 3 for i in range(4)] for i in range(3)]
print(a)
# method chaining 메소드를 줄줄이 연결 한다고 하여 메서드 체이닝이라고 부른다

path = "C:\python_workspace\hellow_world2"
# 파일 이름 찾기
filename = path[path.rfind('\\') + 1:]
print(filename)
x = path.split('\\')
print(x)   # ['C:', 'python_workspace', 'hellow_world2']
print(x[-1])