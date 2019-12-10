import numpy as nm
# list - 자료의 집합
score = [88, 95, 70, 100, 99]
sum = 0
for s in score:
    sum += s
print("총점:", sum)
print("평균:", round(sum/len(score)))
print("총점 %d 평균 %0.1f" % (sum, round(sum/len(score))))
# list slicing
num = [i for i in range(1, 10)]
print(num[2:5])  # 3번 쨰 부터 6번쨰 까지
print(num[:5])  # 처음부터 6번쨰 까지
print(num[6:])  # 6번 쨰 부터 끝까지
print(num[1:7:2]) # 두번 쨰 부터 8번쨰 까지 2번씩

score = [88, 95, 70, 100, 99]
print(score[2])
score[2] = 55
print(score)  # 스코어는 변경이 된다.

# 이중 리스트 a dual list   자바와 씨언어와 다르게 값이 비어도 값이 만들어짐
lol = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10, 11]]
print(lol[0])
# print(lol[0][3]) # list index out of range

for i in lol:
    for j in i:
        print(j, end=" ")
    print()

# 이중 리스트를 이용해서 점수 평균을 내는 예제
score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
]

for students in score:
    sum = 0
    for num in students:
        sum += num
    print("총점? %d 평균? %d" % (sum, sum/len(students)))
total = 0
total_poplar = 0
for students in score:
    for num in students:
        total += num
    nums = len(students)
    total_poplar += nums
print("학급 총점: %d 학급 평균: %d" % (total, total/total_poplar))

# list comprehension

num = [n*2 for n in range(1, 11)]
print(num)
compre = [i for i in range(1, 46, 5)]
print(compre)

# 리스트 관리 -> 추가 append(), insert()
num = [i for i in range(1, 5)]
num.append(5)
num.insert(2, 99)  # insert(index, value)
print(num)
print([i for i in range(1, 51) if i != 50])

# 리스트 삭제
score = [90, 97, 77, 90, 70]
print(score)
score.remove(90)
del score[2]
print(score)
score.pop()
print(score)
score[1:4] = []
print(score)
score.clear()
print(score)

# 리스트 관리
# index -> 특정요소의 위치를 찾는다. count는 특정 요소의 개수를 조사한다. len, min, max 내장 함수를 사용할 수 있다.
score = [88, 95, 70, 100, 99, 80, 78, 50]
perfect = score.index(100)
print("만점의 학생의 번호는 %d" % perfect)
perfect_count = score.count(100)
print("만점자 수는 %d 입니다." % perfect_count)
# print(score.index(22)) # 22 is not in list 인덱스에 값이 없으면 답이 안나옴

print("학생의 수는 %d 입니다." % len(score))
print("최고 점수는 %d 입니다." % max(score))
print("최저 점수는 %d 입니다." % min(score))
print("평균 값은 %d 입니다 " % nm.mean(score))

# 리스트 관리 - 검색
# ans = input("결제 하시겠습니까? ")
# if ans in ['yes', 'y', '예', 'ok']:
#     print("결제 완료 되었습니다.")
# else:
#     print("안녕히 가세요")
# ans = input("결제를 하시겠습니까?")
# if ans in ['no', 'n', '아니요']:
#     print("결제가 취소 되었습니다.")
# else:
#     print("다시 시도해 주세요")

# 리스트 관리- 정렬

score = [88, 96, 70, 123, 332, 12, 123]
score.sort(reverse=False)
print(score)
score.reverse()
print(score)

# 원본을 유지하고 정령하는 방법
score = [88, 96, 70, 123, 332, 12, 123]
score_sort = sorted(score, reverse=True)
print(score)
print(score_sort)

# 인덱스와 요소를 함꼐 출력하기 enumerate (열거하다)

a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index + 1, value)
# 리스트 표현식에 for 가 여러 개일 떄 처리 순서는 뒤에서 앞으로 순이다.
a = [i * j for j in range(2, 10) for i in range(1, 10)]
print(a)

# list 에 map 사용하기
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))

a = [1.2, 2.5, 3.7, 4.6] # 소수점을 맵핑 해준다.
a = list(map(int, a))
print(a)

# 리스트를 편하게 문자열로 맵핑하기

a = list(map(str, range(1, 10)))
print(a)

