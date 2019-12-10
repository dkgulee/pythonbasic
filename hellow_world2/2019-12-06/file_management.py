import os
# 파일 입출력  open = > read - > close
#             open - > write -> close
# 읽기 모드 r 읽기 쓰기 r+ (파일이 없으면 에러)
# 쓰기 모드 w 쓰고 읽기 w+ (파일이 없으면 생성)
# 추가 모드 a 마지막에 새로운 내용을 추가  a+ 읽기 + 추가 : (파일이 없으면 생성)
file = open("live.txt", "w", encoding='UTF-8')
file.write("""
삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니
""")
file.close()

try:
    file = open("C:\\python_workspace\\live1.txt", "r", encoding='UTF-8')
    text = file.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다")
finally:
    file.close()

file = open(r"C:\Users\B0103\Downloads\스몰데이터 활용.txt", "r", encoding='UTF-8')
line = 1
while True:
    row = file.readline()
    if not row:
        break
    print(str(line)+" : "+ row, end="")
    line += 1
file.close()

# 파일 내용 추가
file = open("live.txt", "a", encoding='UTF-8')  # w는 초기화 시킨다음에 다시씀  a 는 append
file.write("\n\n 꾸꾸꾸꾸꾸꾸ㅏㄲ까ㅏㄲ까아")
file.close()
# 특정 경로에서 리스트 축출해서 가져오기
def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = path + "\\" + f # 윈도우에서는 \\
        if os.path.isdir(fullpath):
            print("[" + fullpath + "]")
            dumpdir(fullpath)
        else:
            print("\t" + fullpath)
dumpdir(r"C:\python_workspace\hellow_world2\2019-12-04")