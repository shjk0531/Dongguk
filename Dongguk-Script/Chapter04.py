# c500 = int(input("500원짜리 개수 --> "))
# c100 = int(input("100원짜리 개수 --> "))
# c50 = int(input("50원짜리 개수 --> "))
# c10 = int(input("10원짜리 개수 --> "))

# money = 500*c500 + 100*c100 + 50*c50 + 10*c10
# print("## 동전의 합계 ==> 5270원")


import turtle

## 전역 변수 부분 ##
num = 0
swidth, sheight = 1000, 300
curX, curY = 0, 0


def drawT(num, binary, curX, curY):
    for i in range(len(binary)-2):
        turtle.goto(curX, curY)
        if num & 1:
            turtle.color("red")
            turtle.turtlesize(2)
        else:
            turtle.color("blue")
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num >>= 1


## 메인 코드 부분 ##
if __name__ == "__main__":
    turtle.title("거북이로 두 숫자 비트 논리합(|) 구하기")
    turtle.shape("turtle")
    turtle.setup(width=swidth + 50, height=sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num1 = int(input("2진수를 입력하세요: "), 2)
    num2 = int(input("2진수를 입력하세요: "), 2)
    binary1 = bin(num1)
    binary2 = bin(num2)
    cur1X = swidth/2
    cur1Y = 100
    cur2X = swidth/2
    cur2Y = 0
    cur3X = swidth/2
    cur3Y = -100

    print(num1)
    print(num2)
    print(binary1)
    print(binary2)
    print(type(num1))
    print(type(num2))
    print(type(binary1))
    print(type(binary2))

    drawT(num1, binary1, cur1X, cur1Y)
    drawT(num2, binary2, cur2X, cur2Y)

    if num1 >= num2:
        bigger = binary1
    else:
        bigger = binary2

    for i in range(len(bigger)-2):
        turtle.goto(cur3X, cur3Y)
        if num1 | num2:
            turtle.color("red")
            turtle.turtlesize(2)
        else:
            turtle.color("blue")
            turtle.turtlesize(1)
        turtle.stamp()
        cur3X -= 50
        num1 >>= 1
        num2 >>= 1


turtle.done()

# import turtle
# import random

# ## 전역 변수 선언 부분 ##
# swidth, sheight, pSize, exitCount = 300, 300, 3, 0
# r, g, b, angle, dist, curX, curY = [0]*7

# ## 메인 코드 부분 ##
# turtle.title("거북이가 맘대로 다니기")
# turtle.shape("turtle")
# turtle.pensize(pSize)
# turtle.setup(width=swidth+30, height=sheight+30)
# turtle.screensize(swidth, sheight)

# while True:
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     turtle.pencolor((r, g, b))

#     angle = random.randrange(0, 360)
#     dist = random.randrange(1, 100)
#     turtle.left(angle)
#     turtle.forward(dist)
#     curX = turtle.xcor()
#     curY = turtle.ycor()

#     if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):
#         pass
#     else:
#         turtle.penup()
#         turtle.goto(0, 0)
#         turtle.pendown()

#         exitCount += 1
#         if exitCount >= 5:
#             break

# turtle.done()

# a = ord('A')
# mask = 0x0F

# print("%x & %x = %x" % (a, mask, a & mask))
# print("%X | %X = %X" % (a, mask, a | mask))

# mask = ord('a') - ord('A')

# b = a ^ mask
# print("%c ^ %d = %c" % (a, mask, b))
# a = b ^ mask
# print("%c ^ %d = %c" % (b, mask, a))

# ## 전역 변수 부분 ##
# year = 0

# ## 메인 코드 부분 ##
# if __name__ == "__main__":
#     year = int(input("연도를 입력하세요: "))

#     if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
#         print(("%d년은 윤년입니다." % year))
#     else:
#         print(("%d년은 윤년이 아닙니다." % year))
