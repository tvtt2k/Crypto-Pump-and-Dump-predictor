import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import *
from db_connect import mysql as ms
from ttkthemes import themed_tk as tk1
import datetime
from HistGraph import HistGraph
class HistoricalAnomaly(tk.Frame):
    def __init__(self, window, obj):
        ttk.Frame.__init__(self, window)
        menu = Frame(self)
        self.sql = ms()
        self.mycursor = self.sql.mycursor
        self.db = self.sql.mydb
        l = ttk.Label(menu, text="Menu: ",font=("Times New Roman",14)).pack(side=LEFT)
        bb = ttk.Button(menu, text="Landing page", command=lambda: obj.display_page(obj.Landing)).pack(side=LEFT)
        bd = ttk.Button(menu, text="Realtime Graph", command=lambda: obj.display_page(obj.RealTime)).pack(side=LEFT)
        menu.pack()
        l1 = ttk.Label(self, text="Historical Graph Selection",font=("Times New Roman",14)).pack()
        c_sel = StringVar()
        crypto_frame = ttk.Frame(self)
        currencies = self.sql.currencies
        start_date = datetime.datetime.now()
        l2 = ttk.Label(crypto_frame, text="Select Crypto Currency: ",font=("Times New Roman",14)).pack(side=LEFT)
        sel1 = ttk.Combobox(crypto_frame, values=list(currencies.keys()), textvariable=c_sel).pack(side=LEFT)
        def coin_sel(c_sel):
            self.coin = c_sel
            print(self.coin)

        selb = ttk.Button(crypto_frame, text="Select", command=lambda : coin_sel(c_sel.get())).pack(side=LEFT)
        crypto_frame.pack()
        b = ttk.Button(self, text='OK', command=lambda: self.HistoricGraph()).pack()

    def HistoricGraph(self):
        HistGraph(self.coin)



