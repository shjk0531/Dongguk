from tkinter import *
from tkinter import messagebox
from time import *
from tkinter import ttk

# window = Tk()


# window.title("window practice")
# window.geometry("400x100")
# window.resizable(width=FALSE, height=FALSE)


# label1 = Label(window, text="COOKBOOK~~ Python을")
# label2 = Label(window, text="열심히", font=("은 궁서", 30), fg="blue")
# label3 = Label(window, text="공부 중입니다.", bg="magenta",
#                width=20, height=5, anchor=SE)
# label1.pack()
# label2.pack()
# label3.pack()


# photo = PhotoImage(file="./source/GIF/dog.gif")
# label1 = Label(window, image=photo)
# label1.pack()


# buttton1 = Button(window, text="파이썬 종료", fg="red", command=quit)
# buttton1.pack()


# def myFunc():
#     messagebox.showinfo("강아지 버튼", "강이지가 귀엽죠?")


# photo = PhotoImage(file="./source/GIF/dog2.gif")
# button1 = Button(window, image=photo, command=myFunc)

# button1.pack()


# def myFunc():
#     if chk.get() == 0:
#         messagebox.showinfo("", "체크버튼이 꺼졌어요.")
#     else:
#         messagebox.showinfo("", "체크버튼이 켜졌어요")


# chk = IntVar()
# cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)

# cb1.pack()


# btnList = [None] * 9
# fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif",
#              "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", "pie.gif"]
# photoList = [None] * 9
# i, k = 0, 0
# xPos, yPos = 0, 0
# num = 0

# window.geometry("210x210")

# for i in range(0, 9):
#     photoList[i] = PhotoImage(file="./source/GIF/" + fnameList[i])
#     btnList[i] = Button(window, image=photoList[i])

# for i in range(0, 3):
#     for j in range(0, 3):
#         btnList[num].place(x=xPos, y=yPos)
#         num += 1
#         xPos += 70
#     xPos = 0
#     yPos += 70


# fnameList = []
# for i in range(0, 9):
#     fnameList.append("jeju%s.gif" % str(i+1))
# PhotoList = [None] * 9
# num = 0


# def clickNext():
#     global num
#     num += 1
#     if num > 8:
#         num = 0
#     photo = PhotoImage(file="./source/GIF/" + fnameList[num])
#     pLabel.configure(image=photo)
#     pLabel.image = photo


# def clickPrev():
#     global num
#     num -= 1
#     if num < 0:
#         num = 8
#     photo = PhotoImage(file="./source/GIF/" + fnameList[num])
#     pLabel.configure(image=photo)
#     pLabel.image = photo


# window.geometry("700x500")
# window.title("view photo")

# btnPrev = Button(window, text="<< 이전", command=clickPrev)
# btnNext = Button(window, text="다음 >>", command=clickNext)

# photo = PhotoImage(file="./source/GIF/" + fnameList[0])
# pLabel = Label(window, image=photo)

# btnPrev.place(x=250, y=10)
# btnNext.place(x=400, y=10)
# pLabel.place(x=15, y=50)


# window.mainloop()


# def myFunc():
#     if var.get() == 1:
#         labelImage.configure(image=photo1)
#     elif var.get() == 2:
#         labelImage.configure(image=photo2)
#     else:
#         labelImage.configure(image=photo3)


# var, labelImage = 0, None
# photo1, photo2, photo3 = [None] * 3

# if __name__ == "__main__":
#     window = Tk()
#     window.geometry("400x400")
#     window.title("choice pet")
#     labelText = Label(window, text="좋아하는 동물 투표", fg="blue", font=("은 궁서체", 20))

#     var = IntVar()
#     rb1 = Radiobutton(window, text="강아지", variable=var, value=1)
#     rb2 = Radiobutton(window, text="고양이", variable=var, value=2)
#     rb3 = Radiobutton(window, text="토끼", variable=var, value=3)
#     buttonOk = Button(window, text="사진 보기", command=myFunc)

#     photo1 = PhotoImage(file="./source/GIF/dog3.gif")
#     photo2 = PhotoImage(file="./source/GIF/cat.gif")
#     photo3 = PhotoImage(file="./source/GIF/rabbit.gif")

#     labelImage = Label(window, width=200, height=200, bg="yellow", image=None)

#     labelText.pack(padx=5, pady=5)
#     rb1.pack(padx=5, pady=5)
#     rb2.pack(padx=5, pady=5)
#     rb3.pack(padx=5, pady=5)
#     buttonOk.pack(padx=5, pady=5)
#     labelImage.pack(padx=5, pady=5)

#     window.mainloop()


window = Tk()
# window.iconbitmap("./source/python.ico")

baseTab = ttk.Notebook(window)

tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text="강아지")
tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text="고양이")

baseTab.pack(expand=1, fill="both")

photoDog = PhotoImage(file="./source/GIF/dog7.gif")
labelDog = Label(tabDog, image=photoDog)
labelDog.pack()

photoCat = PhotoImage(file="./source/GIF/cat5.gif")
labelCat = Label(tabCat, image=photoCat)
labelCat.pack()

window.mainloop()
