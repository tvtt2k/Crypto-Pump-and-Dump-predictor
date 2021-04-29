from tkinter import *

import login as l
import register as r
import landing as ld
from tkinter import ttk
from ttkthemes import themed_tk as tk
from PIL import Image, ImageTk
def put(*l):
    for i in l:
        i.pack()


def putl(*l):
    for i in l: 
        i.pack(side = LEFT)

class main():
    def log(self):

        userx = l.login()
        userx.log(self.uname.get(), self.password.get())
        self.a.destroy()
        self.d = ld.land(self.uname.get())
    def reg(self):
        self.a.destroy()
        userx = r.register()
        userx.reg()

    def __init__(self):
        a = tk.ThemedTk()
        a.get_themes()
        a.set_theme('radiance')
        image1 = Image.open("C:/gui/brown_munde.png")
        test = ImageTk.PhotoImage(image1)
        my_canvas = Canvas(a,width=800,height=600)
        my_canvas.pack(fill="both",expand=True)
        my_canvas.create_image(0,0,image=test,anchor='nw')
        self.a = a
        self.uname = StringVar()
        self.password = StringVar()
        user = Frame(my_canvas)
        ul = ttk.Label(user, text="Enter Username :",font=("Times New Roman",14))
        ue = Entry(user, textvariable=self.uname)
        putl(ul, ue)
        pwd = Frame(my_canvas)
        pl = ttk.Label(pwd, text='Enter Password :',font=("Times New Roman",14))
        pe = Entry(pwd, textvariable=self.password, show="*")
        putl(pl, pe)
        loginbut = ttk.Button(my_canvas, text='Login', command=self.log)
        registerbut = ttk.Button(my_canvas, text='Register', command=self.reg)
        put(user, pwd, loginbut, registerbut)
        a.mainloop()
if __name__ == "__main__":
    x = main()