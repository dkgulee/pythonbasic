s = "python"
print(s[2]) # 인덱스는 0부터!
print(s[-2]) # -1 맨 뒤부터!

for c in s:
    print(c, end=",")

# 문자열 변경
# 파이썬의 문자열은 변경 불가능한 자료형이다, 한번 초기화 되면 바꿀 수 없다.
# s[2] = 'k'  # 'str' object does not support item assignment

# slice  []에 범위를 지정하면 부분 문자열을 추출 한다. range 함수 구조와 같음
print()
print("--" * 20)
print(s[2:5])
print(s[3:])
print(s[:4])
print(s[2:-2])
print("--" * 20)
file ='20191204-164320.jpg'
print("촬영 날짜 :", file[4:6], "월", file[6:8], "일")
print("촬영 시간:",  file[9:11], "시", file[11:13], "분")
print("확장자 :", file[-3:])
# find --> 문자열이 없을 경우 -1 리턴  index->  문자열이 없는 경우 오류 발생 not found
print(len(file), file.count("0"), file.index("3"), file.find('0'), file.rfind('0'), sep=",")

s = 'python programming'
print(len(s), s.find('o'), s.rfind('o'), s.index('o'), s.count('n'), sep=",")

# 문자열 조사 --> True False 값 도출
print('a' in s, 'z' in s, 'pro' in s, 'x' not in s, sep=",id")

# slice 객체 사용하기 --> slice 객체를 사용하여 시퀀스 객체를 잘라낼 수 도 있다.
a = range(10)[slice(4, 7, 2)]
print(list(a))
# slice 객체를 만들어서 여러 시퀀스 객체에 사용하는 방법도 있다
a = [i for i in range(10)]
s = slice(4, 7, 2)
print(a[s])
# silcing 하는데 주의사항 --> 범위를 지정해서 요소를 할당했을 때 원래 있던 리스트가 변경되며 새 리스트는 생성되지 않는다
print(a)
a[2:5] = ['a', 'b', 'c']
print(a) # 원래 있던 함수값이 바뀐다.
# 만약 할당할 요소 개수가 적으면 그만큼 리스트의 요소 개수도 줄어든다.
b = [i for i in range(1, 11)]
print(b)
b[2:6] = ['a']  # b[2] 에서 b[5] 까지 값을 대신해서 'a'값이 들어간다
print(b)
# del로 슬라이스 삭제하기 --> a가 삭제됨  새로운 리스트가 생성되지 않음
del b[2:3]
print(b)
# 짝수인덱스만 삭제하기
a = [i for i in range(1, 11)]
print(a)
del a[:11:2]
print(a)
b = [i for i in range(1, 11)]
print(b)
# 짝수 인덱스만 삭제하기
del b[1:11:2]
print(b)