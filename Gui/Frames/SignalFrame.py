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


class SignalFrame:
    def __init__(self, which, relx, rely, top=None):

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
        self.Label1.place(relx=0.45, rely=0.0, height=21, width=50)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''SYGNAŁ''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.192, rely=0.075, height=21, width=144)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''CZAS POCZĄTKOWY''')
        self.Label2.configure(width=144)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.224, rely=0.1605, height=21, width=114)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''CZAS TRWANIA''')
        self.Label3.configure(width=114)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.192, rely=0.246, height=21, width=154)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''CZĘSTOTLIWOŚĆ SYGNAŁU''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.256, rely=0.3315, height=21, width=72)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''AMPLITUDA''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.16, rely=0.417, height=21, width=187)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''CZĘSTOTLIWOŚĆ PRÓBKOWANIA''')

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.816, rely=0.246, height=21, width=20)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Hz''')

        self.Label9 = tk.Label(self.Frame1)
        self.Label9.place(relx=0.816, rely=0.417, height=21, width=20)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Hz''')

        self.Label10 = tk.Label(self.Frame1)
        self.Label10.place(relx=0.816, rely=0.1605, height=21, width=11)
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
        self.Label12.place(relx=0.288, rely=0.8445, height=21, width=27)
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''TYP''')

        self.Label13 = tk.Label(self.Frame1)
        self.Label13.place(relx=0.16, rely=0.5025, height=21, width=187)
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''WSPÓŁCZYNNIK WYPEŁNIENIA''')

        self.Label14 = tk.Label(self.Frame1)
        self.Label14.place(relx=0.288, rely=0.930, height=21, width=30)
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''SZUM''')

        self.Label15 = tk.Label(self.Frame1)
        self.Label15.place(relx=0.16, rely=0.588, height=21, width=187)
        self.Label15.configure(background="#d9d9d9")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''MOMENT SKOKU''')

        self.Label32 = tk.Label(self.Frame1)
        self.Label32.place(relx=0.16, rely=0.6735, height=21, width=187)
        self.Label32.configure(background="#d9d9d9")
        self.Label32.configure(disabledforeground="#a3a3a3")
        self.Label32.configure(foreground="#000000")
        self.Label32.configure(text='''PRAWDOPODOBIEŃSTWO''')

        self.Label33 = tk.Label(self.Frame1)
        self.Label33.place(relx=0.16, rely=0.759, height=21, width=187)
        self.Label33.configure(background="#d9d9d9")
        self.Label33.configure(disabledforeground="#a3a3a3")
        self.Label33.configure(foreground="#000000")
        self.Label33.configure(text='''NUMER PRÓBKI SKOKU''')

        # ----------------------------ENTRIES FRAME-------------------------------

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.528, rely=0.075, height=20, relwidth=0.262)
        self.Entry1.configure(background="#ffffff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=getattr(fs, which + 'Time0Entry'))

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.528, rely=0.1605, height=20, relwidth=0.262)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable=getattr(fs, which + 'TimeEntry'))

        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry3.place(relx=0.528, rely=0.246, height=20, relwidth=0.262)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable=getattr(fs, which + 'FrequencyEntry'))

        self.Entry4 = tk.Entry(self.Frame1)
        self.Entry4.place(relx=0.528, rely=0.3315, height=20, relwidth=0.262)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(textvariable=getattr(fs, which + 'AmplitudeEntry'))

        self.Entry5 = tk.Entry(self.Frame1)
        self.Entry5.place(relx=0.528, rely=0.417, height=20, relwidth=0.262)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(textvariable=getattr(fs, which + 'NOSamplesEntry'))

        self.Entry6 = tk.Entry(self.Frame1)
        self.Entry6.place(relx=0.528, rely=0.5025, height=20, relwidth=0.262)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(textvariable=getattr(fs, which + 'InfiltratorEntry'))

        self.Entry7 = tk.Entry(self.Frame1)
        self.Entry7.place(relx=0.528, rely=0.588, height=20, relwidth=0.262)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(textvariable=getattr(fs, which + 'JumpMomentEntry'))

        self.Entry15 = tk.Entry(self.Frame1)
        self.Entry15.place(relx=0.528, rely=0.6735, height=20, relwidth=0.262)
        self.Entry15.configure(background="white")
        self.Entry15.configure(disabledforeground="#a3a3a3")
        self.Entry15.configure(font="TkFixedFont")
        self.Entry15.configure(foreground="#000000")
        self.Entry15.configure(insertbackground="black")
        self.Entry15.configure(textvariable=getattr(fs, which + 'PossibilityEntry'))

        self.Entry16 = tk.Entry(self.Frame1)
        self.Entry16.place(relx=0.528, rely=0.759, height=20, relwidth=0.262)
        self.Entry16.configure(background="white")
        self.Entry16.configure(disabledforeground="#a3a3a3")
        self.Entry16.configure(font="TkFixedFont")
        self.Entry16.configure(foreground="#000000")
        self.Entry16.configure(insertbackground="black")
        self.Entry16.configure(textvariable=getattr(fs, which + 'JumpSampleEntry'))

        # -----------------------------------------COMBOBOXES FRAME------------------------------------------

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.528, rely=0.8445, height=21
                              , relwidth=0.261)
        self.TCombobox1.configure(width=163)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(textvariable=getattr(fs, which + 'TypeCombobox'))
        self.TCombobox1.configure(
            values=["brak", "sinus", "sinus wyprostowany jednopolowkowo", "sinus wyprostowany dwupolowkowo",
                    "prostokatny", "prostokatny symetryczny", "trojkatny", "skok jednostkowy", "impuls jednostkowy"])
        self.TCombobox1.current(0)

        self.TCombobox2 = ttk.Combobox(self.Frame1)
        self.TCombobox2.place(relx=0.528, rely=0.930, height=21
                              , relwidth=0.261)
        self.TCombobox2.configure(width=163)
        self.TCombobox2.configure(takefocus="")
        self.TCombobox2.configure(textvariable=getattr(fs, which + 'NoiseCombobox'))
        self.TCombobox2.configure(
            values=["brak", "gaussowski", "o rozkladzie jednostajnym", "impulsowy"])
        self.TCombobox2.current(0)

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
        self.Button2.configure(command=lambda: FormManager.FormManager().onSignalDrawClicked(which))

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=relx+0.29, rely=rely+0.559, relheight=0.05, relwidth=0.07)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Zapisz''')
        self.Button3.configure(width=77)
        self.Button3.configure(command=lambda: FormManager.FormManager().onSignalSaveClicked(which))

        self.Button8 = tk.Button(top)
        self.Button8.place(relx=relx+0.21, rely=rely+0.559, relheight=0.05, relwidth=0.07)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''Odczytaj''')
        self.Button8.configure(width=77)
        self.Button8.configure(command=lambda: FormManager.FormManager().onSignalReadClicked(which))

