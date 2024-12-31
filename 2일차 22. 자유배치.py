#pack() : 지정된 방향으로 순서대로 배치
#place(x=좌표값, y=좌표값) : 지정된 위치에 배치

#3x3으로 이미지 9개를 출력하는 프로그램
#이미지 크기가 가로세로 70*3= 가로 210, 세로210
from tkinter import *

btnList = [None]*9 #이미지를 적용할 버튼 9개를 빈값으로 생성
fnameList = [
    "honeycomb.gif",    "icecream.gif",      "jellybean.gif",
    "kitkat.gif",       "lollipop.gif",      "marshmallow.gif",
    "nougat.gif",       "oreo.gif",          "pie.gif"
] #작업할 이미지파일명을 지정
photoList = [None]*9 #그림을 저장할 리스트
xPos, yPos = 0, 0 #버튼을 출력할 좌표
num = 0 #작업할 이미지 번호
window = Tk()
window.geometry("210x210")
#준비(해당폴더에서 이미지파일을 읽어서 photoList에 저장)
#저장한 photoList의 이미지를 버튼에 지정
for i in range(0,9):
    photoList[i] = PhotoImage(file="gif/"+fnameList[i]) #해당이미지 읽기
    btnList[i] = Button(window, image=photoList[i]) #버튼에 이미지를 적용

#출력(가로(3)열X세로(3)행) ===> 행열
#for문의 변수로 규칙을 만들 수 없으면 외부변수를 활용
for i in range(0,3): #y=0,70,140 #0=0,1,2   1=0(3),1(4),2(5)   2=0(6),1(7),2(8)
    for j in range(0,3): #x=0, 70, 140
        btnList[num].place(x=xPos, y=yPos)
        num +=1 #이미지를 이동
        xPos += 70 #가로방향값만 증가
    yPos += 70 #세로 방향값을 증가
    xPos = 0 #다음 행에 가로시작좌표로 초기화




window.mainloop()