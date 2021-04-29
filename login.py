from tkinter import *
from db_connect import  mysql as ms
logsql = ms()
lmydb = logsql.mydb
lmycursor = logsql.mycursor
class login():

    def log(self,uname,password):
        try:
            lmycursor.execute('select user_name,password from users where user_name = %s and password = %s ',(uname,password))
            #unm,pwd = lmycursor.fetchall()[0]

        except:
            msg = Tk()
            l = Label(msg,text='Username or password incorrect',font=("Times New Roman",14)).pack()
            ok = Button(msg,text = 'OK',command=msg.destroy).pack()
            msg.mainloop()