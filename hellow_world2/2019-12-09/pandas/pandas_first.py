import pandas as pd
import matplotlib.pyplot as plt

# data = {
#     "이름": ["John", "Jack", "Adam"],
#     "국어": [80, 90, 75],
#     "영어": [85, 100, 70],
#     "수학": [75, 95, 65]
# }
#
# df = pd.DataFrame(data) # 데이터 프레임으로 마들기
# # df.to_excel('test_score.xlsx')
# df.to_csv("test_score.csv", encoding="UTF-8")

df = pd.read_excel('test_score.xlsx')
print(df)
df = pd.read_csv('test_score.csv')
print(df["국어"])

plt.bar(df["이름"], df["국어"])
plt.show()