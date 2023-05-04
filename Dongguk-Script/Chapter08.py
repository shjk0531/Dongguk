# ss = "파이썬은완전재미있어요"
# sslen = len(ss)

# for i in range(0, sslen):
#     if i % 2 == 0:
#         print(ss[i], end="")
#     else:
#         print('#', end="")


# ss = "  abcd 1234:cd  ABCD  "
# print("ss\t\t\t", ss)
# print("upper()\t\t\t", ss.upper())              # 소문자를 대분자로 변환
# print("lower()\t\t\t", ss.lower())              # 대문자를 소문자로 변환
# print("swapcase()\t\t", ss.swapcase())          # 소문자와 소문자를 상호 변환
# print("title()\t\t\t", ss.title())              # 각 단어의 앞 글자만 대문자로 변환
# print("count(\"cd\")\t\t", ss.count("cd"))      # 찾을문자열의 개수
# print("find(\"cd\")\t\t", ss.find("cd"))        # 찾을문자열의 위치
# print("rfind(\"cd\")\t\t", ss.rfind("cd"))      # 오른쪽부터 찾을문자열 위치
# print("find(\"cd\", 5)\t\t", ss.find("cd", 5))  # 찾을 위치를 5번째부터 시작
# print("find(\"없다\")\t\t", ss.find("없다"))    # 찾을 문자열 없을 경우 -1 반환
# print("index(\"cd\")\t\t", ss.index("cd"))      # find 함수와 동일
# print("rindex(\"cd\")\t\t", ss.rindex("cd"))    # 오른쪽부터 찾음
# print("index(\"cd\", 5)\t\t", ss.index("cd", 5))        # 찾을 위치를 5번째부터 시작
# print("startswith(\"  \")\t", ss.startswith("  "))      # '찾을문자열'로 시작하면 True
# print("startswith(\"ab\", 2)\t", ss.startswith("ab", 2))  # 찾을 위치 설정
# print("endswith(\"CD\")\t\t", ss.startswith("CD"))      # 찾을문자열로 끝나면 True
# print("strip()\t\t\t", ss.strip())          # 앞뒤 공백 삭제
# print("rstrip()\t\t", ss.rstrip())          # 오른쪽 공백 삭제
# print("lstrip()\t\t", ss.lstrip())          # 왼쪽 공백 삭제
# print("replace(\"cd\", \"EF\")\t", ss.replace("cd", "EF"))  # 문자열 변경
# print("split()\t\t\t", ss.split())          # 공백 단위로 분리
# print("split(\':\')\t\t", ss.split(':'))    # :를 단위로 분리
# print("\"a\\nb\\nc\".splitlines()\t", "a\nb\nc\n".splitlines())  # 행 단위로 분리
# print("\'%\'.join(ss)\t\t", "%".join(ss))       # 문자열을 합침
# befor = ['2023', '05', '04']
# after = list(map(int, befor))
# print("befor\t", befor)
# print("list(map(int, befor))\t", list(map(int, befor)))     # 리스트값 하나하나를 함수명에 대입
# print("center(30)\t\t", ss.center(30))      # 숫자만큼 전체 자릿수를 잡은 다음 가운데 배치
# print("center(30, \'-\')\t\t", ss.center(30, '-'))  # 앞뒤 빈 공간에 문자로 채움
# print("ljust(30)\t\t", ss.ljust(30))        # 왼쪽에 붙여서 출력
# print("rjust(30)\t\t", ss.rjust(30))        # 오른쪽에 붙여서 출력
# print("zfill(30)\t\t", ss.zfill(30))        # 오른쪽으로 붙여 쓰고 왼쪽 빈 공간은 0으로 채움
# print("\"123\".isdigit()\t\t", '123'.isdigit())  # 숫자로만 구성되었는지 확인
# print("\"abc\".isalpha()\t\t", "abc".isalpha())  # 글자로만 구성되었는지 확인
# print("\"ab12\".isalnum()\t", "ab12".isalnum())  # 글자와 숫자가 섞여 있는지 확인
# print("\"abc\".islower()\t\t", "abc".islower())  # 전체가 소문자로만 구성되었는지 확인
# print("\"ABC\".isupper()\t\t", "ABC".isupper())  # 전체가 대문자로만 구성되었는지 확인
# print("\"  \".isspace()\t\t", "  ".isspace())   # 공백 문자로만 구성되었는지 확인


# inStr = "<<파<<이>>썬>>"
# outStr = ""

# for i in range(0, len(inStr)):
#     if inStr[i] != '<' and inStr[i] != '>':
#         outStr += inStr[i]

# print("원래 문자열 ==> [%s]" % inStr)
# print("공백 삭제 문자열 ==> [%s]" % outStr)


# ss = input("문자열 입력: ")

# if ss.isdigit():
#     print("숫자입니다.")
# elif ss.isalpha():
#     print("글자입니다.")
# elif ss.isalnum():
#     print("글자+숫자입니다.")
# else:
#     print("모르겠습니다.")


import turtle
import random
from tkinter.simpledialog import *

## 전역 변수 선언 부분 ##
inStr = ""
swidth, sheight = 300, 300
tX, tY, txtSize = [0] * 3

## 메인 코드 부분 ##
turtle.title("tutle text")
turtle.shape("turtle")
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = askstring("enter string", "Enter a string for the turtle to write to")

for ch in inStr:
    tX = random.randrange(-swidth/2, swidth/2)
    tY = random.randrange(-sheight/2, sheight/2)
    r = random.random()
    g = random.random()
    b = random.random()
    txtSize = random.randrange(10, 50)

    turtle.goto(tX, tY)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font=("맑은 고딕", txtSize, "bold"))

turtle.done()
