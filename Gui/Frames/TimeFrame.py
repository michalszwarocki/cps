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


class TimeFrame:
    def __init__(self, relx, rely, top=None):
        # ----------------------------------------------FRAME---------------------------------------------

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=relx, rely=rely, relheight=0.24, relwidth=0.45)

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
        self.Label1.place(relx=0.095, rely=0.5, height=21, width=170)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''CZAS WYKONYWANIA''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.6, rely=0.5, height=21, width=120)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(textvariable=fs.durationTimeTrans)


