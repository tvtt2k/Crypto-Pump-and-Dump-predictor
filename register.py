from db_connect import  mysql as ms
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk1
from PIL import Image, ImageTk
regsql = ms()
rmydb = regsql.mydb
rmycursor = regsql.mycursor
class register():

    def reg(self):
        r = tk1.ThemedTk()
        r.get_themes()
        r.set_theme('radiance')
        image2 = Image.open("C:/gui/xrp.png")
        test = ImageTk.PhotoImage(image2)
        my_canvas1 = Canvas(r, width=800, height=600)
        my_canvas1.pack(fill="both", expand=True)
        my_canvas1.create_image(0, 0, image=test, anchor='nw')
        self.uev=StringVar()
        self.pwdev=StringVar()
        self.emailev=StringVar()
        top = ttk.Label(my_canvas1,text = 'Registeration',font=("Times New Roman",14)).grid(row = 0,column = 0, columnspan = 2)
        ul = ttk.Label(my_canvas1,text = 'Enter Username: ',font=("Times New Roman",14)).grid(row = 1, column = 0)
        ue = Entry(my_canvas1, textvariable=self.uev).grid(row = 1, column = 1)
        pwdl = ttk.Label(my_canvas1, text='Enter Password: ',font=("Times New Roman",14)).grid(row = 2, column = 0)
        pwde = Entry(my_canvas1, textvariable=self.pwdev,show = '?').grid(row = 2, column = 1)
        emaill = ttk.Label(my_canvas1, text='Enter Email Id: ',font=("Times New Roman",14)).grid(row = 3, column = 0)
        emaile = Entry(my_canvas1, textvariable=self.emailev).grid(row = 3, column = 1)
        def mid():
            self.check()
            success = ttk.Label(my_canvas1, text="Login Successful ",font=("Times New Roman",14)).grid(row=9, column=0)
            ok = ttk.Button(my_canvas1, text='ok', command=r.destroy).grid(row=9, column=1)
        che = ttk.Button(my_canvas1,text = 'Register', command = mid).grid(row = 8,column = 0, columnspan = 2)

        r.mainloop()
    def check(self):
        try:
            sql = "insert into users(user_name,password,email_id) values(\"{}\",\"{}\",\"{}\")"

            rmycursor.execute(sql.format(str(self.uev.get()), self.pwdev.get(), self.emailev.get()))
            rmydb.commit()

        except Exception as e:
            print("enter unique username and email id",e)