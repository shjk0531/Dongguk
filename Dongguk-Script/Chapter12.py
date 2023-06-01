# class Car:
#     color = ""
#     speed = 0

#     def upSpeed(self, value):
#         self.speed += value

#     def downSpeed(self, value):
#         self.speed -= value


# myCar1 = Car()
# myCar1.color = "빨강"
# myCar1.speed = 0
# myCar2 = Car()
# myCar2.color = "파랑"
# myCar2.speed = 0
# myCar3 = Car()
# myCar3.color = "노랑"
# myCar3.speed = 0

# myCar1.upSpeed(30)
# print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
# myCar2.upSpeed(60)
# print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))
# myCar3.upSpeed(0)
# print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다." % (myCar3.color, myCar3.speed))


# class Car:
#     speed = 0

#     def upSpeed(self, value):
#         self.speed += value

#         print("현재 속도(슈퍼 클래스): %d" % self.speed)


# class Sedan(Car):
#     def upSpeed(self, value):
#         self.speed += value

#         if self.speed > 150:
#             self.speed = 150

#         print("현재 속도(서브 클래스): %d" % self.speed)


# class Truck(Car):
#     pass


# class Sonata(Sedan):
#     pass


# truck1 = Truck()
# sedan1 = Sedan()
# sonata1 = Sonata()

# print("트럭 -->>", end="")
# truck1.upSpeed(200)

# print("승용차 -->>", end="")
# sedan1.upSpeed(200)

# print("소나타 -->>", end="")
# sonata1.upSpeed(200)


import turtle
import random


class Shape:
    myTurtle = None
    cx, cy = 0, 0

    def __init__(self) -> None:
        self.myTurtle = turtle.Turtle('turtle')

    def setPen(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.myTurtle.pencolor((r, g, b))
        pSize = random.randrange(1, 10)
        self.myTurtle.pensize(pSize)

    def drawShape(self):
        pass


class Rectangle(Shape):
    width, height = [0] * 2

    def __init__(self, x, y) -> None:
        Shape.__init__(self)
        self.cx = x
        self.cy = y
        self.width = random.randrange(20, 100)
        self.height = random.randrange(20, 100)

    def drawShape(self):
        # 네모 그리기
        sx1, sy1, sx2, sy2 = [0] * 4
        sx1 = self.cx - self.width / 2
        sy1 = self.cy - self.height / 2
        sx2 = self.cx + self.width / 2
        sy2 = self.cy + self.height / 2

        self.setPen()
        self.myTurtle.penup()
        self.myTurtle.goto(sx1, sy1)
        self.myTurtle.pendown()
        self.myTurtle.goto(sx1, sy2)
        self.myTurtle.goto(sx2, sy2)
        self.myTurtle.goto(sx2, sy1)
        self.myTurtle.goto(sx1, sy1)


def screenLeftClick(x, y):
    rect = Rectangle(x, y)
    rect.drawShape()


turtle.title("거북이로 객체지향 사각형 그리기")
turtle.onscreenclick(screenLeftClick, 1)
turtle.done()
