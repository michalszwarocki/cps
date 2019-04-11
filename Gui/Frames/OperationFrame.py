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


class OperationFrame:
    def __init__(self, relx, rely, top=None):

        #----------------------------------------------FRAME---------------------------------------------

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=relx, rely=rely, relheight=0.24, relwidth=0.4)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=625)

        #------------------------------------------LABELS FRAME-------------------------------------------

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.45, rely=0.0, height=21, width=60)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''OPERACJE''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.1, rely=0.35, height=21, width=144)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''WYBIERZ OPERACJE''')
        self.Label2.configure(width=144)

        # -----------------------------------------COMBOBOXES FRAME------------------------------------------

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.5, rely=0.33, relheight=0.2
                              , relwidth=0.261)
        self.TCombobox1.configure(width=163)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.configure(textvariable=fs.operationCombobox)
        self.TCombobox1.configure(
            values=["dodawanie", "odejmowanie", "mnożenie", "dzielenie"])
        self.TCombobox1.current(0)

        # -----------------------------------------BUTTONS FRAME------------------------------------------

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.38, rely=0.78, relheight=0.2, relwidth=0.14)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Rysuj''')
        self.Button1.configure(width=77)
        self.Button1.configure(command=lambda: FormManager.FormManager().onOperationDrawClicked())

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.54, rely=0.78, relheight=0.2, relwidth=0.14)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Zapisz''')
        self.Button2.configure(width=77)
        self.Button2.configure(command=lambda: FormManager.FormManager().onOperationSaveClicked())
