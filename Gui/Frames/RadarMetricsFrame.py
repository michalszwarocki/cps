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


class RadarMetricsFrame:
    def __init__(self, relx, rely, top=None):
        # ----------------------------------------------FRAME---------------------------------------------

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=relx, rely=rely, relheight=0.24, relwidth=0.26)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=625)

        # ------------------------------------------LABELS FRAME-------------------------------------------

        self.Label0 = tk.Label(self.Frame1)
        self.Label0.place(relx=0.4, rely=0.0, height=21, width=65)
        self.Label0.configure(background="#d9d9d9")
        self.Label0.configure(disabledforeground="#a3a3a3")
        self.Label0.configure(foreground="#000000")
        self.Label0.configure(text='''RADAR''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.095, rely=0.3, height=21, width=170)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''ODLEGŁOŚĆ RZECZYWISTA''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.1, rely=0.6, height=21, width=160)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''ODLEGŁOŚĆ OBLICZONA''')
        self.Label3.configure(width=144)

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.6, rely=0.3, height=21, width=120)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(textvariable=fs.realDistance)

        self.Label8 = tk.Label(self.Frame1)
        self.Label8.place(relx=0.6, rely=0.6, height=21, width=120)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(textvariable=fs.achievedDistance)
        self.Label8.configure(width=144)

