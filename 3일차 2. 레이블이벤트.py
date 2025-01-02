from tkinter import *
from tkinter import messagebox

def clickImage(evemt):
    messagebox .showinfo("마우스", "토끼 레이블에서 마우스를 클릭했습니다.")

win = Tk()

#이미지 읽기
photo = PhotoImage(file="gif/rabbit2.gif")
label1 = Label(win, image=photo)
label1.pack() #패치
label1.bind("<button>", clickImage) #레이블에 이벤트를 적용

win.mainloop()