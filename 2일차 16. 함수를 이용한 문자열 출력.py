#입력 대화상자를 이용해서 문자열을 입력받아
#한글자씩 분리하여 임의의 크기 및 색상, 위치로 출력하는 프로그램
import turtle
import random
from tkinter.simpledialog import * #윈도우 라이브러리(대화상자 일부분)

#set~ : 받은 인수값을 저장하는 목적으로 사용,
# get~ : return으로 결과값을 전달하고자 할때 사용,
# is~ : 함수내에 if문으로 true, false의 비교결과값으로 전달할때 사용
#일반적인 동작함수는 명사로 구성
def getAstStr(): #문자열을 입력받는 함수
    #문자열을 변수에 저장 후 변경없이 결과처리할 때는 변수가 불필요
    #inStr = askstring("문자열 입력", "문자열을 입력하세요.")
    #return inStr
    return askstring("문자열 입력", "문자열을 입력하세요.")

def getColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def getXYS(swidth, sheight):
    tX = random.randrange(int(-swidth / 2), int(swidth / 2))
    tY = random.randrange(int(-sheight / 2), int(sheight / 2))
    # ;한행에 여러 문장을 표현할 때
    txtSize = random.randrange(10, 50)

    return (tX, tY, txtSize)


inStr = "" #입력받은 문자열을 저장할 변수
swidth, sheight = 300, 300 #윈도우 크기

tX, tY, txtSize = [0]*3 #난수로 생성할 위치, 글자크기를 저장할 변수

turtle.title("거북이 문자열 출력")
turtle.shape("turtle")
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup() #선그리기 해제

#askstring("창제목", "문자열")
inStr = getAstStr()

for ch in inStr: #문자열을 한글자씩 분리해서 반복
    #작업에 필요한 값들을 난수로 완성
    tX, tY, txtSize = getXYS(swidth, sheight)

    r, g, b = getColor()

    turtle.goto(tX, tY) #출력할 위치로 거북이를 이동
    turtle.pencolor((r,g,b))
    turtle.write(ch, font=("Arial", txtSize, 'bold')) #해당문자를 출력


turtle.done
