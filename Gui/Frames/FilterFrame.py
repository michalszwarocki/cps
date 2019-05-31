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


class FilterFrame:
    def __init__(self, relx, rely, top=None):
        self.possibleRelY = [
            [0.2000, False],
            [0.4000, False],
            [0.6000, False],
            [0.2000, False],
            [0.4000, False],
            [0.6000, False]
        ]

        #----------------------------------------------FRAME---------------------------------------------

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=relx, rely=rely, relheight=0.24, relwidth=0.6)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=625)

        #------------------------------------------LABELS FRAME-------------------------------------------

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.45, rely=0.0, height=21, width=65)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''OPERACJE''')


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
        self.Button1.configure(command=lambda: FormManager.FormManager().onFilterOperationDrawClicked())

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
        self.Button2.configure(command=lambda: FormManager.FormManager().onFilterOperationSaveClicked())

        self.Label2 = tk.Label(self.Frame1)
        self.Label3 = tk.Label(self.Frame1)
        self.Label4 = tk.Label(self.Frame1)
        self.Label5 = tk.Label(self.Frame1)
        self.Label6 = tk.Label(self.Frame1)
        self.Label7 = tk.Label(self.Frame1)
        self.Label8 = tk.Label(self.Frame1)

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry4 = tk.Entry(self.Frame1)

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox2 = ttk.Combobox(self.Frame1)

        type = fs.filterOperationCombobox
        type.trace("w", lambda name, index, mode, b=type: self.typeCallback(b))

        self.createOperationType(self.getFirstPossibleRelY())


    def typeCallback(self, sv):
        self.setAllPossibleRelYAsFalse()
        self.disableAllEntries()
        self.disableAllLabels()
        self.disableAllComboboxes()

        if sv.get() == 'filtrowanie':
            self.createFilterType(self.getFirstPossibleRelY(), self.Label2, self.TCombobox1)
            self.createWindowType(self.getFirstPossibleRelY(), self.Label3, self.TCombobox2)
            self.createMValueLabel(self.getFirstPossibleRelY(), self.Label4, self.Entry1)
            self.createFoLabel(self.getFirstPossibleRelY(), self.Label5, self.Entry2, self.Label6)

        if sv.get() == 'radar':
            self.createDistanceValueLabel(self.getFirstPossibleRelY(), self.Label7, self.Entry3)
            self.createSpeedLabel(self.getFirstPossibleRelY(), self.Label8, self.Entry4)


    def getFirstPossibleRelY(self):
        for x in range(len(self.possibleRelY)):
            if not self.possibleRelY[x][1]:
                self.possibleRelY[x][1] = True
                return self.possibleRelY[x][0]
        return 0

    def setAllPossibleRelYAsFalse(self):
        for x in range(len(self.possibleRelY)):
            if x != 0:
                self.possibleRelY[x][1] = False

    def disableAllEntries(self):
        self.Entry1.place_forget()
        self.Entry2.place_forget()
        self.Entry3.place_forget()
        self.Entry4.place_forget()


    def disableAllLabels(self):
        self.Label2.place_forget()
        self.Label3.place_forget()
        self.Label4.place_forget()
        self.Label5.place_forget()
        self.Label6.place_forget()
        self.Label7.place_forget()
        self.Label8.place_forget()

    def disableAllComboboxes(self):
        self.TCombobox1.place_forget()
        self.TCombobox2.place_forget()


    def createOperationType(self, rely):
        Label = tk.Label(self.Frame1)
        Label.place(relx=0.09, rely=rely, height=21, width=65)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''OPERACJA''')

        TCombobox = ttk.Combobox(self.Frame1)
        TCombobox.place(relx=0.23, rely=rely, height=21, relwidth=0.261)
        TCombobox.configure(width=163)
        TCombobox.configure(takefocus="")
        TCombobox.configure(textvariable=fs.filterOperationCombobox)
        TCombobox.configure(values=["splot", "korelacja", "filtrowanie", "radar"])
        TCombobox.current(0)

    def createFilterType(self, rely, Label, TCombobox):
        Label.place(relx=0.1, rely=rely, height=21, width=35)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''FILTR''')

        TCombobox.place(relx=0.23, rely=rely, height=21, relwidth=0.261)
        TCombobox.configure(width=163)
        TCombobox.configure(takefocus="")
        TCombobox.configure(textvariable=fs.filterTypeCombobox)
        TCombobox.configure(values=["dolnoprzepustowy", "gornoprzepustowy", "srodkowoprzepustowy"])
        TCombobox.current(0)

    def createWindowType(self, rely, Label, TCombobox):
        Label.place(relx=0.1, rely=rely, height=21, width=35)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''OKNO''')

        TCombobox.place(relx=0.23, rely=rely, height=21, relwidth=0.261)
        TCombobox.configure(width=163)
        TCombobox.configure(takefocus="")
        TCombobox.configure(textvariable=fs.windowCombobox)
        TCombobox.configure(values=["brak", "Blackman", "Hamming", "Hanning"])
        TCombobox.current(0)

    def createMValueLabel(self, rely, Label, Entry):
        Label.place(relx=0.55, rely=rely, height=21, width=114)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''M''')
        Label.configure(width=114)

        Entry.place(relx=0.75, rely=rely, height=20, relwidth=0.2)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=fs.mValueEntry)

    def createFoLabel(self, rely, Label, Entry, Label1):
        Label.place(relx=0.52, rely=rely, height=21, width=164)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''CZĘSTOTLIWOŚĆ ODCIĘCIA''')

        Entry.place(relx=0.75, rely=rely, height=20, relwidth=0.2)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=fs.foEntry)

        Label1.place(relx=0.95, rely=rely, height=21, width=20)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(foreground="#000000")
        Label1.configure(text='''Hz''')

    def createDistanceValueLabel(self, rely, Label, Entry):
        Label.place(relx=0.085, rely=rely, height=21, width=75)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''ODLEGŁOŚĆ''')
        Label.configure(width=114)

        Entry.place(relx=0.23, rely=rely, height=20, relwidth=0.2)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=fs.distanceValueEntry)

    def createSpeedLabel(self, rely, Label, Entry):
        Label.place(relx=0.09, rely=rely, height=21, width=70)
        Label.configure(background="#d9d9d9")
        Label.configure(disabledforeground="#a3a3a3")
        Label.configure(foreground="#000000")
        Label.configure(text='''PRĘDKOŚĆ''')
        Label.configure(width=114)

        Entry.place(relx=0.23, rely=rely, height=20, relwidth=0.2)
        Entry.configure(background="white")
        Entry.configure(disabledforeground="#a3a3a3")
        Entry.configure(font="TkFixedFont")
        Entry.configure(foreground="#000000")
        Entry.configure(insertbackground="black")
        Entry.configure(textvariable=fs.speedEntry)