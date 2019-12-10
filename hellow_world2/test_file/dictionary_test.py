import turtle as t
from collections import deque
# 딕션너리는 해시 기법을 이용해서 데이터를 저장합니다. 키-값 형태의 자료형을 해시, 해시맵, 해시테이블 등으로 부른다.
# 파이썬에는 데이터를 담는 자료형인 리스트,튜플,딕셔너리,세트를 컨테이너라고 부른다

# fizzbuzz 문제
# for i in range(1, 101):
#     print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
# # turtle

print(t.shape('turtle'))
def N_polygon(n, color):
    """이것은 도형을 n각형을 그려주는 도형이다"""
    print(color)
    t.color(color)
    t.begin_fill()
    for i in range(n):
        t.fd(100)
        t.rt(360/n)
    t.end_fill()

N_polygon(10, 'black')
# 반지름이 120인 원 그리기

def N_circle(n):
    t.speed("fastest")
    for i in range(n):
        t.circle(120)
        t.right(360/n)
N_circle(500)

