from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry("400X400")
label1 = Label(window, text="선택한 파일명")
label1.pack()
#parent=부모창, filetypes 파일 유형=(메세지, 확장자)
#와일드카드
fileName = askopenfilename(parent=window,
                           filetypes=(
                                ("GIF파일", "*.gif"),
                                ("JPG파일", "*.jpg"),
                                ("모든 파일", "*.*")
                                                     )
                           )
#pack()이후에 변경은 configure()
label1.configure(text=str(fileName))

window.mainloop()