import tkinter as tk
import tkinter.ttk as ttk
import cv2
from PIL import ImageTk, Image
import tkinter.filedialog as fd
import matplotlib.pyplot as plt
import numpy as np

class pic():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("LAST")
        self.window.geometry("1200x700")

        self.nb = ttk.Notebook(self.window)
        self.t1 = ttk.Frame(self.nb)
        self.t2 = ttk.Frame(self.nb)
        self.t3 = ttk.Frame(self.nb)
        self.t4 = ttk.Frame(self.nb)
        self.t5 = ttk.Frame(self.nb)

        self.nb.add(self.t1, text='選擇圖片')
        self.nb.add(self.t2, text='灰階')
        self.nb.add(self.t3, text='二值化')
        self.nb.add(self.t4, text='直方圖')
        self.nb.add(self.t5, text='HSV')
        self.nb.pack(expand=1, fill="both")
# =======================================================選擇檔案=======================================================
        self.oimg = ""
        self.btn = tk.Button(self.t1, text="選擇圖片", command=self.openfile)
        self.btn.pack(anchor=tk.S)
        self.label1 = tk.Label(self.t1, text="")
        self.label1.pack(anchor=tk.S)
        self.window.bind('<Motion>', self.motion)
        self.label = tk.Label(self.window, text=" ", font=("SimSun", 24), fg="red")
        self.label.pack()
# =========================================================灰階=========================================================
        self.btn = tk.Button(self.t2, text="灰階", command=self.gray)
        self.btn.pack(anchor=tk.S)
        self.label2 = tk.Label(self.t2, text="")
        self.label2.pack(anchor=tk.S)
# ========================================================二值化========================================================
        '''self.btn = tk.Button(self.t3, text="二值化",command=self.twoval)
        self.btn.pack(anchor=tk.S)'''

        self.sc = tk.Scale(self.t3, from_=0, to=255, length=200, orient=tk.HORIZONTAL, command=self.twoval)
        self.sc.pack(anchor=tk.S)
        self.v = tk.IntVar()
        self.v.set(2)
        self.check = ""
        self.MAX = tk.Radiobutton(self.t3, text="取最大", variable=self.v, value="False", command=self.click1).pack(anchor="s")
        self.MIN = tk.Radiobutton(self.t3, text="取最小", variable=self.v, value="True", command=self.click2).pack(anchor="s")
        self.label3 = tk.Label(self.t3, text="")
        self.label3.pack(anchor=tk.S)
# ========================================================直方圖========================================================
        self.btn = tk.Button(self.t4, text="直方圖", command=self.hist)
        self.btn.pack(anchor=tk.S)
        self.label4 = tk.Label(self.t4, text="")
        self.label4.pack(anchor=tk.S)
# =========================================================HSV=========================================================
        self.label5 = tk.Label(self.t5, text="")
        self.label5.pack(side=tk.LEFT)

        self.lower = np.array([0, 0, 0])
        self.upper = np.array([0, 0, 0])

        # H upper、lower
        self.scHU = tk.Scale(self.t5, label='H upper', from_=0, to=180, length=200, orient=tk.HORIZONTAL, command=self.h_up)
        self.scHU.pack(anchor=tk.E)
        self.scHL = tk.Scale(self.t5, label='H lower', from_=0, to=180, length=200, orient=tk.HORIZONTAL, command=self.h_low)
        self.scHL.pack(anchor=tk.E)
        # S upper、lower
        self.scSU = tk.Scale(self.t5, label='S upper', from_=0, to=255, length=200, orient=tk.HORIZONTAL, command=self.s_up)
        self.scSU.pack(anchor=tk.E)
        self.scSL = tk.Scale(self.t5, label='S lower', from_=0, to=180, length=200, orient=tk.HORIZONTAL, command=self.s_low)
        self.scSL.pack(anchor=tk.E)
        # V upper、lower
        self.scVU = tk.Scale(self.t5, label='V upper', from_=0, to=255, length=200, orient=tk.HORIZONTAL, command=self.v_up)
        self.scVU.pack(anchor=tk.E)
        self.scVL = tk.Scale(self.t5, label='V lower', from_=0, to=180, length=200, orient=tk.HORIZONTAL, command=self.v_low)
        self.scVL.pack(anchor=tk.E)
# ======================================================================================================================
        self.window.mainloop()
# =======================================================選擇檔案=======================================================
    def openfile(self):
        file = fd.askopenfilename()
        print(file)
        if file == "":
            return
        self.img = cv2.imread(file)
        self.oimg = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(self.oimg)
        image2 = ImageTk.PhotoImage(image=im)

        if self.label1 is None:
            self.label1.image = image2
            self.label1.pack()
        else:
            self.label1.configure(image=image2)
            self.label1.image = image2
# =========================================================灰階=========================================================
    def gray(self):
        oimg = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        im = Image.fromarray(oimg)
        image3 = ImageTk.PhotoImage(image=im)
        if self.label2 is None:
            self.label2.image = image3
            self.label2.pack()
        else:
            self.label2.configure(image=image3)
            self.label2.image = image3
    #二值化
        if self.label3 is None:
            self.label3.image = image3
            self.label3.pack()
        else:
            self.label3.configure(image=image3)
            self.label3.image = image3
# ========================================================二值化========================================================
    def twoval(self, x):
        oimg = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        if self.check == "":
            return
        if self.check == False:
            ret, oimg = cv2.threshold(oimg, int(x), 255, cv2.THRESH_BINARY)
        else:
            ret, oimg = cv2.threshold(oimg, int(x), 255, cv2.THRESH_BINARY_INV)

        im = Image.fromarray(oimg)
        image4 = ImageTk.PhotoImage(image=im)

        if self.label3 is None:
            self.label3.image = image4
            self.label3.pack()
        else:
            self.label3.configure(image=image4)
            self.label3.image = image4

    def click1(self):
        self.check = False

    def click2(self):
        self.check = True
# ========================================================直方圖========================================================
    def hist(self):
        #img = cv2.imread('baboon.Bmp')
        oimg = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        plt.hist(oimg.ravel(), 256, [0, 256])
        plt.savefig("filename.png")
        ##plt.show()  #右邊顯示

        img2 = cv2.imread('filename.png')
        oimg = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(oimg)
        image5 = ImageTk.PhotoImage(image=im)
        if self.label4 is None:
            self.label4.image = image5
            self.label4.pack()
        else:
            self.label4.configure(image=image5)
            self.label4.image = image5
# =========================================================HSV=========================================================
    def h_up(self, hu):
        self.upper[0] = hu
        self.pit()
    def h_low(self, hl):
        self.lower[0] = hl
        self.pit()
    def s_up(self, su):
        self.upper[1] = su
        self.pit()
    def s_low(self, sl):
        self.lower[1] = sl
        self.pit()
    def v_up(self, vu):
        self.upper[2] = vu
        self.pit()
    def v_low(self, vl):
        self.lower[2] = vl
        self.pit()

    def pit(self):
        hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        hsv = cv2.inRange(hsv, self.lower, self.upper)  # Threshold the HSV image to get only blue colors
        res = cv2.bitwise_and(self.img, self.img, mask=hsv)
        res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(res)
        hsv1 = ImageTk.PhotoImage(image=im)

        self.label5.configure(image=hsv1)
        self.label5.image = hsv1

        self.label5.pack()
        # Bitwise-AND mask and original image
        #res = cv2.bitwise_and(oimg, oimg, mask=mask)
# =========================================================滑鼠=========================================================
    def motion(self, event):
        x, y = event.x, event.y

        if self.oimg == "":
            return
        try:
            BGR = self.oimg[y,x]
            self.label.configure(text="(x, y) = (" + str(x) + ", " + str(y) + ")" + " " + "BGR : " + str(BGR))
            print("BGR:", BGR)
            print("===================")

        except:
            return

    def topic(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        #hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        plt.hist(gray.ravel(), 256, [0, 256])
        plt.show()

main = pic()