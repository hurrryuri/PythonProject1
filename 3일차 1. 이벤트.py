#마우스, 키보드 이벤트
#마우스는 버튼이 3개로 구성
#<button> : 마우스 버튼
#<button-1> : 왼쪽 버튼
#<button-2> : 가운데 버튼
#<button-3> : 오른쪽 버튼
#마우스 떼었을 때
#<ButtonRelease>
#마우스 더블클릭 했을 때
#<Double-Button>
#마우스 드래그 할 때
#<B1-Motion>
#<B1-Motion>
#<B1-Motion>
#마우스에 이벤트 발생 후 처리하는 함수가 존재
from ctypes import windll
from tkinter import *
from tkinter import messagebox

def clickLeft(event): #event에 발생이벤트 정보가 저장
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")
def clickRight(event):  # event에 발생이벤트 정보가 저장
        messagebox.showinfo("마우스", "마우스 오른쪽 버튼이 클릭됨")

window = Tk()

#이벤트 적용
#대상.bind("이벤트", 메소드)
window.bind("<Button-1>", clickLeft)
window.bind("<Button-2>", clickLeft)
window.bind("<Button-3>", clickRight)

window.mainloop()
window.done()