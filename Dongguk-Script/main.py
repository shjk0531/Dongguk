from tkinter import *

def get_scale_value():
    value = scale_value.get()
    print("Scale 값:", value)

window = Tk()
window.title("Scale 값 가져오기")

scale_value = DoubleVar()
scale = Scale(window, variable=scale_value, from_=2, to=4, resolution=0.1)
scale.pack()

btn = Button(window, text="값 가져오기", command=get_scale_value)
btn.pack()

window.mainloop()
