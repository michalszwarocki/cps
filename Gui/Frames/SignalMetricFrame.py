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


class SignalMetricFrame:
    def __init__(self, relx, rely, top=None):
        # ----------------------------------------------FRAME---------------------------------------------

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=relx, rely=rely, relheight=0.24, relwidth=0.4)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=625)

        # ------------------------------------------LABELS FRAME-------------------------------------------

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.1, rely=0.05, height=21, width=144)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''WARTOŚĆ ŚREDNIA''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.04, rely=0.25, height=21, width=200)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''WARTOŚĆ ŚREDNIA BEZWZGLĘDNA''')
        self.Label2.configure(width=144)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.1, rely=0.45, height=21, width=144)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''MOC ŚREDNIA''')
        self.Label3.configure(width=144)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.1, rely=0.65, height=21, width=144)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''WARIANCJA''')
        self.Label4.configure(width=144)

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.1, rely=0.85, height=21, width=144)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''WARTOŚĆ SKUTECZNA''')
        self.Label5.configure(width=144)

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.6, rely=0.05, height=21, width=120)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(textvariable=fs.text1Label)

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.6, rely=0.25, height=21, width=120)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(textvariable=fs.text2Label)
        self.Label7.configure(width=144)

        self.Label8 = tk.Label(self.Frame1)
        self.Label8.place(relx=0.6, rely=0.45, height=21, width=120)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(textvariable=fs.text3Label)
        self.Label8.configure(width=144)

        self.Label9 = tk.Label(self.Frame1)
        self.Label9.place(relx=0.6, rely=0.65, height=21, width=120)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(textvariable=fs.text4Label)
        self.Label9.configure(width=144)

        self.Label10 = tk.Label(self.Frame1)
        self.Label10.place(relx=0.6, rely=0.85, height=21, width=120)
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(textvariable=fs.text5Label)
        self.Label10.configure(width=144)
