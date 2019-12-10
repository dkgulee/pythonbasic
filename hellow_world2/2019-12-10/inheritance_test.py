#  class Ep:
#     def __init__(self):
#         self.price = 3900
#     def make(self):
#         print("원두를 갈아 넣습니다")
#         print("원두를 축출 합니다.")
#     def get_price(self):
#         print("가격은{}입니다.".format(self.price))
#
#
# ep = Ep()
# ep.get_price()
#
#
# class Am(Ep):
#     def __init__(self):
#         self.price = 4200
#
#     def make(self):
#         print("원두를 갈아 넣습니다.")
#         print("원두를 축출합니다.")
#         print("우유를 추가 합니다")
#     def get_price(self):
#         print("가격은{} 입니다".format(self.price))
#
#
# am = Am()
# am.get_price()
#
#
# class Lt(Ep):
#     def __init__(self):
#         self.price = 4500
#     def make(self):
#         print("원두를 갈아 넣습니다.")
#         print("원두를 축출합니다.")
#         print("우유를 추가 합니다")
#     def get_price(self):
#         print("가격은{} 입니다.".format(self.price))
#
#
# lt = Lt()
# lt.get_price()

# 상속을 받아서 아메리카노 만들기
# 특수 메서드
# - 미리 약속된 잘업을 수행하는 메서드
# - 필요할 떄 자동으로 호출됨


class Ep:
    count = 0
    def __init__(self):
        self.price = 4100
        Ep.count += 1
    def make(self):
        print("기계를 청소합니다")
        print("원두를 갈아 넣습니다")
        print("원두를 축출 합니다.")
    def get_price(self):
        print("가격은{}입니다.".format(self.price))
    @staticmethod
    def sale_count():
        print("에스프레소가 {} 개 팔렸습니다.".format(str(Ep.count)))

class Am(Ep):
    def __init__(self):
        super().__init__() #
        self.price += 200
    def make(self):
        super().make()  # super 를 넣지않으면 슈퍼 클래스의 정보를 가져오지 못한다.
        print("물을 넣습니다.")
    def __str__(self):   # <__main__.Am object at 0x000002E508B78D08> 적용전
        return "아메리카노 가격은 {} 입니다.".format(str(self.price)) # can only concatenate str (not "int") to str

am = Am()
am.get_price()
am.sale_count()
print(am)

class Lt(Ep):
    def __init__(self):
        super().__init__()
        self.price += 600
    def make(self):
        super().make()
        print("우유를 넣습니다.")

lt = Lt()
lt.get_price()

class Maki(Lt):
    def __init__(self):
        super().__init__()
        self.price += 300
    def make(self):
        super().make()
        print("카라멜 시럽을 넣습니다.")

mk = Maki()
mk.get_price()

