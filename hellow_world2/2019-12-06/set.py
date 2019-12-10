# 집합이란?
# - 여러 가지 값의 모임이다.
# - {} 괄호를 사용해 선언한다.
# - 수정가능한 자료형이다.
# - 사전과 다르게 값만 저장한다.
# - 리스트나 튜플은 집합으로 변경할 수 있다.
# - 사전은 키값만 빼서 집합으로 변경할 수 있다.
# - 파이썬 2.3 버전 이후에 추가 되었다.

asia = {"korea", "china", "japan"}  # 값이 랜덤으로 저장이 된다.
asia.add("vietnam")
asia.add("china") # 에러는 내주진 않지만 저장이 되지 않는다.
asia.remove("japan")
print(asia)

asia.update({'singapore', 'hongkong', 'korea'}) # korea는 값이 한번만 저장이 된다.
print(asia)

# set operater
twox = {i for i in range(2, 13, 2)}
threex = {i for i in range(3, 16, 3)}
print(twox)
print(threex)
print("교집합", twox & threex)
print("합집합", twox | threex)
print("차집합", twox - threex)
print("차집합", threex - twox)
print("베타적 차집합", twox ^ threex) # 교집합의 반대

# 부분 집합 연산산
mammal = {"코끼리", "고릴라", "사자", "고래", "사람", "원숭이", "개"}
primate = {"사람", "원숭이", "고릴라"}
if "사자" in mammal:
    print("사자는 포유류이다.")
else:
    print("사자는 포유류가 아니다.")
print(primate <= mammal)
print(primate < mammal)
print(primate <= primate)
print(primate < primate)