# for i in range(0, 3, 1):
#     print("안녕하세요? for 문을 공부 중입니다. ^^")


# i, hap = 0, 0

# for i in range(1, 11, 1):
#     hap = hap + i

# print("1에서 10까지의 합계: %d" % hap)


# i, hap = 0, 0

# for i in range(501, 1001, 2):
#     hap = hap + i

# print("500과 1000 사이에 있는 홀수의 합계: %d" % hap)


# i, hap = 0, 0
# num = 0

# num = int(input("값을 입력하세요: "))

# for i in range(1, num + 1, 1):
#     hap = hap + i

# print("1에서 %d까지의 합계: %d" % (num, hap))


# i, hap = 0, 0
# num1, num2, num3 = 0, 0, 0

# num1 = int(input("시작값을 입력하세요: "))
# num2 = int(input("끝값을 입력하세요: "))
# num3 = int(input("증가값을 입력하세요: "))

# for i in range(num1, num2, num3):
#     hap = hap + i

# print("%d에서 %d까지 %d씩 증가시킨 값의 합계: %d" % (num1, num2, num3, hap))


# i, dan = 0, 0

# dan = int(input("단을 입력하세요: "))

# for i in range(1, 10, 1):
#     print("%d X %d = %2d" % (dan, i, dan*i))


# i, dan = 0, 0

# dan = int(input("단을 입력하세요: "))

# for i in range(9, 0, -1):
#     print("%d X %d = %2d" % (dan, i, dan*i))


# i, k = 0, 0

# for i in range(2, 10, 1):
#     for k in range(1, 10, 1):
#         print("%d X %d = %2d" % (i, k, i*k))
#     print("")


# i, k = 0, 0

# for i in range(2, 10, 1):
#     print("## %d단 ##" % i)
#     for k in range(1, 10, 1):
#         print("%d X %d = %2d" % (i, k, i*k))
#     print("")


# i, k, guguLine = 0, 0, ""

# for i in range(2, 10):
#     guguLine = guguLine + ("#   %d단   #" % i)

# print(guguLine)

# for i in range(1, 10):
#     guguLine = ""
#     for k in range(2, 10):
#         guguLine = guguLine + str("%2d X%2d = %2d" % (k, i, k*i))
#     print(guguLine)


# i, hap = 0, 0

# i = 1
# while i < 11:
#     hap = hap + i
#     i = i + 1

# print("1에서 10까지의 합계: %d" % hap)


# hap = 0
# a, b, = 0, 0

# while (True):
#     a = int(input("더할 첫 번째 수를 입력하세요: "))
#     b = int(input("더할 두 번째 수를 입력하세요: "))
#     hap = a + b
#     print("%d + %d = %d" % (a, b, hap))


# ch = ""
# a, b = 0, 0

# while True:
#     a = int(input("계산할 첫 번째 수를 입력하세요: "))
#     b = int(input("계산할 두 번째 수를 입력하세요: "))
#     ch = input("계산할 연산자를 입력하세요: ")

#     if (ch == "+"):
#         print("%d + %d = %d" % (a, b, a+b))
#     elif (ch == "-"):
#         print("%d - %d = %d" % (a, b, a-b))
#     elif (ch == "*"):
#         print("%d * %d = %d" % (a, b, a*b))
#     elif (ch == "/"):
#         print("%d / %d = %d" % (a, b, a/b))
#     elif (ch == "%"):
#         print("%d %% %d = %d" % (a, b, a % b))
#     elif (ch == "//"):
#         print("%d // %d = %d" % (a, b, a//b))
#     elif (ch == "**"):
#         print("%d ** %d = %d" % (a, b, a**b))
#     else:
#         print("연산자를 잘봇 입력했습니다")


# hap = 0
# a, b = 0, 0

# while True:
#     a = int(input("더할 첫 번째 수를 입력하세요: "))
#     if a == 0:
#         break
#     b = int(input("더할 두 번째 수를 입력하세요: "))
#     hap = a + b
#     print("%d + %d = %d" % (a, b, hap))

# print("0을 입력해 반복문을 탈출했습니다")


# hap, i = 0, 0

# for i in range(1, 101):
#     hap += i

#     if hap >= 1000:
#         break

# print("1~100의 합계를 최초로 1000이 넘게 하는 숫자: %d" % i)


# hap, i = 0, 0

# for i in range(1, 101):
#     if i % 3 == 0:
#         continue

#     hap += i

# print("1~100의 합계(3의 배수 제외): %d" % hap)


# i, k = 0, 0

# i = 0
# while i < 9:
#     if i < 5:
#         k = 0
#         while k < 4 - i:
#             print(" ", end='')
#             k += 1
#         k = 0
#         while k < i * 2 + 1:
#             print("\u2605", end='')
#             k += 1
#     else:
#         k = 0
#         while k < i - 4:
#             print(" ", end='')
#             k += 1
#         k = 0
#         while k < (9-i) * 2 - 1:
#             print("\u2605", end='')
#             k += 1
#     print()
#     i += 1

# hap = 0

# n = 1234
# while n < 4568:
#     if n % 444 == 0:
#         hap += n
#     n += 1

# print(hap)


# hap = 0

# for i in range(3333, 10000):
#     if i % 1234 == 0:
#         continue
#     if hap + i > 100000:
#         break
#     hap += i

# print(hap)


# i, k, heartNum = 0, 0, 0
# numStr, ch, heartStr = "", "", ""

# if __name__ == "__main__":
#     numStr = input("숫자를 여러 개 입력하세요: ")
#     print("")
#     i = 0
#     ch = numStr[i]
#     while True:
#         heartNum = int(ch)

#         heartStr = ""
#         for k in range(0, heartNum):
#             heartStr += "\u2665"
#             k += 1

#         print(heartStr)

#         i += 1
#         if (i > len(numStr) - 1):
#             break

#         ch = numStr[i]


# i, k, heartNum = 0, 0, 0
# numStr, ch, heartStr = "", "", ""

# if __name__ == "__main__":
#     numStr = input("숫자를 여러 개 입력하세요: ")
#     print("")
#     i = 0
#     ch = numStr[i]
#     while True:
#         heartNum = int(ch)

#         heartStr = ""
#         for k in range(0, heartNum * 2):
#             heartStr += "\u2605"
#             k += 1

#         print(heartStr)

#         i += 1
#         if (i > len(numStr) - 1):
#             break

#         ch = numStr[i]


# primeStr = ""

# for i in range(3, 101):
#     for k in range(2, i):
#         if i % k == 0:
#             break
#         if k == i - 1:
#             primeStr = primeStr + str(i) + " "

# print(primeStr)


import turtle
import random

swidth, sheight = 800, 450

turtle.title("star")
turtle.shape("turtle")
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)

for i in range(5):
    turtle.forward(100)
    turtle.left(144)

while True:
    r = random.randrange(1, 255)
    g = random.randrange(1, 255)
    b = random.randrange(1, 255)

    turtle.pencolor([r, g, b])


turtle.done()
