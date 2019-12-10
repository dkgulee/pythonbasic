class Coffe:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def print_result(self):
        print("{}는 가격이 {} 입니다".format(self.name, self.price))

am = Coffe('아메리카노', 3900)
am.price = 10000  # 값이 바뀌어 버린다 .. -> 접근 제한자가 없기 떄문에 값을 수정해버릴 수 있다.
am.print_result()

cf = Coffe('카푸치노', 4100)
cf.print_result()

latt = Coffe('라떼', 4500)
latt.print_result()

