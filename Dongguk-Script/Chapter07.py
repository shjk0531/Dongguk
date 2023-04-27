# aa = []
# hap = 0

# for i in range(0,10):
#     aa.append(0)

# for i in range(0, 10):
#     aa[i] = int(input(str(i + 1) + "번째 숫자: "))

# j = 0
# while j < 10:
#     hap += aa[j]
#     j += 1

# print("합계 ==> %d" % hap)


# aa = []
# bb = []
# value = 0

# for i in range(0, 200):
#     aa.append(value)
#     value += 3

# for i in range(199, -1, -1):
#     bb.append(aa[i])

# print("bb[0]에는 %d이, bb[199]에는 %d이 입력됩니다." % (bb[0], bb[199]))


# list1 = []
# list2 = []
# value = 0

# for i in range(0,4):
#     for j in range(0,5):
#         list1.append(value)
#         value += 3
#     list2.append(list1)
#     list1 = []

# for i in range(0,4):
#     for j in range(0,5):
#         print("%3d" % list2[i][j], end= "")
#     print("")


# import turtle
# import random

# ## 전역 변수 선언 부분 ##
# myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6
# shapeList = []
# playerTurtles = []  # 거북이 2차원 리스트
# swidth, sheight = 500, 500

# ## 메인 코드 부분 ##
# if __name__ == "__main__":
#     turtle.title("거북 리스트 활용")
#     turtle.setup(width=swidth + 50, height=sheight+50)
#     turtle.screensize(swidth, sheight)

#     shapeList = turtle.getshapes()

#     for i in range(0, 100):
#         # random.shuffle(shapeList)
#         # myTurtle = turtle.Turtle(shapeList[0])
#         tmpShape = random.choice(shapeList)
#         myTurtle = turtle.Turtle(tmpShape)
#         tX = random.randrange(int(-swidth/2), int(swidth/2))
#         tY = random.randrange(int(-sheight/2), int(sheight/2))
#         r = random.random()
#         g = random.random()
#         b = random.random()
#         tSize = random.randrange(1, 3)
#         playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])

#     for tList in playerTurtles:
#         myTurtle = tList[0]
#         myTurtle.color((tList[4], tList[5], tList[6]))
#         myTurtle.pencolor((tList[4], tList[5], tList[6]))
#         myTurtle.turtlesize(tList[3])
#         myTurtle.goto(tList[1], tList[2])

#     turtle.done()


myList = [30, 10, 20]
print("현재 리스트: %s" % myList)

# append: 리스트 맨 뒤에 항목을 추가한다
myList.append(40)
print("apppend(40) 후의 리스트: %s" % myList)

# pop: 리스트 맨 뒤의 항목을 빼낸다(리스트에서 해당 항목이 삭제된다).
print("pop()으로 추출한 값: %s" % myList.pop())
print("pop() 후의 리스트: %s" % myList)

# sort: 리스트의 항목을 정렬한다.
myList.sort()
print("sort() 후의 리스트: %s" % myList)

# reverse: 리스트 항목의 순서를 역순으로 만든다
myList.reverse()
print("reverse() 후의 리스트: %s" % myList)

# index: 지정한 값을 찾아 해당 위치를 반환한다.
print("20 값의 위치: %s" % myList.index(20))

# insert: 지정된 위치에 값을 삽입한다.
myList.insert(2, 222)
print("insert(2, 222) 후의 리스트: %s" % myList)

# remove: 리스트에서 지정한 값을 삭제한다. 단 지정한 값이 여러 개면 첫 번째 값만 지운다.
myList.remove(222)
print("remove(222) 후의 리스트: %s" % myList)

# extend: 리스트 뒤에 리스트를 추가한다. 리스트의 더하기(+) 연산과 기능이 동일하다.
myList.extend([77, 88, 77])
print("extend([77, 88, 77]) 후의 리스트: %s" % myList)

# count: 리스트에서 해당 값의 개수를 센다.
print("77값의 개수: %d" % myList.count(77))

# sorted: 리스트의 항목을 정렬해서 새로운 리스트에 대입한다.
myList2 = sorted(myList)
print("sorted(myList) 한 새 리스트 myList2: %s" % myList2)


# tt = ((1, 2, 3),
#       (4, 5, 6),
#       (7, 8, 9))

# for i in range(0, 3):
#     for j in range(0, 3):
#         print("%2d" % tt[i][j], end="")
#     print()


# animals = {"닭": "병아리",
#            "개": "강아지",
#            "곰": "능소니",
#            "고등어": "고도리",
#            "명태": "노가리",
#            "말": "망아지",
#            "호랑이": "개호주"}

# while True:
#     myanimal = input(str(list(animals.keys())) + " 중 새끼 이름을 알고 싶은 동물은?: ")
#     if myanimal in animals:
#         print("<%s>의 새끼는 <%s>입니다." % (myanimal, animals.get(myanimal)))
#     elif myanimal == "끝":
#         break
#     else:
#         print("그런 동물이 없습니다. 확인해 보세요.")
