import tkinter as tk
from tkinter import *
import RealGraph
from tkinter import ttk
from db_connect import mysql as ms
class RealTime(tk.Frame):
    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        menu = Frame(self)
        self.sql = ms()
        self.mycursor = self.sql.mycursor
        self.db = self.sql.mydb
        l = ttk.Label(menu, text="Menu: ",font=("Times New Roman",14)).pack(side=LEFT)
        bb = ttk.Button(menu, text="Landing", command=lambda: obj.display_page(obj.Landing)).pack(side=LEFT)
        bd = ttk.Button(menu, text="Historical Anomaly", command=lambda: obj.display_page(obj.HistoricalAnomaly)).pack(side=LEFT)
        menu.pack()
        l1 = ttk.Label(self,text="Realtime Graph Selection",font=("Times New Roman",14)).pack()
        c_sel = StringVar()
        crypto_frame = Frame(self)
        currencies = self.sql.currencies
        l2 = ttk.Label(crypto_frame, text="Select Crypto Currency: ",font=("Times New Roman",14)).pack(side=LEFT)
        self.paisa = ''
        def coin_sel(c_sel):
            x = c_sel.get()
            print("c_sel : ",x)
            global paisa
            self.paisa = currencies[x][0]
            print(self.paisa)

        sel1 = ttk.Combobox(crypto_frame, values=list(currencies.keys()), textvariable=c_sel).pack(side=LEFT)
        print(self.paisa)

        selb = ttk.Button(crypto_frame, text="Select", command=lambda: coin_sel(c_sel)).pack(side=LEFT)

        crypto_frame.pack()
        b = ttk.Button(self, text='OK', command=lambda: RealGraph.RealGraph(self.paisa)).pack()