import random as rd
# enumerate(iterable, start=0)
# (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

nums = [i for i in range(1, 10)]

for no, i in enumerate(nums, 1):
    print("{}:{}입니다.".format(no, i), end="")

nums2 = [10 * i for i in range(1, 20)] # --> 값이 10이 더 만지만 적은 쪽으로 부터 적용해서 사용
print(zip(nums, nums2)) # <zip object at 0x000002B022595248>
for i in zip(nums, nums2):
    print(i)

# 2의 배수를 람다식을 표연하여 리스트로 도출
a = lambda x : x * 2  # 람다식을 변수지정 하면 함수로 지정
print(a(2))
print(type(a))
print([i for i in map(lambda i: i * 2, range(1, 10))])

# 로또 번호 생성기 -> 1 ~ 45 까지의 난수를 6개 만들어보기
lotto = [i for i in range(1, 46)]
rd.shuffle(lotto)
for i in range(6):
    print(lotto.pop(), end=" ")
print()
