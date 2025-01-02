#키보드 이벤트
#<key> : 모든 키
#<Return>, <BackSpace>, <Tap>, <Shift_L>, <Shift_R>... : 특수키
#<Up>, <Down>, <Left>, <Right>, <F1>~<F12>
#a~z, A~Z, <space>, <less> : 일반키
#<Shift-Up>, <Shift-Down>... : 조합키
from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    #keycode는 ASCII코드 A=>65 ===>chr() 아스키코드를 문자로 변환
    messagebox.showinfo("키보드 이벤트", "눌린키:"+chr(event.keycode)+","+str(event.keycode))

window = Tk()
window.bind("<key>", keyEvent) #키보드 이벤트

window.mainloop()