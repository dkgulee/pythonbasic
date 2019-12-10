def print_under(n):
    print("----" * n)
# 이중 for 문 사용해서 역 삼각형 만들기
for i in range(1, 6):
    for j in range((6-i)):
        print("*", end="")
    print()
print_under(5)
# 그냥 for 문 사용해서 역 삼각형 만들기
for i in range(1, 6):
    print("*" * (6 - i))
print_under(5)
# 이중 for문 사용 해서 삼각형 만들기
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
print_under(5)
# for문 사용해서 삼각형 만들기
for i in range(1, 6):
    print("*" * i)
print_under(5)
# for문 사용해서 피라미드 만들기
for i in range(1, 11):
    print(" " * (11 - i) + "*" * ((2*i) -1))
print_under(5)
# 이중for문 사용해서 피라미드 만들기
def shape(n):
    for i in range(2*n + 1):
        if (i < n):
            print(" " * (n - i) + "*" * 2 * i + " " * (n - i))
        elif i == n:
            print("*" * 2 * n)
        elif i > n:
            print(" " * (i - n) + "*" * 2 *  (2* n - i) + " " * (i - n))
shape(10)