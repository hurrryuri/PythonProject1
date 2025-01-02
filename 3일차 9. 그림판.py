#선을 이용햇허 그림을 그리는 프로그램
#색상, 선두께를 지정하여 마우스 눌렀을때(시작위치), 마우스 떼었을때(끝위치)
#시작과 끝위치에 선을 그리는 프로그램
#작업지(캔버스)-그래픽을 작업할 수 있는 작업영역
from tkinter import *
from tkinter.colorchooser import * #색상대화상자
from tkinter.simpledialog import * #입력대화상자(선두께값)

#선그리기(x1, y1)-(x2,y2) : 시작과 끝 좌표사이에 선을 그린다.
#함수
def mouseClick(event): #마우스를 클릭 시 시작좌표 구하기
    global x1, y1
    x1 = event.x #현재 마우스 버튼을 누른 곳의 x,y 좌표를 저장(시작좌표)
    y1 = event.y

def mouseDrop(event): #마우스를 떼었을 때 끝좌표 구하고, 선그리기 작업
    global x1, y1, x2, y2, penWidth, penColor
    x2 = event.x #마우스 버튼을 떼었을 때 x,y좌표를 저장(끝좌표)
    y2 = event.y
    #해당좌표에 캔버스에 선을 그리는 작업
    canvas.create_line(x1, y1, x2, y2, fill=penColor, width=penWidth)

def getColor(): #선택한 색상값 적용
    #객체 변수는 자동으로 연결
    #일반 변수는 수동으로 연결
    global penColor #전역변수를 함수에 호출

    color = askcolor()
    penColor = color[1] #색상이름을 penColor에 저장

def getWidth(): #선두께값 지정
    global penWidth

    penWidth = askinteger("선두께", "선 두께(1~10)를 입력하세요.",
                          minvalue=1, maxvalue=10)

def windowClose():
    window.quit()
    window.destroy()

#함수와 메인프로그램의 변수전달을 위한 전역변수
window = None #윈도우
canvas = None #이미지 작업지
x1,y1,x2,y2 = [None]*4 #시작과 끝좌표
penColor = 'black' #선색
penWidth = 3 #선 두께

#메인프로그램
window = Tk()
window.title("짝퉁 그림판")
#작업지 구성 및 이벤트
canvas = Canvas(window, height=600, width=300) #작업지 설정
canvas.pack() #윈도우에 작업지 추가

canvas.bind("<button-1>", mouseClick) #마우스클릭
canvas.bind("<buttonRelease-1>", mouseDrop) #마우스 떼었을 때

#색상과 선두께 처리를 위한 메뉴
mainMenu = Menu(window)
window.config(menu=mainMenu)
canvasMenu = Menu(mainMenu) #주메뉴
mainMenu.add_cascade(label="설정", menu=canvasMenu)
canvasMenu.add_command(label="선 색상", command=getColor)
canvasMenu.add_command(label="선 두께", command=getWidth)
canvasMenu.add_separator()
canvasMenu.add_command(label="종료", command=windowClose)

window.mainloop()