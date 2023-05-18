from tkinter import *

inFp = None
fName, inList, inStr = "", [], ""

# inFp = open(
#     "/home/shin/Development/University/Dongguk/Dongguk-Script/DB/data1.txt", "r")

# while True:
#     inStr = inFp.readline()
#     if inStr == "":
#         break
#     print(inStr, end="")

# inFp.close()


# with open(
#         "/home/shin/Development/University/Dongguk/Dongguk-Script/DB/data1.txt", "r") as inFp:
#     inList = inFp.readlines()
#     print(inList)


# fName = input("파일명을 입력하세요: ")
# inFp = open(fName, "r")

# inList = inFp.readlines()
# count = 1
# for inStr in inList:
#     print(str(count)+":", inStr, end="")
#     count += 1


# inFp.close()


# outFp = None
# outStr = ""

# outFp = open(
#     "/home/shin/Development/University/Dongguk/Dongguk-Script/DB/data2.txt", "w")

# while True:
#     outStr = input("내용 입력: ")
#     if outStr != "":
#         outFp.writelines(outStr + "\n")
#     else:
#         break

# outFp.close()
# print("---정상적으로 파일에 씀---")


# inFp, outFp = None, None
# inStr = ""

# inFp = open("/mnt/c/Windows/win.ini", "r")
# outFp = open(
#     "/home/shin/Development/University/Dongguk/Dongguk-Script/DB/data3.txt", "w")

# inList = inFp.readlines()
# for inStr in inList:
#     outFp.writelines(inStr)

# inFp.close()
# outFp.close()
# print("--- 파일이 정상적으로 복사되었음 ---")


# inFp, outFp = None, None
# inStr, outStr = "", ""
# i = 0
# secu = 0

# secuYN = input("1. 암호화   2. 암호 해석 중 선택: ")
# inFname = input("입력 파일며을 입력하세요: ")
# outFname = input("출력 파일명을 입력하세요: ")

# if secuYN == "1":
#     secu = 100
# elif secuYN == "2":
#     secu = -100

# inFp = open(inFname, 'r', encoding='utf-8')
# outFp = open(outFname, 'w', encoding='utf-8')

# while True:
#     inStr = inFp.readline()
#     if not inStr:
#         break

#     outStr = ""
#     for i in range(0, len(inStr)):
#         ch = inStr[i]
#         chNum = ord(ch)
#         chNum = chNum + secu
#         ch2 = chr(chNum)
#         outStr = outStr + ch2

#     outFp.write(outStr)

# outFp.close()
# inFp.close()
# print('%s --> %s 변환 완료' % (inFname, outFname))


def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')

    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()


def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)   # x 뒤에 한 칸 공백
        rgbString += "{" + tmpString + "} "             # } 뒤에 한 칸 공백
    paper.put(rgbString)


window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = []        # 2차원 리스트(메모리)

window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height=XSIZE, width=YSIZE)
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE/2, YSIZE / 2), image=paper, state="normal")


# 파일 --> 메모리
filename = "/home/shin/Development/University/Dongguk/Dongguk-Script/source/RAW/tree.raw"
loadImage(filename)


# 메모리 --> 화면
displayImage(inImage)

canvas.pack()
window.mainloop()
