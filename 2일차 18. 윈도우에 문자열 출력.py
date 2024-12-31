#레이블 객체
#윈도우 창내에 문자열을 출력
#객체는 위에서 아래로 순서대로 출력
#객체 생성 후 윈도우창에 배치
from tkinter import *

window = Tk()
#윈도우 환경을 구성
#label(부모창, text="출력할 문자열", bg="배경색", width="폭", height="높이"
#text="문자열"
#bg="배경색"
#width="가로크기"
#height="세로크기"
#font=("글꼴", 크기, "효과") : 글자체 변경
#fg="글자색"
#andhor : 정렬(n-상단, s-하단, e-오른쪽, w-왼쪽)
#justify : 문자열 정렬(left, right, center)
#image="이미지" : 레이블에 이미지 출력
#padx, pady : 안쪽 여백
label1 = Label(window, text="Hello World") #window이름의 창에 문자열 출력
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text="공부중 입니다.", bg="magenta", width=20, height=5,
               anchor=SE)

label1.pack() #윈도우 창에 출력되는 결과는 pack() 담당
label2.pack() #작성한 객체를 윈도우창에 배치
label3.pack()

window.mainloop()

#pack()속성
#side="방향" : 지정된 방향으로 배치, top, bottom, left, right
#fill="방향" : 해당 객체를 지정한 방향으로 채우기(창크기에 맞게), none, x, y, both
#expand=0,1 : true, false으로 객체가 공간을 차지하도록 확장
#padx, pady : 안쪽 여백

#오브젝트들의 변수명 등을 공통으로 사용해서, 하나의 오브젝트를 익히면 다른 오브젝트를 바로 적용
