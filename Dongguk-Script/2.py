import sqlite3
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
from tkinter.messagebox import showerror, showinfo
import shutil


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

    if saveFp:
        photo2.save(saveFp.name)
        saveToDatabase(os.path.basename(saveFp.name)[:-4], saveFp.name)


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


def func_mirror():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = ImageOps.mirror(photo2)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_rotate():
    global window, canvas, paper, photo, photo2, oriX, oriY
    angle = askinteger("회전", "회전할 각도를 입력하세요", minvalue=1, maxvalue=360)
    photo2 = photo.copy()
    photo2 = photo2.rotate(angle)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_bright():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("밝게", "밝게 할 값(0~2)을 입력하세요", minvalue=0.0, maxvalue=2.0)
    enhancer = ImageEnhance.Brightness(photo)
    photo2 = enhancer.enhance(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_dark():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("어둡게", "어둡게 할 값(0~2)을 입력하세요", minvalue=0.0, maxvalue=2.0)
    enhancer = ImageEnhance.Brightness(photo)
    photo2 = enhancer.enhance(1 / value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_clear():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    newX = oriX
    newY = oriY
    displayImage(photo2, newX, newY)


def saveToDatabase(title, path):
    conn = sqlite3.connect('imageDB')
    cur = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS imageTable (title TEXT, path TEXT)"
    cur.execute(sql)
    sql = "SELECT * FROM imageTable WHERE title='" + title + "'"
    cur.execute(sql)
    if cur.fetchone() != None:
        sql = "UPDATE imageTable SET path=? WHERE title=?"
        cur.execute(sql, (path, title))
    else:
        sql = "INSERT INTO imageTable VALUES (?, ?)"
        cur.execute(sql, (title, path))
    conn.commit()
    conn.close()


def insertData():
    conn = sqlite3.connect('imageDB')
    cur = conn.cursor()
    dirName = askdirectory()
    for dirName, subDirList, fnames in os.walk(dirName):
        for fname in fnames:
            if os.path.basename(fname).split(".")[1].upper() in ['JPG', 'JPEG', 'BMP', 'PNG']:
                fullPath = os.path.join(dirName, fname)
                title = os.path.basename(fname)
                with open(fullPath, 'rb') as f:
                    blobData = f.read()
                sql = "INSERT INTO imageTable (title, path) VALUES (?, ?)"
                cur.execute(sql, (title, fullPath))
    conn.commit()
    conn.close()


def loadData():
    conn = sqlite3.connect('imageDB')
    cur = conn.cursor()
    sql = "SELECT title FROM imageTable"
    cur.execute(sql)
    fileList = cur.fetchall()
    for fname in fileList:
        listBox.insert(END, fname[0])
    conn.close()


def func_exit():
    window.quit()
    window.destroy()


window = Tk()
window.geometry("250x250")
window.title("이미지 뷰어")

canvas = Canvas(window, height=250, width=250)
canvas.pack()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 추가", command=insertData)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

imageDBMenu = Menu(mainMenu)
mainMenu.add_cascade(label="DB", menu=imageDBMenu)
imageDBMenu.add_command(label="불러오기", command=loadData)

controlMenu = Menu(mainMenu)
mainMenu.add_cascade(label="제어", menu=controlMenu)
controlMenu.add_command(label="확대", command=func_zoomin)
controlMenu.add_command(label="축소", command=func_zoomout)
controlMenu.add_command(label="좌우 반전", command=func_mirror)
controlMenu.add_command(label="회전", command=func_rotate)
controlMenu.add_separator()
controlMenu.add_command(label="밝게", command=func_bright)
controlMenu.add_command(label="어둡게", command=func_dark)
controlMenu.add_separator()
controlMenu.add_command(label="원본 복원", command=func_clear)

window.mainloop()
