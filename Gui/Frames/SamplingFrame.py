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

import Gui.FormSupport as fs
import Gui.FormManager as FormManager


class SamplingFrame:
    def __init__(self, relx, rely, top=None):

        # ---------------------------------------FRAME----------------------------------------------

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=relx, rely=rely, relheight=0.558, relwidth=0.45)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=625)

        # ----------------------------------------LABELS FRAME-------------------------------------

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.30, rely=0.0, height=21, width=300)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''PRÓBKOWANIE, KWANTYZACJA, REKONSTRUKCJA''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.192, rely=0.2, height=21, width=144)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''OKRES PRÓBKOWANIA''')
        self.Label2.configure(width=144)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.22, rely=0.4, height=21, width=114)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''BITY KWANTYZACJI''')
        self.Label3.configure(width=114)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.1, rely=0.6, height=21, width=250)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''LICZBA PRÓBEK BRANYCH POD UWAGĘ''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.11, rely=0.8, height=21, width=250)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''DZIAŁANIE''')

        # ----------------------------ENTRIES FRAME-------------------------------

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.528, rely=0.2, height=20, relwidth=0.262)
        self.Entry1.configure(background="#ffffff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=fs.samplingPeriodEntry)

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.528, rely=0.4, height=20, relwidth=0.262)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable=fs.quantizationBitsEntry)

        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry3.place(relx=0.528, rely=0.6, height=20, relwidth=0.262)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable=fs.nOSamplesEntry)

        # -----------------------------------------COMBOBOXES FRAME------------------------------------------

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.528, rely=0.8, height=21
                              , relwidth=0.261)
        self.TCombobox1.configure(width=163)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(textvariable=fs.actionCombobox)
        self.TCombobox1.configure(
            values=["próbkowanie", "kwantyzacja z zaokrągleniem", "ekstrapolacja pierwszego rzędu", "rekonstrukcja sinc"])
        self.TCombobox1.current(0)

        # -----------------------------------------BUTTONS FRAME------------------------------------------

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=relx+0.37, rely=rely+0.559, relheight=0.05, relwidth=0.07)
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
        self.Button2.configure(command=lambda: FormManager.FormManager().onActionDrawClicked())
        #
        # self.Button3 = tk.Button(top)
        # self.Button3.place(relx=relx+0.29, rely=rely+0.559, relheight=0.05, relwidth=0.07)
        # self.Button3.configure(activebackground="#ececec")
        # self.Button3.configure(activeforeground="#000000")
        # self.Button3.configure(background="#d9d9d9")
        # self.Button3.configure(disabledforeground="#a3a3a3")
        # self.Button3.configure(foreground="#000000")
        # self.Button3.configure(highlightbackground="#d9d9d9")
        # self.Button3.configure(highlightcolor="black")
        # self.Button3.configure(pady="0")
        # self.Button3.configure(text='''Zapisz''')
        # self.Button3.configure(width=77)
        # self.Button3.configure(command=lambda: FormManager.FormManager().onSignalSaveClicked(which))
        #
        # self.Button8 = tk.Button(top)
        # self.Button8.place(relx=relx+0.21, rely=rely+0.559, relheight=0.05, relwidth=0.07)
        # self.Button8.configure(activebackground="#ececec")
        # self.Button8.configure(activeforeground="#000000")
        # self.Button8.configure(background="#d9d9d9")
        # self.Button8.configure(disabledforeground="#a3a3a3")
        # self.Button8.configure(foreground="#000000")
        # self.Button8.configure(highlightbackground="#d9d9d9")
        # self.Button8.configure(highlightcolor="black")
        # self.Button8.configure(pady="0")
        # self.Button8.configure(text='''Odczytaj''')
        # self.Button8.configure(width=77)
        # self.Button8.configure(command=lambda: FormManager.FormManager().onSignalReadClicked(which))
