import sqlite3
import os
import io
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *
from PIL import Image, ImageFilter, ImageEnhance, ImageOps


def display_image(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY

    window.geometry(str(width) + "x" + str(height))
    if canvas is not None:
        canvas.destroy()

    canvas = Canvas(window, width=width, height=height)
    paper = PhotoImage(width=width, height=height)
    canvas.create_image((width / 2, height / 2), image=paper, state="normal")
    rgb_string = ""
    rgb_image = img.convert('RGB')
    for i in range(0, height):
        tmpString = ""
        for k in range(0, width):
            r, g, b = rgb_image.getpixel((k, i))
            tmpString += "#%02x%02x%02x " % (r, g, b)   # x 뒤에 한 칸 공백
        rgb_string += "{" + tmpString + "} "            # } 뒤에 한 칸 공백
    paper.put(rgb_string)
    canvas.pack(padx=20, pady=(20, 10))


def func_open():
    global window, canvas, paper, photo, photo2, oriX, oriY
    read_fp = askopenfilename(parent=window, filetypes=(
        ("jpg 파일", "*.jpg"), ("png 파일", "*.png"), ("gif 파일", "*.gif"),
        ("jpeg 파일", "*.jpeg"), ("bmp 파일", "*.bmp"), ("tif 파일", "*.tif"), ("모든 파일", "*.*")))
    photo = Image.open(read_fp).convert('RGB')
    oriX = photo.width
    oriY = photo.height

    photo2 = photo.copy()
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


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


def func_zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY, scale_window

    def get_scale_value():
        global photo2, oriX, oriY
        value = scale_value.get()
        if value == 0.0:
            value = scale.get()
        photo2 = photo2.resize((int(oriX * value), int(oriY * value)))
        newX = photo2.width
        newY = photo2.height
        display_image(photo2, newX, newY)
        scale_window.destroy()

    scale_window = Tk()
    scale_window.title("확대 배율 선택")
    scale_window.geometry("400x150")

    scale_value = DoubleVar()
    scale = Scale(scale_window, variable=scale_value, from_=1, to=4,
                  resolution=0.01, orient="horizontal", length=400, tickinterval=0.5)
    scale.pack(padx=15, pady=15)

    btn = Button(scale_window, text="확인",
                 command=get_scale_value, width=8, height=1)
    btn.pack(padx=5, pady=5)

    window.mainloop()


def func_zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY, scale_window

    def get_scale_value():
        global photo2, oriX, oriY
        value = scale_value.get()
        if value == 0.0:
            value = scale.get()
        photo2 = photo2.resize((int(oriX / value), int(oriY / value)))
        newX = photo2.width
        newY = photo2.height
        display_image(photo2, newX, newY)
        scale_window.destroy()

    scale_window = Tk()
    scale_window.title("축소 배율 선택")
    scale_window.geometry("400x150")

    scale_value = DoubleVar()
    scale = Scale(scale_window, variable=scale_value, from_=1, to=10,
                  resolution=0.01, orient="horizontal", length=400, tickinterval=1)
    scale.pack(padx=15, pady=15)

    btn = Button(scale_window, text="확인",
                 command=get_scale_value, width=8, height=1)
    btn.pack(padx=5, pady=5)

    window.mainloop()


def func_mirror1():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.transpose(Image.FLIP_TOP_BOTTOM)
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


def func_mirror2():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.transpose(Image.FLIP_LEFT_RIGHT)
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


def func_rotate():
    global window, canvas, paper, photo, photo2, oriX, oriY, scale_window

    def get_scale_value():
        global photo2, oriX, oriY
        value = scale_value.get()
        if value == 0.0:
            value = scale.get()
        photo2 = photo2.rotate(value, expand=True)
        newX = photo2.width
        newY = photo2.height
        display_image(photo2, newX, newY)
        scale_window.destroy()

    scale_window = Tk()
    scale_window.title("회전 각도 선택")
    scale_window.geometry("400x150")

    scale_value = DoubleVar()
    scale = Scale(scale_window, variable=scale_value, from_=0, to=360,
                  resolution=5, orient="horizontal", length=400, tickinterval=30)
    scale.pack(padx=15, pady=15)

    btn = Button(scale_window, text="확인",
                 command=get_scale_value, width=8, height=1)
    btn.pack(padx=5, pady=5)

    window.mainloop()


def func_bright():
    global window, canvas, paper, photo, photo2, oriX, oriY, scale_window

    def get_scale_value():
        global photo2, oriX, oriY
        value = scale_value.get()
        if value == 0.0:
            value = scale.get()
        photo2 = ImageEnhance.Brightness(photo2).enhance(value)
        newX = photo2.width
        newY = photo2.height
        display_image(photo2, newX, newY)
        scale_window.destroy()

    scale_window = Tk()
    scale_window.title("밝게 설정")
    scale_window.geometry("400x150")

    scale_value = DoubleVar()
    scale = Scale(scale_window, variable=scale_value, from_=0, to=10,
                  resolution=0.1, orient="horizontal", length=400, tickinterval=1)
    scale.pack(padx=15, pady=15)

    btn = Button(scale_window, text="확인",
                 command=get_scale_value, width=8, height=1)
    btn.pack(padx=5, pady=5)

    window.mainloop()


def func_dart():
    global window, canvas, paper, photo, photo2, oriX, oriY, scale_window

    def get_scale_value():
        global photo2, oriX, oriY
        value = scale_value.get()
        if value == 0.0:
            value = scale.get()
        photo2 = ImageEnhance.Brightness(photo2).enhance(1/value)
        newX = photo2.width
        newY = photo2.height
        display_image(photo2, newX, newY)
        scale_window.destroy()

    scale_window = Tk()
    scale_window.title("어둡게 설정")
    scale_window.geometry("400x150")

    scale_value = DoubleVar()
    scale = Scale(scale_window, variable=scale_value, from_=0, to=10,
                  resolution=0.1, orient="horizontal", length=400, tickinterval=1)
    scale.pack(padx=15, pady=15)

    btn = Button(scale_window, text="확인",
                 command=get_scale_value, width=8, height=1)
    btn.pack(padx=5, pady=5)

    window.mainloop()


def func_blur():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.filter(ImageFilter.BLUR)
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


def func_embo():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.filter(ImageFilter.EMBOSS)
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


def func_bw():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = ImageOps.grayscale(photo2)
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


def func_rollback():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


def func_edge():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.filter(ImageFilter.EDGE_ENHANCE)
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


def func_contour():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.filter(ImageFilter.CONTOUR)
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


def func_smooth():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.filter(ImageFilter.SMOOTH)
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


def func_detail():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.filter(ImageFilter.DETAIL)
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


def func_denoise():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo2.filter(ImageFilter.SHARPEN)
    newX = photo2.width
    newY = photo2.height
    display_image(photo2, newX, newY)


def insert_database(name):
    global path, photo, photo2, idCount
    path = os.path.expanduser('~/imgDB').replace('\\', '/')

    con = sqlite3.connect(path)
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS imageDB (id INTEGER PRIMARY KEY, name TEXT, extension TEXT, image BLOB)")

    # 이름 중복 체크
    cur.execute("SELECT name FROM imageDB WHERE name=?", (name,))
    existing_name = cur.fetchone()

    if existing_name:
        result = messagebox.askquestion(
            "중복 확인", "이미 동일한 이름이 존재합니다. 기존 데이터를 덮어쓰시겠습니까?")
        if result == 'no':
            con.close()
            return

    extension = photo.format

    image_data = io.BytesIO()
    photo2.save(image_data, format='JPEG')
    image_data = image_data.getvalue()

    if existing_name:
        cur.execute("UPDATE imageDB SET extension=?, image=? WHERE name=?",
                    (extension, image_data, name))
    else:
        cur.execute("INSERT INTO imageDB (name, extension, image) VALUES (?, ?, ?)",
                    (name, extension, image_data))

    messagebox.showinfo("저장 완료", "이미지 저장이 완료되었습니다.")
    con.commit()
    con.close()


def input_name():
    global entry_name, name_window

    name = entry_name.get().strip()

    if name == "":
        messagebox.showwarning("경고", "이미지 이름을 입력하세요.")
        return

    insert_database(name)
    name_window.destroy()


def insert_image_to_db():
    global name_window, entry_name

    name_window = Tk()
    name_window.title("이름 입력")
    name_window.geometry("200x110")

    label_name = Label(name_window, text="이미지 이름 입력")
    label_name.pack(padx=5, pady=8)

    entry_name = Entry(name_window)
    entry_name.pack(padx=10, pady=(3, 10))

    btn_submit = Button(name_window, text="확인",
                        command=input_name, width=8, height=1)
    btn_submit.pack(padx=5, pady=5)

    name_window.mainloop()


def load_database():
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
        name_window.geometry("200x370")

        label_name = Label(name_window, text="이미지 선택")
        label_name.pack(pady=5)

        name_listbox = Listbox(name_window, height=15)
        for row in rows:
            name_listbox.insert(END, row[0])
        name_listbox.pack(pady=(0, 10))

        load_button = Button(name_window, text="로드",
                             command=load_image, width=8, height=1)
        load_button.pack(padx=10, pady=5)

        delete_button = Button(name_window, text="삭제",
                               command=delete_DB, width=8, height=1)
        delete_button.pack(pady=5)

        name_window.mainloop()
    else:
        messagebox.showinfo("로드 실패", "로드할 이미지가 없습니다.")


def load_image():
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
        display_image(photo2, newX, newY)
        name_window.destroy()
    else:
        messagebox.showinfo("로드 실패", "로드할 이미지가 없습니다.")


def delete_DB():
    global name_window, name_listbox, load_button, path, photo, photo2, oriX, oriY, window, canvas

    selected_name = name_listbox.get(ANCHOR)
    path = os.path.expanduser('~/imgDB').replace('\\', '/')

    con = sqlite3.connect(path)
    cur = con.cursor()

    cur.execute("DELETE FROM imageDB WHERE name=?", (selected_name,))
    con.commit()
    con.close()

    messagebox.showinfo("삭제 완료", "데이터 삭제가 완료되었습니다.")

    name_window.destroy()
    load_database()


window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0
path = None
idCount = 0
scale = 0

window = Tk()
window.geometry("600x300")
window.title("미니 포토샵")
window.minsize(600, 400)

main_menu = Menu(window)
window.config(menu=main_menu)

file_menu = Menu(main_menu)
main_menu.add_cascade(label="파일", menu=file_menu)
file_menu.add_command(label="파일 열기", command=func_open)
file_menu.add_command(label="파일 저장", command=func_save)
file_menu.add_separator()
file_menu.add_command(label="프로그램 종료", command=func_exit)

imageFrame2 = Frame(window, padx=10, pady=10)
imageFrame2.pack(side=RIGHT)

imageFrame = Frame(window, padx=10, pady=10)
imageFrame.pack(side=RIGHT)

btn_zoomIn = Button(imageFrame, text="확대",
                    command=func_zoomin, width=8, height=1)
btn_zoomOut = Button(imageFrame, text="축소",
                     command=func_zoomout, width=8, height=1)
btn_mirror1 = Button(imageFrame, text="상하 반전",
                     command=func_mirror1, width=8, height=1)
btn_mirror2 = Button(imageFrame, text="좌우 반전",
                     command=func_mirror2, width=8, height=1)
btn_rotate = Button(imageFrame, text="회전",
                    command=func_rotate, width=8, height=1)
btn_bright = Button(imageFrame, text="밝게",
                    command=func_bright, width=8, height=1)
btn_dart = Button(imageFrame, text="어둡게", command=func_dart, width=8, height=1)
btn_blur = Button(imageFrame, text="블러", command=func_blur, width=8, height=1)

btn_zoomIn.pack(padx=5, pady=5)
btn_zoomOut.pack(padx=5, pady=5)
btn_mirror1.pack(padx=5, pady=5)
btn_mirror2.pack(padx=5, pady=5)
btn_rotate.pack(padx=5, pady=5)
btn_bright.pack(padx=5, pady=5)
btn_dart.pack(padx=5, pady=5)
btn_blur.pack(padx=5, pady=5)


btn_embo = Button(imageFrame2, text="엠보싱",
                  command=func_embo, width=8, height=1)
btn_bw = Button(imageFrame2, text="흑백", command=func_bw, width=8, height=1)
btn_edge = Button(imageFrame2, text="선 강조",
                  command=func_edge, width=8, height=1)
btn_contour = Button(imageFrame2, text="윤곽",
                     command=func_contour, width=8, height=1)
btn_smooth = Button(imageFrame2, text="부드럽게",
                    command=func_smooth, width=8, height=1)
btn_detail = Button(imageFrame2, text="디테일",
                    command=func_detail, width=8, height=1)
btn_denoise = Button(imageFrame2, text="선명히",
                     command=func_denoise, width=8, height=1)
btn_rollback = Button(imageFrame2, text="복원",
                      command=func_rollback, width=8, height=1)


btn_embo.pack(padx=5, pady=5)
btn_bw.pack(padx=5, pady=5)
btn_edge.pack(padx=5, pady=5)
btn_contour.pack(padx=5, pady=5)
btn_smooth.pack(padx=5, pady=5)
btn_detail.pack(padx=5, pady=5)
btn_denoise.pack(padx=5, pady=5)
btn_rollback.pack(padx=5, pady=5)


edt_frame = Frame(window, padx=10, pady=10)
edt_frame.pack(side=BOTTOM)

btn_insert = Button(edt_frame, text="이미지 저장",
                    command=insert_image_to_db, width=11, height=1)
btn_load = Button(edt_frame, text="이미지 조회",
                  command=load_database, width=11, height=1)

btn_insert.pack(side=LEFT, padx=20, pady=5)
btn_load.pack(side=LEFT, padx=20, pady=5)


window.mainloop()
