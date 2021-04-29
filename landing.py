from tkinter import *
import tkinter as tk
from tkinter import ttk
from HistoricalAnomaly import HistoricalAnomaly
from RealTime import RealTime
from tkinter import ttk
from ttkthemes import themed_tk as tk1


#import RealGraph as rg
#from RealGraph import RealGraph
#import matplotlib.animation as animation

class landing(tk1.ThemedTk):
    def __init__(self, uname,anime ,*args, **kwargs):
        tk1.ThemedTk.__init__(self, *args, **kwargs)
        self.uname = uname
        window = ttk.Frame(self)
        self.anime = anime
        self.window = window
        self.HistoricalAnomaly = HistoricalAnomaly
        self.RealTime = RealTime
        self.Landing = Landing
        #self.HistGraph = HistGraph
        #self.RealGraph = RealGraph
        window.pack(fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        self.display_page(Landing)

    def display_page(self, sel):
        """if(sel == RealGraph):
            page = sel(self.window, self,self.anime)
        else:"""
        page = sel(self.window,self)
        page.grid(row=0, column=0, sticky="nsew")

class Landing(ttk.Frame):

    def __init__(self,window,obj):
        ttk.Frame.__init__(self,window)
        l = ttk.Label(self, text=" Welcome  {} ".format(obj.uname),font=("Times New Roman",14)).pack(side=TOP)
        bb = ttk.Button(self,text="Check Historical Anomalies",command=lambda: obj.display_page(HistoricalAnomaly)).pack()#, command=lambda: obj.display_page(Buy)
        bs = ttk.Button(self, text="Check Real time prices/anomalies",command=lambda: obj.display_page(RealTime)).pack()#, command=lambda: obj.display_page(Sell)


class land():
    def __init__(self,uname):

        landp = landing(uname,self)
        landp.get_themes()
        landp.set_theme('radiance')
        landp.title("Landing Page")
        #ani = animation.FuncAnimation(rg.f, rg.animate, interval=1000)
        landp.mainloop()
##C:\gui\ary(1)