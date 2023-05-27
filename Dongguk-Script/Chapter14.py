import sqlite3
import os, io
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps


def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY

    window.geometry(str(width) + "x" + str(height))
    if canvas is not None:
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
    canvas.pack(padx=10, pady=10)


def func_open():
    global window, canvas, paper, photo, photo2, oriX, oriY
    readFp = askopenfilename(parent=window, filetypes=(
        ("모든 그림 파일", "*.jpeg, *.bmp, *.png, *tif, *gif, *.jpg"), ("모든 파일", "*.*")))
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
    global window
    window.destroy()


def input_scale():
    global scale_window, scale_value

def func_zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY, scale_window, scale_value

    def get_scale_value():
        value = scale_value.get()

    scale_window = Tk()
    scale_window.title("확대 배율 선택")
    scale_window.geometry("200x100")

    scale_value = DoubleVar()
    scale = Scale(scale_window, variable=scale_value, from_=2, to=4, resolution=0.01)
    scale.pack()

    btn = Button(scale_window, text="확인", command=get_scale_value)
    btn.pack()

    window.mainloop()

    scale = askinteger("확대", "확대할 배율을 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo2.resize((int(oriX*scale), int(oriY*scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("축소", "축소할 배율을 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo2.resize((int(oriX/scale), int(oriY/scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_mirror1():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.transpose(Image.FLIP_TOP_BOTTOM)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_mirror2():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.transpose(Image.FLIP_LEFT_RIGHT)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_rotate():
    global window, canvas, paper, photo, photo2, oriX, oriY
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    photo2 = photo2.rotate(degree, expand=True)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_bright():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("밝게", "값을 입력하세요(1.0~10.0)", minvalue=1.0, maxvalue=10.0)
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_dart():
    global window, canvas, paper, photo, photo2, oriX, oriY
    value = askfloat("어둡게", "값을 입력하세요(0.0~1.0)", minvalue=0.0, maxvalue=1.0)
    photo2 = ImageEnhance.Brightness(photo2).enhance(value)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_blur():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.filter(ImageFilter.BLUR)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_embo():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.filter(ImageFilter.EMBOSS)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_bw():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = ImageOps.grayscale(photo2)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_rollback():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)



def insertDatabase(name):
    global path, photo, photo2, idCount
    path = os.path.expanduser('~/imgDB').replace('\\', '/')

    con = sqlite3.connect(path)
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS imageDB (id INTEGER PRIMARY KEY, name TEXT, extension TEXT, image BLOB)")

    extension = photo.format

    image_data = io.BytesIO()
    photo2.save(image_data, format='JPEG')
    image_data = image_data.getvalue()

    cur.execute("INSERT INTO imageDB (name, extension, image) VALUES (?, ?, ?)",
                (name, extension, image_data))

    messagebox.showinfo("저장 완료", "이미지 저장이 완료되었습니다.")
    con.commit()
    con.close()
    

def inputName():
    global entry_name, name_window
    
    name = entry_name.get().strip()

    if name == "":
        messagebox.showwarning("경고", "이미지 이름을 입력하세요.")
        return

    insertDatabase(name)
    name_window.destroy()


def insert_image_to_db():
    global name_window, entry_name

    name_window = Tk()
    name_window.title("이름 입력")
    name_window.geometry("200x100")

    label_name = Label(name_window, text="이름:")
    label_name.pack()

    entry_name = Entry(name_window)
    entry_name.pack()

    btn_submit = Button(name_window, text="확인", command=inputName)
    btn_submit.pack()

    name_window.mainloop()



def loadDatabase():
    global path, photo, photo2, oriX, oriY, window, canvas, name_window, name_listbox, load_button

    path = os.path.expanduser('~/imgDB').replace('\\', '/')

    con = sqlite3.connect(path)
    cur = con.cursor()

    cur.execute("SELECT name FROM imageDB")
    rows = cur.fetchall()
    con.close()

    if rows:
        name_window = Tk()
        name_window.title("이미지 선택")
        name_window.geometry("200x200")

        label_name = Label(name_window, text="이미지 선택:")
        label_name.pack()

        name_listbox = Listbox(name_window)
        for row in rows:
            name_listbox.insert(END, row[0])
        name_listbox.pack()

        load_button = Button(name_window, text="로드", command=loadImage)
        load_button.pack()

        name_window.mainloop()
    else:
        messagebox.showinfo("로드 실패", "로드할 이미지가 없습니다.")


def loadImage():
    global name_window, name_listbox, load_button, path, photo, photo2, oriX, oriY, window, canvas

    selected_name = name_listbox.get(ANCHOR)
    path = os.path.expanduser('~/imgDB').replace('\\', '/')

    con = sqlite3.connect(path)
    cur = con.cursor()

    cur.execute("SELECT image FROM imageDB WHERE name=?", (selected_name,))
    row = cur.fetchone()
    con.close()

    if row:
        messagebox.showinfo("로드 완료", "이미지 로드가 완료되었습니다.")
        photo = Image.open(io.BytesIO(row[0])).convert('RGB')
        oriX = photo.width
        oriY = photo.height

        photo2 = photo.copy()
        newX = photo2.width
        newY = photo2.height
        displayImage(photo2, newX, newY)
        name_window.destroy()
    else:
        messagebox.showinfo("로드 실패", "로드할 이미지가 없습니다.")


window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0
path = None
idCount = 0
scale = 0

window = Tk()
window.geometry("600x300")
window.title("미니 포토샵")
window.minsize(600, 500)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_command(label="파일 저장", command=func_save)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

imageFrame = Frame(window, padx=10, pady=10)
imageFrame.pack(side=RIGHT)

btnZoomIn = Button(imageFrame, text="확대", command=func_zoomin, width=8, height=1)
btnZoomOut = Button(imageFrame, text="축소", command=func_zoomout, width=8, height=1)
btnMirror1 = Button(imageFrame, text="상하 반전", command=func_mirror1, width=8, height=1)
btnMirror2 = Button(imageFrame, text="좌우 반전", command=func_mirror2, width=8, height=1)
btnRotate = Button(imageFrame, text="회전", command=func_rotate, width=8, height=1)
btnBright = Button(imageFrame, text="밝게", command=func_bright, width=8, height=1)
btnDart = Button(imageFrame, text="어둡게", command=func_dart, width=8, height=1)
btnBlur = Button(imageFrame, text="블러", command=func_blur, width=8, height=1)
btnEmbo = Button(imageFrame, text="엠보싱", command=func_embo, width=8, height=1)
btnBw = Button(imageFrame, text="흑백", command=func_bw, width=8, height=1)
btnRollback = Button(imageFrame, text="복원", command=func_rollback, width=8, height=1)

btnZoomIn.pack(padx=5, pady=5)
btnZoomOut.pack(padx=5, pady=5)
btnMirror1.pack(padx=5, pady=5)
btnMirror2.pack(padx=5, pady=5)
btnRotate.pack(padx=5, pady=5)
btnBright.pack(padx=5, pady=5)
btnDart.pack(padx=5, pady=5)
btnBlur.pack(padx=5, pady=5)
btnEmbo.pack(padx=5, pady=5)
btnBw.pack(padx=5, pady=5)
btnRollback.pack(padx=5, pady=5)


edtFrame = Frame(window, padx=10, pady=10)
edtFrame.pack(side=BOTTOM)

btnInsert = Button(edtFrame, text="이미지 저장", command=insert_image_to_db)
btnLoad = Button(edtFrame, text="이미지 로드", command=loadDatabase)

btnInsert.pack(side=LEFT, padx=5, pady=5)
btnLoad.pack(side=LEFT, padx=5, pady=5)


window.mainloop()
