import sqlite3
import io
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageTk



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
            tmpString += "#%02x%02x%02x " % (r, g, b)  # x 뒤에 한 칸 공백
        rgbString += "{" + tmpString + "} "  # } 뒤에 한 칸 공백
    paper.put(rgbString)
    canvas.pack()


def func_open():
    global window, canvas, paper, photo, photo2, oriX, oriY
    readFp = askopenfilename(parent=window, filetypes=(
        ("모든 그림 파일", "*.jpg; *.jpeg; *.bmp; *.png; *.tif; *.gif"), ("모든 파일", "*.*")))
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
        ("JPG 파일", "*.jpg; *.jpeg"), ("모든 파일", "*.*")))

    photo2.save(saveFp.name)


def func_exit():
    global window, canvas, paper, photo, photo2, oriX, oriY

    pass


def func_zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("확대", "확대할 배율을 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.copy()
    photo2 = photo2.resize((int(oriX * scale), int(oriY * scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("축소", "축소할 배율을 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.copy()
    photo2 = photo2.resize((int(oriX / scale), int(oriY / scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_rotate():
    global window, canvas, paper, photo, photo2, oriX, oriY
    angle = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    photo2 = photo.copy()
    photo2 = photo2.rotate(angle)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_flip():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.transpose(Image.FLIP_LEFT_RIGHT)
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


def func_sharpen():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    photo2 = photo2.filter(ImageFilter.SHARPEN)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_bright():
    global window, canvas, paper, photo, photo2, oriX, oriY
    brightness = askfloat("밝기 조절", "밝기 조절 값을 입력하세요", minvalue=-1.0, maxvalue=1.0)
    enhancer = ImageEnhance.Brightness(photo)
    photo2 = enhancer.enhance(brightness)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_contrast():
    global window, canvas, paper, photo, photo2, oriX, oriY
    contrast = askfloat("대비 조절", "대비 조절 값을 입력하세요", minvalue=0.0, maxvalue=3.0)
    enhancer = ImageEnhance.Contrast(photo)
    photo2 = enhancer.enhance(contrast)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_invert():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = ImageOps.invert(photo)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_reset():
    global window, canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.copy()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_database():
    global window, canvas, paper, photo, photo2, oriX, oriY
    conn = sqlite3.connect("image.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS images (id INTEGER PRIMARY KEY AUTOINCREMENT, image BLOB, name TEXT)"
    )
    # Convert the image to bytes
    img_byte_arr = io.BytesIO()
    photo2.save(img_byte_arr, format="PNG")
    img_bytes = img_byte_arr.getvalue()
    
    # Prompt for image name
    name = askstring("이름 입력", "이미지의 이름을 입력하세요")
    if name:
        # Insert image and name into the database
        cursor.execute("INSERT INTO images (image, name) VALUES (?, ?)", (sqlite3.Binary(img_bytes), name))
        conn.commit()
        messagebox.showinfo("이미지 저장", "이미지가 데이터베이스에 저장되었습니다.")
    conn.close()


def func_loadDatabase():
    global window, canvas, paper, photo, photo2, oriX, oriY
    conn = sqlite3.connect("image.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM images")
    rows = cursor.fetchall()

    # Create a new window to display the loaded images
    load_window = Toplevel()
    load_window.title("로드된 이미지")
    load_window.geometry("400x400")

    scrollbar = Scrollbar(load_window)
    scrollbar.pack(side=RIGHT, fill=Y)

    image_listbox = Listbox(load_window, yscrollcommand=scrollbar.set)
    image_listbox.pack(side=LEFT, fill=BOTH)

    scrollbar.config(command=image_listbox.yview)

    loaded_images = []  # Store the loaded images for future reference

    def select_image(event):
        selection = image_listbox.curselection()
        if selection:
            index = selection[0]
            _, selected_image, _ = loaded_images[index]
            displayImage(selected_image)

            # Add a button to return to the main menu
            return_button = Button(load_window, text="확인", command=load_window.destroy)
            return_button.pack()

    for row in rows:
        image = Image.open(io.BytesIO(row[1]))
        image.thumbnail((50, 50))  # Resize the image for display
        photo = ImageTk.PhotoImage(image)
        loaded_images.append((row[0], image, photo))  # Save the image and photo pair
        image_listbox.insert(END, row[2])  # Display the name in the listbox

    image_listbox.bind("<<ListboxSelect>>", select_image)

    conn.close()

# Move the select_image function outside of func_loadDatabase
def select_image(event):
    selection = image_listbox.curselection()
    if selection:
        index = selection[0]
        _, selected_image, _ = loaded_images[index]
        displayImage(selected_image, newX, newY)

        # Add a button to return to the main menu
        return_button = Button(load_window, text="확인", command=load_window.destroy)
        return_button.pack()

def func_exit():
    global window, canvas, paper, photo, photo2, oriX, oriY
    window.quit()
    window.destroy()


window = Tk()
window.geometry("250x250")
window.title("이미지 처리")

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

imageMenu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지", menu=imageMenu)
imageMenu.add_command(label="축소", command=func_zoomout)
imageMenu.add_command(label="회전", command=func_rotate)
imageMenu.add_command(label="뒤집기", command=func_flip)

effectMenu = Menu(mainMenu)
mainMenu.add_cascade(label="효과", menu=effectMenu)
effectMenu.add_command(label="흐리게", command=func_blur)
effectMenu.add_command(label="선명하게", command=func_sharpen)
effectMenu.add_separator()
effectMenu.add_command(label="밝기 조절", command=func_bright)
effectMenu.add_command(label="대비 조절", command=func_contrast)
effectMenu.add_separator()
effectMenu.add_command(label="색상 반전", command=func_invert)

toolMenu = Menu(mainMenu)
mainMenu.add_cascade(label="도구", menu=toolMenu)
toolMenu.add_command(label="원본 이미지로 복원", command=func_reset)
toolMenu.add_separator()
toolMenu.add_command(label="데이터베이스에 저장", command=func_database)
toolMenu.add_separator()
toolMenu.add_command(label="데이터베이스 불러오기", command=func_loadDatabase)


canvas = Canvas(window, height=500, width=500)
canvas.pack()

window.mainloop()



def func_exit():
    global window, canvas, paper, photo, photo2, oriX, oriY
    window.quit()
    window.destroy()


window = Tk()
window.geometry("250x250")
window.title("이미지 처리")

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

imageMenu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지", menu=imageMenu)
imageMenu.add_command(label="축소", command=func_zoomout)
imageMenu.add_command(label="회전", command=func_rotate)
imageMenu.add_command(label="뒤집기", command=func_flip)

effectMenu = Menu(mainMenu)
mainMenu.add_cascade(label="효과", menu=effectMenu)
effectMenu.add_command(label="흐리게", command=func_blur)
effectMenu.add_command(label="선명하게", command=func_sharpen)
effectMenu.add_separator()
effectMenu.add_command(label="밝기 조절", command=func_bright)
effectMenu.add_command(label="대비 조절", command=func_contrast)
effectMenu.add_separator()
effectMenu.add_command(label="색상 반전", command=func_invert)

toolMenu = Menu(mainMenu)
mainMenu.add_cascade(label="도구", menu=toolMenu)
toolMenu.add_command(label="원본 이미지로 복원", command=func_reset)
toolMenu.add_separator()
toolMenu.add_command(label="데이터베이스에 저장", command=func_database)
toolMenu.add_separator()
toolMenu.add_command(label="데이터베이스 불러오기", command=func_loadDatabase)


canvas = Canvas(window, height=500, width=500)
canvas.pack()

window.mainloop()
