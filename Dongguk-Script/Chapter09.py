# cofee = 0


# def coffee_machine(button):
#     print()
#     print("#1. (자동으로) 뜨거운 물을 준비한다.")
#     print("#2. (자동으로) 종이컵을 준비한다.")

#     if button == 1:
#         print("#3. (자동으로) 보통커피를 탄다.")
#     elif button == 2:
#         print("#3. (자동으로) 설탕커피를 탄다.")
#     elif button == 3:
#         print("#3. (자동으로) 블랙커피를 탄다.")
#     else:
#         print("#3. (자동으로) 아무거나 탄다.\n")

#     print("#4. (자동으로) 물을 붓는다.")
#     print("#5. (자동으로) 스푼으로 젓는다.")
#     print()


# cofee = int(input("어떤 커피 드릴까요? (1:보통, 2:설탕, 3:블랙)"))
# coffee_machine(cofee)
# print("손님~ 커피 여기 있습니다.")


# cofee = 0


# def coffee_machine(button):
#     print()
#     print("#1. (자동으로) 뜨거운 물을 준비한다.")
#     print("#2. (자동으로) 종이컵을 준비한다.")

#     if button == 1:
#         print("#3. (자동으로) 보통커피를 탄다.")
#     elif button == 2:
#         print("#3. (자동으로) 설탕커피를 탄다.")
#     elif button == 3:
#         print("#3. (자동으로) 블랙커피를 탄다.")
#     else:
#         print("#3. (자동으로) 아무거나 탄다.\n")

#     print("#4. (자동으로) 물을 붓는다.")
#     print("#5. (자동으로) 스푼으로 젓는다.")
#     print()


# cofee = int(input("A손님, 어떤 커피 드릴까요? (1:보통, 2:설탕, 3:블랙)"))
# coffee_machine(cofee)
# print("A손님~ 커피 여기 있습니다.")
# cofee = int(input("B손님, 어떤 커피 드릴까요? (1:보통, 2:설탕, 3:블랙)"))
# coffee_machine(cofee)
# print("B손님~ 커피 여기 있습니다.")
# cofee = int(input("C손님, 어떤 커피 드릴까요? (1:보통, 2:설탕, 3:블랙)"))
# coffee_machine(cofee)
# print("C손님~ 커피 여기 있습니다.")


# def coffee_make(name):

#     coffee = 0

#     def coffee_machine(button):
#         print()
#         print("#1. (자동으로) 뜨거운 물을 준비한다.")
#         print("#2. (자동으로) 종이컵을 준비한다.")

#         if button == 1:
#             print("#3. (자동으로) 아메리카노를 탄다.")
#         elif button == 2:
#             print("#3. (자동으로) 카페라떼를 탄다.")
#         elif button == 3:
#             print("#3. (자동으로) 카푸치노를 탄다.")
#         elif button == 4:
#             print("#3. (자동으로) 에스프레소를 탄다.")
#         else:
#             print("#3. (자동으로) 아무거나 탄다.\n")

#         print("#4. (자동으로) 물을 붓는다.")
#         print("#5. (자동으로) 스푼으로 젓는다.")
#         print()

#     cofee = int(
#         input("%s씨, 어떤 커피 드릴까요? (1:아메리카노, 2:카페라떼, 3:카푸치노, 4:에스프레소) " % name))
#     coffee_machine(cofee)
#     print("%s씨~ 커피 여기 있습니다." % name)


# coffee_make("로제")
# coffee_make("리사")
# coffee_make("지수")
# coffee_make("제니")


# def calc(v1, v2, op):
#     result = 0
#     if op == '+':
#         result = v1 + v2
#     elif op == '-':
#         result = v1 - v2
#     elif op == '*':
#         result = v1 * v2
#     elif op == '/':
#         result = v1 / v2
#     elif op == '**':
#         result = v1 ** v2

#     return result


# res = 0
# var1, var2, oper = 0, 0, ""

# var1 = int(input("첫 번째 수를 입력하세요: "))
# oper = input("계산을 입력하세요(+,-,*,/): ")
# var2 = int(input("두 번째 수를 입력하세요: "))

# if oper == "/" and var2 == 0:
#     print("0으로는 나누면 안 됩니다ㅠㅠ")
# else:
#     res = calc(var1, var2, oper)

#     print("## 계산기: %d %s %d = %d" % (var1, oper, var2, res))


# def para_func(v1=0, v2=0, v3=0, v4=0, v5=0, v6=0, v7=0, v8=0, v9=0, v10=0):
#     result = 0
#     result = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10
#     return result


# hap = 0

# hap = para_func(10, 20)
# print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
# hap = para_func(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# print("매개변수가 10개인 함수를 호출한 결과 ==> %d" % hap)


# import random


# def getNumber():
#     return random.randrange(1, 46)


# lotto = []
# num = 0

# print("** 로또 추첨을 시작합니다. **\n")

# while True:
#     num = getNumber()

#     if lotto.count(num) == 0:
#         lotto.append(num)

#     if len(lotto) >= 6:
#         break

# print("추첨된 로또 번호 ==> ", end="")
# lotto.sort()
# for i in range(0, 6):
#     print("%d " % lotto[i], end="")


from myTurtle import *
import turtle

inStr = ""
swith, sheight = 300, 300
tX, tY, tAngle, tSize = [0] * 4

turtle.title("거북이 글자쓰기(모듈버전)")
turtle.shape("turtle")
turtle.setup(width=swith + 50, height=sheight + 50)
turtle.screensize(swith, sheight)
turtle.penup
turtle.speed(5)

inStr = getString()

for ch in inStr:
    tX, tY, tAngle, txtSize = getXYAS(swith, sheight)
    r, g, b = getRGB()

    turtle.goto(tX, tY)
    turtle.left(tAngle)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font=("은 고딕", txtSize, 'bold'))

turtle.done()
