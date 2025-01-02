#pillow 라이브러리를 이용해서 pillow에 제공하는 기능으로 간단한
#이미지 편집 프로그램
#메뉴 구성
#파일 - 파일열기, 파일저장, 프로그램종료
#이미지처리(1) - 확대(축소), 상하반전(좌우반전), 회전
#이미지처리(2) - 밝게(어둡게), 블러링, 엠보싱, 흑백이미지
from tkinter import * #윈도우
from tkinter.filedialog import * #파일 열기/저장
from tkinter.simpledialog import * #밝게/어둡게, 회전각도
from PIL import Image, ImageFilter, ImageEnhance, ImageOps #이미지효과

#함수
def func_open(): #파일열기
    pass

def func_save(): #파일저장
    pass

def func_close(): #윈도우 종료
    pass

def displayImage(): #윈도우 창에 이미지 출력
    pass

def func_zoomin(): #확대/축소
    pass

def func_zoomout(): #확대/축소
    pass

def func_mirror1(): #좌우/ 상하 뒤집기
    pass

def func_mirror2(): #좌우/상하 뒤집기
    pass

def func_rotate(): #회전
    pass

def func_bright(): #밝게
    pass

def func_dark(): #어둡게
    pass

def func_blur(): #블러
    pass

def func_embo(): #엠보싱
    pass

def func_bw(): #흑백이미지
    pass

#이미지읽기 -> 픽셀단위로 저장(paper)->효과적용(canvas) 출력
#모든 효과는 원본(paper)로 작업진행
#전역변수
window, canvas, paper = None, None, None #윈도우, 출력용작업지, 작업용
photo, photo2 = None, None #원본이미지, 결과이미지
oriX, oriY = 0, 0 #원본이미지 크기

##메인플그램(윈도우, 오브젝트배치, 메뉴구성)
window=Tk()
window.title("미니포토샵")
window.geometry("250X250")

window.mainloof()