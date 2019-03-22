#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 21, 2019 10:40:23 PM CET  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import Gui.Form_support as Form_support
import Logic.SignalTypeSelector as SignalTypeSelector
import matplotlib.pyplot as plt

def start_Gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, draw
    root = tk.Tk()
    Form_support.set_Tk_var()
    top = Toplevel1 (root)
    Form_support.init(root, top)
    root.mainloop()

def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    Form_support.set_Tk_var()
    top = Toplevel1 (w)
    Form_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def destroy_Window():
    root.destroy()

def readConfiguration():
    t0 = float(Form_support.entry1.get())
    time = float(Form_support.entry2.get())
    freq = float(Form_support.entry3.get())
    ampli = float(Form_support.entry4.get())
    samples = float(Form_support.entry5.get())
    type = Form_support.var1.get()
    return [t0, time, freq, ampli, samples, type]

def onDrawClicked():
    config = readConfiguration()
    signal = SignalTypeSelector.SignalTypeSelector(config).getSignal()
    plt.subplot(2, 1, 1)
    x = signal.getTime()
    y = signal.getSignal(x)
    plt.plot(x, y, '-', markersize=0.9)
    plt.subplot(2, 1, 2)
    plt.hist(y, bins=100)
    plt.show()

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("661x649+411+24")
        top.title("Generowanie sygnałów")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.03, rely=0.031, relheight=0.408, relwidth=0.946)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=625)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.192, rely=0.075, height=21, width=144)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''CZAS POCZĄTKOWY''')
        self.Label1.configure(width=144)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.224, rely=0.189, height=21, width=114)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''CZAS TRWANIA''')
        self.Label3.configure(width=114)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.192, rely=0.302, height=21, width=154)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''CZĘSTOTLIWOŚĆ SYGNAŁU''')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.528, rely=0.075,height=20, relwidth=0.262)
        self.Entry1.configure(background="#ffffff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=Form_support.entry1)

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.528, rely=0.189,height=20, relwidth=0.262)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable=Form_support.entry2)

        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry3.place(relx=0.528, rely=0.302,height=20, relwidth=0.262)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable=Form_support.entry3)

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.256, rely=0.415, height=21, width=72)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''AMPLITUDA''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.16, rely=0.528, height=21, width=187)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''CZĘSTOTLIWOŚĆ PRÓBKOWANIA''')

        self.Entry4 = tk.Entry(self.Frame1)
        self.Entry4.place(relx=0.528, rely=0.415,height=20, relwidth=0.262)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(textvariable=Form_support.entry4)

        self.Entry5 = tk.Entry(self.Frame1)
        self.Entry5.place(relx=0.528, rely=0.528,height=20, relwidth=0.262)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(textvariable=Form_support.entry5)

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.816, rely=0.302, height=21, width=20)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Hz''')

        self.Label9 = tk.Label(self.Frame1)
        self.Label9.place(relx=0.816, rely=0.528, height=21, width=20)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Hz''')

        self.Label10 = tk.Label(self.Frame1)
        self.Label10.place(relx=0.816, rely=0.189, height=21, width=11)
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''s''')
        self.Label10.configure(width=11)

        self.Label11 = tk.Label(self.Frame1)
        self.Label11.place(relx=0.816, rely=0.075, height=21, width=11)
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''s''')

        self.Label12 = tk.Label(self.Frame1)
        self.Label12.place(relx=0.288, rely=0.642, height=21, width=27)
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''TYP''')

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.528, rely=0.642, relheight=0.079
                , relwidth=0.261)
        self.TCombobox1.configure(width=163)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(textvariable=Form_support.var1)
        self.TCombobox1.configure(values=["sinus", "sinus wyprostowany jednopołówkowo", "sinus wyprostowany dwupołówkowo"])
        self.TCombobox1.current(0)

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.03, rely=0.447, relheight=0.485, relwidth=0.946)

        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=625)

        self.Label13 = tk.Label(self.Frame2)
        self.Label13.place(relx=0.448, rely=0.0, height=21, width=61)
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''OPERACJE''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.862, rely=0.94, height=34, width=77)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Wyjdź''')
        self.Button1.configure(width=77)
        self.Button1.configure(command=lambda: destroy_Window())

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.726, rely=0.94, height=34, width=77)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Rysuj''')
        self.Button2.configure(width=77)
        self.Button2.configure(command=lambda : onDrawClicked())

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.454, rely=0.0, height=21, width=50)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''SYGNAŁ''')






