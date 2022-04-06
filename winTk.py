import copy
from tkinter import *
from tkinter import ttk
import cv2
import image
from tkinter.filedialog import askopenfilename


class MyWindow:

    def __init__(self, win):
        win.title("תפריט")
        win.geometry("600x600+800+50")
        # arrControlres
        self.arrControlers = []
        # button:
        self.btn1 = Button(win, text="בחירת תמונה", command=self.select_picture)
        self.btn2 = Button(win, text="חיתוך", command=self.cut)
        self.btn3 = Button(win, text="הכנסת טקסט", command=self.text)
        self.btn4 = Button(win, text="שמירת שינוים", command=self.save)
        self.btn5 = Button(win, text="צורה")
        self.btn6 = Button(win, text="יציאה", command=self.exit)
        self.lb1 = Label(win, text="לחץ מקש ימיני על התמונה כדי לשנות אותה")
        # btn3
        self.btn3_entry1 = Entry(win)

        # btn5
        self.btn5_btn1 = Button(win, text="עיגול", command=self.circle1)
        self.btn5_btn2 = Button(win, text="ריבוע", command=self.rectangle1)
        global n
        n = IntVar()
        n.set(2)
        self.btn5_label1 = Label(win, text="בחר גודל צורה", fg='blue')
        self.btn5_rdio1 = Radiobutton(win, text="קטן", variable=n, value=1)
        self.btn5_rdio2 = Radiobutton(win, text="בינוני", variable=n, value=2)
        self.btn5_rdio3 = Radiobutton(win, text="גדול", variable=n, value=3)
        self.btn5_label2 = Label(win, text="בחר צבע צורה", fg='blue')
        s = StringVar()
        self.btn5_cmb1 = ttk.Combobox(win, width=27, textvariable=s)
        self.btn5_cmb1['values'] = ("heavy", "normal", "thin")
        self.btn5_listBox = Listbox(win, height=3)
        color = ('red', 'green', 'blue')
        for i in color:
            self.btn5_listBox.insert(END, i)
        # נגדיר מיקום
        self.positions()

    def positions(self):
        self.btn1.grid(row=0, column=5)
        self.btn2.grid(row=0, column=4)
        self.btn3.grid(row=0, column=3)
        self.btn4.grid(row=0, column=2)
        self.btn5.grid(row=0, column=1)
        self.btn6.grid(row=0, column=0)
        self.lb1.place(x=50, y=500)
        # נגדיר ארועים
        self.events()

    def events(self):
        self.btn5.bind('<Button-1>', self.shape)
        self.btn5_cmb1.bind('<<ComboboxSelected>>', self.border)

    def select_picture(self):
        self.clear()
        fopen = askopenfilename()
        image.image1 = image.MyImage(fopen, "t")

    def cut(self):
        self.clear()
        global cut_flag
        if cut_flag:
            cv2.setMouseCallback(image.image1.name_windows, image.image1.affect)
        else:
            cv2.setMouseCallback(image.image1.name_windows, image.image1.cut)
        cut_flag = not cut_flag

    def text(self):
        self.clear()
        self.btn3_entry1.grid(row=1, column=5)
        self.arrControlers.append(self.btn3_entry1)
        cv2.destroyAllWindows()
        cv2.putText(image.image1.img, self.btn3_entry1.get(), (120, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 4)
        cv2.imshow(image.image1.name_windows, image.image1.img)

    def save(self):
        self.clear()
        cv2.imwrite("flow.jpg", image.image1.img)

    def exit(self):
        self.clear()
        cv2.destroyAllWindows()
        window2.destroy()

    def clear(self):
        for i in self.arrControlers:
            i.grid_remove()
        self.arrControlers.clear()

    def shape(self, event):
        self.clear()
        self.btn5_btn1.grid(row=1, column=5)
        self.btn5_btn2.grid(row=2, column=5)
        self.btn5_label1.grid(row=3, column=5)
        self.btn5_rdio1.grid(row=4, column=4)
        self.btn5_rdio2.grid(row=5, column=4)
        self.btn5_rdio3.grid(row=6, column=4)
        self.btn5_label2.grid(row=7, column=5)
        self.btn5_listBox.grid(row=8, column=5)
        self.btn5_cmb1.grid(row=9, column=5)
        # arrControlers
        self.arrControlers.append(self.btn5_btn1)
        self.arrControlers.append(self.btn5_btn2)
        self.arrControlers.append(self.btn5_label1)
        self.arrControlers.append(self.btn5_rdio1)
        self.arrControlers.append(self.btn5_rdio2)
        self.arrControlers.append(self.btn5_rdio3)
        self.arrControlers.append(self.btn5_label2)
        self.arrControlers.append(self.btn5_listBox)
        self.arrControlers.append(self.btn5_cmb1)

    # circle,square...
    def circle1(self):
        # color
        colorT = ()
        if self.btn5_listBox.get(ACTIVE) == "blue":
            colorT = (255, 0, 0)
        if self.btn5_listBox.get(ACTIVE) == "green":
            colorT = (0, 255, 0)
        if self.btn5_listBox.get(ACTIVE) == "red":
            colorT = (0, 0, 255)
        # size
        size = n.get()*10#
        print(n)#
        cv2.destroyAllWindows()
        cv2.circle(image.image1.img, (100, 100), size, colorT, 5)
        cv2.imshow(image.image1.name_windows, image.image1.img)

    def rectangle1(self):
        self.color()
        colorT = ()
        if self.btn5_listBox.get(ACTIVE) == "blue":
            colorT = (255, 0, 0)
        if self.btn5_listBox.get(ACTIVE) == "green":
            colorT = (0, 255, 0)
        if self.btn5_listBox.get(ACTIVE) == "red":
            colorT = (0, 0, 255)
        cv2.destroyAllWindows()
        cv2.rectangle(image.image1.img, (100, 100), (300, 300), colorT, 5)
        cv2.imshow(image.image1.name_windows, image.image1.img)

    def color(self):
        for i in self.btn5_listBox:
            print(i)

    def border(self, event):
        thickness = 5
        selected = self.btn5_cmb1.get()
        if selected == "heavy":
            thickness = 60
        elif selected == "normal":
            thickness = 30
        elif selected == "thin":
            thickness = 10
        dst = cv2.copyMakeBorder(image.image1.img, thickness, thickness, thickness, thickness, cv2.BORDER_CONSTANT,
                                 value=[0, 255, 0])
        image.image1.img = copy.copy(dst)
        cv2.imshow(image.image1.name_windows, image.image1.img)


# false מצב לא חתוך אם נלחץ יתחיל להחתך
n = 0
cut_flag = False
window2 = Tk()
myWin = MyWindow(window2)
window2.mainloop()
cv2.waitKey(0)
