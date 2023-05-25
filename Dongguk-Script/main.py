from tkinter import *
import sqlite3
import os


# img -> DB
def loadImage(fname):
    global path, inImage, XSIZE, YSIZE
    
    con = sqlite3.connect(path)
    cur = con.cursor()
    fp = open(fname, 'rb')
    for row in range(0, XSIZE):
        for col in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            sql = 'INSERT INTO rawTable VALUES(' + str(row) + "," + str(col) + "," + str(data) + ")" 
            cur.execute(sql)
    
    fp.close()
    con.commit()
    con.close()


# DB -> 메모리
def loadDatabase():
    global path, inImage, XSIZE, YSIZE
    row, col, data = 0, 0, 0
    record = None

    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute("SELECT * FROM rawTable")
    
    # 빈 inImage 생성
    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
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
    
    con.close()


def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)
        rgbString += "{" + tmpString + "} "
    paper.put(rgbString)

path = os.path.expanduser('~/rawDB').replace('\\', '/')


window, canvas, XSIZE, YSIZE = None, None, 256, 256
inImage = []

if __name__ == "__main__":
    window = Tk()
    window.title("RAW-->DB")
    canvas = Canvas(window, height=XSIZE, width=YSIZE)
    paper = PhotoImage(width=XSIZE, height=YSIZE)
    canvas.create_image((XSIZE / 2, YSIZE / 2), image=paper, state="normal")

    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS rawTable")
    cur.execute("CREATE TABLE rawTable(row int, col int, dta int)")  # 행, 열, 픽셀값
    con.commit()
    con.close()

    filename = 'C:/Users/shinj/Development/University/Dongguk/Dongguk-Script/source/RAW/tree.raw'
    loadImage(filename)
    loadDatabase()
    displayImage(inImage)

    canvas.pack()
    window.mainloop()