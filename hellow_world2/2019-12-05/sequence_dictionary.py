# dictionary --> { key : value } 형태로 저장이 됨
dic = {"boy": "소년", "school": "학교", "book": "책"}
dic2 = {"boy": "소년", "school": "학교", "book": "책"}
print(dic["boy"])
print(len(dic))
print(dic.get("sdasdasd"))  # 기본적으로 None 값을 return
print(dic.get("student", "사전에 없음"))  # 값을 바꿔 줄 수 있다.
# in l
dic = {"boy": "소년", "school": "학교", "book": "책"}
if "student" in dic:
    print("사전에 있는 단어 입니다.")
else:
    print("사전에 없는 단어 입니다.")
if "boy" not in dic:
    print("사전에 없는 단어입니다.")
else:
    print("사전에 있는 단어입니다.")

print("--"*5)
def get_value(key, dic):
    if key in dic:
        print("사전에 있는 단어 입니다.")
    else:
        print("사전에 없는 단어 입니다.")

get_value("boy", dic)

dic = {"boy": "소년", "school": "학교", "book": "책"}
dic["boy"] = "남자애" # 값 변경
dic["girl"] = "여자애" # 값 추가
print(dic)

del dic['book']
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items()) # 튜플로 보여줌

# 두개의 dictionary를 병합하기
dic = {"boy": "소년", "school": "학교", "book": "책"}
dic2 = {"student": "학생", "teacher": "선생님", "book": "서적"}
dic2.update(dic)  # 누구를 기준으로 업데이트 할건지 주의 해라!
print(dic)
print(dic2)

# dictionary activity

song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
new how shall we sing the lord's song in a strange land
"""

alphabet = {}
for c in song:
    if c.isalpha() == False:
        continue
    c = c.lower()
    if c in alphabet:
        alphabet[c] += 1
    else:
        alphabet[c] = 1
print(alphabet)

# dictionary에 키-값 쌍 추가하기
# setdefault : 키 -값 쌍 추가
# upate: 키의 값 수정, 키가 없으면 키-값 쌍 추가
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e') # key 값에 e 를 추가 하고 value 에 None을 저장합니다.
print(x)

key = list(alphabet.keys())
key.sort()

for c in key:
    print(c, "=>", alphabet[c])

# 딕셔너리에서 키의 값 수정하기 -->  update
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 60}
x.update(a = 90)  # 수정하면 그 자체의 값이 바뀐다.
print(x)
x.update(a=100, e=900)
print(x)
x.setdefault('f', 10) #  키- 값 추가
print(x)
# claer()는 딕셔너리의 모든 키-값 쌍을 삭제한다.
# dictionart key 값 가져오기
print(x.keys(), x.items(), x.values(), sep="\n")
print({key: value for key, value in x.items()})