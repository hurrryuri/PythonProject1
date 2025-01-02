#강아지, 고양이, 토끼를 옵션단추로 구성해서 원하는 동물을 선택해서
#사진보기 버튼을 클릭하면 해당이미지를 출력하는 프로그램
from tkinter import *

#사진보기 버튼시 처리할 함수
def imageClick():
    if var.get() == 1:
        labelImage.configure(image=photo1)
    elif var.get() == 2:
        labelImage.configure(image=photo2)
    else: #1,2가 아닌 모든 경우
        labelImage.configure(image=photo3)

var, labelImage = 0, None #옵션단추, 이미지
photo1, photo2, photo3 = [None] * 3 # 강아지, 고양이, 토끼 이미지 저장

###메인

window = Tk()
#화면 구성
window.geometry("400X400") #윈도우 크기
window.title("동물 투표")
window.resizable(width=0, height=0) #윈도우 고정

#작업에 필요한 이미지(시간이 오래 걸리는 작업은 초기)
photo1 = PhotoImage(file="gif/dog3.gif")
photo2 = PhotoImage(file="gif/cat3.gif")
photo3 = PhotoImage(file="gif/rabbit2.gif")

labelText = label(window, text="좋아하는 동물 투표", fg="blue",
                  font=("궁서체", 20))
labelText.pack(padx=5, pady=5) #여백

#옵션단추
var = IntVar() #정수형을 저장할 수 있는 상태로 초기화
rb1 = Radiobutton(window, text="강아지", variable=var, value=1)
rb2 = Radiobutton(window, text="고양이", variable=var, value=2)
rb3 = Radiobutton(window, text="토끼", variable=var, value=3)
rb1.pack(padx=5, pady=5)
rb2.pack(padx=5, pady=5)
rb3.pack(padx=5, pady=5)

#버튼
btn = Button(window, text="사진 보기", command=imageClick)
btn.pack(padx=5, pady=5)

#그림을 출력할 레이블
labelImage = Label(window, image=None, width=200, height=200)
labelImage.pack(padx=5, pady=5)

#작업에 필요한 이미지


window.mainloop()