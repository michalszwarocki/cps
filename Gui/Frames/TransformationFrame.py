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


class TransformationFrame:
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
        self.Label1.place(relx=0.42, rely=0.0, height=21, width=110)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''TRANSFORMACJE''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.14, rely=0.25, height=21, width=210)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''CZĘSTOTLIWOŚĆ PRÓBKOWANIA''')
        self.Label2.configure(width=114)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.22, rely=0.5, height=21, width=130)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''TYP TRANSFORMACJI''')
        self.Label3.configure(width=114)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.1, rely=0.75, height=21, width=250)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''TYP WYKRESU''')


        # -----------------------------------------COMBOBOXES FRAME------------------------------------------
        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.528, rely=0.25, height=21, relwidth=0.261)
        self.Entry1.configure(background="#ffffff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=fs.samplingFrequencyTrans)


        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.528, rely=0.5, height=21
                              , relwidth=0.261)
        self.TCombobox1.configure(width=163)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(textvariable=fs.transformationCombobox)
        self.TCombobox1.configure(
            values=["dft", "fft", "dwtDb6"])
        self.TCombobox1.current(0)


        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.528, rely=0.75, height=21
                              , relwidth=0.261)
        self.TCombobox1.configure(width=163)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(textvariable=fs.plotCombobox)
        self.TCombobox1.configure(
            values=["real(freq) + imag(freq)", "|complex|(freq) + complex(freq)"])
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
        self.Button2.configure(command=lambda: FormManager.FormManager().onTransformationDrawClicked())

