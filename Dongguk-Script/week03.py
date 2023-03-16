# print("100")
# print("%d" % 100)

# print("100 + 100")
# print("%d" % (100 + 100))

# print("%d" % (100, 200))
# print("%d %d" % (100))

# print("%d / %d = %5.1f" % (100, 200, 0.5))

# print("%d" % 123)
# print("%5d" % 123)
# print("%05d" % 123)

# print("%f" % 123.45)
# print("%7.1f" % 123.45)
# print("%7.3f" % 123.45)

# print("%s" % "python")
# print("%10s" % "python")

# print("%d %5d %05d" % (123, 123, 123))
# print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))
# print("{2:d} {1:d} {0:d}".format(100, 200, 300))

# print("\n줄바꿈\n연습")
# print("\t탭키\t연습")
# print("글자가 \"강조\"되는 효과1")
# print("글자가 \'강조\'되는 효과2")
# print("\\\\\\ 역슬래시 세 개 출력")
# print(r"\n \t \" \\를 그대로 출력")

# print("    *    ")
# print("   ***   ")
# print("  *****  ")
# print(" ******* ")
# print("*********")
# print(" ******* ")
# print("  *****  ")
# print("   ***   ")
# print("    *    ")

# sel = int(input("입력 진수 결정(16/10/8/2): "))
# num = input("값 입력: ")

# if sel == 16:
#     num10 = int(num, 16)
# if sel == 10:
#     num10 = int(num, 10)
# if sel == 8:
#     num10 = int(num, 8)
# if sel == 2:
#     num10 = int(num, 2)

# print("16진수 ==>", hex(num10))
# print("10진수 ==>", num10)
# print("8진수  ==>", oct(num10))
# print("2진수  ==>", bin(num10))

## 함수 선언 부분 ##
def myFunc():
    print("함수를 호출함.")


## 전역 변수 선언 부분 ##
gVar = 100

## 메인 코드 부분 ##
if __name__ == "__main__":
    print("메인 함수 부분이 실행됩니다.")
    myFunc()
    print("전역 변수 값:", gVar)
