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


class MetricsFrame:
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
        self.Label1.place(relx=0.1, rely=0.05, height=21, width=200)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''BŁĄD ŚREDNIOKWADRATOWY''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.1, rely=0.3, height=21, width=200)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''STOSUNEK SYGNAŁ-SZUM''')
        self.Label2.configure(width=144)

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.06, rely=0.55, height=21, width=230)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''SZCZYTOWY STOSUNEK SYGNAŁ-SZUM''')
        self.Label3.configure(width=144)

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.15, rely=0.8, height=21, width=144)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''MAKSYMALNA RÓŻNICA''')
        self.Label4.configure(width=144)

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.6, rely=0.05, height=21, width=120)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(textvariable=fs.mseLabel)

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.6, rely=0.3, height=21, width=120)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(textvariable=fs.snrLabel)
        self.Label7.configure(width=144)

        self.Label8 = tk.Label(self.Frame1)
        self.Label8.place(relx=0.6, rely=0.55, height=21, width=120)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(textvariable=fs.psnrLabel)
        self.Label8.configure(width=144)

        self.Label9 = tk.Label(self.Frame1)
        self.Label9.place(relx=0.6, rely=0.8, height=21, width=120)
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(textvariable=fs.mdLabel)
        self.Label9.configure(width=144)

