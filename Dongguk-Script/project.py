# 필요한 모듈을 임포트합니다
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askinteger, askstring
from PIL import Image, ImageTk, ImageFilter, ImageOps

# 전역 변수를 선언합니다
window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0
db_conn = None

# 함수를 정의합니다

# 데이터베이스 연결


def connect_database():
    global db_conn
    db_conn = sqlite3.connect('image_database.db')
    cursor = db_conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS images (name TEXT, image BLOB)')

# 데이터베이스 연결 해제


def disconnect_database():
    global db_conn
    if db_conn:
        db_conn.close()

# 이미지를 데이터베이스에 저장


def save_image_to_database(name, image):
    global db_conn
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO images (name, image) VALUES (?, ?)", (name, image))
    db_conn.commit()

# 데이터베이스에서 이미지를 불러옴


def load_image_from_database(name):
    global db_conn
    cursor = db_conn.cursor()
    cursor.execute("SELECT image FROM images WHERE name=?", (name,))
    image_data = cursor.fetchone()[0]
    image = Image.open(BytesIO(image_data))
    return image


def displayImage(image, newX, newY):
    global window, canvas, paper
    canvas.delete("IMG")
    canvas.config(width=newX, height=newY)
    paper = PhotoImage(width=newX, height=newY)
    canvas.create_image((newX // 2, newY // 2), image=paper, tag="IMG")
    for i in range(0, newX, 10):
        canvas.create_line([(i, 0), (i, newY)], tag='IMG', fill='gray')
    for j in range(0, newY, 10):
        canvas.create_line([(0, j), (newX, j)], tag='IMG', fill='gray')
    image = image.resize((newX, newY))
    paper = ImageTk.PhotoImage(image)
    canvas.create_image((newX // 2, newY // 2), image=paper, tag="IMG")


def func_open():
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 파일을 열기 위한 대화상자를 표시하고 이미지를 불러옵니다
    file = askopenfilename(parent=window,
                           filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    photo = Image.open(file)
    photo2 = photo.copy()
    oriX, oriY = photo2.width, photo2.height
    newX, newY = oriX, oriY

    # 이미지를 화면에 표시합니다
    window.geometry(str(newX) + "x" + str(newY))
    displayImage(photo2, newX, newY)


def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 저장할 파일 경로를 선택하기 위한 대화상자를 표시하고 이미지를 저장합니다
    if photo2 is None:
        return
    file = asksaveasfilename(parent=window,
                             filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")),
                             defaultextension=".gif")
    photo2.save(file)


def func_exit():
    global window
    disconnect_database()
    window.quit()


def func_zoom():
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 이미지를 축소하기 위한 대화상자를 표시하고 입력값을 받아옵니다
    scale = askinteger("축소", "축소할 배율을 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.copy()
    photo2 = photo2.resize((int(oriX / scale), int(oriY / scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_flip():
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 이미지를 좌우로 뒤집습니다
    if photo2 is None:
        return
    photo2 = photo2.transpose(Image.FLIP_LEFT_RIGHT)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_rotate():
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 이미지를 회전하기 위한 대화상자를 표시하고 입력값을 받아옵니다
    if photo2 is None:
        return
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=1, maxvalue=360)
    photo2 = photo2.rotate(degree)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_blur():
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 이미지를 흐리게 처리합니다
    if photo2 is None:
        return
    photo2 = photo2.filter(ImageFilter.BLUR)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_sharpen():
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 이미지를 날카롭게 처리합니다
    if photo2 is None:
        return
    photo2 = photo2.filter(ImageFilter.SHARPEN)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_bw():
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 이미지를 흑백으로 변환합니다
    if photo2 is None:
        return
    photo2 = photo2.convert("L")
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_invert():
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 이미지의 색상을 반전시킵니다
    if photo2 is None:
        return
    photo2 = ImageOps.invert(photo2)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_reset():
    global window, canvas, paper, photo, photo2, oriX, oriY

    # 이미지를 원본으로 되돌립니다
    photo2 = photo.copy()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


# 데이터베이스에 저장
def func_saveDatabase():
    global photo2
    if photo2 is None:
        return
    name = askstring("데이터베이스 저장", "이미지 이름을 입력하세요")
    if name:
        photo2.save(name + ".gif")


# 데이터베이스 불러오기
def func_loadDatabase():
    global photo, photo2
    file = askopenfilename(parent=window, filetypes=(
        ("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    if file:
        photo = Image.open(file)
        photo2 = photo.copy()
        oriX, oriY = photo2.width, photo2.height
        newX, newY = oriX, oriY
        window.geometry(str(newX) + "x" + str(newY))
        displayImage(photo2, newX, newY)


# 메인 코드를 실행합니다
window = Tk()
window.title("이미지 처리 프로그램")

# 캔버스를 생성합니다
canvas = Canvas(window, height=500, width=500)
canvas.pack()

# 메뉴를 생성합니다
mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_command(label="저장", command=func_save)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

imageMenu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지", menu=imageMenu)
imageMenu.add_command(label="축소", command=func_zoom)
imageMenu.add_command(label="좌우 뒤집기", command=func_flip)
imageMenu.add_command(label="회전", command=func_rotate)
imageMenu.add_separator()
imageMenu.add_command(label="흐리게", command=func_blur)
imageMenu.add_command(label="날카롭게", command=func_sharpen)
imageMenu.add_separator()
imageMenu.add_command(label="흑백", command=func_bw)
imageMenu.add_command(label="색상 반전", command=func_invert)
imageMenu.add_separator()
imageMenu.add_command(label="원본으로 되돌리기", command=func_reset)


databaseMenu = Menu(mainMenu)
mainMenu.add_cascade(label="데이터베이스", menu=databaseMenu)
databaseMenu.add_command(label="데이터베이스 저장", command=func_saveDatabase)
databaseMenu.add_command(label="데이터베이스 불러오기", command=func_loadDatabase)

# 이벤트 루프를 시작합니다
window.mainloop()
