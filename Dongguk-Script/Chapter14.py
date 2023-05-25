import sqlite3
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps


def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY

    window.geometry(str(width) + "x" + str(height))
    if canvas != None:
        canvas.destroy()

    canvas = Canvas(window, width=width, height=height)
    paper = PhotoImage(width=width, height=height)
    canvas.create_image((width / 2, height / 2), image=paper, state="normal")
    rgbString = ""
    rgbImage = img.convert('RGB')
    for i in range(0, height):
        tmpString = ""
        for k in range(0, width):
            r, g, b = rgbImage.getpixel((k, i))
            tmpString += "#%02x%02x%02x " % (r, g, b)   # x 뒤에 한 칸 공백
        rgbString += "{" + tmpString + "} "             # } 뒤에 한 칸 공백
    paper.put(rgbString)
    canvas.pack()


def func_open():
    global window, canvas, paper, photo, photo2, oriX, oriY
    readFp = askopenfilename(parent=window, filetypes=(
        ("모든 그림 파일", "*.jpg, *.jpeg, *.bmp, *.png, *tif, *gif"), ("모든 파일", "*.*")))
    photo = Image.open(readFp).convert('RGB')
    oriX = photo.width
    oriY = photo.height

    photo2 = photo.copy()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None:
        return
    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(
        ("JPG 파일", "*.jpg; *jpeg"), ("모든 파일", "*.*")))

    photo2.save(saveFp.name)


def func_exit():
    global window, canvas, paper, photo, photo2, oriX, oriY

    pass


def func_zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("확대", "확대할 배율을 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.copy()
    photo2 = photo2.resize((int(oriX*scale), int(oriY*scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("축소", "축소할 배율을 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.copy()
    photo2 = photo2.resize((int(oriX/scale), int(oriY/scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_mirror1():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.transpose(Image.FLIP_TOP_BOTTOM)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_mirror2():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.transpose(Image.FLIP_LEFT_RIGHT)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_rotate():
    global window, canvas, paper, photo, photo2, oriX, oriY
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    photo2 = photo.copy()
    photo2 = photo2.rotate(degree, expand=True)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_bright():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("밝게", "값을 입력하세요(1.0~10.0)", minvalue=1.0, maxvalue=10.0)
    photo2 = photo.copy()
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_dart():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("어둡게", "값을 입력하세요(0.0~1.0)", minvalue=0.0, maxvalue=1.0)
    photo2 = photo.copy()
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_blur():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.filter(ImageFilter.BLUR)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_embo():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.filter(ImageFilter.EMBOSS)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_bw():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = ImageOps.grayscale(photo2)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)



def start():
    global path
    path = os.path.expanduser('~/naverDB').replace('\\', '/')

    con = sqlite3.connect(path)
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE userTable (id int, name char(15), data text")
    except Exception as e:
        print(e)


# sql 데이터 저장
def insertData(img, width, height):
    global path, idCount
    global photo, photo2
    con = sqlite3.connect(path)
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) FROM userTable")
    count = cur.fetchone()[0]
    print("데이터 개수:", count)

    imgRGB = img.convert('RGB')
    RGBstr = ""
    for i in range(0, height):
        tmpstr = ""
        for k in range(0, width):
            r, g, b = imgRGB.getpixel((k,i))
            tmpstr += "#%x%x%x" % (r, g, b)
        RGBstr += tmpstr



# img -> DB
def loadImage(fname, width, height):
    global path, inImage
    con = sqlite3.connect(path)
    cur = con.cursor()
    fp = open(fname, 'rb')
    for row in range(0, width):
        for col in range(0, height):
            data = int(ord(fp.read(1)))
            sql = 'INSERT INTO imgTable (' +str(row) + "," + str(col) + str(col) + "," + str(data) + ")" 
            cur.execute(sql)
    
    fp.close()
    con.commit()
    con.close()


# DB -> 메모리
def loadDatabase(width, height):
    global path, inImage
    row, col, data = 0, 0, 0
    record = None

    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute("SELECT * FROM imgTable")
    
    # 빈 inImage 생성
    for i in range(0, width):
        tmpList = []
        for k in range(0, height):
            data = 0
            tmpList.append(data)
        inImage.append(tmpList)

    # 테이블 --> inImage
    while(True):
        record = cur.fetchone()
        if record == None:
            break
        row = record[0]
        col = record[1]
        data = record[2]
        inImage[row][col] = data
    
    con.close

def saveDatabase():
    pass

window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0
path = None
idCount = 0

window = Tk()
window.geometry("600x300")
window.title("미니 포토샵")

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_command(label="파일 저장", command=func_save)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(1)", menu=image1Menu)
image1Menu.add_command(label="확대", command=func_zoomin)
image1Menu.add_command(label="축소", command=func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label="상하 반전", command=func_mirror1)
image1Menu.add_command(label="좌우 반전", command=func_mirror2)
image1Menu.add_command(label="회전", command=func_rotate)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(2)", menu=image2Menu)
image2Menu.add_command(label="밝게", command=func_bright)
image2Menu.add_command(label="어둡게", command=func_dart)
image2Menu.add_separator()
image2Menu.add_command(label="블러링", command=func_blur)
image2Menu.add_command(label="엠보싱", command=func_embo)
image2Menu.add_separator()
image2Menu.add_command(label="흑백이미지", command=func_bw)

edtFrame = Frame(window)
edtFrame.pack(side=BOTTOM)

edtName = Entry(edtFrame, width=10)
edtName.pack(side=LEFT, padx=10, pady=10)
btnInsert = Button(edtFrame, text="저장", command=saveDatabase)
btnInsert.pack(side=LEFT)
btnLoad = Button(edtFrame, text="조회", command=loadDatabase)
btnLoad.pack(side=LEFT)

window.mainloop()
