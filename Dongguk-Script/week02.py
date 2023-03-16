import turtle
import random

# 변수 선언 부분
t = turtle.Turtle()
r, g, b = 0.0, 0.0, 0.0


# 함수 선언 부분
def click_right(x, y):
    r, g, b = 0.0, 0.0, 0.0
    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor((r, g, b))
    t.color((r, g, b))

    t.goto(x, y)

    size = random.randrange(1, 10)
    t.shapesize(size)
    t.stamp()


# 메인 코드 부분
t.shape("turtle")
turtle.onscreenclick(click_right, 3)
turtle.done()


# # 함수 선언 부분
# def screenLeftClick(x, y):
#     global r, g, b
#     turtle.pencolor((r, g, b))
#     turtle.pendown()
#     turtle.goto(x, y)


# def screenRightClick(x, y):
#     turtle.penup()
#     turtle.goto(x, y)


# def screenMidClick(x, y):
#     global r, g, b
#     tSize = random.randrange(1, 10)
#     turtle.shapesize(tSize)
#     r = random.random()
#     g = random.random()
#     b = random.random()


# # 변수 선언 부분
# pSize = 10
# r, g, b = 0.0, 0.0, 0.0

# # 메인 코드 부분
# turtle.title("거북이로 그림 그리기")
# turtle.shape("turtle")
# turtle.pensize(pSize)

# turtle.onscreenclick(screenLeftClick, 1)
# turtle.onscreenclick(screenMidClick, 2)
# turtle.onscreenclick(screenRightClick, 3)

# turtle.done()


# t = turtle.Turtle()
# t.shape("turtle")
# t.color("black", "white")
# s = turtle.Screen()
# s.bgcolor('skyblue')


# def draw_snow(x, y, size):
#     t = turtle.Turtle()
#     t.hideturtle()
#     t.left(90)

#     t.pen(speed=0)
#     t.width(size/3)

#     t.up()
#     t.goto(x, y)
#     t.down()

#     for i in range(1, 7):
#         t.forward(size*3)
#         t.forward(-size)
#         t.left(60)
#         t.forward(size)
#         t.forward(-size)

#         t.right(120)
#         t.forward(size)
#         t.forward(-size)

#         t.left(60)
#         t.forward(-size)
#         t.left(60)
#         t.forward(size)
#         t.forward(-size)
#         t.right(120)
#         t.forward(size)
#         t.forward(-size)

#         t.left(60)
#         t.forward(-size)
#         t.left(60)


# draw_snow(-100, -100)
# draw_snow(100, -100)


# a = int(input("첫 번째 숫자를 입력하세요: "))
# b = int(input("두 번째 숫자를 입력하세요: "))

# result1 = a+b
# result2 = a-b
# result3 = a*b
# result4 = a/b

# print(a, '+', b, '=', result1)
# print(a, '-', b, '=', result2)
# print(a, '*', b, '=', result3)
# print(a, '/', b, '=', result4)
