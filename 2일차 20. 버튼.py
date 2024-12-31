#버튼은 윈도우 창에서 동작을 지시할 때
#Label로 속성과 동일하게 속성을 적용 가능
#추가된 부분은 command=작업지정
from tkinter import *
from tkinter import messagebox #메세지창, alert
def myFunc():
    #알림창("제목", "문자열")
    messagebox.showinfo('강아지 버튼', '강아지 버튼을 눌렀습니다.')

#==============================================
win = Tk()
photo = PhotoImage(file="gif/dog2.gif") #이미지를 읽기
#함수명() 바로 실행, 함수명은 대기
button = Button(win, image=photo, command=myFunc)

button.pack()
win.mainloop()