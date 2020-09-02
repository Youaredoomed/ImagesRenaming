'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                                        2020-09-02
                     Renaming Books (ver 1.0.0)
                                                     by Youaredoomed
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os.path
import glob
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

class tkGUI():
    def __init__(self):
        self.new_dir = ''
        self.new_name = ''
        self.file_extension = ''

        w=600; h=400; x=300; y=300
        self.root = tk.Tk()
        self.root.title("Renaming books")
        self.root.geometry("{}x{}+{}+{}".format(w,h,x,y)) #뒤에 값은 실행 시 나오는 위치
        self.root.resizable(width=False, height=False) #사이즈 변경 불가능
        self.filedl_index=0

        self.gui()
        self.root.mainloop()

    def gui(self):
        #TODO: 메뉴 구성
        menu = tk.Menu(self.root)
        menu.add_cascade(label="Help")

        self.root.config(menu=menu)


        # 위젯 구성
        frameList = tk.Frame(self.root, takefocus=True, background="blue")
        scrollbar_X = tk.Scrollbar(frameList, orient=tk.HORIZONTAL )
        scrollbar_Y = tk.Scrollbar(frameList, )
        self.listbox = tk.Listbox(frameList, xscrollcommand = scrollbar_X, yscrollcommand = scrollbar_Y, activestyle="none", width=109)

        lbl_dir = tk.Label(self.root, text="PATH")
        self.ent_dir = tk.Entry(self.root, width=63, state="normal")
        lbl_name = tk.Label(self.root, text="name")
        self.ent_name = tk.Entry(self.root, textvariable=tk.StringVar(self.root,value='Noname'))
        lbl_flex = tk.Label(self.root, text="확장자")
        self.combox = ttk.Combobox(self.root, width=10, state="readonly")
        self.combox['value'] = ('gif','png','jpg')

        # command=함수()로 사용시 바로 실행이 됩니다. command=함수명 으로 입력하세요.
        btn_up = tk.Button(self.root, text="Up", width=5, command=self.listUp)
        btn_down = tk.Button(self.root, text="Down", width=5, command=self.listDown)
        btn_findFolder = tk.Button(self.root, text="폴더 추가", width=10, command=self.filedl_folder)
        btn_findFile = tk.Button(self.root, text="파일 추가", width=10, command=self.filedl_file)
        btn_ok = tk.Button(self.root, text="변환", width=10, command=self.run)
        btn_delete = tk.Button(self.root, text="선택 제거", width=10, command=self.listDel)
        btn_findPath = tk.Button(self.root, text="경로 찾기", width=10, command=self.findFolder)

        # 위젯 배치
        frameList.place(x=5, y=5, width=500, height=300)
        scrollbar_X.pack(side='bottom', fill="both")
        scrollbar_Y.pack(side="right", fill="both")
        self.listbox.pack(side="left", fill="both")

        lbl_dir.place(x=5, y=315)
        self.ent_dir.place(x=45, y=315)
        lbl_name.place(x=5, y=350)
        self.ent_name.place(x=45, y=350)

        btn_up.place(x=520, y=130)
        btn_down.place(x=520, y=170)
        btn_findFolder.place(x=510, y=5)
        btn_findFile.place(x=510, y=35)
        btn_ok.place(x=510, y=350)
        btn_delete.place(x=510, y=250)
        btn_findPath.place(x=510, y=315)

        lbl_flex.place(x=350,y=350)
        self.combox.place(x=395, y=350)

        # todo: 스크롤바 사이즈 조절
        scrollbar_X["command"] = self.listbox.xview
        scrollbar_Y["command"] = self.listbox.yview

    def findFolder(self):
        filedl = filedialog.askdirectory(parent=self.root, title='경로 찾기')
        if (filedl == ''):
            return
        else:
            self.ent_dir.delete(0,255)
            self.ent_dir.insert(0, filedl)

    #들어가는 순서가 엉뚱함.
    def filedl_folder(self):
        filedl = filedialog.askdirectory(parent=self.root, title='폴더 열기')
        if (filedl == ''):
            return
        else:
            self.ent_dir.delete(0, 255)  # 255자 삭제
            self.ent_dir.insert(0, filedl)

            #폴더 내에 PNG 파일 찾기
            filedl_png = filedl +'/' +'*.PNG'
            fileList = glob.glob(filedl_png) # \문자 사용
            # \ 문자 대신 /로 변환
            count_here = 0
            for index in fileList:
                fileList[count_here] = index.replace('\\', '/')
                count_here += 1
            #중복확인
            for content in fileList:
                brk_label = False
                for i in range(self.listbox.size()):
                    brk_label = False
                    if(content == self.listbox.get(i)):
                        brk_label = True
                        break
                if brk_label == False:
                    self.listbox.insert(self.filedl_index, content)
                    self.filedl_index += 1

            #위와 동일
            filedl_jpg = filedl + '\*.JPG'
            fileList = glob.glob(filedl_jpg)
            count_here = 0
            for index in fileList:
                fileList[count_here] = index.replace('\\', '/')
                count_here += 1
            for content in fileList:
                brk_label = False
                for i in range(self.listbox.size()):
                    brk_label = False
                    if(content == self.listbox.get(i)):
                        brk_label = True
                        break
                if brk_label == False:
                    self.listbox.insert(self.filedl_index, content)
                    self.filedl_index += 1

    def filedl_file(self):
        filedl = filedialog.askopenfilenames(filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*")))
        print(filedl)
        if(filedl == ''):
            return
        else:
            self.ent_dir.delete(0,255) #255자 삭제
            self.ent_dir.insert(0, os.path.dirname(filedl[0])) #파일 경로를 넣어야함 -> 현재 파일경로가 아님

            for content in filedl:
                brk_label = False
                for i in range(self.listbox.size()):
                    brk_label = False
                    if (content == self.listbox.get(i)):
                        brk_label = True
                        break
                if brk_label == False:
                    self.listbox.insert(self.filedl_index, content)
                    self.filedl_index += 1

    def listUp(self):
        selected = self.listbox.curselection()
        try:
            selectedNum = selected[0]
        except IndexError:
            print("IndexError")
            return

        if selectedNum== 0 :
            return
        else:
            self.listbox.insert(selectedNum-1,self.listbox.get(selectedNum))
            self.listbox.delete(selectedNum+1)
            #커서 원위치
            self.listbox.activate(selectedNum)
            self.listbox.select_set(selectedNum-1)
            return

    def listDown(self):
        selected = self.listbox.curselection()
        try:
            selectedNum = selected[0]
        except IndexError:
            print("IndexError")
            return

        if selectedNum == self.listbox.size():
            return
        else:
            self.listbox.insert(selectedNum +2, self.listbox.get(selectedNum))
            self.listbox.delete(selectedNum)
            # 커서 원위치
            self.listbox.activate(selectedNum)
            self.listbox.select_set(selectedNum +1)
            return

    def listDel(self):
        selected = self.listbox.curselection()
        try:
            selectedNum = selected[0]
        except IndexError:
            print("IndexError")
            return
        self.listbox.delete(selectedNum)

    def clearList(self):
        for i in range(self.listbox.size()):
            self.listbox.delete(0)

    #todo: 순서 정렬 기능
    def descOrder(self):
        # 이름 순 정렬
        print("아직")

    def run(self):
        if self.ent_dir.get() =='':
            messagebox.showinfo("알림", "파일을 저장할 경로를 선택해주세요.")
            return
        else:
            self.new_dir = self.ent_dir.get()

        if self.combox.get() == '':
            messagebox.showinfo("알림", "파일 확장자를 선택해주세요.")
            return
        else:
            self.file_extension = self.combox.get()
        self.new_name = self.ent_name.get()
        self.new_dir = self.ent_dir.get()

        files = self.listbox.get(0, self.listbox.size())

        size = len(files)  # 파일 갯수
        size_len = len(str(size))  # 파일 갯수의 자릿수

        count = 0
        for index_file in files:
            count += 1
            len_zero = size_len - len(str(count))
            zeros = ''
            for index in range(len_zero):
                zeros = zeros + '0'
            os.rename(index_file, self.new_dir + '\\' +self.new_name + '_' + zeros + str(count) + '.' + self.file_extension)
        messagebox.showinfo("Finish", "작업이 완료되었습니다.")
        self.clearList()

        return print("성공")

if __name__ == '__main__':
    run = tkGUI()