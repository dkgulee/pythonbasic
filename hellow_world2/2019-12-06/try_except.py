# 예외란  실행중 예기치 않은 문제가 발생 할 수 있다.
# 사용자 입력을 받을 경우 입력값을 예상할 수 없다
# 네트워크나 외부 장치도 언제 어떻게 연결이 끊어질지 예상할 수 없다.

str = "89"
try:
    score = int(str)
    print(score)
    a = str[5]
except ValueError:
    print("점수의 형식이 잘못 되었습니다.")
except IndexError:
    print("첨자의 범위를 벗어났습니다.")
except TypeError:
    print("타입 오류 발생 ")
print("프로그램 정상 정료")

def calccsum(n):
    if n < 0:
        raise ValueError
    sum = 0
    for i in range(n + 1):
        sum += sum + i
    return sum

try:
    print(calccsum((10)))
    print("-----------")
    print(calccsum((- 10)))
except ValueError:
    print('값을 잘못 입력')
print("프로그램 정상 종료")

# 자원 정리

try:
    print('네트워크 접속')
    a = 2/0
    print("네트워크  통신 수행")
except ZeroDivisionError:
    print("나누기 오류")
finally:                         #무조건 처리해줌
    print("네트워크 접속 해제")
print("작업 완료")

try:
    4 / 0
except ZeroDivisionError as e:   # 변수지정해서 에러를 쉽게 확인

    print(e)
