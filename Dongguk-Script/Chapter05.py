# a = 200

# if a < 100:
#     print("100보다 작군요.")
#     print("거짓이므로 이 문장은 안 보이겠죠?")

# print("프로그램 끝")


# a = 200

# if a < 100:
#     print("100보다 작군요.")
# else:
#     print("100보다 크군요.")


# a = 200

# if a < 100:
#     print("100보다 작군요.")
#     print("참이면 이 문장도 보이겠죠?")
# else:
#     print("100보다 크군요.")
#     print("거짓이면 이 문장도 보이겠죠?")

# print("프로그램 끝")


# a = int(input("정수를 입력하세요: "))

# if a % 2 == 0:
#     print("짝수를 입력했군요")
# else:
#     print("홀수를 입력했군요.")


# a = 75

# if a > 50:
#     if a < 100:
#         print("50보다 크고 100보다 작군요.")
#     else:
#         print("와~~ 100보다 크군요.")
# else:
#     print("에고~ 50보다 작군요.")


# score = int(input("점수를 입력하세요: "))

# if score >= 90:
#     print("A")
# else:
#     if score >= 80:
#         print("B")
#     else:
#         if score >= 70:
#             print("C")
#         else:
#             if score >= 60:
#                 print("D")
#             else:
#                 print("F")
# print("학접입니다. ^^")

# score = int(input("점수를 입력하세요: "))

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# print("학점입니다. ^^")


# jumsu = 55
# res = ""
# res = "합격" if jumsu >= 60 else "불합격"
# print(res)


# import turtle

# swidth, sheight = 500, 500

# turtle.title("무지개색 원그리기")
# turtle.shape("turtle")
# turtle.setup(width=swidth + 50, height=sheight+50)
# turtle.screensize(swidth, sheight)
# turtle.penup()
# turtle.goto(0, -sheight/2)
# turtle.pendown()
# turtle.speed(0)

# for radius in range(1, 250):
#     if radius % 7 == 1:
#         turtle.pencolor("red")
#     elif radius % 7 == 2:
#         turtle.pencolor("orange")
#     elif radius % 7 == 3:
#         turtle.pencolor("yellow")
#     elif radius % 7 == 4:
#         turtle.pencolor("green")
#     elif radius % 7 == 5:
#         turtle.pencolor("blue")
#     elif radius % 7 == 6:
#         turtle.pencolor("navyblue")
#     else:
#         turtle.pencolor("purple")

#     turtle.circle(radius)

# turtle.done()


# fruit = ["사과", "배", "딸기", "포도"]
# print(fruit)

# fruit.append("귤")
# print(fruit)

# if "딸기" in fruit:
#     print("딸기가 있네요.^^")


# import random

# numbers = []
# for num in range(0, 10):
#     numbers.append(random.randrange(0, 10))

# print("생성된 리스트", numbers)

# for num in range(0, 10):
#     if num not in numbers:
#         print("숫자 %d는(은) 리스트에 없네요." % num)


# select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

# select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계: "))

# if select == 1:
#     numStr = input(" *** 수식을 입력하세요: ")
#     answer = eval(numStr)
#     print("%s 결과는 %5.1f입니다." % (numStr, answer))
# elif select == 2:
#     num1 = int(input("*** 첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("*** 두 번째 숫자를 입력하세요: "))
#     for i in range(num1, num2+1):
#         answer = answer + i
#     print("%d+...+%d는 %d입니다." % (num1, num2, answer))
# else:
#     print("1 또는 2만 입력해야 합니다.")


# import random

# numbers = []
# for num in range(0, 20):
#     numbers.append(random.randrange(0, 20))

# print("생성된 리스트", numbers)

# for num in range(0, 20):
#     if num in numbers:
#         print("숫자 %d는(은) 뽑혔습니다." % num)


# import random

# a = random.choices(range(1, 6), k=2)
# b = random.choices(range(1, 6), k=2)

# print(a, b)
# print("A의 주사위 숫자는 %d %d입니다." % (a[0], a[1]))
# print("B의 주사위 숫자는 %d %d입니다." % (b[0], b[1]))

# aSum = a[0] + a[1]
# bSum = b[0] + b[1]

# if aSum > bSum:
#     print("A가 이겼습니다.")
# elif aSum == bSum:
#     print("둘이 비겼습니다.")
# elif aSum < bSum:
#     print("B가 이겼습니다.")


# import turtle
# import math
# import random

# t1, t2, t3 = [None] * 3
# t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6
# swidth, sheight = 300, 300


# def gotoStart(turtle, x, y):
#     if x < -swidth/2 or x > swidth/2 or y < -sheight/2 or y > sheight/2:
#         turtle.home()


# if __name__ == "__main__":
#     turtle.title("거북이 만나기")
#     turtle.setup(width=swidth + 50, height=swidth + 50)
#     turtle.screensize(swidth, sheight)

#     t1 = turtle.Turtle("turtle")
#     t1.color("red")
#     t1.speed(10)
#     t1.penup()
#     t2 = turtle.Turtle("turtle")
#     t2.color("green")
#     t2.speed(10)
#     t2.penup()
#     t3 = turtle.Turtle("turtle")
#     t3.color("blue")
#     t3.speed(10)
#     t3.penup()

#     t1.goto(-100, -100)
#     t2.goto(0, 0)
#     t3.goto(100, 100)

#     t1Size, t2Size, t3Size = 1, 1, 1
#     t1.turtlesize(t1Size)
#     t2.turtlesize(t2Size)
#     t3.turtlesize(t3Size)

#     while True:
#         angle = random.randrange(0, 360)
#         dist = random.randrange(1, 50)
#         t1.left(angle)
#         t1.forward(dist)
#         angle = random.randrange(0, 360)
#         dist = random.randrange(1, 50)
#         t2.left(angle)
#         t2.forward(dist)
#         angle = random.randrange(0, 360)
#         dist = random.randrange(1, 50)
#         t3.left(angle)
#         t3.forward(dist)

#         t1X = t1.xcor()
#         t1Y = t1.ycor()
#         t2X = t2.xcor()
#         t2Y = t2.ycor()
#         t3X = t3.xcor()
#         t3Y = t3.ycor()

#         gotoStart(t1, t1X, t1Y)
#         gotoStart(t2, t2X, t2Y)
#         gotoStart(t3, t3X, t3Y)

#         if math.sqrt(((t1X - t2X) ** 2) + ((t1Y - t2Y) ** 2)) <= (t1Size + t2Size)*10:
#             t1Size = random.randrange(1, 9)
#             t2Size = random.randrange(1, 9)
#             t1.turtlesize(t1Size)
#             t2.turtlesize(t2Size)
#         elif math.sqrt(((t1X - t3X) ** 2) + ((t1Y - t3Y) ** 2)) <= (t1Size + t3Size)*10:
#             t1Size = random.randrange(1, 9)
#             t3Size = random.randrange(1, 9)
#             t1.turtlesize(t1Size)
#             t3.turtlesize(t3Size)
#         elif math.sqrt(((t3X - t2X) ** 2) + ((t3Y - t2Y) ** 2)) <= (t3Size + t2Size)*10:
#             t2Size = random.randrange(1, 9)
#             t3Size = random.randrange(1, 9)
#             t2.turtlesize(t2Size)
#             t3.turtlesize(t3Size)


# import random

# dice1, dice2, dice3, dice4, dice5, dice6 = [0] * 6
# throwCount, serialCount = 0, 0

# if __name__ == "__main__":
#     while True:
#         throwCount += 1

#         dice1 = random.randrange(1, 7)
#         dice2 = random.randrange(1, 7)
#         dice3 = random.randrange(1, 7)
#         dice4 = random.randrange(1, 7)
#         dice5 = random.randrange(1, 7)
#         dice6 = random.randrange(1, 7)

#         if dice1 == dice2 == dice3 == dice4 == dice5 == dice6:
#             print("6개의 주사위가 모두 동일한 숫자가 나옴 -->", dice1,
#                   dice2, dice3, dice4, dice5, dice6)
#             break
#         elif (dice1 == 1 or dice2 == 1 or dice3 == 3 or dice4 == 1 or dice5 == 1 or dice6 == 1) and \
#             (dice1 == 2 or dice2 == 2 or dice3 == 3 or dice4 == 2 or dice5 == 2 or dice6 == 2) and \
#             (dice1 == 3 or dice2 == 3 or dice3 == 3 or dice4 == 3 or dice5 == 3 or dice6 == 3) and \
#             (dice1 == 4 or dice2 == 4 or dice3 == 3 or dice4 == 4 or dice5 == 4 or dice6 == 4) and \
#             (dice1 == 5 or dice2 == 5 or dice3 == 3 or dice4 == 5 or dice5 == 5 or dice6 == 5) and \
#                 (dice1 == 6 or dice2 == 6 or dice3 == 3 or dice4 == 6 or dice5 == 6 or dice6 == 6):
#             serialCount += 1

#     print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 홧수 -->", throwCount)
#     print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수 -->", serialCount)


import random
import math
import turtle

t1, t2, t3 = [None] * 3
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6
swidth, sheight = 300, 300


if __name__ == "__main__":
    turtle.title("거북이 만나기")
    turtle.setup(width=swidth + 50, height=swidth + 50)
    turtle.screensize(swidth, sheight)

    t1 = turtle.Turtle("turtle")
    t1.color("red")
    t1.penup()
    t2 = turtle.Turtle("turtle")
    t2.color("green")
    t2.penup()
    t3 = turtle.Turtle("turtle")
    t3.color("blue")
    t3.penup()

    t1.goto(-100, -100)
    t2.goto(0, 0)
    t3.goto(100, 100)

    while True:
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t1.left(angle)
        t1.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t2.left(angle)
        t2.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t3.left(angle)
        t3.forward(dist)

        t1X = t1.xcor()
        t1Y = t1.ycor()
        t2X = t2.xcor()
        t2Y = t2.ycor()
        t3X = t3.xcor()
        t3Y = t3.ycor()

        if math.sqrt(((t1X - t2X) ** 2) + ((t1Y - t2Y) ** 2)) <= 20 or \
                math.sqrt(((t1X - t3X) ** 2) + ((t1Y - t3Y) ** 2)) <= 20 or \
                math.sqrt(((t2X - t3X) ** 2) + ((t2Y - t3Y) ** 2)) <= 20:
            t1.turtlesize(3)
            t2.turtlesize(3)
            t3.turtlesize(3)
            break

turtle.done()
